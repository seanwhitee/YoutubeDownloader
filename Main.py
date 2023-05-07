from pytube import YouTube
import ssl
import streamlit as st


def main():
    ssl._create_default_https_context = ssl._create_stdlib_context
    
    st.markdown("""# Download Youtube Video""")
    
    with st.form("my_form"):
        
        # User input url
        url = st.text_input(label='URL', placeholder='https://www.youtube.com/...')
        download_path = st.text_input(label='Download Path', placeholder='/Users/sean/Desktop/downloaded-video')
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            try:
                # Create youtube object
                yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
                stream = yt.streams.get_highest_resolution()
                stream.download(f"{download_path}")
                st.success(f"Successfully download {yt.title} to {download_path}")
                
            except Exception as e:
                st.error(e)
                
if __name__ == '__main__':
    main()