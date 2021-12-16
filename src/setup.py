from os.path import exists
from os.path import join

# Sets up user and accounts, if they do not already exist

required_files = [join("src", "user_info.json"), join("src", "api_keys.json")]


def run_setup():
    create_required_files(required_files)


def create_required_files(files):
    for file in files:
        if not check_file(file):
            create_file(file)


def check_file(file_name):
    return exists(file_name)


def create_file(file_name):
    with open(file_name, "w"):
        pass


if __name__ == "__main__":
    run_setup()
