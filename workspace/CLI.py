import CLI_backend as cli

RUN = True

optionsValues = {
    0: "  0. Quitter", # OK!
    1: "  1. Inférer une image", # OK!
    2: "  2. Inférer le flux caméra", # OK!
    3: "  3. Evaluation by cartucho", # OK!
    4: "  4. In-build Keras evaluation", # TODO
    5: "  5. Modifier la valeur de threshold", # TODO
}

def processUserInput(usr_input):
    if usr_input == '0':
        exit()
    elif usr_input == '1':
        cli.run_inferer_img()
    elif usr_input == '2':
        cli.run_video()
    elif usr_input == '3':
        cli.run_eval_cartucho()
    elif usr_input == '4':
        cli.run_eval_keras()
    elif usr_input == '5':
        cli.run_edit_threshold()
    else:
        print("Erreur: should be unreachable")
        # Exception("usr_input value not handled.")
        return

def printHeader():
    print("  _   __  _____  _____   ___    _____")
    print(" | | / / |  ___ | ___ \  / _ \  /  ___|")
    print(" | |/ /  | |__  | |_/ / / /_\ \ \\ `--.")
    print(" |    \  |  __| |    /  |  _  |  `--. \\")
    print(" | |\  \ | |___ | |\ \  | | | | /\__/ /")
    print(" \_| \_/ \____/ \_| \_\ \_| |_/ \____/")
    print("****************  Mask Detector  ****************")
    print("Builded upon fizyr/keras-retinanet repository")
    print("Dataset: custom made by ESIREM 5th year student\n         under professor O. BROUSSE supervision.")
    print("*************************************************")
    print("       names          @ Github account")
    print("  Elouan  GOUINGUENET @ Skylli202")
    print("  Jérôme  MASSARD     @ JeromeMSD")
    print("*************************************************")

def printOptions():
    for i in optionsValues:
        print(optionsValues[i])
    print("Que souhaitez-vous faire ?")

def askOptions():
    usrInput = cli.askInput()
    return usrInput

def processOptionsChoice(usr_input):
    processUserInput(usr_input)


def mainCLI():
    while RUN:
        printHeader()
        printOptions()
        usr_input = askOptions()
        processOptionsChoice(usr_input)
