#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:
"""
from fabric.api import *
from os import path
from datetime import datetime


env.hosts = ['52.200.131.229', '54.146.160.217']
env.user = 'ubuntu'


def do_pack():
    """Function to pack the contents of web_static folder
    """
    bak_file = 'versions/web_static_{:s}.tgz'\
               .format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local('mkdir -p versions')
    command = local("tar -cvzf " + bak_file + " ./web_static/")
    if command.succeeded:
        return bak_file
    return None


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
    d_unpack = run('tar -xzf /tmp/' + archive_file + '.tgz' +
                   ' -C /data/web_static/releases/' + archive_file + '/')
    if d_unpack.failed:
        ret_value = False
    # Delete the archive from the web server
    d_cleanfile = run('rm /tmp/' + archive_file + '.tgz')
    if d_cleanfile.failed:
        ret_value = False
    # The files are created under a web_static folder move it.
    d_move = run('mv /data/web_static/releases/' + archive_file +
                 '/web_static/* /data/web_static/releases/' + archive_file +
                 '/')
    if d_move.failed:
        ret_value = False
    # Remove the now empty folder
    d_cleanfolder = run('rm -rf /data/web_static/releases/' + archive_file +
                        '/web_static')
    if d_cleanfolder.failed:
        ret_value = False
    # Delete the symbolic link /data/web_static/current from the web server
    d_removeold = run('rm -rf /data/web_static/current')
    if d_removeold.failed:
        ret_value = False
    # Create a new the symbolic link /data/web_static/current on the
    # web server, linked to the new version of your code
    # (/data/web_static/releases/<archive filename without extension>)
    d_createnew = run('ln -sf /data/web_static/releases/' + archive_file +
                      '/' + ' /data/web_static/current')
    if d_createnew.failed:
        ret_value = False
    # All set
    if ret_value:
        print("All tasks succeeded!")
    return ret_value


def do_clean(number=0):
    n = int(number)
    """Deletes out-of-date archives
    """
    with lcd('versions'):
        if n == 0 or n == 1:
            local('ls -t | tail -n +2 | xargs rm -rfv')
        else:
            local('ls -t | tail -n +{} | xargs rm -rfv'.format(n + 1))
    with cd('/data/web_static/releases/'):
        if n == 0 or n == 1:
            run('ls -t | tail -n +2 | xargs rm -rfv')
        else:
            run('ls -t | tail -n +{} | xargs rm -rfv'.format(n + 1))


def deploy():
    """Distribute to all servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
