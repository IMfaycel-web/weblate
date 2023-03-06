git pull --rebase
./manage.py migrate
./manage.py compilemessages
./manage.py collectstatic --noinput
./manage.py setuplang
