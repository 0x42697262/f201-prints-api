# Requirements

You must have at least [Python 3.11](https://www.python.org/downloads/) and [PostgreSQL 15](https://www.python.org/downloads/) installed. If you are on a linux distro, please use your package manager to install.

Arch:

```
pacman -S python postgresql
```

# Setup

## Setup the virtual environment

Install `virtualenv` and `virtualenvwrapper` in your base Python environment.

```
pip install virtualenv
pip install virtualenvwrapper
```

Add these to your `.bashrc` or `.zshrc`

```sh
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

If you cannot find your `virtualenvwrapper.sh`, do a

```
find / -name "virtualenvwrapper.sh"
```

and use that as the source path.

Alternatively, you can source the provided shell at `./.shells/env.sh`.

After activating the virtual environment, create a new virtual environemnt

```
mkvirtualenv f201-prints
```

and activate

```
workon f201-prints
```

## Setup the dependencies

Install the dependencies

```
pip install -r requirements.txt
```

## Setup the environment file

Copy the `./.env.dist` file and rename it to `.env`.

```
DEBUG=boolean
SECRET_KEY=secret
POSTGRES_USERNAME=username
POSTGRES_PASSWORD=password
POSTGRES_HOST=host
ALLOWED_HOSTS=hosts
```
