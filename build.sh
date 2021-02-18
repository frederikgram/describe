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
echo "Copied ./dev   -> ./prod
Old version: $old_version -> New version: $new_version"
cat <<< "$new_version" > "./prod/version"
