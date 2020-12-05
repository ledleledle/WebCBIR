# WebCBIR

This repo reffer from this <a href="https://github.com/ledleledle/CBIR">Repository</a> and i just convert it to some web. I'm using <a href="https://demos.creative-tim.com/argon-dashboard-pro/">Argon Template</a> which its nice :) . Its just like google image search but i just showing 5 picture most relevant (hopefully most relevant with object). Like always... Its just a school project. The datasets focus on desert, sea and mountain, also i add some wrong random image for testing. Sadly the datasets still have duplicate :(

# Dependencies that we need
- Python 3.x
- virtualenv

# Installation
### Arch Linux
```
sudo pacman -Syu python-pip
pip install virtualenv
```

### Ubuntu
```
sudo apt-get install python3-pip
pip3 install virtualenv
```

### Windows User
```
GTFO lossers!!!
```

# Requirements
Just run <code>pip install -r requirements.txt</code> and you'll be okay.

# Usage
- Go to cloned folder and activate <code>virtualenv</code>. Run <code>. venv/bin/activate</code>
- Then just run the python file <code>python runner.py</code>
- Open <code>localhost:5000</code> on your browser
- Enjoy
- If you want to update the dataset, Just do it from terminal (after you copy or change the images) run <code>python index-console.py</code>


# Preview
- Before Searching
![preview1](https://raw.githubusercontent.com/ledleledle/WebCBIR/master/wtf3.png)
- After Searching
![preview2](https://raw.githubusercontent.com/ledleledle/WebCBIR/master/wtf2.png)

My method is, you upload the image, opencv and numpy process your image, system will save image to the temporary folder, showing the result, and the <code>app.route('/')</code> i use for checking the temporary folder is there exist or not. I will keep update this project and keep find the best method for best result. Hope you enjoy

Sorry for my bad English :(
