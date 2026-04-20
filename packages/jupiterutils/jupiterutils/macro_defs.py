from jupiterutils.Utility import JPT
import re
from jupiterutils.macro_material import *
import math 

DFLT_INT = 2147483647
DFLT_INT_64 = 4294967295
DFLT_DBL = 1.7976931348623158e+308
FLT_MAX = 3.402823466e+38

class CursorStr:
    def __init__(self, typeId, ids):
        self.typeId = typeId
        self.ids = ids
    def __str__(self):
        return ', '.join('{0}:{1}'.format(self.typeId, id_) for id_ in self.ids)
    def __repr__(self):
        return self.__str__()

cursorTypes = {
    0:   'Unknown',
    1:   'Project',
    2:   'Inst',
    3:   'Part',
    4:   'Vertex',
    5:   'Edge',
    6:   'Face',
    7:   'Solid',
    8:   'ShapeLink',
    9:   'BodyLink',
    10:  'Node',
    11:  'Elem',
    12:  'RefPart',
    13:  'RefVertex',
    14:  'RefEdge',
    15:  'RefFace',
    16:  'RefSolid',
    17:  'RefShapeLink',
    18:  'RefBodyLink',
    19:  'RefNode',
    20:  'RefElem',
    21:  'LocalSetting',
    22:  'Material',
    23:  'EntityAttrCADInfo',
    24:  'FemFieldScalar',
    25:  'FemFieldVector',
    26:  'FemFieldTensor',
    27:  'Coord',
    28:  'LoadCase',
    29:  'LbcForce',
    30:  'LbcForceND',
    31:  'LbcForceQuadratic',
    32:  'LbcForceSine',
    33:  'LbcForceVector',
    34:  'LbcNolin1',
    35:  'LbcNolin3',
    36:  'LbcNolin4',
    37:  'LbcConstraint',
    38:  'LbcEnforcedDisp',
    39:  'LbcGravity',
    40:  'LbcGPressure',
    41:  'LbcHPressure',
    42:  'LbcTPressure',
    43:  'LbcPressureQuadratic',
    44:  'LbcPressureSine',
    45:  'LbcTCentrifugalForce',
    46:  'LbcCSCentrifugalForce',
    47:  'LbcTempIni',
    48:  'LbcTempLoad',
    49:  'LbcTempLoadGeneral',
    50:  'LbcTempLoadADVCFile',
    51:  'LbcTempLoadNastran',
    52:  'LbcTempLoadADVCResultReference',
    53:  'LbcTempBoundary',
    54:  'LbcConcentrateFlux',
    55:  'LbcSurfaceFlux',
    56:  'LbcThermalConvection',
    57:  'LbcEnforcedVelocity',
    58:  'LbcEnforcedAcceleration',
    59:  'LbcDynamicInitialCondition',
    60:  'LbcContactClearance',
    61:  'LbcMappingPressure',
    62:  'LbcMappingForce',
    63:  'LbcMappingTempLoad',
    64:  'LbcMappingTempBoundary',
    65:  'LbcMappingThermalConvection',
    66:  'LbcInitStressGeneral',
    67:  'LbcInitStressMapping',
    68:  'LbcPretension',
    69:  'LbcPretensionAbaqus',
    70:  'LbcSurfaceLoads',
    71:  'LbcSubModelForcedDisp',
    72:  'LbcSubModelForcedTemp',
    73:  'LbcSubModelForcedFlux',
    74:  'LbcInsideHeatGeneration',
    75:  'LbcRigidWall',
    76:  'LbcInitAngularVelAbaqus',
    77:  'LbcWeld',
    78:  'SupGroup',
    79:  'Group',
    80:  'ElemEdgeGroup',
    81:  'FieldData',
    82:  'Property0DMass',
    83:  'Property1DBar',
    84:  'Property1DBeam',
    85:  'Property1DRod',
    86:  'Property1DPlot',
    87:  'Property2DShell',
    88:  'Property2DCompositeShell',
    89:  'Property3DSolid',
    90:  'Property3DGasket',
    91:  'Property3DCohesive',
    92:  'Property3DWeldBead',
    93:  'SectionGeneral',
    94:  'SectionLibrary',
    95:  'SectionSketcher',
    96:  'ConnectMpc',
    97:  'ConnectSpring',
    98:  'ConnectRbe2',
    99:  'ConnectConm',
    100: 'ConnectProd',
    101: 'ConnectRbar',
    102: 'ConnectRbe3',
    103: 'ConnectBush',
    104: 'ConnectMoment',
    105: 'ConnectWeld',
    106: 'ConnectDamper',
    107: 'ConnectConnector',
    108: 'ContactADVC',
    109: 'ContactNXNastran',
    110: 'ContactMSCNastran',
    111: 'ContactAbaqus',
    112: 'ContactAnsys',
    113: 'Contact',
    114: 'CustomAttrString',
    115: 'CustomAttrVector',
    116: 'CustomAttrDouble',
    117: 'DCS',
    118: 'ADVCProcess',
    119: 'ADVCProcessStatic',
    120: 'ADVCProcessDynamic',
    121: 'ADVCProcessEigen',
    122: 'ADVCProcessCreep',
    123: 'ADVCProcessDynamicExplicit',
    124: 'ADVCProcessFatigue',
    125: 'ADVCProcessModalFreqResp',
    126: 'ADVCProcessRespSpec',
    127: 'ADVCProcessRandResp',
    128: 'ADVCProcessSSH',
    129: 'ADVCProcessTH',
    130: 'ADVCJob',
    131: 'AbaqSteps',
    132: 'AbaqStepsStruct',
    133: 'AbaqStepsThermal',
    134: 'AbaqStepsStructStatic',
    135: 'AbaqStepsStructFrequency',
    136: 'AbaqStepsStructCoupledTD',
    137: 'AbaqStepsStructDynamic',
    138: 'AbaqStepsStructDynamicCoupledTD',
    139: 'AbaqStepsStructDynamicExplicit',
    140: 'AbaqStepsStructStaticRisk',
    141: 'AbaqStepsThermalSS',
    142: 'AbaqStepsThermalTransient',
    143: 'AbaqusJob',
    144: 'LbcMappingHeatFlux',
    145: 'ConnectGap',
    146: 'AnsysJob',
    147: 'NastranJob',
    148: 'DynamisJob',
    149: 'WeldOrder',
    150: 'AttributeFXWeld',
    151: 'ActranJob',
    152: 'LSDynaJob',
    153: 'NCS',
    154: 'AttributePSBlendSurface',
    155: 'LbcDOFSet',
    156: 'BeamPropAttr',
    157: 'BeamPropAttr2',
    158: 'ShellPropAttr',
    159: 'ConnPropAttr',
    160: 'LbcPretensionNXN',
    161: 'LbcMappingTempMarineEngine',
    162: 'UserProp',
    163: 'ConnectionElement',
    164: 'ContactTSSS',
    165: 'LbcMappingForcedDsiplacement',
    166: 'LbcMappingForcedTemp',
    167: 'NastranOP2PostJob',
    168: 'ADVC2PostJob',
    169: 'UserResult',
    170: 'LbcPretensionADVC',
    171: 'ContactTSSOlver',
    172: 'NastranHDF5PostJob',
    173: 'PermasJob',
    176: 'LbcPretensionSunShine',
    183: 'TSVPostJob',
    192: 'RONode',
    193: 'ROElem',
    195: 'PostFreqAnalysis',
    197: 'PostFreqLoad',
    202: 'PostTransLoadCase',
    204: 'PostTransLoad',
    216: 'PostActranLoadCase',
    221: 'PostFreqAnalysisSolver'
}

