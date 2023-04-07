# YoutubeDownloader 

[![Made with streamlit](https://img.shields.io/badge/Made%20with-streamlit-orange)](https://streamlit.io/)
[![MIT License](https://img.shields.io/badge/license-MIT-red)](https://github.com/seanwhitee/YoutubeDownloader/blob/main/license)
[![Made with python](https://img.shields.io/badge/Made%20with-Python-brightgreen)](https://www.python.org/)

## About
This is a simple python script to download youtube video via url.


## Dependency
- pytube
- streamlit

## Usage
1. Create a venv for your project.
```bash
python3 -m venv env

source env/bin/activate #Linux/Mac
env/Scripts/activate # Windows
```
2. Install dependencies.
```bash
pip install pytube
pip install streamlit
```

3. Run project

- If you want visualize using browser.
```bash
streamlit run Main.py
```
- If you want to run with python script
- Modify the code  in the Main.py file. (using terminal based input instead of streamlit brower based input).
- And using following command to run the script.

```bash
python3 Main.py
```

## License
[MIT](https://github.com/seanwhitee/YoutubeDownloader/blob/main/license)