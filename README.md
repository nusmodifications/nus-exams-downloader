<img src="icon.png" alt="Icon" width="128">

NUS Exam Paper Downloader
===============

Simple script to download exam papers from the NUS database. Requires NUSNET login.

Runs on Python 2.7 only.

### Using via Command Line
```
$ python examdownloader-cli.py
```

The required username and target destination can be set in the script or passed as a command line argument.
If no command line arguments are provided, the user is prompted for input.

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
  $ pyinstaller build.spec
  ```
The compiled app can be found inside the `dist` folder.

### Credits

- Oh Shunhao [(https://github.com/Ohohcakester)](https://github.com/Ohohcakester)
- Liu Xinan [(https://github.com/xinan)](https://github.com/xinan)
- Yangshun Tay [(https://github.com/yangshun)](https://github.com/yangshun)
