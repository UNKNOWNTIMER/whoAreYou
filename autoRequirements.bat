@echo off
::  Python 3.11.9
python --version | findstr "3.11.9"
if %errorlevel% equ 0 (
    echo Python 3.11.9 is already installed.
) else (
    echo Installing Python 3.11.9...
    curl -o python-3.11.9.exe https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
    start /wait python-3.11.9.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-3.11.9.exe
)

pip --version
if %errorlevel% equ 0 (
    echo pip is already installed.
) else (
    echo Installing pip...
    curl -o get-pip.py https://mirrors.aliyun.com/pypi/get-pip.py
    python get-pip.py
    del get-pip.py
)

pip show openai pillow pygame > nul
if %errorlevel% equ 0 (
    echo All required packages are already installed.
) else (
    echo Installing pip packages...
    pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip install openai pillow pygame -i https://pypi.tuna.tsinghua.edu.cn/simple
)
echo Installation complete!
pause
