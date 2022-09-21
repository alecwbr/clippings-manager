# clippings-manager

A simple flask app that turns your `My Clippings.txt` into a convenient API. Still a WIP.

## Getting Started

#### First make a virtual environment and activate it:

```
cd server
python3 -m venv venv
source venv/bin/activate
```

#### Next, install requirements.txt:

```
pip install -r requirements.txt
```

#### Create the database and seed it with a `My Clippings.txt` file:

```
python init_db.py
python load_file.py path/to/file.txt
```

#### Run the flask app:

```
export FLASK_APP=clippings_manager.py
flask run --no-debugger
```
