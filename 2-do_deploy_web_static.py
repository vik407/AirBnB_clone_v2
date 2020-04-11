#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy:
"""
from fabric.api import *
from os import path

env.hosts = ['52.200.131.229', '54.146.160.217']


def do_deploy(archive_path):
    """Deploy an archive to servers
    """
    if not path.exists(archive_path):
        return False
    ret_value = True
    # Set the folder
    d_folder = put(archive_path, '/tmp/')
    if d_folder.failed:
        ret_value = False
    # Prepare the file name and the destination folder
    archive_file = archive_path.replace(".tgz", "").replace("versions/", "")
    d_dest = run('mkdir -p /data/web_static/releases/' + archive_file + '/')
    if d_dest.failed:
        ret_value = False
    # Upload the archive to the /tmp/ directory of the web server
    # Uncompress the archive to the folder
    # /data/web_static/releases/<archive filename without extension>
    # on the web server
    c = run('tar -xzf /tmp/' + archive_file + '.tgz' +
            ' -C /data/web_static/releases/' + archive_file + '/')
    if c.failed:
        ret_value = False
    # Delete the archive from the web server
    d = run('rm /tmp/' + archive_file + '.tgz')
    if d.failed:
        ret_value = False
    # The files are created under a web_static folder move it.
    e = run('mv /data/web_static/releases/' + archive_file +
            '/web_static/* /data/web_static/releases/' + archive_file + '/')
    if e.failed:
        ret_value = False
    # Remove the now empty folder
    f = run('rm -rf /data/web_static/releases/' + archive_file + '/web_static')
    if f.failed:
        ret_value = False
    # Delete the symbolic link /data/web_static/current from the web server
    g = run('rm -rf /data/web_static/current')
    if g.failed:
        ret_value = False
    # Create a new the symbolic link /data/web_static/current on the web server,
    # linked to the new version of your code
    # (/data/web_static/releases/<archive filename without extension>)
    h = run('ln -sf /data/web_static/releases/' + archive_file +
            '/' + ' /data/web_static/current')
    if h.failed:
        ret_value = False
    # All set
    if ret_value:
        print("All tasks succeeded!")
    return ret_value
