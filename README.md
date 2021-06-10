# Flask-Blog
![GitHub all releases](https://img.shields.io/github/downloads/MLH-Fellowship/3.3.1.1-flask-blog/total?style=flat-square&logo=appveyor)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MLH-Fellowship/3.3.1.1-flask-blog?style=flat-square&logo=appveyor)
![GitHub](https://img.shields.io/github/license/MLH-Fellowship/3.3.1.1-flask-blog?style=flat-square&logo=appveyor)
![GitHub issues](https://img.shields.io/github/issues/MLH-Fellowship/3.3.1.1-flask-blog?style=flat-square&logo=appveyor)
![GitHub forks](https://img.shields.io/github/forks/MLH-Fellowship/3.3.1.1-flask-blog?style=flat-square&logo=appveyor)

## Introduction
Add introduction and description here. 
Minimal Flask template to get started on your blog application for MLH Fellowship Production Engineering track.

## Visuals
Add some screenies of the website :)   
Embed the video here as well!

## Prerequisites and Requirements
Flask version 2.0.1   
Python version 3.X

## Technologies Used
Python (Flask), Bootstrap, HTML/CSS.


## QuickStart Guide

### Installation for Windows 
Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv

```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

### Usage

Create a .env file using the example.env template

Start flask development server

```bash
$ export FLASK_ENV=development
$ flask run
```

###  Installation for Mac OS: 
Set up Python's default version from 2.7 to 3.x

Open ~/.bash_profile file:

```
vi ~/.bash_profile
```

Then put the alias as follows:

```
alias python='python3'
```

Now save the file and then run the ~/.bash_profile file:

```
source ~/.bash_profile
```

Congratulation !!! Now, you can use python3 by typing python. Check version by running:

```
python --version
```

After setting up, make sure to run all python commands with 3. For example, instead of:

```
python -m venv python3-virtualenv
```

run:

```
python3 -m venv python3-virtualenv
```

[for other versions](https://stackoverflow.com/questions/18425379/how-to-set-pythons-default-version-to-3-x-on-os-x)

## License
All assets are under the MIT license. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

