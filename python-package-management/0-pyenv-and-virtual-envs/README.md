# pyenv

## Summary

Lets you install multiple versions of Python on your machine.

## Install

Intro: https://realpython.com/intro-to-pyenv/

Installation (via Homebrew): https://github.com/pyenv/pyenv#installation

## Usage

Install a version:
`pyenv install 3.4.0`

See the versions you have installed:
`pyenv versions`

See the version that will ren when you execute `python`:
`pyenv which python`

Set the version of Python that you would like pyenv to use in your project:
`pyenv local 3.8.7`



# virtual envs

## Summary

Isolates the environment of your project from your global python install. In other words, it allows you to install python packages in your project, rather than installing the packages onto your global python install, and it prevents Python packages installed on your global python install from getting used by your project.

## Install

If using Python 3.3 or newer, do to virtual envs, you only need `pyenv` and not `pyenv-virtualenv`. Per https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/

## Usage

### Create a Virtual Env

`python -m venv .venv`

```sh
project-dir/
|- .python-version
|- .venv/
  |- bin/
    |- a bunch of stuff
  |- include/
  |- lib/
    |- a bunch of stuff
  |- pyvenv.cfg
```

### Use a Virtual Env

#### Activate Your Virtual Env
aaron-macbook:python-sandbox houli$ `source venv/bin/activate`

#### Install a Package
(venv) aaron-macbook:python-sandbox houli$ `pip install PACKAGE_NAME`

#### See The Packages Installed in Your Virtual Env
(venv) aaron-macbook:python-sandbox houli$ `pip list`

#### Deactivate Your Virtual Env
(venv) aaron-macbook:python-sandbox houli$ `deactivate`

#### Run Your Flask App
(venv) aaron-macbook:python-sandbox houli$ `python app.py`



# pipx

You'll need some Python packages installed as CLI tools.

When you install a Python CLI tool with pipx, pipx gives it its own virtual env, so that its dependencies don't clash with the dependencies of other CLI tools you've installed.



## Example

`pip install awscli-local`

`pip install aws-sam-cli-local`
