#!/usr/bin/env bash
# Setup webservers for web static AirBnB_clone_V2

apt-get update
apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'
# Create folders and and index file
mkdir -p /data/web_static/{releases/test,shared}
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
sed -i '/listen 80 default_server/a \\tlocation /hbnb_static/ {\n\t alias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
# Adjust permissions
chown ubuntu:ubuntu -R /data
# Restart nginx
sudo service nginx restart
# Exit with 0 code
exit 0
