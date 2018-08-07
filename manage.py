from app import app

import sys
import os
from flask_script import Manager


manage = Manager(app)
if __name__ == "__main__":
    app.run()