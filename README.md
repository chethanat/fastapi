```
# create an virtual environment
python -m venv virtual_env_name

# activate virtual environment
virtual_env_name/bin/activate

#Install dependencies
pip3 install -r requirements.txt

#uvicorn
it is async web server

# to run the flaskAPI
uvicorn main:app --reload  (reload flag will always reload the page if any new changes

#access the file under url 127.0.0.1:8000 and url path
Ex: https://127.0.0.1:8000/

you can get swagger doc under /docs
ex: https://127.0.0.1:8000/docs

# main.py
It is the main entry point for our FastApi application


```
