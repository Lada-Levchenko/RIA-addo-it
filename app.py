# Testing generateDS classes

import IAPDclasses
from IAPDclasses import GeneratedsSuper
from utils.myutils import recursive_representation

rootObject = IAPDclasses.parse('IA_Indvl_Feeds1.xml', silence=True)
recursive_representation(rootObject)    # prints out proper json representation of objects

# this gave wrong result with excess fields

# import jsonpickle
# frozen = jsonpickle.encode(rootObject)
# print(frozen)
