import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from app import app, db
from app.models import Guest

if __name__ == "__main__":
    guests = Guest.query.all()
    for g in guests:
        print(g.name + " | " + g.email + " | " + g.attending)