"""
Below code defines like the following functions.

def Inst(*ids):
    return CursorStr(2, ids)

def Part(*ids):
    return CursorStr(3, ids)

Part(1, 2) is not [Part(1), Part(2)] but Part(1), Part(2). It is only sequence.
[Part(1, 2), Elem(1)] is [Part(1), Part(2), Elem(1)].
"""
for k,v in cursorTypes.items():
    if 12 <= k <= 20: continue
    def func_(k):
        return lambda *ids: CursorStr(k, ids)
    locals()[v] = func_(k)

class ReferenceCursorStr:
    def __init__(self, typeId, extKeyIds):
        self.typeId = typeId
        self.extKeyIds = extKeyIds
    def __str__(self):
        return ', '.join('{}:{}-{}'.format(self.typeId, extId, keyId) for extId, keyId in self.extKeyIds)
    def __repr__(self):
        return self.__str__()

# for reference cursor
"""
Below code defines like the following functions.

def RefPart(*extKeyId):
    return ReferenceCursorStr(12, extKeyId)
"""
for k,v in cursorTypes.items():
    if 12 <= k <= 20:
        def func_(k):
           return lambda *ids: ReferenceCursorStr(k, ids)
        locals()[v] = func_(k)

class CursorPairStr:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __str__(self):
        return '{0}-{1}'.format(str(self.first), str(self.second))
    def __repr__(self):
        return self.__str__()

