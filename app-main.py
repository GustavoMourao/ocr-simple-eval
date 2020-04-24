import pytesseract
import cv2
from PIL import Image
import argparse
import pandas as pd


def ocr_process(video_name):
    """
    OCR processing using tysseract.

    Args:
    ---------
        vide_name: name of video [string]

    Return:
    ---------

    """
    cap = cv2.VideoCapture(video_name)

    recorded_values = []

    try:
        while True:
            _, cv2_im = cap.read()
            cv2_im = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
            pil_im = Image.fromarray(cv2_im)

            text_ = pytesseract.image_to_string(
                pil_im,
                config=''
            )
            recorded_values.append(text_)
            print(len(recorded_values))

    except Exception:

        data_recoded = pd.DataFrame(recorded_values)
        data_recoded.to_csv('characters.csv', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--video',
        help="Input Video File"
    )
    args = parser.parse_args()
    ocr_process(args.video)
