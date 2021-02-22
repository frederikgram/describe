if [ -d "./env" ]
then
    source ./env/bin/activate
else
    python3 -m venv env
    source ./env/bin/activate
    if [ -f "./requirements.txt" ]
    then
        pip3 install -r requirements.txt
    else
        echo "Error, could not install dependencies into newly created virtualenv: requirements.txt not found"
        exit 125
    fi
fi
export FLASK_APP=frontend
export FLASK_ENV=development
flask run
