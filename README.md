# Flask-Blog

Minimal Flask template to get started on your blog application for MLH Fellowship Production Engineering track.

## Installation

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

## Usage

Create a .env file using the example.env template

Start flask development server

```bash
$ export FLASK_ENV=development
$ flask run
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Installation for Mac OS: Set up Python's default version from 2.7 to 3.x

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
