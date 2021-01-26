import os
import cv2
import numpy as np

import draw
import config
import cartucho as mAP

from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image


def load_model():
    model = models.load_model(config.MODEL_PATH, backbone_name='resnet50')
    model = models.convert_model(model)
    return model


def inf_img(filename, dataset="", cartucho=False, output=''):
    if dataset == "":
        for IMG_PATH in config.IMG_PATHS:
            lstdir = os.listdir(IMG_PATH)
            if filename in lstdir:
                img_path = IMG_PATH + "/" + filename
                break
            else:
                img_path = ""

        if img_path == "":
            print("Image introuvable..")
            return
    else:
        imgs_path = config.IMG_PATHS[config.DATASETS_NAMES.index(dataset)]
        img_path = imgs_path + "/" + filename

    my_model = load_model()

    # img_path = ""
    img = read_image_bgr(img_path)
    deep_cp_img = img.copy()
    deep_cp_img = cv2.cvtColor(deep_cp_img, cv2.COLOR_RGB2RGBA)
    boxes, scores, labels = my_model.predict_on_batch(np.expand_dims(img, axis=0))

    deep_cp_img = draw.draw_boxes(deep_cp_img, boxes, scores, labels)

    if cartucho:
       mAP.gen_detection_results_file(img_path.split('/')[-1], boxes, scores, labels)

    if output == '':
        cv2.imwrite("./main_output/inferenced_img.jpg", deep_cp_img)
    else:
        cv2.imwrite(output, deep_cp_img)
    return


def cartucho_evaluate(dataset):
    imgs_path = config.IMG_PATHS[config.DATASETS_NAMES.index(dataset)]

    img_lst = os.listdir(imgs_path)

    my_model = load_model()

    img_done = 0

    for img in img_lst:
        img_path = imgs_path + "/" + img
        # inf_img(img, dataset, True)

        img = read_image_bgr(img_path)
        boxes, scores, labels = my_model.predict_on_batch(np.expand_dims(img, axis=0))
        mAP.gen_detection_results_file(img_path.split('/')[-1], boxes, scores, labels)
        img_done += 1

        if img_done % 10 == 0:
            print("img done: " + str(img_done))

    return
