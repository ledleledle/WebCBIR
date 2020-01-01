# WebCBIR

This repo reffer from this <a href="https://github.com/ledleledle/CBIR">Repository</a> and i just convert it to some web. I'm using <a href="https://demos.creative-tim.com/argon-dashboard-pro/">Argon Template</a> which its nice :) . Its just like google image search but i just showing 5 picture most relevant (hopefully most relevant with object). Like always... Its just a school project.

# Requirement
- Python 3.x
- virtualenv

Note : if you use <code>virtualenv</code> you don't need to install all the requirements, but if you using some local or cloud server like nginx or something, you must install all requirements!!!
-

# Requirement (if you're not using virtualenv)
- imuitils
- python-opencv
- numpy
- Pillow
- flask

Naaahhh... Just run <code>pip install -r requirements.txt</code>

# Usage
- Go to cloned folder and activate <code>virtualenv</code>. Run <code>. venv/bin/activate</code>
- Then just run the python file <code>python runner.py</code>
- Open <code>localhost:5000</code> on your browser
- Enjoy
- If you want to update the dataset, you can do it from web in the top right corner and follow the instructions. Or just do it from terminal (after you copy or change the images) run <code>python index-console.py</code>

FYI : if you got error when running this project, delete folder <code>venv</code> make new <code>virtualenv</code> and install all the requirements or just rename the project to <code>webcbir</code> lowercase! Or (again) run <code>virtualenv --relocatable</code> command on your terminal.
-

# Preview
- Sorry the preview still broken, i make some update on the front end. So... i delete all the screenshoots and will be update soon.... :) 
- Before Searching
![preview1](https://raw.githubusercontent.com/ledleledle/WebCBIR/master/Screenshot_2019-12-30_12-24-39.png)
- After Searching
![preview2](https://raw.githubusercontent.com/ledleledle/WebCBIR/master/Screenshot_2019-12-30_12-33-36.png)

My method is, you upload the image, opencv and numpy process your image, system will save image to the temporary folder, showing the result, and the <code>app.route('/')</code> i use for checking the temporary folder is there exist or not. I will keep update this project and keep find the best method for best result. Hope you enjoy
