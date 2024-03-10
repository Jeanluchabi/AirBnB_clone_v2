#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder
    """
    # Create the 'versions' directory if it doesn't exist
    if not isdir("versions"):
        local("mkdir -p versions")

    # Create the archive filename with the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Create the archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Check if the archive was created successfully
    if result.return_code == 0:
        return "versions/{}".format(archive_name)
    else:
        return None


if __name__ == "__main__":
    do_pack()

