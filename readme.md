# Déploiement

```bash
git clone https://github.com/Skylli202/IA_MaskDetection.git

cd IA_MaskDetection
mkdir cartucho/input/detection-results
mkdir models

pip install tensorflow

cd keras-retinanet
python install . --user

```

Il vous faut maintenant mettre a jour les chemins relatifs vers les datasets dans `workspace/config.py`\
ou alors créer l'arborescence suivante :\
IA_MaskDetection\
    |__ catucho \
    |__ dataset \
    ---|__ CSV \
    ---|__ test \
    ---|---|__ Annotations \
    ---|---|__ Images \
    ---|__ train \
    ---|---|__ Annotations \
    ---|---|__ Images \
    |__ keras-retinanet \
    |__ models \
    |__ scripts \
    |__ workspace

Enfin copier les modèles fournis dans le répertoire `models/`.

# Lancer l'application console (CLI App)
```bash
cd <absolute path IA_MaskDetection>
python workspace/main.py
```

# Lancer keras-retinanet evaluate en console
```
python <absolute path IA_MaskDetection>/keras-retinanet/rekas_retinat/bin/evaluate.py --backbone resnet50 --gpu 0  csv <absolute path IA_MaskDetection>IA_MaskDetection/datasets/CSV/TEST_annotations.csv <absolute path IA_MaskDetection>/IA_MaskDetection/datasets/CSV/labels.csv <absolute path IA_MaskDetection>/IA_MaskDetection/models/resnet50_csv_17.h5 --convert-model
```

# Lancer cartucho en console
Il faut au préalable avoir placer dans `cartucho/input/detection-results` les fichiers de détections, et dans `cartucho/input/ground-truth` les fichiers ground-truth.
Le fichier python `workspace/cartucho.py` permet de générer ces fichiers.

```bash
cd <absolute path IA_MaskDetection>
python cartucho/cartucho.py
```
### Note
> Nous préconisons l'utilisation de cartucho au travers de l'application console.