""" Python libs """
import cv2
import time
import numpy as np
import pathlib

""" Homemade libs """
import draw
import model
import config
import CLI_backend as clib

""" Functions imports """


def detect_cam_port():
    all_camera_idx_available = []

    for camera_idx in range(1000):
        cap = cv2.VideoCapture(camera_idx)
        if cap.isOpened():
            print(f'Camera index available: {camera_idx}')
            all_camera_idx_available.append(camera_idx)
            cap.release()

    print(all_camera_idx_available)
    return

# TODO: rendre l'emplacement d'enregistrement de la vidéo paramétrable
def video(show_fps=True, mirror=True, record=False):
    cap = cv2.VideoCapture(config.CAMERA_PORT)

    if not cap.isOpened():
        print(
            "Erreur: la caméra n'a pas pu être ouverte, lancer la fonction detect_cam_port() pour détecter votre numéro de port de caméra et mettez a jour la variable globale CAMERA_PORT")
        return

    my_model = model.load_model()

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    if show_fps:
        prev_frame_time = 0
        new_frame_time = 0

    if record:
        file_path = 'main_output/outpy.mp4'
        # TODO : implémenter une vérification
        # if pathlib.Path.exists(file_path):
        #     if not clib.askUserYesNo("Le fichier existe déjà, êtes vous sur de voulez continuer ?\n"
        #                       "Le fichier existant sera réécrit, et donc perdu. (Y/N)\n"
        #                       "  Y : continuer, réécrire le fichier"
        #                       "  N : met fin au programme"):
        #         print("Fin de la vidéo.")
        #         cap.release()
        #         cv2.destroyAllWindows()
        #         return
        # video_writer = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,(frame_width, frame_height))
        video_writer = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'mp4v'), 10, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if mirror:
            frame = cv2.flip(frame, 1)

        boxes, scores, labels, = my_model.predict_on_batch(np.expand_dims(frame, axis=0))
        draw.draw_boxes(frame, boxes, scores, labels)

        if ret:
            if show_fps:
                new_frame_time = time.time()
                fps = str(int(1 / (new_frame_time - prev_frame_time)))
                prev_frame_time = new_frame_time
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

            if record:
                video_writer.write(frame)

            # Display the resulting frame
            cv2.imshow('frame', frame)

            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) == 27:
                break

        # Break the loop
        else:
            break

    cap.release()
    if record:
        video_writer.release()
    cv2.destroyAllWindows()
    return
