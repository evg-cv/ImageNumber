import os

from utils.folder_file_manager import make_directory_if_not_exists

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(CUR_DIR, 'input')
OUT_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'output'))

CREDENTIAL_PATH = os.path.join(CUR_DIR, 'utils', 'credential', 'OCR label project-ff37d8323b53.json')
CSV_PATH = os.path.join(CUR_DIR, 'utils', 'OCR.csv')
TEMP_PATH = os.path.join(OUT_DIR, "temp.jpg")
CROP_PATH = os.path.join(OUT_DIR, 'crop.jpg')
PROCESSED_FILES = os.path.join(CUR_DIR, 'processed_files.txt')
CROP_MARGIN = 40
LOCAL = False
