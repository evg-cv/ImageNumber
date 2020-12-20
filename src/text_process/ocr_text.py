import json
import os
import imageio

from src.csv_import.new_image_name import extract_new_name_from_old
from utils.google_ocr import GoogleVisionAPI
from utils.image_rotation import rotate_skewed_image, adjust_boundary_with_margin
from settings import OUT_DIR, LOCAL, CUR_DIR

if LOCAL:
    import ntpath
    from utils.folder_file_manager import save_file


class TextProcess:

    def __init__(self):

        self.google_ocr = GoogleVisionAPI()

    @staticmethod
    def extract_info_from_json(json_result):

        number = ""
        jsons = json_result["textAnnotations"][1:]
        for i, _json in enumerate(jsons):

            if "Stea" in _json["description"]:

                cmp_left = _json["boundingPoly"]["vertices"][0]["x"]
                cmp_right = _json["boundingPoly"]["vertices"][1]["x"]

                count = i + 1
                if cmp_left - 10 <= jsons[count]["boundingPoly"]["vertices"][0]["x"] <= cmp_right + 10 or \
                        cmp_left - 10 <= jsons[count]["boundingPoly"]["vertices"][1]["x"] <= cmp_right + 10:
                    bounding_ret = False
                else:
                    bounding_ret = True

                while not jsons[count]["description"].isdigit() or bounding_ret:
                    count += 1
                    if cmp_left - 10 <= jsons[count]["boundingPoly"]["vertices"][0]["x"] <= cmp_right + 10 or \
                            cmp_left - 10 <= jsons[count]["boundingPoly"]["vertices"][1]["x"] <= cmp_right + 10:

                        bounding_ret = False

                # name = jsons[count - 1]["description"]
                number = jsons[count]["description"]
                break

        return number

    def process_ocr_text(self, frame_path):

        image_ocr_json = self.google_ocr.detect_text(img_path=frame_path)
        if LOCAL:
            json_file_path = os.path.join(CUR_DIR, 'temp', "temp_{}.json".format(ntpath.basename(frame_path).
                                                                                 replace(".jpg", "")))
            save_file(filename=json_file_path, content=json.dumps(image_ocr_json), method="w")

        new_name = self.get_new_image_name(origin_json=image_ocr_json, frame_path=frame_path)
        new_frame_path = os.path.join(OUT_DIR, new_name + ".gif")

        frame = imageio.imread(frame_path)
        imageio.mimsave(new_frame_path, [frame])

        return new_frame_path

    def get_new_image_name(self, origin_json, frame_path):

        left = None
        right = None
        top = None
        bottom = None

        crop_path = rotate_skewed_image(json_val=origin_json, frame_path=frame_path)
        corrected_json = self.google_ocr.detect_text(img_path=crop_path)

        for _json in corrected_json["textAnnotations"][1:]:

            if "Stea" in _json["description"]:
                left = _json["boundingPoly"]["vertices"][0]["x"]
                right = _json["boundingPoly"]["vertices"][1]["x"]
                top = _json["boundingPoly"]["vertices"][0]["y"]

            if "Patent" in _json["description"]:

                bottom = _json["boundingPoly"]["vertices"][2]["y"]

        if bottom is None:

            bottom = top + 2 * (right - left)

        frame = imageio.imread(crop_path)
        left, top, right, bottom = adjust_boundary_with_margin(left_p=left, right_p=right, bottom_p=bottom, top_p=top,
                                                               fm_width=frame.shape[1], fm_height=frame.shape[0])
        if abs(right - left) <= 0.8 * frame.shape[1] or abs(bottom - top) <= 0.8 * frame.shape[0]:
            re_cropped_frame = frame[top:bottom, left:right]
            imageio.imwrite(crop_path, re_cropped_frame)
            corrected_json = self.google_ocr.detect_text(img_path=crop_path)

        number = self.extract_info_from_json(json_result=corrected_json)
        print("Number:{}".format(number))
        new_name = extract_new_name_from_old(number=number)

        return new_name


if __name__ == '__main__':
    text_processor = TextProcess()
    path = ""
    with open('') as f:
        json_content = json.load(f)

    name_ = text_processor.get_new_image_name(json_content, path)
    print(name_)
