# Blank Python Repository

## Getting started:

### Pyenv

Set up `~/.bashrc`: Make sure the following lines are included
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Set up the virtual environment
```
# pyenv install 3.10.8 if not already installed
# Pick an appropriate ENV_NAME for the repo
pyenv virtualenv 3.10.8 ENV_NAME
pyenv shell ENV_NAME
```
Configure the repository as a python package
```
pip install -e .
```
