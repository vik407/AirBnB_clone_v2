#!/usr/bin/env bash
# Setup webservers for web static AirBnB_clone_V2

apt-get update
apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'
# Create folders and and index file
mkdir -p /data/web_static/{releases/test,shared}
chown -R /data
cat >> /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
# Restart nginx
sudo service nginx restart
