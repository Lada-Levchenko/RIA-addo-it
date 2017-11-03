#!/usr/bin/env python

#
# Generated Thu Nov  2 09:50:11 2017 by generateDS.py version 2.28.2.
# Python 3.5.2 (default, Nov 17 2016, 17:05:23)  [GCC 5.4.0 20160609]
#
# Command line options:
#   ('-a', 'xsd:')
#   ('-o', 'IAPDclasses.py')
#   ('-s', 'IAPDsubclasses.py')
#
# Command line arguments:
#   IAPDIndividualBulkFeed.xsd
#
# Command line:
#   generateDS.py -a "xsd:" -o "IAPDclasses.py" -s "IAPDsubclasses.py" IAPDIndividualBulkFeed.xsd
#
# Current working directory (os.getcwd()):
#   generateDS-2.28.2
#

import sys
from lxml import etree as etree_

import IAPDclasses as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class IAPDIndividualReportTypeSub(supermod.IAPDIndividualReportType):
    def __init__(self, GenOn=None, Indvls=None):
        super(IAPDIndividualReportTypeSub, self).__init__(GenOn, Indvls, )
supermod.IAPDIndividualReportType.subclass = IAPDIndividualReportTypeSub
# end class IAPDIndividualReportTypeSub


class IndvlsTypeSub(supermod.IndvlsType):
    def __init__(self, Indvl=None):
        super(IndvlsTypeSub, self).__init__(Indvl, )
supermod.IndvlsType.subclass = IndvlsTypeSub
# end class IndvlsTypeSub


class IndvlTypeSub(supermod.IndvlType):
    def __init__(self, Info=None, OthrNms=None, CrntEmps=None, Exms=None, Dsgntns=None, PrevRgstns=None, EmpHss=None, OthrBuss=None, DRPs=None):
        super(IndvlTypeSub, self).__init__(Info, OthrNms, CrntEmps, Exms, Dsgntns, PrevRgstns, EmpHss, OthrBuss, DRPs, )
supermod.IndvlType.subclass = IndvlTypeSub
# end class IndvlTypeSub


class InfoTypeSub(supermod.InfoType):
    def __init__(self, lastNm=None, firstNm=None, midNm=None, sufNm=None, indvlPK=None, actvAGReg=None, link=None):
        super(InfoTypeSub, self).__init__(lastNm, firstNm, midNm, sufNm, indvlPK, actvAGReg, link, )
supermod.InfoType.subclass = InfoTypeSub
# end class InfoTypeSub


class OthrNmsTypeSub(supermod.OthrNmsType):
    def __init__(self, OthrNm=None):
        super(OthrNmsTypeSub, self).__init__(OthrNm, )
supermod.OthrNmsType.subclass = OthrNmsTypeSub
# end class OthrNmsTypeSub


class OthrNmTypeSub(supermod.OthrNmType):
    def __init__(self, lastNm=None, firstNm=None, midNm=None, sufNm=None):
        super(OthrNmTypeSub, self).__init__(lastNm, firstNm, midNm, sufNm, )
supermod.OthrNmType.subclass = OthrNmTypeSub
# end class OthrNmTypeSub


class CrntEmpsTypeSub(supermod.CrntEmpsType):
    def __init__(self, CrntEmp=None):
        super(CrntEmpsTypeSub, self).__init__(CrntEmp, )
supermod.CrntEmpsType.subclass = CrntEmpsTypeSub
# end class CrntEmpsTypeSub


class CrntEmpTypeSub(supermod.CrntEmpType):
    def __init__(self, orgNm=None, orgPK=None, str1=None, str2=None, city=None, state=None, cntry=None, postlCd=None, CrntRgstns=None, BrnchOfLocs=None):
        super(CrntEmpTypeSub, self).__init__(orgNm, orgPK, str1, str2, city, state, cntry, postlCd, CrntRgstns, BrnchOfLocs, )
supermod.CrntEmpType.subclass = CrntEmpTypeSub
# end class CrntEmpTypeSub


class CrntRgstnsTypeSub(supermod.CrntRgstnsType):
    def __init__(self, CrntRgstn=None):
        super(CrntRgstnsTypeSub, self).__init__(CrntRgstn, )
supermod.CrntRgstnsType.subclass = CrntRgstnsTypeSub
# end class CrntRgstnsTypeSub


class CrntRgstnTypeSub(supermod.CrntRgstnType):
    def __init__(self, regAuth=None, regCat=None, st=None, stDt=None):
        super(CrntRgstnTypeSub, self).__init__(regAuth, regCat, st, stDt, )
supermod.CrntRgstnType.subclass = CrntRgstnTypeSub
# end class CrntRgstnTypeSub


class BrnchOfLocsTypeSub(supermod.BrnchOfLocsType):
    def __init__(self, BrnchOfLoc=None):
        super(BrnchOfLocsTypeSub, self).__init__(BrnchOfLoc, )
supermod.BrnchOfLocsType.subclass = BrnchOfLocsTypeSub
# end class BrnchOfLocsTypeSub


class BrnchOfLocTypeSub(supermod.BrnchOfLocType):
    def __init__(self, str1=None, str2=None, city=None, state=None, cntry=None, postlCd=None):
        super(BrnchOfLocTypeSub, self).__init__(str1, str2, city, state, cntry, postlCd, )
