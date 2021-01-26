""" Python libs """
import os
import cv2
import numpy as np

""" Homemade libs """
import draw
import config
import backend
import cartucho as mAP

""" Functions imports """
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image


def load_model():
    model = models.load_model(config.MODEL_PATH, backbone_name='resnet50')
    model = models.convert_model(model)
    return model


def inf_img(filename, dataset="", preprocess=False, cartucho=False, output=''):
    img_path = backend.filenameToFullPath(filename, dataset)

    my_model = load_model()

    # img_path = ""
    img = read_image_bgr(img_path)

    if preprocess:
        img = preprocess_image(img)
        img, scale = resize_image(img)

    deep_cp_img = img.copy()
    deep_cp_img = cv2.cvtColor(deep_cp_img, cv2.COLOR_RGB2RGBA)

    boxes, scores, labels = my_model.predict_on_batch(np.expand_dims(img, axis=0))

    if preprocess:
        boxes = boxes/scale

    deep_cp_img = draw.draw_boxes(deep_cp_img, boxes, scores, labels)

    if cartucho:
       mAP.gen_detection_results_file(img_path.split('/')[-1], boxes, scores, labels)

    if output == '':
        cv2.imwrite("./main_output/inferenced_img.jpg", deep_cp_img)
    else:
        cv2.imwrite(output, deep_cp_img)
    return


def cartucho_evaluate(dataset, preprocess=False, verbose=False):
    imgs_path = config.IMG_PATHS[config.DATASETS_NAMES.index(dataset)]

    img_lst = os.listdir(imgs_path)

    my_model = load_model()

    img_done = 0

    for img in img_lst:
        img_path = imgs_path + "/" + img
        # inf_img(img, dataset, True)

        img = read_image_bgr(img_path)

        if preprocess:
            img = preprocess_image(img)
            img, scale = resize_image(img)

        boxes, scores, labels = my_model.predict_on_batch(np.expand_dims(img, axis=0))

        if preprocess:
            boxes = boxes/scale

        mAP.gen_detection_results_file(img_path.split('/')[-1], boxes, scores, labels)
        img_done += 1

        if verbose:
            if img_done % 10 == 0:
                print("Image inférée: " + str(img_done) + '/' + str(len(img_lst)))

    return
