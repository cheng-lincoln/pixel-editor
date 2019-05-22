# About

Pixel-Editor is a lightweight python program for quick and easy frame editing. Pixel-Editor provides a GUI for you to design N by N frames and save them to a data file that is easily readable and compatible with most, if not all languages. 

For example, this tool was used for animating frames for LED displays / HATs for the Raspberry Pi.



# Setup

It is recommended to install and use the Anaconda Distribution of Python.

1) Install Anaconda for your operating system

2) Open the Anaconda Prompt (Windows), or the Terminal (Mac OSX / Linux)

3) Change to the project's directory. Assuming you saved this project's folder to `~/Desktop/pixel-editor`:

```bash
cd ~/Desktop/pixel-editor
```

4) Create a virtual environment to run this project:

```bash
conda create -n pixeleditorenv python=3.7.3 pip
```

5) Activate the environment and install the required dependencies

```bash
conda activate pixeleditorenv
pip install -r requirements.txt
```



# How to Use

1) To run the program, make sure that you are in the project's directory. Assuming you saved this project's folder to `~/Desktop/pixel-editor`:

```bash
cd ~/Desktop/pixel-editor
```

2) Run the program:

```python
python -m main data1
```

In the above example, if the file `data1` does not exist, it will be created in the `data` directory inside the project folder. If `data1` already exists, then it will be read and you could edit it via the GUI from there.