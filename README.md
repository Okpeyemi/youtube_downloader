# 📥 YouTube Downloader

Script CLI en Python pour lister les formats disponibles d’une vidéo YouTube et télécharger le format souhaité avec fusion audio/vidéo via FFmpeg.

---

## 🚀 Fonctionnalités

- Liste les formats disponibles (résolutions courantes et pistes audio)
- Sélection du format par numéro (interface en ligne de commande)
- Fusion automatique de la meilleure piste audio avec la vidéo choisie
- Sortie en MP4 (via FFmpeg)
- Création d’un sous-dossier “Youtube_Downloader” dans le répertoire de destination

---

## 📦 Prérequis

- Python 3.x installé
- yt-dlp installé
- FFmpeg installé et disponible dans le PATH

---

## 🔧 Installation

1) Cloner le dépôt
```bash
git clone git@github.com:Okpeyemi/youtube_downloader.git
cd youtube_downloader
```

2) Installer la dépendance Python
```bash
pip install yt-dlp
```

3) Installer FFmpeg

- Windows:
  - Téléchargez un build récent depuis la page officielle des releases: https://github.com/BtbN/FFmpeg-Builds/releases
  - Extrayez par exemple vers C:\ffmpeg
  - Ajoutez C:\ffmpeg\bin à la variable d’environnement PATH

- macOS:
  - Avec Homebrew: brew install ffmpeg

- Linux (Debian/Ubuntu):
  - sudo apt update && sudo apt install -y ffmpeg

Vérification:
```bash
ffmpeg -version
```

---

## ▶️ Utilisation

Exécuter le script:
```bash
python youtube_download.py
```

Étapes dans le terminal:
1) Entrez l’URL de la vidéo YouTube
2) Entrez le répertoire de téléchargement (exemples)
   - Windows: C:\Users\votre_nom\Videos\ ou C:\Users\votre_nom\Downloads\
   - Linux: /home/votre_nom/Videos/ ou /home/votre_nom/Téléchargements/
   - macOS: /Users/votre_nom/Movies/ ou /Users/votre_nom/Downloads/
3) Choisissez le format par numéro dans la liste

Exemple de session:
```text
Entrez l'URL de la vidéo Youtube: https://www.youtube.com/watch?v=EXAMPLE
Entrez le dossier de téléchargement 
 (Windows: C:\Users\votre_nom\Videos\ ou C:\Users\votre_nom\Download\ 
 Linux: /home/votre_nom/Videos/ ou /home/votre_nom/Téléchargements/): C:\Users\me\Videos\
Formats disponibles:
1. 18 - mp4 - 360p - 30fps
2. 22 - mp4 - 720p - 30fps
3. 137 - mp4 - 1080p - 30fps
4. 251 - webm - audio only - 0fps
Entrez le numéro du format de la vidéo que vous voulez : 2
Téléchargement terminé!
```

Le script créera automatiquement un sous-dossier:
- Cible finale: <dossier_saisi>/Youtube_Downloader

---

## 🧠 Détails techniques

- Liste des formats: le script agrège les formats fournis par yt-dlp, retient les résolutions courantes (144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p) et “audio only”, puis conserve le meilleur fps par résolution.
- Téléchargement:
  - Option yt-dlp: format = <format_id> + "+bestaudio/best"
  - Fusion/encapsulation: merge_output_format = "mp4" (nécessite FFmpeg)
  - Modèle de nom de fichier: %(title)s.%(ext)s
- Fichier principal: youtube_download.py

---

## ❗ Dépannage

- ffmpeg not found / impossible de trouver FFmpeg
  - Assurez-vous que ffmpeg est installé et accessible dans votre PATH (voir section Installation).
- SSL: CERTIFICATE_VERIFY_FAILED
  - Mettez à jour certifi: pip install -U certifi
- Erreur de permission (Permission denied)
  - Vérifiez les droits d’écriture dans le répertoire de destination saisi.
- Formats vides ou vidéo restreinte
  - Certaines vidéos nécessitent des cookies/connexion; ce script n’inclut pas la gestion avancée (cookies, authentification).
- Format invalide ou hors plage
  - Entrez un numéro correspondant à la liste affichée.

---

## 🔒 Avertissement légal

Respectez les conditions d’utilisation de YouTube et les lois applicables dans votre pays. Ne téléchargez que du contenu dont vous détenez les droits ou pour lequel vous avez une autorisation.

---

## 📁 Structure du projet (simple)

```
.
├─ youtube_download.py
└─ README.md
```

---

## 🤝 Contributions

Les suggestions d’amélioration sont bienvenues:
- Ajout d’un requirements.txt
- Gestion des cookies pour les vidéos restreintes
- Téléchargements par lot (fournir un fichier d’URLs)
- Sélection avancée des formats (bitrate audio, codec, etc.)
- Emballage sous forme d’exécutable (PyInstaller)

Proposition classique:
1) Fork
2) Branche: git checkout -b feat/ma-feature
3) Commit: git commit -m "feat: description"
4) PR: ouvrez une Pull Request

---

## 📜 Licence

Aucune licence explicite trouvée dans le dépôt. Ajoutez un fichier LICENSE si nécessaire (MIT recommandé).

---

## 👤 Auteur

- GitHub: @Okpeyemi
