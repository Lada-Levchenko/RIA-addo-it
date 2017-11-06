import IAPDclasses
import sys
from models import init_db

init_db()

rootObject = IAPDclasses.parse(sys.argv[1], silence=True)
