import os
from pathlib import Path
import configparser

class database(object):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    project_dir = Path(ROOT_DIR)
    #print(project_dir)
    userdata_location = (os.path.join(project_dir, 'authenticator.ini'))
    my_config_parser = configparser.ConfigParser()
    my_config_parser.read(userdata_location)
    userdata = my_config_parser["userdata"]
    #print(my_config_parser.sections())
