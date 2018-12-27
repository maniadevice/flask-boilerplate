### Environment Requirements
* pyenv
- [Installation](https://github.com/pyenv/pyenv#installation)
* pipenv
- [Installation](https://pipenv.readthedocs.io/en/latest/install/#pragmatic-installation-of-pipenv)

### Instructions
* Open Pipfile and edit the python_version that you require for this project. If you do edit the version number, make sure that you have verified that the dependencies you're going to install are compatible with the python version.
* If your environment does not already have the python version you need, install it with pyenv. If you do, optionally you can set the python version inside the project root by running: 
```sh
pyenv local <<python_version>>
```
This makes sure running python within the folder will always refer to the version you chose. if the installation of the python version failed, try installing libffi-dev (```sudo apt install libffi-dev```)
* Now to setup your virtualenv and install dependencies
```sh
pipenv install
```
* Activate the shell for you virtual environment
```sh
pipenv shell
```

* To start the Flask server, run the following commands:
```sh
export FLASK_ENV=development
export FLASK_APP=run.py
flask run
```

Follow instructions from your terminal to verify your app is running. 

Note that in your project you would generally put instance/ folder in your .gitignore.

More flask documentation [here](http://flask.pocoo.org/docs). Enjoy! :)