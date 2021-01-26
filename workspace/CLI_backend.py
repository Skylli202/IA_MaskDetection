""" Python libs """
import os
import time

""" Homemade libs """
import CLI
import model
import camera
import backend

""" Functions imports """


def kerasFlood(sleepTime=1):
    print("Attention !! Keras flood incoming !")
    time.sleep(sleepTime)


def space(nb_line=3):
    for i in range(nb_line):
        print()


def isValidInput(usr_input):
    keys = CLI.optionsValues.keys()
    for key in keys:
        if str(key) == usr_input:
            return True
    return False


def askInput():
    usr_input = input()
    while True:
        if isValidInput(usr_input):
            return usr_input
        else:
            print("Valeur incorrect réessayer")
            usr_input = askInput()


def askUserYesNo(msg):
    while True:
        usr_input = input(msg)
        if usr_input.upper() == 'Y':
            return True
        elif usr_input.upper() == 'N':
            return False
        else:
            msg = "Erreur, répondez par Y ou N\n"


def run_inferer_img():
    # Demander l'image que l'utilisateur souhaite inférer
    filename = input("Quel image souhaitez-vous inférer ?\n")
    dataset = input("A quel dataset appartient cette image ? \nRépondez champ vide si vous ne le savez pas.\n")
    print(dataset)
    # img_path = backend.filenameToFullPath(filename, dataset)
    # Demander les paramètres d'inférence
    # filename OK!, dataset="" OK!, preprocess=False, cartucho=False, output=''

    msg = "Souhaitez-vous inférer avec les paramètres par défaut ?\n" \
          "Pas de préprocess, pas de création du fichier cartucho et\n" \
          "l'image sera sauvegarder dans : workspace/main_output/inferenced_img.jpg\n"
    custom_option = askUserYesNo(msg)

    if not custom_option:
        ask_preprocess_msg = "Souhaitez-vous appliquer un préprocess ? (Y/N)\n"
        preprocess = askUserYesNo(ask_preprocess_msg)  # preprocess OK!

        ask_cartucho_msg = "Souhaitez-vous créer le fichier cartucho detection-result par la même occasion ? (Y/N)\n"
        cartucho = askUserYesNo(ask_cartucho_msg)  # cartucho OK!

        # TODO: debugger l'emplacement souhaitez du résultat de l'inférence
        # output = input("Entrer le chemin relatif ET le nom souhaitez AINSI que son extension vers l'emplacement de sauvegarde souhaitez. \n"
        #                "Le point de départ du chemin relatif est workspace/main.py\n"
        #                "")
        output = ''
    else:
        preprocess = False
        cartucho = False
        output = ''

    # Lancer l'inférence
    kerasFlood()

    start_inf_time = time.time()
    model.inf_img(filename, dataset, preprocess, cartucho, output)
    end_inf_time = time.time()

    print("\n\n\nL'inférence a mit {:.3f} secondes.".format(float(end_inf_time - start_inf_time)))
    space()


def run_video():
    msg = "Souhaitez-vous lancer la vidéo avec les paramètres par défaut ?\n" \
          "IPS: Avec, Miroir: Avec, Enregistrement: Sans \n" \
          "La vidéo sera sauvegarder dans : workspace/main_output/outpy.mp4\n"
    custom_option = askUserYesNo(msg)
    if not custom_option:
        ask_fps_msg = "Afficher les images par secondes (IPS) (Y/N)\n"
        fps = askUserYesNo(ask_fps_msg)

        ask_mirror_msg = "Appliquer un traitement miroir sur l'image poru qu'elle soit à l'endroit ?  (Y/N)\n"
        mirror = askUserYesNo(ask_mirror_msg)

        ask_record_msg = "Souhaitez-vous enregistrer la vidéo ?  (Y/N)\n" \
                         "Emplacement : workspace/main_output/outpy.mp4\n" \
                         "ATTENTION: si le fichier existe déjà, il sera réécrit.\n"
        record = askUserYesNo(ask_record_msg)
    else:
        fps = True
        mirror = True
        record = False

    print("Appuyez sur ESC pour quitter la vidéo.")
    print("Appuyez sur ESC pour quitter la vidéo.")
    print("Appuyez sur ESC pour quitter la vidéo.")
    print("Appuyez sur ESC pour quitter la vidéo.")
    print("Appuyez sur ESC pour quitter la vidéo.")
    print("Appuyez sur ESC pour quitter la vidéo.")
    print("Appuyez sur ESC pour quitter la vidéo.")
    print("Appuyez sur ESC pour quitter la vidéo.")
    print("Appuyez sur ESC pour quitter la vidéo.")
    print("Appuyez sur ESC pour quitter la vidéo.")
    time.sleep(2)
    kerasFlood()

    camera.video(fps, mirror, record)


def run_eval_cartucho():
    ask_preprocess_msg = "Souhaitez-vous appliquer un préprocess ? (Y/N)\n"
    preprocess = askUserYesNo(ask_preprocess_msg)  # preprocess OK!

    print("Lancement de la création des fichiers \"dectection-results\"...")
    kerasFlood()
    start_eval_time = time.time()
    model.cartucho_evaluate('test', preprocess, True)
    end_eval_time = time.time()

    print("\n\n\nL'inférence a mit {:.3f} secondes.".format(float(end_eval_time - start_eval_time)))
    space()

    # TODO: run cartucho.py with subprocess


def run_eval_keras():
    print("Je dois run l'eval de fizyr/keras")
    # TODO: subprocess keras
