<img src="icon.png" alt="Icon" width="128">

NUS Exam Paper Downloader
===============

Simple script to download exam papers from the NUS database. Requires NUSNET login.

Runs on Python 2.7 only.

### Using via Command Line
```
$ python examdownloader-cli.py <MODULE CODE> <NUSNET ID>
```

### Using via a Graphical User Interface
```
$ python examdownloader-gui.py
```


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