def CursorPair(first, second):
    return CursorPairStr(first, second)

def getCursorStr(cr):
    """
    >>> getCursorStr([10, 1])
    'Node(1)'
    """
    if cr == [0, 0]:
        return 'None'
    elif cr[0] in cursorTypes:
        return '{0}({1})'.format(cursorTypes[cr[0]], cr[1])

def getCursorListStr(crs):
    """
    >>> getCursorListStr([[10, 1], [10, 2], [11, 1]])
    '[Node(1, 2), Elem(1)]'
    """
    if crs == [[0, 0]]:
        return '[None]'
    crIds_d = {}
    for cr in crs:
        typeId, id_ = cr[0], cr[1]
        if typeId in cursorTypes:
            if typeId in crIds_d:
                crIds_d[typeId].append(id_)
            else:
                crIds_d[typeId] = [id_]
    crStrs = []
    for crType in sorted(crIds_d):
        crIds = crIds_d[crType]
        crStr = '{0}({1})'.format(cursorTypes[crType], ', '.join(str(id_) for id_ in crIds))
        crStrs.append(crStr)
    return '[' + ', '.join(crStr for crStr in crStrs) + ']'

def getCursorListListStr(crss):
    """
    >>> getCursorListListStr([[[6, 11]]])
    '[[Face(11)]]'
    """
    if crss == [[[0, 0]]]:
        return '[[None]]'
    crStrs = []
    for crs in crss:
        crStr = getCursorListStr(crs)
        crStrs.append(crStr)
    return '[' + ', '.join(crStr for crStr in crStrs) + ']'

def getCursorPairStr(crPair):
    """
    >>> getCursorPairStr([[10,75], [10,428]])
    'CursorPair(Node(75), Node(428))'
    """
    firstStr = getCursorStr(crPair[0])
    secondStr = getCursorStr(crPair[1])
    return 'CursorPair({0}, {1})'.format(firstStr, secondStr)

def getCursorPairListStr(crPairs):
    """
    >>> getCursorPairListStr([[[10,11], [10,22]], [[10,33], [10,44]]])
    '[CursorPair(Node(11), Node(22)), CursorPair(Node(33), Node(44))]'
    """
    return '[' + ', '.join(getCursorPairStr(crPair) for crPair in crPairs) + ']'

def getReferenceCursorStr(refCr):
    """
    >>> getReferenceCursorStr([12, 1, 1])
    'RefPart((1, 1))'
    """
    crTypeStr = cursorTypes[refCr[0]]
    extId = refCr[1]
    keyId = refCr[2]
    return '{0}(({1}, {2}))'.format(crTypeStr, extId, keyId)

def getReferenceCursorListStr(refCrs):
    """
    >>> getReferenceCursorListStr([[12, 1, 1], [12, 1, 2], [15, 1, 1]])
    '[RefPart((1, 1), (1, 2)), RefFace((1, 1))]'
    """
    if refCrs == [[0, 0, 0]]:
        return '[None]'
    crIds_d = {}
    for cr in refCrs:
        typeId, extId_, keyId_ = cr[0], cr[1], cr[2]
        if typeId in cursorTypes:
            if typeId in crIds_d:
                crIds_d[typeId].append((extId_, keyId_))
            else:
                crIds_d[typeId] = [(extId_, keyId_)]
    crStrs = []
    for crType in sorted(crIds_d):
        crIds = crIds_d[crType]
        crStr = '{0}({1})'.format(cursorTypes[crType], ', '.join('({}, {})'.format(extId_, keyId_) for extId_, keyId_ in crIds))
        crStrs.append(crStr)
    return '[' + ', '.join(crStr for crStr in crStrs) + ']'

def getBoolStr(val):
    """
    >>> getBoolStr(0)
    'False'
    >>> getBoolStr(1)
    'True'
    """
    if val:
        return 'True'
    else:
        return 'False'

def getBoolListStr(vals):
    """
    >>> getBoolListStr([0, 1, 1])
    '[False, True, True]'
    """
    return '[' + ', '.join('True' if val else 'False' for val in vals) + ']'

