# Testing generateDS classes

import IAPDclasses
from models import init_db

init_db()

rootObject = IAPDclasses.parse('resources/IA_Indvl_Feeds1.xml', silence=True)
