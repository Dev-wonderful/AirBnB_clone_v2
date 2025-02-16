#!/usr/bin/python3
"""A fabfile to zip web_static folder"""
import os
from datetime import datetime
from fabric.api import *


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