def getValueStr(val):
    if type(val) == list:
        vals = []
        for v in val:
            if type(v) == float and JPT.IsDefaultDouble(v):
                vals.append('DFLT_DBL')
            elif type(v) == int and JPT.IsDefaultInt(v):
                vals.append('DFLT_INT')
            else:
                vals.append(str(v))
        return '[' + ', '.join(v for v in vals) + ']'
    elif type(val) == float and JPT.IsDefaultDouble(val):
        return 'DFLT_DBL'
    elif type(val) == int and JPT.IsDefaultInt(val):
        return 'DFLT_INT'
    return str(val)

def normalizeDoubleType(val):
    """
    >>> normalizeDoubleType(1)
    1.0
    >>> normalizeDoubleType([1, 0, 0])
    [1.0, 0.0, 0.0]
    """
    if type(val) is list:
        if len(val) and type(val[0]) is list:
            return [[float(v) if not JPT.IsDefaultDouble(v) else DFLT_DBL for v in vec] for vec in val]
        else:
            return [float(v) if not JPT.IsDefaultDouble(v) else DFLT_DBL for v in val]
    elif type(val) is int:
        return float(val)
    else:
        return val if not JPT.IsDefaultDouble(val) else DFLT_DBL

def getCursorValue(cr):
    """
    >>> getCursorValue([10, 1])
    10:1
    """
    if cr == [0, 0]:
        return None
    else:
        return eval(getCursorStr(cr))

def getCursorListValue(crs):
    """
    >>> getCursorListValue([[10, 1], [10, 2], [11, 1]])
    [10:1, 10:2, 11:1]
    """
    if crs is [[0, 0]]:
        return [None]
    else:
        return [getCursorValue(cr) for cr in crs]

def getBoolValue(val):
    """
    >>> getBoolValue(0)
    False
    >>> getBoolValue(1)
    True
    """
    if val:
        return True
    else:
        return False

def getBoolValueFromString(val):
    """
    >>> getBoolValueFromString("0")
    False
    >>> getBoolValueFromString("1")
    True
    """
    if val == '1':
        return True
    else:
        return False
    
def getCursorValueStr(cr):
    """
    >>> getCursorValueStr(Node(1))
    'Node(1)'
    """
    if cr is None:
        return 'None'
    elif isinstance(cr, CursorStr):
        return '{0}({1})'.format(cursorTypes[cr.typeId], cr.ids[0])

def getCursorListValueStr(crs):
    """
    >>> getCursorListValueStr([Node(1, 2), Elem(1)])
    '[Node(1, 2), Elem(1)]'
    """
    if crs == [None]:
        return '[None]'
    crIds_d = {}
    for cr in crs:
        typeId, id_ = cr.typeId, list(cr.ids)
        if typeId in cursorTypes:
            if typeId in crIds_d:
                crIds_d[typeId].extend(id_)
            else:
                crIds_d[typeId] = id_
    crStrs = []
    for crType in sorted(crIds_d):
        crIds = crIds_d[crType]
        crStr = '{0}({1})'.format(cursorTypes[crType], ', '.join(str(id_) for id_ in crIds))
        crStrs.append(crStr)
    return '[' + ', '.join(crStr for crStr in crStrs) + ']'

def isNativeParam(param):
    return isinstance(param, list)

def isNativeParamList(param, clsType):
    if not isinstance(param, list):
        raise ValueError
    if param == []:
        return True
    return not any(isinstance(val, clsType) for val in param)

def getCursorValueByStr(crStr):
    if crStr == 'FAILED' or crStr == '0':
        return None    
    toks = crStr.split(':')
    cr = [int(toks[0]), int(toks[1])]
    return getCursorValue(cr)

def toCursor(crStr):
    toks = crStr.split(':')
    cr = [int(toks[0]), int(toks[1])]
    return cr
    
def getListCursorValueByStr(crStrs):
    if crStrs == 'FAILED' or crStrs == '0':
        return None 
    crStrs = crStrs.replace('[', '')
    crStrs = crStrs.replace(']', '')
    if not crStrs:
        return None
    toks = crStrs.split(',')
    crs = []
    for tok in toks:
        cr = toCursor(tok)
        crs.append(cr)
    pass
    return getCursorListValue(crs)

def getListDoubleValueByStr(doubleStr):
    doubleList = []
    if doubleStr == 'FAILED' or doubleStr == '0':
        return doubleList 
    doubleStr = doubleStr.replace('[', '')
    doubleStr = doubleStr.replace(']', '')
    toks = doubleStr.split(',')
    doubleList = []
    for tok in toks:
        doubleList.append(tok)
    pass
    return doubleList

