import numpy as np
import math
import imutils
import json
import imageio

from settings import TEMP_PATH, CROP_PATH, CROP_MARGIN


def rotate_skewed_image(json_val, frame_path):

    temp_jpg = TEMP_PATH
    frame = imageio.imread(frame_path)

    width = frame.shape[1]
    height = frame.shape[0]
    base_vec = [width, 0]
    word_angle = 0

    left = json_val["textAnnotations"][0]["boundingPoly"]["vertices"][0]["x"]
    right = json_val["textAnnotations"][0]["boundingPoly"]["vertices"][2]["x"]
    top = json_val["textAnnotations"][0]["boundingPoly"]["vertices"][0]["y"]
    bottom = json_val["textAnnotations"][0]["boundingPoly"]["vertices"][2]["y"]
    left, top, right, bottom = adjust_boundary_with_margin(left_p=left, right_p=right, bottom_p=bottom, top_p=top,
                                                           fm_height=height, fm_width=width)
    cropped_image = frame[top: bottom, left:right]

    try:

        for page in json_val['fullTextAnnotation']['pages']:
            for block in page['blocks']:
                for paragraph in block['paragraphs']:
                    for words in paragraph['words']:
                        word = ""
                        for symbols in words["symbols"]:
                            word += symbols["text"]

                        if "Steam" not in word:
                            continue

                        line_start_point = words['symbols'][0]["boundingBox"]["vertices"][3]
                        line_end_point = words['symbols'][-1]["boundingBox"]["vertices"][3]
                        # cv2.line(frame, (line_start_point["x"], line_start_point["y"]),
                        #          (line_end_point["x"], line_end_point["y"]), (0, 0, 255), 2)
                        word_vec = [line_end_point['x'] - line_start_point['x'],
                                    line_end_point['y'] - line_start_point['y']]

                        word_angle = math.acos(((word_vec[0] * base_vec[0]) + (word_vec[1] * base_vec[1]))
                                               / ((math.sqrt(word_vec[0] ** 2 + word_vec[1] ** 2)) *
                                                  (math.sqrt(base_vec[0] ** 2 + base_vec[1] ** 2))))
                        if word_vec[1] <= 0:
                            word_angle = word_angle * 180 / np.pi
                        else:
                            word_angle = - (word_angle * 180 / np.pi)
    except Exception as e:
        print(e)

    rotated_frame = imutils.rotate_bound(frame, word_angle)
    rotated_cropped_frame = imutils.rotate_bound(cropped_image, word_angle)

    imageio.imwrite(CROP_PATH, rotated_cropped_frame)
    imageio.imwrite(temp_jpg, rotated_frame)

    return CROP_PATH


def adjust_boundary_with_margin(left_p, top_p, right_p, bottom_p, fm_width, fm_height):

    if left_p < CROP_MARGIN:
        left_p = 0
    else:
        left_p -= CROP_MARGIN

    if right_p > fm_width - CROP_MARGIN:
        right_p = fm_width
    else:
        right_p += CROP_MARGIN

    if top_p < CROP_MARGIN:
        top_p = 0
    else:
        top_p -= CROP_MARGIN

    if bottom_p > fm_height - CROP_MARGIN:
        bottom_p = fm_height
    else:
        bottom_p += CROP_MARGIN

    return left_p, top_p, right_p, bottom_p


if __name__ == '__main__':

    img_path = ""
    with open('') as f:
        json_content = json.load(f)
    rotate_skewed_image(json_val=json_content, frame_path=img_path)
