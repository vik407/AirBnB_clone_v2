#!/usr/bin/env bash
# Setup webservers for web static AirBnB_clone_V2
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
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
# Adjust permissions
chown ubuntu:ubuntu -R /data
sed -i '/listen 80 default_server/a \\tlocation /hbnb_static/ {\n\t alias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
# Restart nginx
service nginx restart
# Exit with 0 code
exit 0
