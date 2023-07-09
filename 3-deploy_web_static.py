#!/usr/bin/python3
"""deploy script: all in one"""
import os
from datetime import datetime
from fabric.api import put, local, env, run

env.hosts = ['54.160.79.143', '18.233.65.33']


def do_pack():
    """pack the files"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    parent_dir = os.getcwd()
    full_path = os.path.join(parent_dir, 'versions')
    if not os.path.isdir('versions'):
        os.makedirs(full_path)
    archd_file = 'web_static_{}.tgz'.format(date)
    cmd = 'tar -cvzf versions/{} web_static'.format(archd_file)
    result = local('{}'.format(cmd))
    if result.return_code == 0:
        location = os.path.join(full_path, archd_file)
        size = os.path.getsize(location)
        print('web_static packed: versions/{} -> {}Bytes'.format(archd_file,
                                                                 size))
        return 'versions/{}'.format(archd_file)
    else:
        return None
    
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

def deploy():
    """Calls do_pack and do_deploy to merge the two tasks into one task"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    success_status = do_deploy(archive_path)
    return success_status
