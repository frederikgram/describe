if [ -d "./full_backup" ]
then
    rm -r ./full_backup
fi
mkdir ./full_backup
cp -r ./dev ./full_backup/dev
cp -r ./prod ./full_backup/dev
echo "Copied ./dev and ./prod -> ./full_backup"
