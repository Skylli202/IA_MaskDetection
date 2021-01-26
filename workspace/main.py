#
#  _   __ ___________  ___   _____        ___________   ___ _____ _____ _____       ______ _____ _____ _____ _____ _____ ___________
# | | / /|  ___| ___ \/ _ \ /  ___|      |  _  | ___ \ |_  |  ___/  __ \_   _|      |  _  \  ___|_   _|  ___/  __ \_   _|  _  | ___ \
# | |/ / | |__ | |_/ / /_\ \\ `--.       | | | | |_/ /   | | |__ | /  \/ | |        | | | | |__   | | | |__ | /  \/ | | | | | | |_/ /
# |    \ |  __||    /|  _  | `--. \      | | | | ___ \   | |  __|| |     | |        | | | |  __|  | | |  __|| |     | | | | | |    /
# | |\  \| |___| |\ \| | | |/\__/ /      \ \_/ / |_/ /\__/ / |___| \__/\ | |        | |/ /| |___  | | | |___| \__/\ | | \ \_/ / |\ \
# \_| \_/\____/\_| \_\_| |_/\____/        \___/\____/\____/\____/ \____/ \_/        |___/ \____/  \_/ \____/ \____/ \_/  \___/\_| \_|
#
#       ___  ___  ___   _____ _   __      ______ _____ _____ _____ _____ _____ ___________
#       |  \/  | / _ \ /  ___| | / /      |  _  \  ___|_   _|  ___/  __ \_   _|  _  | ___ \
#       | .  . |/ /_\ \\ `--.| |/ /       | | | | |__   | | | |__ | /  \/ | | | | | | |_/ /
#       | |\/| ||  _  | `--. \    \       | | | |  __|  | | |  __|| |     | | | | | |    /
#       | |  | || | | |/\__/ / |\  \      | |/ /| |___  | | | |___| \__/\ | | \ \_/ / |\ \
#       \_|  |_/\_| |_/\____/\_| \_/      |___/ \____/  \_/ \____/ \____/ \_/  \___/\_| \_|
#
#
#  _____ _                                _____ _____ _   _ _____ _   _ _____ _   _ _____ _   _  _____ _____
# |  ___| |                              |  __ \  _  | | | |_   _| \ | |  __ \ | | |  ___| \ | ||  ___|_   _|
# | |__ | | ___  _   _  __ _ _ __        | |  \/ | | | | | | | | |  \| | |  \/ | | | |__ |  \| || |__   | |
# |  __|| |/ _ \| | | |/ _` | '_ \       | | __| | | | | | | | | | . ` | | __| | | |  __|| . ` ||  __|  | |
# | |___| | (_) | |_| | (_| | | | |      | |_\ \ \_/ / |_| |_| |_| |\  | |_\ \ |_| | |___| |\  || |___  | |
# \____/|_|\___/ \__,_|\__,_|_| |_|       \____/\___/ \___/ \___/\_| \_/\____/\___/\____/\_| \_/\____/  \_/
#
#
#    ___                                     ___  ___  ___   _____ _____  ___  ____________
#   |_  |                                    |  \/  | / _ \ /  ___/  ___|/ _ \ | ___ \  _  \
#     | | ___ _ __ ___  _ __ ___   ___       | .  . |/ /_\ \\ `--.\ `--./ /_\ \| |_/ / | | |
#     | |/ _ \ '__/ _ \| '_ ` _ \ / _ \      | |\/| ||  _  | `--. \`--. \  _  ||    /| | | |
# /\__/ /  __/ | | (_) | | | | | |  __/      | |  | || | | |/\__/ /\__/ / | | || |\ \| |/ /
# \____/ \___|_|  \___/|_| |_| |_|\___|      \_|  |_/\_| |_/\____/\____/\_| |_/\_| \_|___/
#
#
#  _____ _____ ___________ ________  ___       _____  ___         _____ _____  ___
# |  ___/  ___|_   _| ___ \  ___|  \/  |      |  ___|/ _ \       /  ___|_   _|/ _ \
# | |__ \ `--.  | | | |_/ / |__ | .  . |      |___ \/ /_\ \      \ `--.  | | / /_\ \
# |  __| `--. \ | | |    /|  __|| |\/| |          \ \  _  |       `--. \ | | |  _  |
# | |___/\__/ /_| |_| |\ \| |___| |  | |      /\__/ / | | |      /\__/ /_| |_| | | |
# \____/\____/ \___/\_| \_\____/\_|  |_/      \____/\_| |_/      \____/ \___/\_| |_/
#


""" Python libs """
import os
import subprocess
# os.environ["CUDA_VISIBLE_DEVICES"] = '-1'

# import tensorflow as tf
# gpus = tf.config.experimental.list_physical_devices('GPU')
# print(gpus)
# tf.config.experimental.set_virtual_device_configuration(gpus[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
# if gpus:
#     try:
#         for gpu in gpus:
#             tf.config.experimental.set_memory_growth(gpu, True)
#
#     except RuntimeError as e:
#         print(e)

# from tensorflow.compat.v1 import ConfigProto
# from tensorflow.compat.v1 import InteractiveSession
#
# config = ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.2
# config.gpu_options.allow_growth = True
# session = InteractiveSession(config=config)

""" Homemade libs """
import CLI
import model
import config
import camera
import cartucho
import backend

""" Functions imports """

# Command
# train     : python C:\Users\Skylli\PycharmProjects\IA_MaskDetection\keras-retinanet\keras_retinanet\bin\train.py --batch-size 1 --steps 10 --epochs 5 --freeze-backbone --backbone resnet50 --gpu 0 csv C:\Users\Skylli\PycharmProjects\IA_MaskDetection\workspace\TEST_annotations.csv C:\Users\Skylli\PycharmProjects\IA_MaskDetection\workspace\labels.csv
# eval test : python C:\Users\Skylli\PycharmProjects\IA_MaskDetection\keras-retinanet\keras_retinanet\bin\evaluate.py --backbone resnet50 --gpu 0  csv C:\Users\Skylli\PycharmProjects\IA_MaskDetection\datasets\CSV\TEST_annotations.csv C:\Users\Skylli\PycharmProjects\IA_MaskDetection\datasets\CSV\labels.csv C:\Users\Skylli\PycharmProjects\IA_MaskDetection\models\resnet50_csv_17.h5 --convert-model


if __name__ == '__main__':
    # print("KERAS OBJECT DETECION\n     MASK DETECTOR\nElouan GOUINGUENET\nJérome MASSARD\nESIREM 5A ILC 2021/2021")
    # model.cartucho_evaluate('test', True)
    CLI.mainCLI()