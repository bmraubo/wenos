from os.path import exists

# Sets up user and accounts, if they do not already exist

required_files = ["user_info.json", "api_keys.json"]


def check_file(file_name):
    return exists(file_name)


def create_file(file_name):
    with open(file_name, "w"):
        pass
