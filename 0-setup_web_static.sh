#!/usr/bin/env bash
# A Bash script that sets up the web servers for the deployment of web_static

# Installs Nginx if not installed
if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt -y install nginx
fi

# Creates necessary directories
sudo mkdir -p /data/web_static/{releases/test,shared}

# Creates a fake HTML file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Creates or recreates symbolic link
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Gives ownership to ubuntu user and group
sudo chown -hR luc:luc /data/

# Updates Nginx configuration
config="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"
sudo sed -i "/server_name _;/a $config" /etc/nginx/sites-available/default

# Restarts Nginx
sudo service nginx restart

exit 0

