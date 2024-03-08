def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
    """
    Creates a .tgz archive from the contents of the web_static folder
    """
    """Creates the 'versions' directory if it doesn't exist"""
    local("mkdir -p versions")

    """Creates the archive filename with the current timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    """Creates the archive"""
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    """Checks if the archive was created successfully"""
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None


if __name__ == "__main__":
    do_pack()
