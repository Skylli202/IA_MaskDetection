from os import listdir


def check_jpg_xml_count(path, verbose=0, ann_folder='Annotations', img_folder='Images'):
    annotations_files = listdir(path + '/' + ann_folder)
    images_files = listdir(path + '/' + img_folder)

    amount_of_annotations = len(annotations_files)
    amount_of_images = len(images_files)

    if verbose:
        print("Il y a ", amount_of_annotations, " annotations.\n",
              "Il y a ", amount_of_images, " images.\n"
              )

    return amount_of_annotations == amount_of_images


def check_ids(path, verbose=0, ann_folder='Annotations', img_folder='Images'):
    annotations_files = listdir(path + '/' + ann_folder)
    images_files = listdir(path + '/' + img_folder)

    annotations_ids = get_ids(annotations_files)
    images_ids = get_ids(images_files)

    if verbose:
        if annotations_ids == images_ids:
            print("Everything matched")
            return True
        else:
            print("Some file are missing")
            return False
    else:
        if annotations_ids == images_ids:
            return True
        else:
            return False


def get_ids(l):
    res = []
    for item in l:
        res.append(item.replace('.xml', '').replace('.jpg', ''))
    return res


def get_xml_that_have_every_classes(ann_path):
    from os import listdir
    files = listdir(ann_path)

    for file in files:
        from xml.etree import ElementTree
        tree = ElementTree.parse(ann_path + '/' + file)

        from xml.etree import ElementTree
        root = tree.getroot()

        has_with_mask = False
        has_without_mask = False
        has_mask_weared_incorrect = False

        for object in root.findall('object'):
            if 'with_mask' == object.find('name').text:
                has_with_mask = True
            elif 'without_mask' == object.find('name').text:
                has_without_mask = True
            elif 'mask_weared_incorrect' == object.find('name').text:
                has_mask_weared_incorrect = True

            if has_with_mask and has_without_mask and has_mask_weared_incorrect:
                print(file)
                break
