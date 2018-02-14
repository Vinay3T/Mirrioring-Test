import os, sys

lib_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib')
sys.path.insert(0, lib_path)

from .app import app

if __name__ == "__main__":
    app.run()