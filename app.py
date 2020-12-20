import glob
import os
import ntpath

from settings import INPUT_DIR, TEMP_PATH, PROCESSED_FILES, CROP_PATH
from src.text_process.ocr_text import TextProcess
from utils.folder_file_manager import log_print, save_file, load_text


if __name__ == '__main__':

    text_process = TextProcess()

    input_image_path = glob.glob(os.path.join(INPUT_DIR, "*.*"))
    processed_files = load_text(filename=PROCESSED_FILES)
    total_lens = len(input_image_path)
    for i, path in enumerate(input_image_path):

        file_name = ntpath.basename(path).replace(".jpg", "")
        if file_name in processed_files:
            continue

        print("Process {}-({} / {})".format(path, i + 1, total_lens))
        try:
            saved_path = text_process.process_ocr_text(frame_path=path)
            log_print(info_str=path + "\n" + "Successfully saved")
            print("Successfully saved {}".format(saved_path))
            save_file(content=file_name + "\n", filename=PROCESSED_FILES, method="a")
        except Exception as e:
            log_print(info_str=path)
            log_print(info_str=e)

    os.remove(TEMP_PATH)
    os.remove(CROP_PATH)
