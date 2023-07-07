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
    archived_file = 'web_static_{}.tgz'.format(date)
    cmd = 'tar -cvzf versions/{} web_static'.format(archived_file)
    result = local('{}'.format(cmd))
    if result.return_code == 0:
        size = os.path.getsize(os.path.join(full_path, archived_file))
        print('web_static packed: versions/{} -> {}Bytes'.format(archived_file,
                                                                 size))
    else:
        print('None')
