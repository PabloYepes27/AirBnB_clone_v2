#!/usr/bin/python3
""" Write a Fabric script (based on the file
1-pack_web_static.py) that distributes an archive
to your web servers, using the function do_deploy
"""
from fabric.api import local, env, run, put
from datetime import datetime
from os import path

env.hosts = ['34.73.169.245', '35.231.18.60']


def do_pack():
    """[summary]"""
    local('mkdir -p versions')
    tar_dir = local("tar -czvf versions/web_static_{}.tgz web_static/".format((
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))), capture=True)

    if tar_dir.succeeded:
        return tar_dir
    return None


def do_deploy(archive_path):
    """[summary]"""
    # Returns False if the file at the path archive_path doesn’t exist
    if not path.exists(archive_path):
        return False
    try:
        file_path = archive_path.split("/")[1]
        serv_path = "/data/web_static/releases/{}".format(
            archive_path.replace(".tgz", "").split("/")[1])
        # Upload the archive to the /tmp/ directory of the web server
        put('{}'.format(archive_path), '/tmp/')
        # Uncompress the archive to the folde <..> on the web server
        run('tar -xzvf /tmp/{} -C {}'.format(
            file_path,
            serv_path))
        # Delete the archive from the web server
        run('rm /tmp/{}'.format(file_path))

        run('mv {}/web_static/* {}/'.format(serv_path, serv_path))

        # Delete the symbolic link <..> from the web server
        run('rm -rf {}/web_static'.format(
            serv_path))

        run('unlink /data/web_static/current')

        # Create a new Symbolic link, linked to the new version of your code
        run('ln -s {} /data/web_static/current'.format(
            serv_path))
        # Retur  True if all operations have been done correctly
        return True
    except:
        return False
