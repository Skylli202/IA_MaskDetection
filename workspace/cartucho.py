""" Python libs """
import os

""" Homemade libs """
import config

""" Functions imports """
from xml.etree import ElementTree


def gen_ground_truth_files(dataset):
    if dataset not in config.DATASETS_NAMES:
        print('Impossible de générer les ground truth files, ce dataset n\'existe pas')
        return

    dataset_path = config.DATASETS_PATH + "/" + dataset
    xmls_path = dataset_path + "/Annotations"

    pascal_voc_xmls = os.listdir(xmls_path)

    for xml in pascal_voc_xmls:
        print("Generating ground truth for " + xml)
        tree = ElementTree.parse(xmls_path + "/" + xml)
        root = tree.getroot()

        grnd_file_path = config.CARTUCHO_GROUND_TRUTH_PATH + "/" + root.find('filename').text.replace('.png','.txt').replace('.jpg','.txt')
        with open(grnd_file_path, 'w') as file:
            lines = ""
            for member in root.findall('object'):
                line = member[0].text + " "
                line += member.find('bndbox')[0].text.split('.')[0] + " "
                line += member.find('bndbox')[1].text.split('.')[0] + " "
                line += member.find('bndbox')[2].text.split('.')[0] + " "
                line += member.find('bndbox')[3].text.split('.')[0] + "\n"
                lines += line
            file.write(lines)
    return


def gen_detection_results_file(filename, boxes, scores, labels):
    file = config.CARTUCHO_DETECTIONS_RETULTS_FILES_PATH + "/" + filename.replace('.png','.txt').replace('.jpg','.txt')
    with open(file, 'w') as detection_results_file:
        for box, score, label in zip(boxes[0], scores[0], labels[0]):
            if score < config.THRESHOLD:
                break
            b = box.astype(int)
            detection_results_file.write("%s %.6f %d %d %d %d\n" % (config.CLASS2LABEL[label], score, b[0], b[1], b[2], b[3]))
    return