def getDoubleValueByStr(doubleStr):
    doubleValue = 0.0
    if doubleStr == 'FAILED' or doubleStr == '0':
        return doubleValue 
    return float(doubleStr)
            
def getListIDValueByStrForAssemble(idStr, bMating = True):
    mtFacesList = []
    
    if idStr == 'FAILED' or idStr == '0':
        return mtFacesList    
    
    splitted = re.split(r',\s*(?![^(\[\]]*\])', idStr)
    FacePairs = splitted[1]
    
    mtFaces = FacePairs[1:-1].split(', ')
    
    for i in mtFaces:
        pair = i[1:-1].split('-')
        mtFacesList.append(int(pair[0]))
        if bMating == True:
            mtFacesList.append(int(pair[1]))
        
    return mtFacesList
        
def getCursorListValueByFindContactPairs(idStr):
    """
    >>> getCursorListValueByFindContactPairs('1, ["[6:24], [6:49, 6:54]"]')
    [[[6:24], [6:49, 6:54]]]
    """
    contact_pairs = []
    if idStr == 'FAILED' or idStr == '0':
        return contact_pairs
    def get_inner_str(str_, begin='[', end=']'):
        return str_[str_.find(begin)+1:str_.rfind(end)].strip()
    # remove return value
    # '1, ["[6:24], [6:49, 6:54]"]' => '["[6:24], [6:49, 6:54]"]'
    idStr = idStr[idStr.find(',')+1:].strip()
    # remove square bracket
    # '["[6:24], [6:49, 6:54]"]' => '"[6:24], [6:49, 6:54]"'
    idStr = get_inner_str(idStr)
    # split by comma to make pair list
    # '["[6:24], [6:49, 6:54]"]' => ['"[6:24], [6:49, 6:54]"']
    cnt = 0
    for i, s in enumerate(idStr):
        if '"' == s: cnt += 1
        if ',' == s and cnt == 2:
            cnt = 0
            idStr = idStr[:i] + '_' + idStr[i+1:]
    pair_list = [tok.strip() for tok in idStr.split('_')]
    def getFaceIDList(crStrs):
        crStrs = get_inner_str(crStrs)
        crs = []
        for tok in crStrs.split(','):
            type_, id_ = tok.split(':')
            crs.append(int(id_))
        return crs
    for pair in pair_list:
        # remove double quotation
        # '"[6:24], [6:49, 6:54]"' => '[6:24], [6:49, 6:54]'
        pair = get_inner_str(pair, '"', '"')
        # split by comma to divide master and slave
        # '[6:24], [6:49, 6:54]' => ['[6:24]', '[6:49, 6:54]']
        cnt = 0
        for i, s in enumerate(pair):
            if '[' == s or ']' == s: cnt += 1
            if ',' == s and cnt == 2:
                cnt = 0
                pair = pair[:i] + '_' + pair[i+1:]
        master_str, slave_str = [tok.strip() for tok in pair.split('_')]
        # get face ids
        # '[6:49, 6:54]' => [49, 54]
        master_ids = getFaceIDList(master_str)
        slave_ids = getFaceIDList(slave_str)
        # get face
        master = Face(*master_ids)
        slave = Face(*slave_ids)
        # append faces pairs
        contact_pairs.append([[master], [slave]])
    return contact_pairs

def getListOfListCursorValueByStr(crStrs):
    """
    >>> getListOfListCursorValueByStr('[[3:1, 3:2], [3:3, 3:4], [3:5, 3:6]]')
    [[3:1, 3:2], [3:3, 3:4], [3:5, 3:6]] # List
    """
    if crStrs == 'FAILED' or crStrs == '0':
        return None
    crStrs = crStrs[1:-1].replace('], [', ']; [')
    toks = crStrs.split(';')
    listCrs = []
    for sublist in toks:
        sublist = sublist.replace('[', '')
        sublist = sublist.replace(']', '')
        toks = sublist.split(',')
        crs = []
        for tok in toks:
            if not tok.strip():
                continue
            cr = toCursor(tok)
            crs.append(cr)
        listCrs.append(crs)
    return [getCursorListValue(crs) for crs in listCrs]

def convertAngleFromDegToRad(angle):
    return angle * math.pi / 180

# Sub-function for PostExportToTxt
getStringListStr = lambda strList: '[{0}]'.format(", ".join(f'"{string}"' for string in strList))

### NOTE: YOU HAVE TO ADD YOUR NEW FUNTION TO \macro\macro_defs.py also. It will support tool gen      
 
if __name__ == '__main__':
    import doctest
    doctest.testmod()