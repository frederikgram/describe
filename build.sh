if [ -d "./prod" ]
then
    if [ -f "./prod/version" ]
    then
        old_version=$(cat ./prod/version)
    else
        old_version="None"
        new_version=0
    fi
else
    mkdir ./prod
    old_version="None"
    new_version=0
fi

rm -r -f prod
cp -r dev prod

if [ -f "./dev/env/bin/activate" ]
then
    echo "> found virtualenv in ./dev"
    source ./dev/env/bin/activate
    echo "> freezing requirements into ./prod/requirements.txt"
    pip3 freeze > ./prod/requirements.txt
    echo "> removing ./prod/env"
    rm -r ./prod/env
fi
echo "> Copied ./dev   -> ./prod
> Old version: $old_version -> New version: $new_version"
cat <<< "$new_version" > "./prod/version"
