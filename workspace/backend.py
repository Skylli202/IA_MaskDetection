""" Python libs """
import os

""" Homemade libs """
import config


def filenameToFullPath(filename, dataset=""):
    if dataset == "":
        for IMG_PATH in config.IMG_PATHS:
            lstdir = os.listdir(IMG_PATH)
            if filename in lstdir:
                img_path = IMG_PATH + "/" + filename
                break
            else:
                img_path = ""

        if img_path == "":
            print("Image introuvable...")
            # Exception("Image introuvable...")
            return
    else:
        imgs_path = config.IMG_PATHS[config.DATASETS_NAMES.index(dataset)]
        img_path = imgs_path + "/" + filename

        if os.path.exists(img_path):
            return img_path
        else:
            if config.DATASETS_NAMES.index(dataset):
                return config.IMG_PATHS[0] + '/' + filename
            else:
                return config.IMG_PATHS[1] + '/' + filename



        #

