# Matroid Theory in Python

This is a repository to learn matroid theory with concrete examples.

## Usage

### 1. Download this repository and move to 

```bash
# Download this repository
$ git clone https://github.com/PotassiumIodide/matroid-theory-in-python.git

# Change directory
$ cd matroid-theory-in-python
```

### 2. pyenv
This project has been tested with Python 3.9.0.
If you're using version 3.9 or later, you can skip this step.
If you're using version 3.8 or earlier, you may need to update Python,
or use [pyenv](https://github.com/pyenv/pyenv):

```bash
# Download pyenv to $HOME/.pyenv (recommended)
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Settings of environment variables
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

# Add PATH
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

# Reload .bashrc
$ exec bash
```

Then install and switch to Python 3.9.0 with `pyenv`:

```bash
# Install Python 3.9.0
$ pyenv install 3.9.0

# Switch the version to 3.9.0
$ pyenv shell 3.9.0
```

### 3. venv


At first, make sure that the version of your Python is 3.9.0 or later:

```bash
$ python -V
3.9.0
```

and create a virtual environment with `venv`:

```bash
$ python -m venv .venv
```

and activate:

```bash
$ source .venv/bin/activate
```

To deactivate, run:

```bash
$ deactivate
```

> If you're using [direnv](https://github.com/direnv/direnv), you can automate the activatation 
> (as well as deactivatation) of the virtual environment by simply writing the following line in the `.envrc` file in this repository:
> ```
> source .venv/bin/activate
> ```
> For now, there is already `.envrc` but it may be removed for security reasons. 