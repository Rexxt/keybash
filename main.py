# Keybash compiler in Python 3
# Follows Keybash 1.0.0
from sys import argv
import yaml

def compiler(args):
    # Project path
    _project_path = args[1] # Note => args = sys.argv
    _config_file = open(f"{_project_path}/keybash.yaml", 'r')
    _config_file_contents = yaml.load(_config_file, Loader=yaml.FullLoader)
    print("Overall")
    for key, value in _config_file_contents.items():
        print(f"{key}: {value}")
    print("Project")
    for key, value in _config_file_contents["Project"].items():
        print(f"{key}: {value}")
    print("Files")
    for key, value in _config_file_contents["Files"].items():
        print(f"{key}: {value}")

compiler(argv)