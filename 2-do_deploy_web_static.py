#!/usr/bin/python3
"""deploy with fabric"""
import os
from fabric.api import run, put, env

env.hosts = ['54.160.79.143', '18.233.65.33']


def do_deploy(archive_path):
    """deploy zipped web_static version"""

    if os.path.exists(archive_path) is False:
        return None
    # split the archive name from the path given
    archive_name = archive_path.split('/')[-1].split('.')[0]
    # the destination path where the unzipped dir would be saved
    path = '/data/web_static/releases'
    # process your archive in the remote machine
    if put(archive_path, '/tmp/').failed:
        return False
    if run('mkdir -p {}/{}'.format(path, archive_name)).failed:
        return False
    if run('tar -xzf /tmp/{1}.tgz -C {0}/{1}/'.format(path, 
                                                      archive_name)).failed:
        return False
    if run('rm /tmp/{}.tgz'.format(archive_name)).failed:
        return False
    if run('mv {0}/{1}/web_static/* {0}/{1}/'.format(path, 
                                                     archive_name)).failed:
        return False
    if run('rm -rf {}/{}/web_static'.format(path, archive_name)).failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run('ln -s {}/{}/ /data/web_static/current'
           .format(path, archive_name)).failed:
        return False
    
    return True
