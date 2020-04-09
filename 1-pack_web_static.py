#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import run, local, sudo
from datetime import datetime


def do_pack():
    """Function to pack the contents of web_static folder"""

    bak_file = 'versions/web_static_{:s}.tgz'\
               .format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local('mkdir -p versions')
    command = local("tar -cvzf " + bak_file + " ./web_static/")
    if command.succeeded:
        return file_name
    return None
