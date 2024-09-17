import yt_dlp
import os
from pathlib import Path



def download_videos(url_file_path, output_path):
    # Read URLs from the text file
    if os.path.exists(url_file_path):
        with open(url_file_path, 'r') as file:
            urls = file.readlines()
    else:
        print(f"Error: The file {url_file_path} does not exist.")
        return

    # Strip any extra whitespace characters like newlines
    urls = [url.strip() for url in urls]

    # Check if the list of URLs is empty
    if not urls:
        print("❌❌ Your URLs file is empty ❌❌")
        return

    # Options for yt-dlp
    ydl_opts = {
        'format': 'best',  # Download the best quality available
        'outtmpl': output_path,  # Path to save the video
        'noplaylist': True,  # Download only the single video, not the entire playlist
    }

    # Download each video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)
    print("Video Successfully downloaded ✅")

def download_facebook_videos():
    base_path = Path(__file__).parent
    url_file_path = base_path / 'facebook_urls.txt'
    output_path = base_path / 'Downloads' / 'Facebook Videos' / '%(title)s.%(ext)s'
    download_videos(str(url_file_path), str(output_path))

def download_tiktok_videos():
    base_path = Path(__file__).parent
    url_file_path = base_path / 'tiktok_urls.txt'
    output_path = base_path / 'Downloads' / 'TikTok Videos' / '%(title)s.%(ext)s'
    download_videos(str(url_file_path), str(output_path))

def download_youtube_videos():
    base_path = Path(__file__).parent
    url_file_path = base_path / 'youtube_urls.txt'
    output_path = base_path / 'Downloads' / 'YouTube Videos' / '%(title)s.%(ext)s'
    download_videos(str(url_file_path), str(output_path))

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()  # Clear the screen before printing the header
    print("-"*149)
    print("\t\t\t\t\t" + "❤"*5 + " Welcome to the All-in-One Video Downloader " + "❤"*5)
    print("-"*149)
    print("Developer: \033[1;34mM.Ahmed\033[0m")  # Green color for name
    print("Contact: \033[1;33m0313-0258817\033[0m")  # Green color for name
    print("\t\t\t\t\t" + " "*96 + "Version: \033[1;32m1.0\033[0m")  # Green color for version
    print("-"*149)
    print("\n")

def main():

    print_header()

    while True:
        print("Choose an option for automatic video downloading:")
        print("1. Automatic Facebook videos Download ✅")
        print("2. Automatic TikTok videos Download ✅")
        print("3. Automatic YouTube videos Download ✅")
        print("Q. Quit")

        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            download_facebook_videos()
        elif choice == '2':
            download_tiktok_videos()
        elif choice == '3':
            download_youtube_videos()
        elif choice in ('Q', 'q'):
            print("Thank you! Goodbye and have a nice day ❤")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
