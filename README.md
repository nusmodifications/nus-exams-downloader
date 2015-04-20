NUS Exam Paper Downloader
===============

Simple script to download exam papers from the NUS database. Requires NUSNET login.

### Compiling the Binary

1. Install `pyinstaller`:
```
$ pip install pyinstaller
```

2. Compile the app:
```
$ pyinstaller --onefile --windowed -i icon.icns -n 'NUS Exams Paper Downloader' examdownloader-gui.py
```
The compiled app can be found inside the `dist` folder. 

### Credits
- Oh Shunhao [(https://github.com/Ohohcakester)](https://github.com/Ohohcakester)
- Liu Xinan [(https://github.com/xinan)](https://github.com/xinan)
- Tay Yang Shun [(https://github.com/yangshun)](https://github.com/yangshun)
