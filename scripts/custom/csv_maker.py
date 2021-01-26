from os import listdir
from xml.etree import ElementTree


def csv_line_of(xml_file, path=''):
    res = ""

    tree = ElementTree.parse(xml_file)
    root = tree.getroot()

    img_name = root.find('filename').text

    # Loop through all object
    for object in root.findall('object'):
        label = object.find('name').text
        xmin = object.find('bndbox').find('xmin').text.split('.')[0]
        ymin = object.find('bndbox').find('ymin').text.split('.')[0]
        xmax = object.find('bndbox').find('xmax').text.split('.')[0]
        ymax = object.find('bndbox').find('ymax').text.split('.')[0]

        res += path + img_name + "," + xmin + "," + ymin + "," + xmax + "," + ymax + "," + label + "\n"

    return res


def get_csv(src_path, drive_path='', annotations_foldername='Annotations', images_foldername='Images'):
    # var
    res = ""

    # Path
    annotations_path = src_path + '/' + annotations_foldername
    images_path = src_path + '/' + images_foldername

    xml_files = listdir(annotations_path)

    # Loop through every xml
    for xml_file in xml_files:
        # if parameter haven't been set, its a local csv
        if drive_path == '':
            res += csv_line_of(annotations_path + '/' + xml_file, images_path + '/')  # Do not forget the / or \
        else:
            res += csv_line_of(annotations_path + '/' + xml_file, drive_path + '/' + images_foldername + '/') # Do not forget the / or \

    return res


def get_csv_as_list(src_path, drive_path='', annotations_foldername='Annotations', images_foldername='Images'):
    csv = get_csv(src_path, drive_path, annotations_foldername, images_foldername)
    return csv.split()



def make_csv(src_path, drive_path='', filename='annotations.csv', ann_folder='Annotations', img_folder='Images'):
    # write down the csv on file system
    with open(filename, 'w') as f:
        csv = get_csv(src_path, '', ann_folder, img_folder)
        f.write(csv)
