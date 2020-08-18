#!/usr/bin/env bash
# cript that sets up your web servers for the deployment of web_static
dpkg -s nginx &> /dev/null
result="echo $?"
if [ "$result" == 0 ]
then
    sudo apt-get -y update
    sudo apt-get install -y nginx
    sudo service nginx start
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

source_file="/data/web_static/current"
destiny_file="/data/web_static/releases/test/"
sudo ln -sf "$destiny_file" "$source_file"
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "38i \\\\tlocation /hbnb_static/ {\n\t\talias $source_file/;\n\tautoindex off;\n\t}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart