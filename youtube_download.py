import yt_dlp
import os

def list_formats(video_url):
    ydl_opts = {}
    
    common_resolutions = {
        '144p': 144,
        '240p': 240,
        '360p': 360,
        '480p': 480,
        '720p': 720,
        '1080p': 1080,
        '1440p': 1440,
        '2160p': 2160
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get('formats', [])
            
            best_formats = {}
            for f in formats:
                format_id = f.get('format_id', 'N/A')
                ext = f.get('ext', 'N/A')
                height = f.get('height', None)
                fps = f.get('fps', 0) or 0  # Assure que fps est un entier
                
                resolution = f"{height}p" if height else 'audio only'
                
                if height in common_resolutions.values() or 'audio only' in resolution:
                    if resolution not in best_formats or (fps > best_formats[resolution]['fps']):
                        best_formats[resolution] = {
                            'format_id': format_id,
                            'ext': ext,
                            'resolution': resolution,
                            'fps': fps
                        }
            
            format_list = []
            for resolution, data in best_formats.items():
                format_list.append(f"{data['format_id']} - {data['ext']} - {data['resolution']} - {data['fps']}fps")
            
            return format_list
    
    except Exception as e:
        print(f"Une erreur s'est produite lors de la récupération des formats: {e}")
        return []

def download_youtube_video(video_url, format_id, download_directory):
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
        
    ydl_opts = {
        'format': format_id + '+bestaudio/best',
        'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Téléchargement terminé!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Entrez l'URL de la vidéo Youtube: ")
    download_directory = input(r"Entrez le dossier de téléchargement \n (Windows: C:\Users\votre_nom\Videos\ ou C:\Users\votre_nom\Download\ \n Linux: /home/votre_nom/Videos/ ou /home/votre_nom/Téléchargements/): ")
    sub_folder = "Youtube_Downloader"
    download_directory = os.path.join(download_directory, sub_folder)
    formats = list_formats(video_url)
    
    if formats:
        print("Formats disponibles:")
        for idx, f in enumerate(formats, 1):
            print(f"{idx}. {f}")
        
        format_choice = int(input("Entrez le numéro du format de la vidéo que vous voulez : "))
        format_id = formats[format_choice - 1].split(" - ")[0]
        
        download_youtube_video(video_url, format_id, download_directory)
    else:
        print("Aucun format trouvé ou une erreur s'est produite.")
