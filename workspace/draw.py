import config

from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.visualization import draw_box, draw_caption

def draw_boxes(draw, boxes, scores, labels):
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        if score < config.THRESHOLD:
            break

        caption = "{} {:.3f}".format(config.CLASS2LABEL[label], score)
        color = label_color(label)
        b = box.astype(int)
        draw_box(draw, b, color=color)
        draw_caption(draw, b, caption=caption)
    return draw
