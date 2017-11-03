# Testing generateDS classes

import IAPDclasses
rootObject = IAPDclasses.parse('IA_Indvl_Feeds1.xml', silence=True)
print(rootObject.Indvls.Indvl[0].__dict__)
