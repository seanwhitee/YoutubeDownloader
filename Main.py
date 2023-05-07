from pytube import YouTube
import ssl

def main():
    ssl._create_default_https_context = ssl._create_stdlib_context
    
        
    # User input url
    url = input("Youtube video url: ")
    download_path = input("Download path: ")
    
    
    # Create youtube object
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    stream = yt.streams.get_highest_resolution()
    stream.download(f"{download_path}")
            
                
if __name__ == '__main__':
    main()