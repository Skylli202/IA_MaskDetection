""" GENERAL """
THRESHOLD = 0.5

""" CSV """
TRAIN_CSV = "../datasets/CSV/TRAIN_annotations.csv"
TEST_CSV = "../datasets/CSV/TEST_annotations.csv"
LABELS_CSV = "../datasets/CSV/labels.csv"

""" LABELS """
CLASS2LABEL = { # pd.read_csv(config.LABELS_CSV, header=None).T.loc[0].to_dict()
    0:"without_mask",
    1:"with_mask",
    2:"mask_weared_incorrect"
}

""" DATASETS """
DATASETS_NAMES = ['test', 'train']
DATASETS_PATH = "../datasets"
# test
DATASET_TEST_PATH = DATASETS_PATH + "/test"
TEST_ANN_PATH = DATASET_TEST_PATH + "/Annotations"
TEST_IMG_PATH = DATASET_TEST_PATH + "/Images"
# train
DATASET_TRAIN_PATH = DATASETS_PATH + "/train"
TRAIN_ANN_PATH = DATASET_TRAIN_PATH + "/Annotations"
TRAIN_IMG_PATH = DATASET_TRAIN_PATH + "/Images"

IMG_PATHS = [TEST_IMG_PATH, TRAIN_IMG_PATH]

""" MODELS """
MODELS_PATH = "../models"
MODEL_NAME = "resnet50_csv_17.h5"
MODEL_PATH = MODELS_PATH + "/" + MODEL_NAME

""" CAMERA """
CAMERA_PORT = 700

""" CARTUCHO mAP """
CARTUCHO_GROUND_TRUTH_PATH = "../cartucho/input/ground-truth"
CARTUCHO_DETECTIONS_RETULTS_FILES_PATH = "../cartucho/input/detection-results"
