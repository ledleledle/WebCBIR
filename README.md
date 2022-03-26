# WebCBIR

This repo reffer from this <a href="https://github.com/ledleledle/CBIR">Repository</a> and i just convert it to some web. I'm using <a href="https://demos.creative-tim.com/argon-dashboard-pro/">Argon Template</a> which its nice :) . Its just like google image search but i just showing 5 picture most relevant (hopefully most relevant with object). Like always... Its just a school project. The datasets focus on desert, sea and mountain, also i add some wrong random image for testing. Sadly the datasets still have duplicate :(

## Demo
Go to [cbir.leonprasetya.my.id](https://cbir.leonprasetya.my.id)

### Before you start
> - Don't ask me how to clone retard :)
> - My recommendation you have to use docker

# Dependencies that we need
- Python 3.x
- virtualenv

# Installation
### Arch Linux
```
sudo pacman -Syu python-pip python-virtualenv
```

### Ubuntu
[Follow this tutorial!](https://linoxide.com/linux-how-to/setup-python-virtual-environment-ubuntu). And
```
pip install --upgrade pip
sudo apt install libgl1-mesa-glx
```

### Windows
Too much GUI Installer and a bit tricky compared by Linux, and I didn't like that alot.<br>
[Follow this tutorial to install Python, pip and virtualenv](https://phoenixnap.com/kb/how-to-install-python-3-windows). Then you'll be okay. Also, if you're facing problem like this.
```
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\users\\sweet\\appdata\\local\\programs\\python\\python37\\Lib\\venv\\scripts\\nt\\python.exe'
```
Then you'll have to [read this](https://stackoverflow.com/questions/55380296/how-to-fix-error-errno-2-no-such-file-or-directory-c-program-files-pytho)!
<br>
**FYI** : For Windows users. No **GUI** please, only **CMD**.

# Usage
### Basic Usage
- Go to cloned folder `cd WebCBIR`
- Create virual environment **Arch Linux & Windows** `virtualenv venv` and for **Ubuntu** `python3 -m venv venv`
- Activate **virtualenv**. Run <code>source venv/bin/activate</code> for **Linux Family** or if you're **Windows user** run `.\venv\Scripts\activate.bat`
- Upgrade pip `pip install --upgrade pip`
- For requirements. Just run <code>pip install -r requirements.txt</code> and you'll be okay.
- Then just run the python file <code>python runner.py</code>
- Open <code>localhost:5000</code> on your browser
- Enjoy
- If you want to update the dataset, Just do it from terminal (after you copy or change the images) run <code>python index-console.py</code>

### Docker
We don't need install everything else, just install docker
```
docker build -t webcbir .
docker run -d --name webcbir -p 5000:5000 -v path_to_cloned_folder:/app webcbir
```
If you have any changes on source code, just restart the container
```
docker container restart webcbir
```

# Preview
- Before Searching
![preview1](screenshots/1.png)
- After Searching
![preview2](screenshots/2.png)

# Note
Make PR's if you have any problem and done solving it, or maybe you want contribute in this repository, I will very welcome you guys. Cheers 🍻

# TODO
- [X] Responsive Design
- [ ] Add & Update Dataset Feature
- [ ] Add more dataset for more acuracy 
