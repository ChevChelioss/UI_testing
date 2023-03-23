import os
import ui_testing.resources


def create_path(name_file):
    return os.path.abspath(os.path.join(os.path.dirname(ui_testing.resources.__file__), name_file))
