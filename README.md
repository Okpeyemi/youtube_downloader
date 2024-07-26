# 📥 YouTube Downloader

Ce script permet de lister les formats disponibles d'une vidéo YouTube et de télécharger le format souhaité.

## Prérequis

- Python 3.x doit être installé sur votre machine.
- `yt-dlp` doit être installé pour gérer le téléchargement des vidéos.
- FFmpeg doit être installé et configuré dans le PATH de votre système.

## Installation

### Étape 1 : Clonez le dépôt

Clonez ce dépôt sur votre machine locale :
```sh
git clone git@github.com:Okpeyemi/youtube_downloader.git
cd youtube_downloader
```
### Étape 2 : Installez les dépendances nécessaires

Installez `yt-dlp` via pip :
```sh
pip install yt-dlp
```

### Étape 3 : Téléchargez et installez FFmpeg
1. Rendez-vous sur le repo "BtbN/FFmep-Builds" officiel de [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases) et téléchargez la version récente et correspondante à votre système d'exploitation.
2. Extrayez les fichiers téléchargés.
3. Ajoutez le chemin vers le dossier bin de FFmpeg à la variable d'environnement PATH.

#### Instructions pour ajouter FFmpeg au PATH (Windows) :
1. Extrayez les fichiers téléchargés dans un dossier, par exemple `C:\ffmpeg`.
2. Ouvrez le Panneau de configuration, allez dans Système et sécurité > Système > Paramètres système avancés.
3. Cliquez sur Variables d'environnement.
4. Dans la section Variables système, trouvez la variable Path, sélectionnez-la et cliquez sur Modifier.
5. Ajoutez le chemin complet vers le dossier bin de FFmpeg (par exemple, `C:\ffmpeg\bin`) et cliquez sur `OK`.

#### Instructions pour ajouter FFmpeg au PATH (Linux) :
1. Extrayez les fichiers téléchargés dans un dossier, par exemple `~/ffmpeg`.
2. Ouvrez le fichier `~/.bashrc` avec votre éditeur de texte préféré.
3. Ajoutez la ligne suivante à la fin du fichier :
```sh
export PATH="$HOME/ffmpeg/bin:$PATH"
```
4. Sauvegardez le fichier et rechargez la configuration :
```sh
source ~/.bashrc
```

## Utilisation
Pour utiliser ce script, exécutez la commande suivante dans votre terminal :
```sh
python youtube_download.py
```

## Étapes pour utiliser le script :
1. Entrez l'URL de la vidéo YouTube que vous souhaitez télécharger.
2. Entrez le répertoire de téléchargement où vous souhaitez sauvegarder la vidéo. Par exemple :
    - Windows: `C:\Users\votre_nom\Videos\` ou `C:\Users\votre_nom\Download\`
    - Linux: `/home/votre_nom/Videos/` ou `/home/votre_nom/Téléchargements/`
3. Sélectionnez le format de la vidéo à partir de la liste des formats disponibles.
4. Le téléchargement commence et la vidéo est sauvegardée dans le répertoire spécifié.

### Exemple
Voici un exemple de session d'utilisation du script :
>Entrez l'URL de la vidéo Youtube: https://www.youtube.com/watch?v=example  
>Entrez le dossier de téléchargement (Windows: C:\Users\votre_nom\Videos\ ou C:\Users\votre_nom\Download\ | Linux: /home/votre_nom/Videos/ ou /home/votre_nom/Téléchargements/): /home/user/Videos/  
>Formats disponibles:  
>1. 18 - mp4 - 360p - 30fps
>2. 22 - mp4 - 720p - 30fps
>3. 137 - mp4 - 1080p - 30fps
>4. 140 - m4a - audio only - 0fps
>Entrez le numéro du format de la vidéo que vous voulez : 3  
>Téléchargement terminé!  

Ne faites pas attention au format audio :
>4. 140 - m4a - audio only - 0fps

Il se téléchargera tout seul. Laissez juste la magie opérée. ✨