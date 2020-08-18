from fabric.api import local
from datetime import datetime
from os import path

def do_pack():
    """[summary]"""
    local('mkdir -p versions')
    tar_dir = local("tar -czvf versions/web_static_{}.tgz web_static/".format((datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))), capture=True)

    if path.exists(tar_dir):
        return tar_dir
    return None