supermod.BrnchOfLocType.subclass = BrnchOfLocTypeSub
# end class BrnchOfLocTypeSub


class ExmsTypeSub(supermod.ExmsType):
    def __init__(self, Exm=None):
        super(ExmsTypeSub, self).__init__(Exm, )
supermod.ExmsType.subclass = ExmsTypeSub
# end class ExmsTypeSub


class ExmTypeSub(supermod.ExmType):
    def __init__(self, exmCd=None, exmNm=None, exmDt=None):
        super(ExmTypeSub, self).__init__(exmCd, exmNm, exmDt, )
supermod.ExmType.subclass = ExmTypeSub
# end class ExmTypeSub


class DsgntnsTypeSub(supermod.DsgntnsType):
    def __init__(self, Dsgntn=None):
        super(DsgntnsTypeSub, self).__init__(Dsgntn, )
supermod.DsgntnsType.subclass = DsgntnsTypeSub
# end class DsgntnsTypeSub


class DsgntnTypeSub(supermod.DsgntnType):
    def __init__(self, dsgntnNm=None):
        super(DsgntnTypeSub, self).__init__(dsgntnNm, )
supermod.DsgntnType.subclass = DsgntnTypeSub
# end class DsgntnTypeSub


class PrevRgstnsTypeSub(supermod.PrevRgstnsType):
    def __init__(self, PrevRgstn=None):
        super(PrevRgstnsTypeSub, self).__init__(PrevRgstn, )
supermod.PrevRgstnsType.subclass = PrevRgstnsTypeSub
# end class PrevRgstnsTypeSub


class PrevRgstnTypeSub(supermod.PrevRgstnType):
    def __init__(self, orgNm=None, orgPK=None, regBeginDt=None, regEndDt=None, BrnchOfLocs=None):
        super(PrevRgstnTypeSub, self).__init__(orgNm, orgPK, regBeginDt, regEndDt, BrnchOfLocs, )
supermod.PrevRgstnType.subclass = PrevRgstnTypeSub
# end class PrevRgstnTypeSub


class PrevBrnchOfLocsTypeSub(supermod.PrevBrnchOfLocsType):
    def __init__(self, BrnchOfLoc=None):
        super(PrevBrnchOfLocsTypeSub, self).__init__(BrnchOfLoc, )
supermod.PrevBrnchOfLocsType.subclass = PrevBrnchOfLocsTypeSub
# end class PrevBrnchOfLocsTypeSub


class PrevBrnchOfLocTypeSub(supermod.PrevBrnchOfLocType):
    def __init__(self, city=None, state=None):
        super(PrevBrnchOfLocTypeSub, self).__init__(city, state, )
supermod.PrevBrnchOfLocType.subclass = PrevBrnchOfLocTypeSub
# end class PrevBrnchOfLocTypeSub


class EmpHistsTypeSub(supermod.EmpHistsType):
    def __init__(self, EmpHs=None):
        super(EmpHistsTypeSub, self).__init__(EmpHs, )
supermod.EmpHistsType.subclass = EmpHistsTypeSub
# end class EmpHistsTypeSub


class EmpHistTypeSub(supermod.EmpHistType):
    def __init__(self, fromDt=None, toDt=None, orgNm=None, city=None, state=None):
        super(EmpHistTypeSub, self).__init__(fromDt, toDt, orgNm, city, state, )
supermod.EmpHistType.subclass = EmpHistTypeSub
# end class EmpHistTypeSub


class OthrBussTypeSub(supermod.OthrBussType):
    def __init__(self, OthrBus=None):
        super(OthrBussTypeSub, self).__init__(OthrBus, )
supermod.OthrBussType.subclass = OthrBussTypeSub
# end class OthrBussTypeSub


class OthrBusTypeSub(supermod.OthrBusType):
    def __init__(self, desc=None):
        super(OthrBusTypeSub, self).__init__(desc, )
supermod.OthrBusType.subclass = OthrBusTypeSub
# end class OthrBusTypeSub


class DRPsTypeSub(supermod.DRPsType):
    def __init__(self, DRP=None):
        super(DRPsTypeSub, self).__init__(DRP, )
supermod.DRPsType.subclass = DRPsTypeSub
# end class DRPsTypeSub


class DRPTypeSub(supermod.DRPType):
    def __init__(self, hasRegAction=None, hasCriminal=None, hasBankrupt=None, hasCivilJudc=None, hasBond=None, hasJudgment=None, hasInvstgn=None, hasCustComp=None, hasTermination=None):
        super(DRPTypeSub, self).__init__(hasRegAction, hasCriminal, hasBankrupt, hasCivilJudc, hasBond, hasJudgment, hasInvstgn, hasCustComp, hasTermination, )
supermod.DRPType.subclass = DRPTypeSub
# end class DRPTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IAPDIndividualReportType'
        rootClass = supermod.IAPDIndividualReportType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IAPDIndividualReportType'
        rootClass = supermod.IAPDIndividualReportType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IAPDIndividualReportType'
        rootClass = supermod.IAPDIndividualReportType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IAPDIndividualReportType'
        rootClass = supermod.IAPDIndividualReportType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
