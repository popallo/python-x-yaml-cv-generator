# Python x Yaml CV Gen 📄

Un générateur de CV professionnel utilisant Flask pour créer des CV élégants au format HTML et PDF à partir de données YAML.

## 🌟 Fonctionnalités

- Interface web responsive
- Export PDF
- Design moderne avec sidebar
- Support des emojis
- Mise en page optimisée pour le format A4
- Personnalisation via fichier YAML
- Support du HTML dans les textes
- Conteneurisation Docker

## 🚀 Installation

### Option 1 : Avec Docker (recommandé)

1. Cloner le dépôt :
```bash
git clone [URL_DU_REPO]
cd cv-generator
```

2. Construire et lancer avec Docker Compose :
```bash
docker-compose up -d --build
```

### Option 2 : Installation locale

#### Prérequis

- Python 3.8 ou supérieur
- pip
- pip (gestionnaire de paquets Python)



#### Installation du projet

1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# ou
.\venv\Scripts\activate  # Windows
```

2. Installer les dépendances Python :
```bash
pip install -r requirements.txt
```

3. Lancer l'application :
```bash
python app.py
```

## 📁 Structure des données

Les fichiers de CV et photos sont stockés dans les dossiers suivants :
```
cv-generator/
└── data/
    ├── cvs/            # Fichiers YAML de CV (incluant cv_sample.yaml)
    └── photos/         # Photos de profil (incluant photo_sample.jpg)
```

### Format des fichiers

1. CV YAML : 
   - Placez votre fichier YAML dans `data/cvs/`
   - Nommez-le avec un identifiant unique (ex: `mon-cv.yaml`)
   - Vous pouvez vous inspirer de l'exemple fourni `data/cvs/cv_sample.yaml`

2. Photo de profil :
   - Placez votre photo dans `data/photos/`
   - Nommez-la avec le même identifiant que votre CV (ex: `mon-cv.jpg`)
   - Formats supportés : JPG, JPEG, PNG

### Exemple de création de CV

1. Créez votre CV :
```bash
# Copier l'exemple
cp data/cvs/cv_sample.yaml data/cvs/mon-cv.yaml

# Éditer le fichier avec vos informations
nano data/cvs/mon-cv.yaml
```

2. Ajoutez votre photo :
```bash
cp votre-photo.jpg data/photos/mon-cv.jpg
```

3. Accédez à votre CV :
   - Ouvrez `http://localhost:5000` dans votre navigateur
   - Cliquez sur votre CV dans la liste
   - Ou accédez directement via `http://localhost:5000/cv/mon-cv`

## 📋 Format YAML

Le fichier YAML supporte les balises HTML dans les champs texte :
```yaml
cv:
  resume:
    summary: |
      <strong>Ingénieur DevOps</strong> avec plus de 8 ans d'expérience...
```

Structure complète :
```yaml
cv:
  resume:
    name: "Votre Nom"
    summary: "Votre résumé"
  
  experiences:
    - period: "2022 - Aujourd'hui"
      company: "Nom de l'entreprise"
      title: "Titre du poste"
      responsibilities:
        - "Description de la responsabilité 1"
        - "Description de la responsabilité 2"
  
  education:
    - period: "2018 - 2020"
      diploma: "Nom du diplôme"
      institution: "Nom de l'école"
  
  skills:
    technique:
      - "Compétence 1"
      - "Compétence 2"
    langues:
      - "Langue 1"
      - "Langue 2"
```

## 🛠️ Structure du projet

```
cv-generator/
├── app.py               # Application Flask
├── config/
│   └── settings.py      # Configuration du projet
├── data/               # Données des CV et photos
│   ├── cvs/
│   └── photos/
├── templates/          # Templates HTML
├── requirements.txt    # Dépendances Python
├── Dockerfile         
└── docker-compose.yaml
```

## ⚙️ Personnalisation du style

Le template utilise des variables CSS pour les couleurs et la mise en page :
- Les dimensions sont optimisées pour le format A4
- La mise en page utilise CSS Grid et Flexbox
- Les couleurs peuvent être modifiées via les variables CSS

## 🐳 Docker

### Variables d'environnement
- `FLASK_APP`: Nom de l'application Flask (défaut: app.py)
- `FLASK_ENV`: Environnement Flask (défaut: production)

### Volumes
- `./data:/app/data`: Stockage des CVs et photos (lecture/écriture)

### Ports
Le port 5000 est exposé et mappé sur l'hôte.

## 📄 Licence

MIT License - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commit vos changements
4. Push vers la branche
5. Ouvrir une Pull Request

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue.


### Linux : Installation des dépendances

WIP : Filtrer si dépendance inutiles ci-dessous. Elles ont été générées par l'assistant Claude 3.5.
```
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

### Windows : Installation des dépendances

```
A compléter 
```