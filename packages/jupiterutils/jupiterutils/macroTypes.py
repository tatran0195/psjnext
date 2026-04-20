from jupiterutils.macro_defs import *

class CAD_SPATIAL_PARAM_DATA:
    def __init__(self,
        dSurfacePlaneTolerance=0.0,
        dSufacePlaneAngle=20.0,
        dMaxFacetWidth=0.1,
        bNXMultipart=True,
        bHealing=True):
        self.dSurfacePlaneTolerance = dSurfacePlaneTolerance
        self.dSufacePlaneAngle = dSufacePlaneAngle
        self.dMaxFacetWidth = dMaxFacetWidth
        self.bNXMultipart = bNXMultipart
        self.bHealing = bHealing
    def isDefault(self):
        obj =  CAD_SPATIAL_PARAM_DATA()
        return self.dSurfacePlaneTolerance == obj.dSurfacePlaneTolerance and \
            self.dSufacePlaneAngle == obj.dSufacePlaneAngle and \
            self.dMaxFacetWidth == obj.dMaxFacetWidth and \
            self.bNXMultipart == obj.bNXMultipart and \
            self.bHealing == obj.bHealing
    def fromList(self, cadSpatialParamData):
        obj =  CAD_SPATIAL_PARAM_DATA()
        self.dSurfacePlaneTolerance = normalizeDoubleType(cadSpatialParamData[0]) if len(cadSpatialParamData) > 0 else obj.dSurfacePlaneTolerance
        self.dSufacePlaneAngle = normalizeDoubleType(cadSpatialParamData[1]) if len(cadSpatialParamData) > 1 else obj.dSufacePlaneAngle
        self.dMaxFacetWidth = normalizeDoubleType(cadSpatialParamData[2]) if len(cadSpatialParamData) > 2 else obj.dMaxFacetWidth
        self.bNXMultipart = getBoolValue(cadSpatialParamData[3]) if len(cadSpatialParamData) > 3 else obj.bNXMultipart
        self.bHealing = getBoolValue(cadSpatialParamData[4]) if len(cadSpatialParamData) > 4 else obj.bHealing
        return self
    def __str__(self):
        obj =  CAD_SPATIAL_PARAM_DATA()
        paramArgs = []
        if self.dSurfacePlaneTolerance != obj.dSurfacePlaneTolerance:
            paramArgs.append('dSurfacePlaneTolerance={0}'.format(getValueStr(self.dSurfacePlaneTolerance)))
        if self.dSufacePlaneAngle != obj.dSufacePlaneAngle:
            paramArgs.append('dSufacePlaneAngle={0}'.format(getValueStr(self.dSufacePlaneAngle)))
        if self.dMaxFacetWidth != obj.dMaxFacetWidth:
            paramArgs.append('dMaxFacetWidth={0}'.format(getValueStr(self.dMaxFacetWidth)))
        if self.bNXMultipart != obj.bNXMultipart:
            paramArgs.append('bNXMultipart={0}'.format(getBoolStr(self.bNXMultipart)))
        if self.bHealing != obj.bHealing:
            paramArgs.append('bHealing={0}'.format(getBoolStr(self.bHealing)))
        return ' CAD_SPATIAL_PARAM_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            self.dSurfacePlaneTolerance,
            self.dSufacePlaneAngle,
            self.dMaxFacetWidth,
            1 if self.bNXMultipart else 0,
            1 if self.bHealing else 0) + rightBracket

class CAD_PROE_PARAM_DATA:
    def __init__(self,
                  dChordHeightTolerance = 0.0,
                  dAngleToleranceDegree = 20.0,
                  dStepMaxSize = 0.1):
        self.dChordHeightTolerance = dChordHeightTolerance
        self.dAngleToleranceDegree = dAngleToleranceDegree
        self.dStepMaxSize = dStepMaxSize
    def isDefault(self):
        obj = CAD_PROE_PARAM_DATA()
        return self.dChordHeightTolerance == obj.dChordHeightTolerance and \
               self.dAngleToleranceDegree == obj.dAngleToleranceDegree and \
               self.dStepMaxSize == obj.dStepMaxSize
    def fromList(self, cadProeParamData):
        obj = CAD_PROE_PARAM_DATA()
        self.dChordHeightTolerance = normalizeDoubleType(cadProeParamData[0]) if len(cadProeParamData) > 0 else obj.dChordHeightTolerance
        self.dAngleToleranceDegree = normalizeDoubleType(cadProeParamData[1]) if len(cadProeParamData) > 1 else obj.dAngleToleranceDegree
        self.dStepMaxSize = normalizeDoubleType(cadProeParamData[2]) if len(cadProeParamData) > 2 else obj.dStepMaxSize
        return self        
    def __str__(self):
        obj = CAD_PROE_PARAM_DATA()
        paramArgs = []
        if self.dChordHeightTolerance != obj.dChordHeightTolerance:
            paramArgs.append('dChordHeightTolerance={0}'.format(getValueStr(self.dChordHeightTolerance)))
        if self.dAngleToleranceDegree != obj.dAngleToleranceDegree:
            paramArgs.append('dAngleToleranceDegree={0}'.format(getValueStr(self.dAngleToleranceDegree)))
        if self.dStepMaxSize != obj.dStepMaxSize:
            paramArgs.append('dStepMaxSize={0}'.format(getValueStr(self.dStepMaxSize)))
        return 'CAD_PROE_PARAM_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.dChordHeightTolerance,
            self.dAngleToleranceDegree,
            self.dStepMaxSize) + rightBracket

class FORCE_LBC:
    def __init__(self,
        vecForce=[DFLT_DBL, DFLT_DBL, DFLT_DBL],
        vecMoment=[DFLT_DBL, DFLT_DBL, DFLT_DBL],
        iEndArrowDir=0,
        iEndDistribute=0,
        crCurCoord=None,
        crTable=None,
        crNodeSet=None,
        dPhase=0.0,
        dDelay=0.0,
        crPhaseTable=None,
        strFormulaTX="",
        strFormulaTY="",
        strFormulaTZ="",
        strFormulaRX="",
        strFormulaRY="",
        strFormulaRZ=""):
        self.vecForce = vecForce
        self.vecMoment = vecMoment
        self.iEndArrowDir = iEndArrowDir
        self.iEndDistribute = iEndDistribute
        self.crCurCoord = crCurCoord
        self.crTable = crTable
        self.crNodeSet = crNodeSet
        self.dPhase = dPhase
        self.dDelay = dDelay
        self.crPhaseTable = crPhaseTable
        self.strFormulaTX = strFormulaTX
        self.strFormulaTY = strFormulaTY
        self.strFormulaTZ = strFormulaTZ
        self.strFormulaRX = strFormulaRX
        self.strFormulaRY = strFormulaRY
        self.strFormulaRZ = strFormulaRZ
    def isDefault(self):
        obj = FORCE_LBC()
        return self.vecForce == obj.vecForce and \
            self.vecMoment == obj.vecMoment and \
            self.iEndArrowDir == obj.iEndArrowDir and \
            self.iEndDistribute == obj.iEndDistribute and \
            self.crCurCoord == obj.crCurCoord and \
            self.crTable == obj.crTable and \
            self.crNodeSet == obj.crNodeSet and \
            self.dPhase == obj.dPhase and \
            self.dDelay == obj.dDelay and \
            self.crPhaseTable == obj.crPhaseTable and \
            self.strFormulaTX == obj.strFormulaTX and \
            self.strFormulaTY == obj.strFormulaTY and \
            self.strFormulaTZ == obj.strFormulaTZ and \
            self.strFormulaRX == obj.strFormulaRX and \
            self.strFormulaRY == obj.strFormulaRY and \
            self.strFormulaRZ == obj.strFormulaRZ
    def fromList(self, param):
        obj = FORCE_LBC()
        self.vecForce = [normalizeDoubleType(tok) for tok in param[0]] if len(param) > 0 else obj.vecForce
        self.vecMoment = [normalizeDoubleType(tok) for tok in param[1]] if len(param) > 1 else obj.vecMoment
        self.iEndArrowDir = param[2] if len(param) > 2 else obj.iEndArrowDir
        self.iEndDistribute = param[3] if len(param) > 3 else obj.iEndDistribute
        self.crCurCoord = getCursorValue(param[4]) if len(param) > 4 else obj.crCurCoord
        self.crTable = getCursorValue(param[5]) if len(param) > 5 else obj.crTable
        self.crNodeSet = getCursorValue(param[6]) if len(param) > 6 else obj.crNodeSet
        self.dPhase = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dPhase
        self.dDelay = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dDelay
        self.crPhaseTable = getCursorValue(param[9]) if len(param) > 9 else obj.crPhaseTable
        self.strFormulaTX = param[10] if len(param) > 10 else obj.strFormulaTX
        self.strFormulaTY = param[11] if len(param) > 11 else obj.strFormulaTY
        self.strFormulaTZ = param[12] if len(param) > 12 else obj.strFormulaTZ
        self.strFormulaRX = param[13] if len(param) > 13 else obj.strFormulaRX
        self.strFormulaRY = param[14] if len(param) > 14 else obj.strFormulaRY
        self.strFormulaRZ = param[15] if len(param) > 15 else obj.strFormulaRZ
        return self
    def __str__(self):
        obj = FORCE_LBC()
        paramArgs = []
        if self.vecForce != obj.vecForce:
            paramArgs.append('vecForce={0}'.format(getValueStr(self.vecForce)))
        if self.vecMoment != obj.vecMoment:
            paramArgs.append('vecMoment={0}'.format(getValueStr(self.vecMoment)))
        if self.iEndArrowDir != obj.iEndArrowDir:
            paramArgs.append('iEndArrowDir={0}'.format(getValueStr(self.iEndArrowDir)))
        if self.iEndDistribute != obj.iEndDistribute:
            paramArgs.append('iEndDistribute={0}'.format(getValueStr(self.iEndDistribute)))
        if self.crCurCoord != obj.crCurCoord:
            paramArgs.append('crCurCoord={0}'.format(getCursorValueStr(self.crCurCoord)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        if self.crNodeSet != obj.crNodeSet:
            paramArgs.append('crNodeSet={0}'.format(getCursorValueStr(self.crNodeSet)))
        if self.dPhase != obj.dPhase:
            paramArgs.append('dPhase={0}'.format(getValueStr(self.dPhase)))
        if self.dDelay != obj.dDelay:
            paramArgs.append('dDelay={0}'.format(getValueStr(self.dDelay)))
        if self.crPhaseTable != obj.crPhaseTable:
            paramArgs.append('crPhaseTable={0}'.format(getCursorValueStr(self.crPhaseTable)))
        if self.strFormulaTX != obj.strFormulaTX:
            paramArgs.append('strFormulaTX={0}'.format('"' + self.strFormulaTX + '"'))
        if self.strFormulaTY != obj.strFormulaTY:
            paramArgs.append('strFormulaTY={0}'.format('"' + self.strFormulaTY + '"'))
        if self.strFormulaTZ != obj.strFormulaTZ:
            paramArgs.append('strFormulaTZ={0}'.format('"' + self.strFormulaTZ + '"'))
        if self.strFormulaRX != obj.strFormulaRX:
            paramArgs.append('strFormulaRX={0}'.format('"' + self.strFormulaRX + '"'))
        if self.strFormulaRY != obj.strFormulaRY:
            paramArgs.append('strFormulaRY={0}'.format('"' + self.strFormulaRY + '"'))
        if self.strFormulaRZ != obj.strFormulaRZ:
            paramArgs.append('strFormulaRZ={0}'.format('"' + self.strFormulaRZ + '"'))
        return 'FORCE_LBC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}'.format(
            self.vecForce,
            self.vecMoment,
            self.iEndArrowDir,
            self.iEndDistribute,
            str(self.crCurCoord) if self.crCurCoord is not None else '0:0',
            str(self.crTable) if self.crTable is not None else '0:0',
            str(self.crNodeSet) if self.crNodeSet is not None else '0:0',
            self.dPhase,
            self.dDelay,
            str(self.crPhaseTable) if self.crPhaseTable is not None else '0:0',
            '"' + self.strFormulaTX + '"',
            '"' + self.strFormulaTY + '"',
            '"' + self.strFormulaTZ + '"',
            '"' + self.strFormulaRX + '"',
            '"' + self.strFormulaRY + '"',
            '"' + self.strFormulaRZ + '"') + rightBracket

class RBAR_CONNECTION:
    def __init__(self,
        strName="",
        iEType=7,
        iMethod=1,
        crCoordSys=None,
        iCoordSys=0):
        self.strName = strName
        self.iEType = iEType
        self.iMethod = iMethod
        self.crCoordSys = crCoordSys
        self.iCoordSys = iCoordSys
    def isDefault(self):
        obj = RBAR_CONNECTION()
        return self.strName == obj.strName and \
            self.iEType == obj.iEType and \
            self.iMethod == obj.iMethod and \
            self.crCoordSys == obj.crCoordSys and \
            self.iCoordSys == obj.iCoordSys
    def fromList(self, param):
        obj = RBAR_CONNECTION()
        self.strName = param[0] if len(param) > 0 else obj.strName
        self.iEType = param[1] if len(param) > 1 else obj.iEType
        self.iMethod = param[2] if len(param) > 2 else obj.iMethod
        self.crCoordSys = getCursorValue(param[3]) if len(param) > 3 else obj.crCoordSys
        self.iCoordSys = param[4] if len(param) > 4 else obj.iCoordSys
        return self
    def __str__(self):
        obj = RBAR_CONNECTION()
        paramArgs = []
        if self.strName != obj.strName:
            paramArgs.append('strName={0}'.format('"' + self.strName + '"'))
        if self.iEType != obj.iEType:
            paramArgs.append('iEType={0}'.format(getValueStr(self.iEType)))
        if self.iMethod != obj.iMethod:
            paramArgs.append('iMethod={0}'.format(getValueStr(self.iMethod)))
        if self.crCoordSys != obj.crCoordSys:
            paramArgs.append('crCoordSys={0}'.format(getCursorValueStr(self.crCoordSys)))
        if self.iCoordSys != obj.iCoordSys:
            paramArgs.append('iCoordSys={0}'.format(getValueStr(self.iCoordSys)))
        return 'RBAR_CONNECTION({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            '"' + self.strName + '"',
            self.iEType,
            self.iMethod,
            str(self.crCoordSys) if self.crCoordSys is not None else '0:0',
            self.iCoordSys) + rightBracket

class ADVC_STRUCT_TIME_STEP:
    def __init__(self,
        iFixedOrAuto=0,
        iNumOfInc=1,
        dMaxTime=1.0,
        dMaxDt=DFLT_DBL,
        dMinDt=DFLT_DBL,
        iLoadType=-1,
        iOutputLast=-1,
        iOutputInterval=DFLT_INT,
        iRestartLast=-1,
        iRestartInterval=DFLT_INT,
        dOutputTimeInterval=DFLT_DBL,
        dRestartTimeInterval=DFLT_DBL,
        dInitDt=DFLT_DBL):
        self.iFixedOrAuto = iFixedOrAuto
        self.iNumOfInc = iNumOfInc
        self.dMaxTime = dMaxTime
        self.dMaxDt = dMaxDt
        self.dMinDt = dMinDt
        self.iLoadType = iLoadType
        self.iOutputLast = iOutputLast
        self.iOutputInterval = iOutputInterval
        self.iRestartLast = iRestartLast
        self.iRestartInterval = iRestartInterval
        self.dOutputTimeInterval = dOutputTimeInterval
        self.dRestartTimeInterval = dRestartTimeInterval
        self.dInitDt = dInitDt
    def isDefault(self):
        obj = ADVC_STRUCT_TIME_STEP()
        return self.iFixedOrAuto == obj.iFixedOrAuto and \
            self.iNumOfInc == obj.iNumOfInc and \
            self.dMaxTime == obj.dMaxTime and \
            self.dMaxDt == obj.dMaxDt and \
            self.dMinDt == obj.dMinDt and \
            self.iLoadType == obj.iLoadType and \
            self.iOutputLast == obj.iOutputLast and \
            self.iOutputInterval == obj.iOutputInterval and \
            self.iRestartLast == obj.iRestartLast and \
            self.iRestartInterval == obj.iRestartInterval and \
            self.dOutputTimeInterval == obj.dOutputTimeInterval and \
            self.dRestartTimeInterval == obj.dRestartTimeInterval and \
            self.dInitDt == obj.dInitDt
    def fromList(self, param):
        obj = ADVC_STRUCT_TIME_STEP()
        self.iFixedOrAuto = param[0] if len(param) > 0 else obj.iFixedOrAuto
        self.iNumOfInc = param[1] if len(param) > 1 else obj.iNumOfInc
        self.dMaxTime = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dMaxTime
        self.dMaxDt = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dMaxDt
        self.dMinDt = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dMinDt
        self.iLoadType = param[5] if len(param) > 5 else obj.iLoadType
        self.iOutputLast = param[6] if len(param) > 6 else obj.iOutputLast
        self.iOutputInterval = param[7] if len(param) > 7 else obj.iOutputInterval
        self.iRestartLast = param[8] if len(param) > 8 else obj.iRestartLast
        self.iRestartInterval = param[9] if len(param) > 9 else obj.iRestartInterval
        self.dOutputTimeInterval = normalizeDoubleType(param[10]) if len(param) > 10 else obj.dOutputTimeInterval
        self.dRestartTimeInterval = normalizeDoubleType(param[11]) if len(param) > 11 else obj.dRestartTimeInterval
        self.dInitDt = normalizeDoubleType(param[12]) if len(param) > 12 else obj.dInitDt
        return self
    def __str__(self):
        obj = ADVC_STRUCT_TIME_STEP()
        paramArgs = []
        if self.iFixedOrAuto != obj.iFixedOrAuto:
            paramArgs.append('iFixedOrAuto={0}'.format(getValueStr(self.iFixedOrAuto)))
        if self.iNumOfInc != obj.iNumOfInc:
            paramArgs.append('iNumOfInc={0}'.format(getValueStr(self.iNumOfInc)))
        if self.dMaxTime != obj.dMaxTime:
            paramArgs.append('dMaxTime={0}'.format(getValueStr(self.dMaxTime)))
        if self.dMaxDt != obj.dMaxDt:
            paramArgs.append('dMaxDt={0}'.format(getValueStr(self.dMaxDt)))
        if self.dMinDt != obj.dMinDt:
            paramArgs.append('dMinDt={0}'.format(getValueStr(self.dMinDt)))
        if self.iLoadType != obj.iLoadType:
            paramArgs.append('iLoadType={0}'.format(getValueStr(self.iLoadType)))
        if self.iOutputLast != obj.iOutputLast:
            paramArgs.append('iOutputLast={0}'.format(getValueStr(self.iOutputLast)))
        if self.iOutputInterval != obj.iOutputInterval:
            paramArgs.append('iOutputInterval={0}'.format(getValueStr(self.iOutputInterval)))
        if self.iRestartLast != obj.iRestartLast:
            paramArgs.append('iRestartLast={0}'.format(getValueStr(self.iRestartLast)))
        if self.iRestartInterval != obj.iRestartInterval:
            paramArgs.append('iRestartInterval={0}'.format(getValueStr(self.iRestartInterval)))
        if self.dOutputTimeInterval != obj.dOutputTimeInterval:
            paramArgs.append('dOutputTimeInterval={0}'.format(getValueStr(self.dOutputTimeInterval)))
        if self.dRestartTimeInterval != obj.dRestartTimeInterval:
            paramArgs.append('dRestartTimeInterval={0}'.format(getValueStr(self.dRestartTimeInterval)))
        if self.dInitDt != obj.dInitDt:
            paramArgs.append('dInitDt={0}'.format(getValueStr(self.dInitDt)))
        return 'ADVC_STRUCT_TIME_STEP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}'.format(
            self.iFixedOrAuto,
            self.iNumOfInc,
            self.dMaxTime,
            self.dMaxDt,
            self.dMinDt,
            self.iLoadType,
            self.iOutputLast,
            self.iOutputInterval,
            self.iRestartLast,
            self.iRestartInterval,
            self.dOutputTimeInterval,
            self.dRestartTimeInterval,
            self.dInitDt) + rightBracket

class ADVC_CONVERGENCE:
    def __init__(self,
        dCgTol=DFLT_DBL,
        dCgNrTol=DFLT_DBL,
        dCgDispTol=DFLT_DBL,
        dCgNrDispTol=DFLT_DBL,
        dCgDispLimitTol=DFLT_DBL,
        dCgTotalDispLimitTol=DFLT_DBL,
        dNewtonTol=DFLT_DBL,
        dNewtonDispTol=DFLT_DBL,
        dNewtonDispLimitTol=DFLT_DBL,
        dNewtonTotalDispLimitTol=DFLT_DBL,
        iCgloopMax=DFLT_INT,
        iNewtonMax=DFLT_INT,
        dHtNlLoopTol=DFLT_DBL,
        iHtNlLoopMax=DFLT_INT):
        self.dCgTol = dCgTol
        self.dCgNrTol = dCgNrTol
        self.dCgDispTol = dCgDispTol
        self.dCgNrDispTol = dCgNrDispTol
        self.dCgDispLimitTol = dCgDispLimitTol
        self.dCgTotalDispLimitTol = dCgTotalDispLimitTol
        self.dNewtonTol = dNewtonTol
        self.dNewtonDispTol = dNewtonDispTol
        self.dNewtonDispLimitTol = dNewtonDispLimitTol
        self.dNewtonTotalDispLimitTol = dNewtonTotalDispLimitTol
        self.iCgloopMax = iCgloopMax
        self.iNewtonMax = iNewtonMax
        self.dHtNlLoopTol = dHtNlLoopTol
        self.iHtNlLoopMax = iHtNlLoopMax
    def isDefault(self):
        obj = ADVC_CONVERGENCE()
        return self.dCgTol == obj.dCgTol and \
            self.dCgNrTol == obj.dCgNrTol and \
            self.dCgDispTol == obj.dCgDispTol and \
            self.dCgNrDispTol == obj.dCgNrDispTol and \
            self.dCgDispLimitTol == obj.dCgDispLimitTol and \
            self.dCgTotalDispLimitTol == obj.dCgTotalDispLimitTol and \
            self.dNewtonTol == obj.dNewtonTol and \
            self.dNewtonDispTol == obj.dNewtonDispTol and \
            self.dNewtonDispLimitTol == obj.dNewtonDispLimitTol and \
            self.dNewtonTotalDispLimitTol == obj.dNewtonTotalDispLimitTol and \
            self.iCgloopMax == obj.iCgloopMax and \
            self.iNewtonMax == obj.iNewtonMax and \
            self.dHtNlLoopTol == obj.dHtNlLoopTol and \
            self.iHtNlLoopMax == obj.iHtNlLoopMax
    def fromList(self, param):
        obj = ADVC_CONVERGENCE()
        self.dCgTol = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dCgTol
        self.dCgNrTol = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dCgNrTol
        self.dCgDispTol = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dCgDispTol
        self.dCgNrDispTol = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dCgNrDispTol
        self.dCgDispLimitTol = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dCgDispLimitTol
        self.dCgTotalDispLimitTol = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dCgTotalDispLimitTol
        self.dNewtonTol = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dNewtonTol
        self.dNewtonDispTol = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dNewtonDispTol
        self.dNewtonDispLimitTol = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dNewtonDispLimitTol
        self.dNewtonTotalDispLimitTol = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dNewtonTotalDispLimitTol
        self.iCgloopMax = param[10] if len(param) > 10 else obj.iCgloopMax
        self.iNewtonMax = param[11] if len(param) > 11 else obj.iNewtonMax
        self.dHtNlLoopTol = normalizeDoubleType(param[12]) if len(param) > 12 else obj.dHtNlLoopTol
        self.iHtNlLoopMax = param[13] if len(param) > 13 else obj.iHtNlLoopMax
        return self
    def __str__(self):
        obj = ADVC_CONVERGENCE()
        paramArgs = []
        if self.dCgTol != obj.dCgTol:
            paramArgs.append('dCgTol={0}'.format(getValueStr(self.dCgTol)))
        if self.dCgNrTol != obj.dCgNrTol:
            paramArgs.append('dCgNrTol={0}'.format(getValueStr(self.dCgNrTol)))
        if self.dCgDispTol != obj.dCgDispTol:
            paramArgs.append('dCgDispTol={0}'.format(getValueStr(self.dCgDispTol)))
        if self.dCgNrDispTol != obj.dCgNrDispTol:
            paramArgs.append('dCgNrDispTol={0}'.format(getValueStr(self.dCgNrDispTol)))
        if self.dCgDispLimitTol != obj.dCgDispLimitTol:
            paramArgs.append('dCgDispLimitTol={0}'.format(getValueStr(self.dCgDispLimitTol)))
        if self.dCgTotalDispLimitTol != obj.dCgTotalDispLimitTol:
            paramArgs.append('dCgTotalDispLimitTol={0}'.format(getValueStr(self.dCgTotalDispLimitTol)))
        if self.dNewtonTol != obj.dNewtonTol:
            paramArgs.append('dNewtonTol={0}'.format(getValueStr(self.dNewtonTol)))
        if self.dNewtonDispTol != obj.dNewtonDispTol:
            paramArgs.append('dNewtonDispTol={0}'.format(getValueStr(self.dNewtonDispTol)))
        if self.dNewtonDispLimitTol != obj.dNewtonDispLimitTol:
            paramArgs.append('dNewtonDispLimitTol={0}'.format(getValueStr(self.dNewtonDispLimitTol)))
        if self.dNewtonTotalDispLimitTol != obj.dNewtonTotalDispLimitTol:
            paramArgs.append('dNewtonTotalDispLimitTol={0}'.format(getValueStr(self.dNewtonTotalDispLimitTol)))
        if self.iCgloopMax != obj.iCgloopMax:
            paramArgs.append('iCgloopMax={0}'.format(getValueStr(self.iCgloopMax)))
        if self.iNewtonMax != obj.iNewtonMax:
            paramArgs.append('iNewtonMax={0}'.format(getValueStr(self.iNewtonMax)))
        if self.dHtNlLoopTol != obj.dHtNlLoopTol:
            paramArgs.append('dHtNlLoopTol={0}'.format(getValueStr(self.dHtNlLoopTol)))
        if self.iHtNlLoopMax != obj.iHtNlLoopMax:
            paramArgs.append('iHtNlLoopMax={0}'.format(getValueStr(self.iHtNlLoopMax)))
        return 'ADVC_CONVERGENCE({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}'.format(
            self.dCgTol,
            self.dCgNrTol,
            self.dCgDispTol,
            self.dCgNrDispTol,
            self.dCgDispLimitTol,
            self.dCgTotalDispLimitTol,
            self.dNewtonTol,
            self.dNewtonDispTol,
            self.dNewtonDispLimitTol,
            self.dNewtonTotalDispLimitTol,
            self.iCgloopMax,
            self.iNewtonMax,
            self.dHtNlLoopTol,
            self.iHtNlLoopMax) + rightBracket

class ADVC_CONTACT_ITER:
    def __init__(self,
        iSubdivideMode=-1,
        iContactloopMax=DFLT_INT,
        iInternalContactloopMax=DFLT_INT,
        dSeparationTol=DFLT_DBL,
        dRelativeSeparationTol=DFLT_DBL,
        dPenetrationTol=DFLT_DBL,
        dRelativePenetrationTol=DFLT_DBL,
        iMaxchp=DFLT_INT,
        iFrictionOnset=0,
        dStickSlipTol=DFLT_DBL,
        dFrictionTol=DFLT_DBL,
        iEstimateImpactTime=0):
        self.iSubdivideMode = iSubdivideMode
        self.iContactloopMax = iContactloopMax
        self.iInternalContactloopMax = iInternalContactloopMax
        self.dSeparationTol = dSeparationTol
        self.dRelativeSeparationTol = dRelativeSeparationTol
        self.dPenetrationTol = dPenetrationTol
        self.dRelativePenetrationTol = dRelativePenetrationTol
        self.iMaxchp = iMaxchp
        self.iFrictionOnset = iFrictionOnset
        self.dStickSlipTol = dStickSlipTol
        self.dFrictionTol = dFrictionTol
        self.iEstimateImpactTime = iEstimateImpactTime
    def isDefault(self):
        obj = ADVC_CONTACT_ITER()
        return self.iSubdivideMode == obj.iSubdivideMode and \
            self.iContactloopMax == obj.iContactloopMax and \
            self.iInternalContactloopMax == obj.iInternalContactloopMax and \
            self.dSeparationTol == obj.dSeparationTol and \
            self.dRelativeSeparationTol == obj.dRelativeSeparationTol and \
            self.dPenetrationTol == obj.dPenetrationTol and \
            self.dRelativePenetrationTol == obj.dRelativePenetrationTol and \
            self.iMaxchp == obj.iMaxchp and \
            self.iFrictionOnset == obj.iFrictionOnset and \
            self.dStickSlipTol == obj.dStickSlipTol and \
            self.dFrictionTol == obj.dFrictionTol and \
            self.iEstimateImpactTime == obj.iEstimateImpactTime
    def fromList(self, param):
        obj = ADVC_CONTACT_ITER()
        self.iSubdivideMode = param[0] if len(param) > 0 else obj.iSubdivideMode
        self.iContactloopMax = param[1] if len(param) > 1 else obj.iContactloopMax
        self.iInternalContactloopMax = param[2] if len(param) > 2 else obj.iInternalContactloopMax
        self.dSeparationTol = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dSeparationTol
        self.dRelativeSeparationTol = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dRelativeSeparationTol
        self.dPenetrationTol = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dPenetrationTol
        self.dRelativePenetrationTol = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dRelativePenetrationTol
        self.iMaxchp = param[7] if len(param) > 7 else obj.iMaxchp
        self.iFrictionOnset = param[8] if len(param) > 8 else obj.iFrictionOnset
        self.dStickSlipTol = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dStickSlipTol
        self.dFrictionTol = normalizeDoubleType(param[10]) if len(param) > 10 else obj.dFrictionTol
        self.iEstimateImpactTime = param[11] if len(param) > 11 else obj.iEstimateImpactTime
        return self
    def __str__(self):
        obj = ADVC_CONTACT_ITER()
        paramArgs = []
        if self.iSubdivideMode != obj.iSubdivideMode:
            paramArgs.append('iSubdivideMode={}'.format(getValueStr(self.iSubdivideMode)))
        if self.iContactloopMax != obj.iContactloopMax:
            paramArgs.append('iContactloopMax={}'.format(getValueStr(self.iContactloopMax)))
        if self.iInternalContactloopMax != obj.iInternalContactloopMax:
            paramArgs.append('iInternalContactloopMax={}'.format(getValueStr(self.iInternalContactloopMax)))
        if self.dSeparationTol != obj.dSeparationTol:
            paramArgs.append('dSeparationTol={}'.format(getValueStr(self.dSeparationTol)))
        if self.dRelativeSeparationTol != obj.dRelativeSeparationTol:
            paramArgs.append('dRelativeSeparationTol={}'.format(getValueStr(self.dRelativeSeparationTol)))
        if self.dPenetrationTol != obj.dPenetrationTol:
            paramArgs.append('dPenetrationTol={}'.format(getValueStr(self.dPenetrationTol)))
        if self.dRelativePenetrationTol != obj.dRelativePenetrationTol:
            paramArgs.append('dRelativePenetrationTol={}'.format(getValueStr(self.dRelativePenetrationTol)))
        if self.iMaxchp != obj.iMaxchp:
            paramArgs.append('iMaxchp={}'.format(getValueStr(self.iMaxchp)))
        if self.iFrictionOnset != obj.iFrictionOnset:
            paramArgs.append('iFrictionOnset={}'.format(getValueStr(self.iFrictionOnset)))
        if self.dStickSlipTol != obj.dStickSlipTol:
            paramArgs.append('dStickSlipTol={}'.format(getValueStr(self.dStickSlipTol)))
        if self.dFrictionTol != obj.dFrictionTol:
            paramArgs.append('dFrictionTol={}'.format(getValueStr(self.dFrictionTol)))
        if self.iEstimateImpactTime != obj.iEstimateImpactTime:
            paramArgs.append('iEstimateImpactTime={}'.format(getValueStr(self.iEstimateImpactTime)))
        return 'ADVC_CONTACT_ITER({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}'.format(
            self.iSubdivideMode,
            self.iContactloopMax,
            self.iInternalContactloopMax,
            self.dSeparationTol,
            self.dRelativeSeparationTol,
            self.dPenetrationTol,
            self.dRelativePenetrationTol,
            self.iMaxchp,
            self.iFrictionOnset,
            self.dStickSlipTol,
            self.dFrictionTol,
            self.iEstimateImpactTime) + rightBracket

class ADVC_AUTO_INCREMENT:
    def __init__(self,
        iNewtonResidueIncrMax=DFLT_INT,
        iBeginResidueIncrCheck=DFLT_INT,
        iBeginLogarithmicRateCheck=DFLT_INT,
        dCutBackFactorForDivergence=DFLT_DBL,
        dCutBackFactorForTooSlowConvergence=DFLT_DBL,
        dCutBackFactorForExcessiveDistortion=DFLT_DBL,
        iIncrEnlargeNewtonMax=DFLT_INT,
        iIncrEnlargeSuppress=DFLT_INT,
        dIncreaseFactorForStatic=DFLT_DBL,
        dIncreaseFactorForDynamic=DFLT_DBL,
        dIncreaseFactorForCreep=DFLT_DBL,
        dIncreaseFactorForRdnlk=DFLT_DBL,
        dTemperatureIncrMax=DFLT_DBL,
        iUseTemperatureIncrMax=0,
        dHalfStepTol=DFLT_DBL,
        dStraTol=DFLT_DBL,
        dCreepStraTol=DFLT_DBL,
        dRdnlkStraTol=DFLT_DBL):
        self.iNewtonResidueIncrMax = iNewtonResidueIncrMax
        self.iBeginResidueIncrCheck = iBeginResidueIncrCheck
        self.iBeginLogarithmicRateCheck = iBeginLogarithmicRateCheck
        self.dCutBackFactorForDivergence = dCutBackFactorForDivergence
        self.dCutBackFactorForTooSlowConvergence = dCutBackFactorForTooSlowConvergence
        self.dCutBackFactorForExcessiveDistortion = dCutBackFactorForExcessiveDistortion
        self.iIncrEnlargeNewtonMax = iIncrEnlargeNewtonMax
        self.iIncrEnlargeSuppress = iIncrEnlargeSuppress
        self.dIncreaseFactorForStatic = dIncreaseFactorForStatic
        self.dIncreaseFactorForDynamic = dIncreaseFactorForDynamic
        self.dIncreaseFactorForCreep = dIncreaseFactorForCreep
        self.dIncreaseFactorForRdnlk = dIncreaseFactorForRdnlk
        self.dTemperatureIncrMax = dTemperatureIncrMax
        self.iUseTemperatureIncrMax = iUseTemperatureIncrMax
        self.dHalfStepTol = dHalfStepTol
        self.dStraTol = dStraTol
        self.dCreepStraTol = dCreepStraTol
        self.dRdnlkStraTol = dRdnlkStraTol
    def isDefault(self):
        obj = ADVC_AUTO_INCREMENT()
        return self.iNewtonResidueIncrMax == obj.iNewtonResidueIncrMax and \
            self.iBeginResidueIncrCheck == obj.iBeginResidueIncrCheck and \
            self.iBeginLogarithmicRateCheck == obj.iBeginLogarithmicRateCheck and \
            self.dCutBackFactorForDivergence == obj.dCutBackFactorForDivergence and \
            self.dCutBackFactorForTooSlowConvergence == obj.dCutBackFactorForTooSlowConvergence and \
            self.dCutBackFactorForExcessiveDistortion == obj.dCutBackFactorForExcessiveDistortion and \
            self.iIncrEnlargeNewtonMax == obj.iIncrEnlargeNewtonMax and \
            self.iIncrEnlargeSuppress == obj.iIncrEnlargeSuppress and \
            self.dIncreaseFactorForStatic == obj.dIncreaseFactorForStatic and \
            self.dIncreaseFactorForDynamic == obj.dIncreaseFactorForDynamic and \
            self.dIncreaseFactorForCreep == obj.dIncreaseFactorForCreep and \
            self.dIncreaseFactorForRdnlk == obj.dIncreaseFactorForRdnlk and \
            self.dTemperatureIncrMax == obj.dTemperatureIncrMax and \
            self.iUseTemperatureIncrMax == obj.iUseTemperatureIncrMax and \
            self.dHalfStepTol == obj.dHalfStepTol and \
            self.dStraTol == obj.dStraTol and \
            self.dCreepStraTol == obj.dCreepStraTol and \
            self.dRdnlkStraTol == obj.dRdnlkStraTol
    def fromList(self, param):
        obj = ADVC_AUTO_INCREMENT()
        self.iNewtonResidueIncrMax = param[0] if len(param) > 0 else obj.iNewtonResidueIncrMax
        self.iBeginResidueIncrCheck = param[1] if len(param) > 1 else obj.iBeginResidueIncrCheck
        self.iBeginLogarithmicRateCheck = param[2] if len(param) > 2 else obj.iBeginLogarithmicRateCheck
        self.dCutBackFactorForDivergence = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dCutBackFactorForDivergence
        self.dCutBackFactorForTooSlowConvergence = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dCutBackFactorForTooSlowConvergence
        self.dCutBackFactorForExcessiveDistortion = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dCutBackFactorForExcessiveDistortion
        self.iIncrEnlargeNewtonMax = param[6] if len(param) > 6 else obj.iIncrEnlargeNewtonMax
        self.iIncrEnlargeSuppress = param[7] if len(param) > 7 else obj.iIncrEnlargeSuppress
        self.dIncreaseFactorForStatic = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dIncreaseFactorForStatic
        self.dIncreaseFactorForDynamic = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dIncreaseFactorForDynamic
        self.dIncreaseFactorForCreep = normalizeDoubleType(param[10]) if len(param) > 10 else obj.dIncreaseFactorForCreep
        self.dIncreaseFactorForRdnlk = normalizeDoubleType(param[11]) if len(param) > 11 else obj.dIncreaseFactorForRdnlk
        self.dTemperatureIncrMax = normalizeDoubleType(param[12]) if len(param) > 12 else obj.dTemperatureIncrMax
        self.iUseTemperatureIncrMax = param[13] if len(param) > 13 else obj.iUseTemperatureIncrMax
        self.dHalfStepTol = normalizeDoubleType(param[14]) if len(param) > 14 else obj.dHalfStepTol
        self.dStraTol = normalizeDoubleType(param[15]) if len(param) > 15 else obj.dStraTol
        self.dCreepStraTol = normalizeDoubleType(param[16]) if len(param) > 16 else obj.dCreepStraTol
        self.dRdnlkStraTol = normalizeDoubleType(param[17]) if len(param) > 17 else obj.dRdnlkStraTol
        return self
    def __str__(self):
        obj = ADVC_AUTO_INCREMENT()
        paramArgs = []
        if self.iNewtonResidueIncrMax != obj.iNewtonResidueIncrMax:
            paramArgs.append('iNewtonResidueIncrMax={}'.format(getValueStr(self.iNewtonResidueIncrMax)))
        if self.iBeginResidueIncrCheck != obj.iBeginResidueIncrCheck:
            paramArgs.append('iBeginResidueIncrCheck={}'.format(getValueStr(self.iBeginResidueIncrCheck)))
        if self.iBeginLogarithmicRateCheck != obj.iBeginLogarithmicRateCheck:
            paramArgs.append('iBeginLogarithmicRateCheck={}'.format(getValueStr(self.iBeginLogarithmicRateCheck)))
        if self.dCutBackFactorForDivergence != obj.dCutBackFactorForDivergence:
            paramArgs.append('dCutBackFactorForDivergence={}'.format(getValueStr(self.dCutBackFactorForDivergence)))
        if self.dCutBackFactorForTooSlowConvergence != obj.dCutBackFactorForTooSlowConvergence:
            paramArgs.append('dCutBackFactorForTooSlowConvergence={}'.format(getValueStr(self.dCutBackFactorForTooSlowConvergence)))
        if self.dCutBackFactorForExcessiveDistortion != obj.dCutBackFactorForExcessiveDistortion:
            paramArgs.append('dCutBackFactorForExcessiveDistortion={}'.format(getValueStr(self.dCutBackFactorForExcessiveDistortion)))
        if self.iIncrEnlargeNewtonMax != obj.iIncrEnlargeNewtonMax:
            paramArgs.append('iIncrEnlargeNewtonMax={}'.format(getValueStr(self.iIncrEnlargeNewtonMax)))
        if self.iIncrEnlargeSuppress != obj.iIncrEnlargeSuppress:
            paramArgs.append('iIncrEnlargeSuppress={}'.format(getValueStr(self.iIncrEnlargeSuppress)))
        if self.dIncreaseFactorForStatic != obj.dIncreaseFactorForStatic:
            paramArgs.append('dIncreaseFactorForStatic={}'.format(getValueStr(self.dIncreaseFactorForStatic)))
        if self.dIncreaseFactorForDynamic != obj.dIncreaseFactorForDynamic:
            paramArgs.append('dIncreaseFactorForDynamic={}'.format(getValueStr(self.dIncreaseFactorForDynamic)))
        if self.dIncreaseFactorForCreep != obj.dIncreaseFactorForCreep:
            paramArgs.append('dIncreaseFactorForCreep={}'.format(getValueStr(self.dIncreaseFactorForCreep)))
        if self.dIncreaseFactorForRdnlk != obj.dIncreaseFactorForRdnlk:
            paramArgs.append('dIncreaseFactorForRdnlk={}'.format(getValueStr(self.dIncreaseFactorForRdnlk)))
        if self.dTemperatureIncrMax != obj.dTemperatureIncrMax:
            paramArgs.append('dTemperatureIncrMax={}'.format(getValueStr(self.dTemperatureIncrMax)))
        if self.iUseTemperatureIncrMax != obj.iUseTemperatureIncrMax:
            paramArgs.append('iUseTemperatureIncrMax={}'.format(getValueStr(self.iUseTemperatureIncrMax)))
        if self.dHalfStepTol != obj.dHalfStepTol:
            paramArgs.append('dHalfStepTol={}'.format(getValueStr(self.dHalfStepTol)))
        if self.dStraTol != obj.dStraTol:
            paramArgs.append('dStraTol={}'.format(getValueStr(self.dStraTol)))
        if self.dCreepStraTol != obj.dCreepStraTol:
            paramArgs.append('dCreepStraTol={}'.format(getValueStr(self.dCreepStraTol)))
        if self.dRdnlkStraTol != obj.dRdnlkStraTol:
            paramArgs.append('dRdnlkStraTol={}'.format(getValueStr(self.dRdnlkStraTol)))
        return 'ADVC_AUTO_INCREMENT({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}'.format(
            self.iNewtonResidueIncrMax,
            self.iBeginResidueIncrCheck,
            self.iBeginLogarithmicRateCheck,
            self.dCutBackFactorForDivergence,
            self.dCutBackFactorForTooSlowConvergence,
            self.dCutBackFactorForExcessiveDistortion,
            self.iIncrEnlargeNewtonMax,
            self.iIncrEnlargeSuppress,
            self.dIncreaseFactorForStatic,
            self.dIncreaseFactorForDynamic,
            self.dIncreaseFactorForCreep,
            self.dIncreaseFactorForRdnlk,
            self.dTemperatureIncrMax,
            self.iUseTemperatureIncrMax,
            self.dHalfStepTol,
            self.dStraTol,
            self.dCreepStraTol,
            self.dRdnlkStraTol) + rightBracket

class ADVC_LOAD_NODE:
    def __init__(self,
        cr=None,
        crModify=None,
        flag=1,
        shrink=False,
        interference=DFLT_DBL,
        stabilized=0,
        residual_factor=DFLT_DBL,
        effective_dist=DFLT_DBL,
        type_=0,
        cn=DFLT_DBL,
        ct=DFLT_DBL):
        self.cr = cr
        self.crModify = crModify
        self.flag = flag
        self.shrink = shrink
        self.interference = interference
        self.stabilized = stabilized
        self.residual_factor = residual_factor
        self.effective_dist = effective_dist
        self.type = type_
        self.cn = cn
        self.ct = ct
    def isDefault(self):
        obj = ADVC_LOAD_NODE()
        return self.cr == obj.cr and \
            self.crModify == obj.crModify and \
            self.flag == obj.flag and \
            self.interference == obj.interference and \
            self.shrink == obj.shrink and \
            self.stabilized == obj.stabilized and \
            self.residual_factor == obj.residual_factor and \
            self.effective_dist == obj.effective_dist and \
            self.type == obj.type and \
            self.cn == obj.cn and \
            self.ct == obj.ct
    def isContactLoadNode(self):
        if isinstance(self.cr, CursorStr):
            typeCr = self.cr.typeId
            return ((108 <= typeCr and typeCr <= 113) or typeCr == 164 or typeCr == 171)
        if (
            108 <= int(self.cr.split(":")[0]) <= 113
            or int(self.cr.split(":")[0]) == 164
            or int(self.cr.split(":")[0]) == 171
        ):
            return True
        return False
    def fromList(self, param):
        obj = ADVC_LOAD_NODE()
        self.cr = getCursorValue(param[0]) if len(param) > 0 else obj.cr
        self.crModify = getCursorValue(param[1]) if len(param) > 1 else obj.crModify
        self.flag = param[2] if len(param) > 2 else obj.flag
        self.interference = normalizeDoubleType(param[3]) if len(param) > 3 else obj.interference
        self.shrink = getBoolValue(param[4]) if len(param) > 4 else obj.shrink
        self.stabilized = param[5] if len(param) > 5 else obj.stabilized
        self.residual_factor = normalizeDoubleType(param[6]) if len(param) > 6 else obj.residual_factor
        self.effective_dist = normalizeDoubleType(param[7]) if len(param) > 7 else obj.effective_dist
        self.type = param[8] if len(param) > 8 else obj.type
        self.cn = normalizeDoubleType(param[9]) if len(param) > 9 else obj.cn
        self.ct = normalizeDoubleType(param[10]) if len(param) > 10 else obj.ct
        return self
    def __str__(self):
        obj = ADVC_LOAD_NODE()
        paramArgs = []
        if self.cr != obj.cr:
            paramArgs.append('cr={}'.format(getCursorValueStr(self.cr)))
        if self.crModify != obj.crModify:
            paramArgs.append('crModify={}'.format(getCursorValueStr(self.crModify)))
        if self.flag != obj.flag:
            paramArgs.append('flag={}'.format(getValueStr(self.flag)))
        if self.isContactLoadNode():
            if self.interference != obj.interference:
                paramArgs.append('interference={}'.format(getValueStr(self.interference)))
            if self.shrink != obj.shrink:
                paramArgs.append('shrink={}'.format(getBoolStr(self.shrink)))
            if self.stabilized != obj.stabilized:
                paramArgs.append('stabilized={}'.format(getValueStr(self.stabilized)))
            if self.residual_factor != obj.residual_factor:
                paramArgs.append('residual_factor={}'.format(getValueStr(self.residual_factor)))
            if self.effective_dist != obj.effective_dist:
                paramArgs.append('effective_dist={}'.format(getValueStr(self.effective_dist)))
            if self.type != obj.type:
                paramArgs.append('type={}'.format(getValueStr(self.type)))
            if self.cn != obj.cn:
                paramArgs.append('cn={}'.format(getValueStr(self.cn)))
            if self.ct != obj.ct:
                paramArgs.append('ct={}'.format(getValueStr(self.ct)))
        return 'ADVC_LOAD_NODE({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        if self.isContactLoadNode():
            return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(
                str(self.cr) if self.cr is not None else '0:0',
                str(self.crModify) if self.crModify is not None else '0:0',
                self.flag,
                self.interference,
                1 if (self.shrink) else 0,         
                self.stabilized,
                self.residual_factor,
                self.effective_dist,
                self.type,
                self.cn,
                self.ct) + rightBracket
        else:
            return leftBracket + '{0}, {1}, {2}'.format(
                str(self.cr) if self.cr is not None else '0:0',
                str(self.crModify) if self.crModify is not None else '0:0',
                self.flag,) + rightBracket

class ADVC_REFERENCE_STRESS_RESULT:
    def __init__(self,
        proc=DFLT_INT,
        step=DFLT_INT,
        factor=DFLT_DBL):
        self.proc = proc
        self.step = step
        self.factor = factor
    def isDefault(self):
        obj = ADVC_REFERENCE_STRESS_RESULT()
        return self.proc == obj.proc and \
            self.step == obj.step and \
            self.factor == obj.factor
    def fromList(self, param):
        obj = ADVC_REFERENCE_STRESS_RESULT()
        self.proc = param[0] if len(param) > 0 else obj.proc
        self.step = param[1] if len(param) > 1 else obj.step
        self.factor = normalizeDoubleType(param[2]) if len(param) > 2 else obj.factor
        return self
    def __str__(self):
        obj = ADVC_REFERENCE_STRESS_RESULT()
        paramArgs = []
        if self.proc != obj.proc:
            paramArgs.append('proc={0}'.format(getValueStr(self.proc)))
        if self.step != obj.step:
            paramArgs.append('step={0}'.format(getValueStr(self.step)))
        if self.factor != obj.factor:
            paramArgs.append('factor={0}'.format(getValueStr(self.factor)))
        return 'ADVC_REFERENCE_STRESS_RESULT({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.proc,
            self.step,
            self.factor) + rightBracket

class RENUMBER_PROP:
    def __init__(self,
        crTarget=None,
        crMat=None,
        newId=0):
        self.crTarget = crTarget
        self.crMat = crMat
        self.newId = newId
    def isDefault(self):
        obj = RENUMBER_PROP()
        return self.crTarget == obj.crTarget and \
            self.crMat == obj.crMat and \
            self.newId == obj.newId
    def fromList(self, param):
        obj = RENUMBER_PROP()
        self.crTarget = getCursorValue(param[0]) if len(param) > 0 else obj.crTarget
        self.crMat = getCursorValue(param[1]) if len(param) > 1 else obj.crMat
        self.newId = param[2] if len(param) > 2 else obj.newId
        return self
    def __str__(self):
        obj = RENUMBER_PROP()
        paramArgs = []
        if self.crTarget != obj.crTarget:
            paramArgs.append('crTarget={}'.format(getCursorValueStr(self.crTarget)))
        if self.crMat != obj.crMat:
            paramArgs.append('crMat={}'.format(getCursorValueStr(self.crMat)))
        if self.newId != obj.newId:
            paramArgs.append('newId={}'.format(getValueStr(self.newId)))
        return 'RENUMBER_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            str(self.crTarget) if self.crTarget is not None else '0:0',
            str(self.crMat) if self.crMat is not None else '0:0',
            self.newId) + rightBracket

class BALL_HEXA_SETTING:
    def __init__(self,
        vecCenter=[0.0, 0.0, 0.0],
        dRadius=0.0,
        dMeshSize=0.0,
        iType=0,
        iLayer=0,
        bMakeCenterNode=True,
        strPartName=""):
        self.vecCenter = vecCenter
        self.dRadius = dRadius
        self.dMeshSize = dMeshSize
        self.iType = iType
        self.iLayer = iLayer
        self.bMakeCenterNode = bMakeCenterNode
        self.strPartName = strPartName
    def isDefault(self):
        obj = BALL_HEXA_SETTING()
        return self.vecCenter == obj.vecCenter and \
            self.dRadius == obj.dRadius and \
            self.dMeshSize == obj.dMeshSize and \
            self.iType == obj.iType and \
            self.iLayer == obj.iLayer and \
            self.bMakeCenterNode == obj.bMakeCenterNode and \
            self.strPartName == obj.strPartName
    def fromList(self, param):
        obj = BALL_HEXA_SETTING()
        self.vecCenter = [normalizeDoubleType(tok) for tok in param[0]] if len(param) > 0 else obj.vecCenter
        self.dRadius = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dRadius
        self.dMeshSize = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dMeshSize
        self.iType = param[3] if len(param) > 3 else obj.iType
        self.iLayer = param[4] if len(param) > 4 else obj.iLayer
        self.bMakeCenterNode = getBoolValue(param[5]) if len(param) > 5 else obj.bMakeCenterNode
        self.strPartName = param[6] if len(param) > 6 else obj.strPartName
        return self
    def __str__(self):
        obj = BALL_HEXA_SETTING()
        paramArgs = []
        if self.vecCenter != obj.vecCenter:
            paramArgs.append('vecCenter={0}'.format(getValueStr(self.vecCenter)))
        if self.dRadius != obj.dRadius:
            paramArgs.append('dRadius={0}'.format(getValueStr(self.dRadius)))
        if self.dMeshSize != obj.dMeshSize:
            paramArgs.append('dMeshSize={0}'.format(getValueStr(self.dMeshSize)))
        if self.iType != obj.iType:
            paramArgs.append('iType={0}'.format(getValueStr(self.iType)))
        if self.iLayer != obj.iLayer:
            paramArgs.append('iLayer={0}'.format(getValueStr(self.iLayer)))
        if self.bMakeCenterNode != obj.bMakeCenterNode:
            paramArgs.append('bMakeCenterNode={0}'.format(getBoolStr(self.bMakeCenterNode)))
        if self.strPartName != obj.strPartName:
            paramArgs.append('strPartName={0}'.format('"' + self.strPartName + '"'))
        return 'BALL_HEXA_SETTING({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            self.vecCenter,
            self.dRadius,
            self.dMeshSize,
            self.iType,
            self.iLayer,
            1 if self.bMakeCenterNode else 0,
            '"' + self.strPartName + '"') + rightBracket

class ENFORCED_ACCELERATION_LBC:
    def __init__(self,
        iDwDof=0,
        dFVel1=DFLT_DBL,
        dFVel2=DFLT_DBL,
        dFVel3=DFLT_DBL,
        dFVel4=DFLT_DBL,
        dFVel5=DFLT_DBL,
        dFVel6=DFLT_DBL,
        crCurCoord=None,
        iEnArrowDir=0,
        crTable=None,
        crNodeSet=None,
        dFPhase=DFLT_DBL,
        dFDelay=DFLT_DBL,
        crPhaseTable=None,
        bExport=False,
        crMEExport1=None,
        crMEExport2=None,
        crMEExport3=None,
        crMEExport4=None,
        crMEExport5=None,
        crMEExport6=None,
        iAcUnit=0,
        iRotUnit=0):
        self.iDwDof = iDwDof
        self.dFVel1 = dFVel1
        self.dFVel2 = dFVel2
        self.dFVel3 = dFVel3
        self.dFVel4 = dFVel4
        self.dFVel5 = dFVel5
        self.dFVel6 = dFVel6
        self.crCurCoord = crCurCoord
        self.iEnArrowDir = iEnArrowDir
        self.crTable = crTable
        self.crNodeSet = crNodeSet
        self.dFPhase = dFPhase
        self.dFDelay = dFDelay
        self.crPhaseTable = crPhaseTable
        self.bExport = bExport
        self.crMEExport1 = crMEExport1
        self.crMEExport2 = crMEExport2
        self.crMEExport3 = crMEExport3
        self.crMEExport4 = crMEExport4
        self.crMEExport5 = crMEExport5
        self.crMEExport6 = crMEExport6
        self.iAcUnit = iAcUnit
        self.iRotUnit = iRotUnit
    def isDefault(self):
        obj = ENFORCED_ACCELERATION_LBC()
        return self.iDwDof == obj.iDwDof and \
            self.dFVel1 == obj.dFVel1 and \
            self.dFVel2 == obj.dFVel2 and \
            self.dFVel3 == obj.dFVel3 and \
            self.dFVel4 == obj.dFVel4 and \
            self.dFVel5 == obj.dFVel5 and \
            self.dFVel6 == obj.dFVel6 and \
            self.crCurCoord == obj.crCurCoord and \
            self.iEnArrowDir == obj.iEnArrowDir and \
            self.crTable == obj.crTable and \
            self.crNodeSet == obj.crNodeSet and \
            self.dFPhase == obj.dFPhase and \
            self.dFDelay == obj.dFDelay and \
            self.crPhaseTable == obj.crPhaseTable and \
            self.bExport == obj.bExport and \
            self.crMEExport1 == obj.crMEExport1 and \
            self.crMEExport2 == obj.crMEExport2 and \
            self.crMEExport3 == obj.crMEExport3 and \
            self.crMEExport4 == obj.crMEExport4 and \
            self.crMEExport5 == obj.crMEExport5 and \
            self.crMEExport6 == obj.crMEExport6 and \
            self.iAcUnit == obj.iAcUnit and \
            self.iRotUnit == obj.iRotUnit
    def fromList(self, param):
        obj = ENFORCED_ACCELERATION_LBC()
        self.iDwDof = param[0] if len(param) > 0 else obj.iDwDof
        self.dFVel1 = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dFVel1
        self.dFVel2 = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dFVel2
        self.dFVel3 = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dFVel3
        self.dFVel4 = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dFVel4
        self.dFVel5 = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dFVel5
        self.dFVel6 = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dFVel6
        self.crCurCoord = getCursorValue(param[7]) if len(param) > 7 else obj.crCurCoord
        self.iEnArrowDir = param[8] if len(param) > 8 else obj.iEnArrowDir
        self.crTable = getCursorValue(param[9]) if len(param) > 9 else obj.crTable
        self.crNodeSet = getCursorValue(param[10]) if len(param) > 10 else obj.crNodeSet
        self.dFPhase = normalizeDoubleType(param[11]) if len(param) > 11 else obj.dFPhase
        self.dFDelay = normalizeDoubleType(param[12]) if len(param) > 12 else obj.dFDelay
        self.crPhaseTable = getCursorValue(param[13]) if len(param) > 13 else obj.crPhaseTable
        self.bExport = getBoolValue(param[14]) if len(param) > 14 else obj.bExport
        self.crMEExport1 = getCursorValue(param[15]) if len(param) > 15 else obj.crMEExport1
        self.crMEExport2 = getCursorValue(param[16]) if len(param) > 16 else obj.crMEExport2
        self.crMEExport3 = getCursorValue(param[17]) if len(param) > 17 else obj.crMEExport3
        self.crMEExport4 = getCursorValue(param[18]) if len(param) > 18 else obj.crMEExport4
        self.crMEExport5 = getCursorValue(param[19]) if len(param) > 19 else obj.crMEExport5
        self.crMEExport6 = getCursorValue(param[20]) if len(param) > 20 else obj.crMEExport6
        self.iAcUnit = param[21] if len(param) > 21 else obj.iAcUnit
        self.iRotUnit = param[22] if len(param) > 22 else obj.iRotUnit
        return self
    def __str__(self):
        obj = ENFORCED_ACCELERATION_LBC()
        paramArgs = []
        if self.iDwDof != obj.iDwDof:
            paramArgs.append('iDwDof={0}'.format(getValueStr(self.iDwDof)))
        if self.dFVel1 != obj.dFVel1:
            paramArgs.append('dFVel1={0}'.format(getValueStr(self.dFVel1)))
        if self.dFVel2 != obj.dFVel2:
            paramArgs.append('dFVel2={0}'.format(getValueStr(self.dFVel2)))
        if self.dFVel3 != obj.dFVel3:
            paramArgs.append('dFVel3={0}'.format(getValueStr(self.dFVel3)))
        if self.dFVel4 != obj.dFVel4:
            paramArgs.append('dFVel4={0}'.format(getValueStr(self.dFVel4)))
        if self.dFVel5 != obj.dFVel5:
            paramArgs.append('dFVel5={0}'.format(getValueStr(self.dFVel5)))
        if self.dFVel6 != obj.dFVel6:
            paramArgs.append('dFVel6={0}'.format(getValueStr(self.dFVel6)))
        if self.crCurCoord != obj.crCurCoord:
            paramArgs.append('crCurCoord={0}'.format(getCursorValueStr(self.crCurCoord)))
        if self.iEnArrowDir != obj.iEnArrowDir:
            paramArgs.append('iEnArrowDir={0}'.format(getValueStr(self.iEnArrowDir)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        if self.crNodeSet != obj.crNodeSet:
            paramArgs.append('crNodeSet={0}'.format(getCursorValueStr(self.crNodeSet)))
        if self.dFPhase != obj.dFPhase:
            paramArgs.append('dFPhase={0}'.format(getValueStr(self.dFPhase)))
        if self.dFDelay != obj.dFDelay:
            paramArgs.append('dFDelay={0}'.format(getValueStr(self.dFDelay)))
        if self.crPhaseTable != obj.crPhaseTable:
            paramArgs.append('crPhaseTable={0}'.format(getCursorValueStr(self.crPhaseTable)))
        if self.bExport != obj.bExport:
            paramArgs.append('bExport={0}'.format(getBoolStr(self.bExport)))
        if self.crMEExport1 != obj.crMEExport1:
            paramArgs.append('crMEExport1={0}'.format(getCursorValueStr(self.crMEExport1)))
        if self.crMEExport2 != obj.crMEExport2:
            paramArgs.append('crMEExport2={0}'.format(getCursorValueStr(self.crMEExport2)))
        if self.crMEExport3 != obj.crMEExport3:
            paramArgs.append('crMEExport3={0}'.format(getCursorValueStr(self.crMEExport3)))
        if self.crMEExport4 != obj.crMEExport4:
            paramArgs.append('crMEExport4={0}'.format(getCursorValueStr(self.crMEExport4)))
        if self.crMEExport5 != obj.crMEExport5:
            paramArgs.append('crMEExport5={0}'.format(getCursorValueStr(self.crMEExport5)))
        if self.crMEExport6 != obj.crMEExport6:
            paramArgs.append('crMEExport6={0}'.format(getCursorValueStr(self.crMEExport6)))
        if self.iAcUnit != obj.iAcUnit:
            paramArgs.append('iAcUnit={0}'.format(getValueStr(self.iAcUnit)))
        if self.iRotUnit != obj.iRotUnit:
            paramArgs.append('iRotUnit={0}'.format(getValueStr(self.iRotUnit)))
        return 'ENFORCED_ACCELERATION_LBC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}'.format(
            self.iDwDof,
            self.dFVel1,
            self.dFVel2,
            self.dFVel3,
            self.dFVel4,
            self.dFVel5,
            self.dFVel6,
            str(self.crCurCoord) if self.crCurCoord is not None else '0:0',
            self.iEnArrowDir,
            str(self.crTable) if self.crTable is not None else '0:0',
            str(self.crNodeSet) if self.crNodeSet is not None else '0:0',
            self.dFPhase,
            self.dFDelay,
            str(self.crPhaseTable) if self.crPhaseTable is not None else '0:0',
            1 if self.bExport else 0,
            str(self.crMEExport1) if self.crMEExport1 is not None else '0:0',
            str(self.crMEExport2) if self.crMEExport2 is not None else '0:0',
            str(self.crMEExport3) if self.crMEExport3 is not None else '0:0',
            str(self.crMEExport4) if self.crMEExport4 is not None else '0:0',
            str(self.crMEExport5) if self.crMEExport5 is not None else '0:0',
            str(self.crMEExport6) if self.crMEExport6 is not None else '0:0',
            self.iAcUnit,
            self.iRotUnit) + rightBracket

class ROD_1D_PROP:
    def __init__(self,
        crMat=None,
        dArea=DFLT_DBL,
        dTorConst=DFLT_DBL,
        dTorStressCoeff=DFLT_DBL,
        dNSM=DFLT_DBL):
        self.crMat = crMat
        self.dArea = dArea
        self.dTorConst = dTorConst
        self.dTorStressCoeff = dTorStressCoeff
        self.dNSM = dNSM
    def isDefault(self):
        obj = ROD_1D_PROP()
        return self.crMat == obj.crMat and \
            self.dArea == obj.dArea and \
            self.dTorConst == obj.dTorConst and \
            self.dTorStressCoeff == obj.dTorStressCoeff and \
            self.dNSM == obj.dNSM
    def fromList(self, param):
        obj = ROD_1D_PROP()
        self.crMat = getCursorValue(param[0]) if len(param) > 0 else obj.crMat
        self.dArea = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dArea
        self.dTorConst = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dTorConst
        self.dTorStressCoeff = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dTorStressCoeff
        self.dNSM = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dNSM
        return self
    def __str__(self):
        obj = ROD_1D_PROP()
        paramArgs = []
        if self.crMat != obj.crMat:
            paramArgs.append('crMat={0}'.format(getCursorValueStr(self.crMat)))
        if self.dArea != obj.dArea:
            paramArgs.append('dArea={0}'.format(getValueStr(self.dArea)))
        if self.dTorConst != obj.dTorConst:
            paramArgs.append('dTorConst={0}'.format(getValueStr(self.dTorConst)))
        if self.dTorStressCoeff != obj.dTorStressCoeff:
            paramArgs.append('dTorStressCoeff={0}'.format(getValueStr(self.dTorStressCoeff)))
        if self.dNSM != obj.dNSM:
            paramArgs.append('dNSM={0}'.format(getValueStr(self.dNSM)))
        return 'ROD_1D_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            str(self.crMat) if self.crMat is not None else '0:0',
            self.dArea,
            self.dTorConst,
            self.dTorStressCoeff,
            self.dNSM) + rightBracket

class GRID_MESH:
    def __init__(self,
        crlFace=[],
        crlCorner=[],
        ilMeshCount=[],
        iShape=-1,
        iElemtype=3,
        bSwap=False,
        bLocalSetting=False,
        bOptimize=False,
        bFreezeBoundary=False):
        self.crlFace = crlFace
        self.crlCorner = crlCorner
        self.ilMeshCount = ilMeshCount
        self.iShape = iShape
        self.iElemtype = iElemtype
        self.bSwap = bSwap
        self.bLocalSetting = bLocalSetting
        self.bOptimize = bOptimize
        self.bFreezeBoundary = bFreezeBoundary
    def isDefault(self):
        obj = GRID_MESH()
        return self.crlFace == obj.crlFace and \
            self.crlCorner == obj.crlCorner and \
            self.ilMeshCount == obj.ilMeshCount and \
            self.iShape == obj.iShape and \
            self.iElemtype == obj.iElemtype and \
            self.bSwap == obj.bSwap and \
            self.bLocalSetting == obj.bLocalSetting and \
            self.bOptimize == obj.bOptimize and \
            self.bFreezeBoundary == obj.bFreezeBoundary
    def fromList(self, param):
        obj = GRID_MESH()
        self.crlFace = getCursorListValue(param[0]) if len(param) > 0 else obj.crlFace
        self.crlCorner = getCursorListValue(param[1]) if len(param) > 1 else obj.crlCorner
        self.ilMeshCount = param[2] if len(param) > 2 else obj.ilMeshCount
        self.iShape = param[3] if len(param) > 3 else obj.iShape
        self.iElemtype = param[4] if len(param) > 4 else obj.iElemtype
        self.bSwap = getBoolValue(param[5]) if len(param) > 5 else obj.bSwap
        self.bLocalSetting = getBoolValue(param[6]) if len(param) > 6 else obj.bLocalSetting
        self.bOptimize = getBoolValue(param[7]) if len(param) > 7 else obj.bOptimize
        self.bFreezeBoundary = getBoolValue(param[8]) if len(param) > 8 else obj.bFreezeBoundary
        return self
    def __str__(self):
        obj = GRID_MESH()
        paramArgs = []
        if self.crlFace != obj.crlFace:
            paramArgs.append('crlFace={0}'.format(getCursorListValueStr(self.crlFace)))
        if self.crlCorner != obj.crlCorner:
            paramArgs.append('crlCorner={0}'.format(getCursorListValueStr(self.crlCorner)))
        if self.ilMeshCount != obj.ilMeshCount:
            paramArgs.append('ilMeshCount={0}'.format(getValueStr(self.ilMeshCount)))
        if self.iShape != obj.iShape:
            paramArgs.append('iShape={0}'.format(getValueStr(self.iShape)))
        if self.iElemtype != obj.iElemtype:
            paramArgs.append('iElemtype={0}'.format(getValueStr(self.iElemtype)))
        if self.bSwap != obj.bSwap:
            paramArgs.append('bSwap={0}'.format(getBoolStr(self.bSwap)))
        if self.bLocalSetting != obj.bLocalSetting:
            paramArgs.append('bLocalSetting={0}'.format(getBoolStr(self.bLocalSetting)))
        if self.bOptimize != obj.bOptimize:
            paramArgs.append('bOptimize={0}'.format(getBoolStr(self.bOptimize)))
        if self.bFreezeBoundary != obj.bFreezeBoundary:
            paramArgs.append('bFreezeBoundary={0}'.format(getBoolStr(self.bFreezeBoundary)))
        return 'GRID_MESH({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            str(self.crlFace) if self.crlFace != [None] else '[0:0]',
            str(self.crlCorner) if self.crlCorner != [None] else '[0:0]',
            self.ilMeshCount,
            self.iShape,
            self.iElemtype,
            1 if self.bSwap else 0,
            1 if self.bLocalSetting else 0,
            1 if self.bOptimize else 0,
            1 if self.bFreezeBoundary else 0) + rightBracket

class ERISHELL_THETA_PROP:
    def __init__(self,
        iPropId1=0,
        iElemId1=0,
        dTheta=0):
        self.iPropId1 = iPropId1
        self.iElemId1 = iElemId1
        self.dTheta = dTheta
    def isDefault(self):
        obj = ERISHELL_THETA_PROP()
        return self.iPropId1 == obj.iPropId1 and \
            self.iElemId1 == obj.iElemId1 and \
            self.dTheta == obj.dTheta
    def fromList(self, param):
        obj = ERISHELL_THETA_PROP()
        self.iPropId1 = param[0] if len(param) > 0 else obj.iPropId1
        self.iElemId1 = param[1] if len(param) > 1 else obj.iElemId1
        self.dTheta = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dTheta
        return self
    def __str__(self):
        obj = ERISHELL_THETA_PROP()
        paramArgs = []
        if self.iPropId1 != obj.iPropId1:
            paramArgs.append('iPropId1={0}'.format(getValueStr(self.iPropId1)))
        if self.iElemId1 != obj.iElemId1:
            paramArgs.append('iElemId1={0}'.format(getValueStr(self.iElemId1)))
        if self.dTheta != obj.dTheta:
            paramArgs.append('dTheta={0}'.format(getValueStr(self.dTheta)))
        return 'ERISHELL_THETA_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iPropId1,
            self.iElemId1,
            self.dTheta) + rightBracket

class ERISHELL_CS_PROP:
    def __init__(self,
        iPropId2=0,
        iElemId2=0,
        iCS=0):
        self.iPropId2 = iPropId2
        self.iElemId2 = iElemId2
        self.iCS = iCS
    def isDefault(self):
        obj = ERISHELL_CS_PROP()
        return self.iPropId2 == obj.iPropId2 and \
            self.iElemId2 == obj.iElemId2 and \
            self.iCS == obj.iCS
    def fromList(self, param):
        obj = ERISHELL_CS_PROP()
        self.iPropId2 = param[0] if len(param) > 0 else obj.iPropId2
        self.iElemId2 = param[1] if len(param) > 1 else obj.iElemId2
        self.iCS = param[2] if len(param) > 2 else obj.iCS
        return self
    def __str__(self):
        obj = ERISHELL_CS_PROP()
        paramArgs = []
        if self.iPropId2 != obj.iPropId2:
            paramArgs.append('iPropId2={0}'.format(getValueStr(self.iPropId2)))
        if self.iElemId2 != obj.iElemId2:
            paramArgs.append('iElemId2={0}'.format(getValueStr(self.iElemId2)))
        if self.iCS != obj.iCS:
            paramArgs.append('iCS={0}'.format(getValueStr(self.iCS)))
        return 'ERISHELL_CS_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iPropId2,
            self.iElemId2,
            self.iCS) + rightBracket

class ERISHELL_ZOFFS_PROP:
    def __init__(self,
        iPropId3=0,
        iElemId3=0,
        dZoffs=0.0):
        self.iPropId3 = iPropId3
        self.iElemId3 = iElemId3
        self.dZoffs = dZoffs
    def isDefault(self):
        obj = ERISHELL_ZOFFS_PROP()
        return self.iPropId3 == obj.iPropId3 and \
            self.iElemId3 == obj.iElemId3 and \
            self.dZoffs == obj.dZoffs
    def fromList(self, param):
        obj = ERISHELL_ZOFFS_PROP()
        self.iPropId3 = param[0] if len(param) > 0 else obj.iPropId3
        self.iElemId3 = param[1] if len(param) > 1 else obj.iElemId3
        self.dZoffs = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dZoffs
        return self
    def __str__(self):
        obj = ERISHELL_ZOFFS_PROP()
        paramArgs = []
        if self.iPropId3 != obj.iPropId3:
            paramArgs.append('iPropId3={0}'.format(getValueStr(self.iPropId3)))
        if self.iElemId3 != obj.iElemId3:
            paramArgs.append('iElemId3={0}'.format(getValueStr(self.iElemId3)))
        if self.dZoffs != obj.dZoffs:
            paramArgs.append('dZoffs={0}'.format(getValueStr(self.dZoffs)))
        return 'ERISHELL_ZOFFS_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iPropId3,
            self.iElemId3,
            self.dZoffs) + rightBracket

class NASTRAN_CONTACT:
    def __init__(self,
        iType=0,
        iAlg=0,
        dRROR=0.5,
        dFNTOL=DFLT_DBL,
        dFRIC=DFLT_DBL,
        dCINTERF=DFLT_DBL,
        iISEARCH=DFLT_INT,
        iICOORD=DFLT_INT,
        dFRLIM=DFLT_DBL,
        dBIAS=DFLT_DBL,
        iISTYP=DFLT_INT,
        iIshellelemfaceSlave=0,
        iIshellelemfaceMaster=0,
        iIbeambarshellelemedgeSlave=0,
        iIbeambarshellelemedgeMaster=0):
        self.iType = iType
        self.iAlg = iAlg
        self.dRROR = dRROR
        self.dFNTOL = dFNTOL
        self.dFRIC = dFRIC
        self.dCINTERF = dCINTERF
        self.iISEARCH = iISEARCH
        self.iICOORD = iICOORD
        self.dFRLIM = dFRLIM
        self.dBIAS = dBIAS
        self.iISTYP = iISTYP
        self.iIshellelemfaceSlave = iIshellelemfaceSlave
        self.iIshellelemfaceMaster = iIshellelemfaceMaster
        self.iIbeambarshellelemedgeSlave = iIbeambarshellelemedgeSlave
        self.iIbeambarshellelemedgeMaster = iIbeambarshellelemedgeMaster
    def isDefault(self):
        obj = NASTRAN_CONTACT()
        return self.iType == obj.iType and \
            self.iAlg == obj.iAlg and \
            self.dRROR == obj.dRROR and \
            self.dFNTOL == obj.dFNTOL and \
            self.dFRIC == obj.dFRIC and \
            self.dCINTERF == obj.dCINTERF and \
            self.iISEARCH == obj.iISEARCH and \
            self.iICOORD == obj.iICOORD and \
            self.dFRLIM == obj.dFRLIM and \
            self.dBIAS == obj.dBIAS and \
            self.iISTYP == obj.iISTYP and \
            self.iIshellelemfaceSlave == obj.iIshellelemfaceSlave and \
            self.iIshellelemfaceMaster == obj.iIshellelemfaceMaster and \
            self.iIbeambarshellelemedgeSlave == obj.iIbeambarshellelemedgeSlave and \
            self.iIbeambarshellelemedgeMaster == obj.iIbeambarshellelemedgeMaster
    def fromList(self, param):
        obj = NASTRAN_CONTACT()
        self.iType = param[0] if len(param) > 0 else obj.iType
        self.iAlg = param[1] if len(param) > 1 else obj.iAlg
        self.dRROR = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dRROR
        self.dFNTOL = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dFNTOL
        self.dFRIC = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dFRIC
        self.dCINTERF = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dCINTERF
        self.iISEARCH = param[6] if len(param) > 6 else obj.iISEARCH
        self.iICOORD = param[7] if len(param) > 7 else obj.iICOORD
        self.dFRLIM = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dFRLIM
        self.dBIAS = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dBIAS
        self.iISTYP = param[10] if len(param) > 10 else obj.iISTYP
        self.iIshellelemfaceSlave = param[11] if len(param) > 11 else obj.iIshellelemfaceSlave
        self.iIshellelemfaceMaster = param[12] if len(param) > 12 else obj.iIshellelemfaceMaster
        self.iIbeambarshellelemedgeSlave = param[13] if len(param) > 13 else obj.iIbeambarshellelemedgeSlave
        self.iIbeambarshellelemedgeMaster = param[14] if len(param) > 14 else obj.iIbeambarshellelemedgeMaster
        return self
    def __str__(self):
        obj = NASTRAN_CONTACT()
        paramArgs = []
        if self.iType != obj.iType:
            paramArgs.append('iType={0}'.format(getValueStr(self.iType)))
        if self.iAlg != obj.iAlg:
            paramArgs.append('iAlg={0}'.format(getValueStr(self.iAlg)))
        if self.dRROR != obj.dRROR:
            paramArgs.append('dRROR={0}'.format(getValueStr(self.dRROR)))
        if self.dFNTOL != obj.dFNTOL:
            paramArgs.append('dFNTOL={0}'.format(getValueStr(self.dFNTOL)))
        if self.dFRIC != obj.dFRIC:
            paramArgs.append('dFRIC={0}'.format(getValueStr(self.dFRIC)))
        if self.dCINTERF != obj.dCINTERF:
            paramArgs.append('dCINTERF={0}'.format(getValueStr(self.dCINTERF)))
        if self.iISEARCH != obj.iISEARCH:
            paramArgs.append('iISEARCH={0}'.format(getValueStr(self.iISEARCH)))
        if self.iICOORD != obj.iICOORD:
            paramArgs.append('iICOORD={0}'.format(getValueStr(self.iICOORD)))
        if self.dFRLIM != obj.dFRLIM:
            paramArgs.append('dFRLIM={0}'.format(getValueStr(self.dFRLIM)))
        if self.dBIAS != obj.dBIAS:
            paramArgs.append('dBIAS={0}'.format(getValueStr(self.dBIAS)))
        if self.iISTYP != obj.iISTYP:
            paramArgs.append('iISTYP={0}'.format(getValueStr(self.iISTYP)))
        if self.iIshellelemfaceSlave != obj.iIshellelemfaceSlave:
            paramArgs.append('iIshellelemfaceSlave={0}'.format(getValueStr(self.iIshellelemfaceSlave)))
        if self.iIshellelemfaceMaster != obj.iIshellelemfaceMaster:
            paramArgs.append('iIshellelemfaceMaster={0}'.format(getValueStr(self.iIshellelemfaceMaster)))
        if self.iIbeambarshellelemedgeSlave != obj.iIbeambarshellelemedgeSlave:
            paramArgs.append('iIbeambarshellelemedgeSlave={0}'.format(getValueStr(self.iIbeambarshellelemedgeSlave)))
        if self.iIbeambarshellelemedgeMaster != obj.iIbeambarshellelemedgeMaster:
            paramArgs.append('iIbeambarshellelemedgeMaster={0}'.format(getValueStr(self.iIbeambarshellelemedgeMaster)))
        return 'NASTRAN_CONTACT({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}'.format(
            self.iType,
            self.iAlg,
            self.dRROR,
            self.dFNTOL,
            self.dFRIC,
            self.dCINTERF,
            self.iISEARCH,
            self.iICOORD,
            self.dFRLIM,
            self.dBIAS,
            self.iISTYP,
            self.iIshellelemfaceSlave,
            self.iIshellelemfaceMaster,
            self.iIbeambarshellelemedgeSlave,
            self.iIbeambarshellelemedgeMaster) + rightBracket

class DESIGNER_CONTACT:
    def __init__(self,
        iContactType=1,
        dInterferenceClosure=0.05,
        dFrictionCoefficient=0,
        iShellOffset=0,
        iMasterShellOrientation=0,
        iSlaveShellOrientation=0,
        iMarkerColor=65280,
        bInitialAdjustment=0):
        self.iContactType = iContactType
        self.dInterferenceClosure = dInterferenceClosure
        self.dFrictionCoefficient = dFrictionCoefficient
        self.iShellOffset = iShellOffset
        self.iMasterShellOrientation = iMasterShellOrientation
        self.iSlaveShellOrientation = iSlaveShellOrientation
        self.iMarkerColor = iMarkerColor
        self.bInitialAdjustment = bInitialAdjustment
    def isDefault(self):
        obj = DESIGNER_CONTACT()
        return self.iContactType == obj.iContactType and \
            self.dInterferenceClosure == obj.dInterferenceClosure and \
            self.dFrictionCoefficient == obj.dFrictionCoefficient and \
            self.iShellOffset == obj.iShellOffset and \
            self.iMasterShellOrientation == obj.iMasterShellOrientation and \
            self.iSlaveShellOrientation == obj.iSlaveShellOrientation and \
            self.iMarkerColor == obj.iMarkerColor and \
            self.bInitialAdjustment == obj.bInitialAdjustment
    def fromList(self, param):
        obj = DESIGNER_CONTACT()
        self.iContactType = param[0] if len(param) > 0 else obj.iContactType
        self.dInterferenceClosure = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dInterferenceClosure
        self.dFrictionCoefficient = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dFrictionCoefficient
        self.iShellOffset = param[3] if len(param) > 3 else obj.iShellOffset
        self.iMasterShellOrientation = param[4] if len(param) > 4 else obj.iMasterShellOrientation
        self.iSlaveShellOrientation = param[5] if len(param) > 5 else obj.iSlaveShellOrientation
        self.iMarkerColor = param[6] if len(param) > 6 else obj.iMarkerColor
        self.bInitialAdjustment = getBoolValue(param[7]) if len(param) > 7 else obj.bInitialAdjustment
        return self
    def __str__(self):
        obj = DESIGNER_CONTACT()
        paramArgs = []
        if self.iContactType != obj.iContactType:
            paramArgs.append('iContactType={0}'.format(getValueStr(self.iContactType)))
        if self.dInterferenceClosure != obj.dInterferenceClosure:
            paramArgs.append('dInterferenceClosure={0}'.format(getValueStr(self.dInterferenceClosure)))
        if self.dFrictionCoefficient != obj.dFrictionCoefficient:
            paramArgs.append('dFrictionCoefficient={0}'.format(getValueStr(self.dFrictionCoefficient)))
        if self.iShellOffset != obj.iShellOffset:
            paramArgs.append('iShellOffset={0}'.format(getValueStr(self.iShellOffset)))
        if self.iMasterShellOrientation != obj.iMasterShellOrientation:
            paramArgs.append('iMasterShellOrientation={0}'.format(getValueStr(self.iMasterShellOrientation)))
        if self.iSlaveShellOrientation != obj.iSlaveShellOrientation:
            paramArgs.append('iSlaveShellOrientation={0}'.format(getValueStr(self.iSlaveShellOrientation)))
        if self.iMarkerColor != obj.iMarkerColor:
            paramArgs.append('iMarkerColor={0}'.format(getValueStr(self.iMarkerColor)))
        if self.bInitialAdjustment != obj.bInitialAdjustment:
            paramArgs.append('bInitialAdjustment={0}'.format(getBoolStr(self.bInitialAdjustment)))
        return 'DESIGNER_CONTACT({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(
            self.iContactType,
            self.dInterferenceClosure,
            self.dFrictionCoefficient,
            self.iShellOffset,
            self.iMasterShellOrientation,
            self.iSlaveShellOrientation,
            self.iMarkerColor,
            1 if self.bInitialAdjustment else 0) + rightBracket

class ELEM_COORSYSTEM_TOOL:
    def __init__(self,
        iMethod=0,
        iDispType=0,
        bDispXDir=0,
        bDispCoord=0,
        bDispZCoord=0,
        dDispScale=1,
        dDiverseFactor=0.755):
        self.iMethod = iMethod
        self.iDispType = iDispType
        self.bDispXDir = bDispXDir
        self.bDispCoord = bDispCoord
        self.bDispZCoord = bDispZCoord
        self.dDispScale = dDispScale
        self.dDiverseFactor = dDiverseFactor
    def isDefault(self):
        obj = ELEM_COORSYSTEM_TOOL()
        return self.iMethod == obj.iMethod and \
            self.iDispType == obj.iDispType and \
            self.bDispXDir == obj.bDispXDir and \
            self.bDispCoord == obj.bDispCoord and \
            self.bDispZCoord == obj.bDispZCoord and \
            self.dDispScale == obj.dDispScale and \
            self.dDiverseFactor == obj.dDiverseFactor
    def fromList(self, param):
        obj = ELEM_COORSYSTEM_TOOL()
        self.iMethod = param[0] if len(param) > 0 else obj.iMethod
        self.iDispType = param[1] if len(param) > 1 else obj.iDispType
        self.bDispXDir = getBoolValue(param[2]) if len(param) > 2 else obj.bDispXDir
        self.bDispCoord = getBoolValue(param[3]) if len(param) > 3 else obj.bDispCoord
        self.bDispZCoord = getBoolValue(param[4]) if len(param) > 4 else obj.bDispZCoord
        self.dDispScale = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dDispScale
        self.dDiverseFactor = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dDiverseFactor
        return self
    def __str__(self):
        obj = ELEM_COORSYSTEM_TOOL()
        paramArgs = []
        if self.iMethod != obj.iMethod:
            paramArgs.append('iMethod={0}'.format(getValueStr(self.iMethod)))
        if self.iDispType != obj.iDispType:
            paramArgs.append('iDispType={0}'.format(getValueStr(self.iDispType)))
        if self.bDispXDir != obj.bDispXDir:
            paramArgs.append('bDispXDir={0}'.format(getBoolStr(self.bDispXDir)))
        if self.bDispCoord != obj.bDispCoord:
            paramArgs.append('bDispCoord={0}'.format(getBoolStr(self.bDispCoord)))
        if self.bDispZCoord != obj.bDispZCoord:
            paramArgs.append('bDispZCoord={0}'.format(getBoolStr(self.bDispZCoord)))
        if self.dDispScale != obj.dDispScale:
            paramArgs.append('dDispScale={0}'.format(getValueStr(self.dDispScale)))
        if self.dDiverseFactor != obj.dDiverseFactor:
            paramArgs.append('dDiverseFactor={0}'.format(getValueStr(self.dDiverseFactor)))
        return 'ELEM_COORSYSTEM_TOOL({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            self.iMethod,
            self.iDispType,
            1 if self.bDispXDir else 0,
            1 if self.bDispCoord else 0,
            1 if self.bDispZCoord else 0,
            self.dDispScale,
            self.dDiverseFactor) + rightBracket

class ADVC_DYNAMIC:
    def __init__(self,
        dAlpha=DFLT_DBL,
        dBeta=DFLT_DBL,
        dGamma=DFLT_DBL):
        self.dAlpha = dAlpha
        self.dBeta = dBeta
        self.dGamma = dGamma
    def isDefault(self):
        obj = ADVC_DYNAMIC()
        return self.dAlpha == obj.dAlpha and \
            self.dBeta == obj.dBeta and \
            self.dGamma == obj.dGamma
    def fromList(self, param):
        obj = ADVC_DYNAMIC()
        self.dAlpha = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dAlpha
        self.dBeta = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dBeta
        self.dGamma = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dGamma
        return self
    def __str__(self):
        obj = ADVC_DYNAMIC()
        paramArgs = []
        if self.dAlpha != obj.dAlpha:
            paramArgs.append('dAlpha={0}'.format(getValueStr(self.dAlpha)))
        if self.dBeta != obj.dBeta:
            paramArgs.append('dBeta={0}'.format(getValueStr(self.dBeta)))
        if self.dGamma != obj.dGamma:
            paramArgs.append('dGamma={0}'.format(getValueStr(self.dGamma)))
        return 'ADVC_DYNAMIC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.dAlpha,
            self.dBeta,
            self.dGamma) + rightBracket

class TRANS_LBC_COPY:
    def __init__(self,
        iAxis=0,
        crCoord=None,
        dlTransVec=[0,0,0],
        dMag=0,
        dOffset=0,
        dTol=0):
        self.iAxis = iAxis
        self.crCoord = crCoord
        self.dlTransVec = dlTransVec
        self.dMag = dMag
        self.dOffset = dOffset
        self.dTol = dTol
    def isDefault(self):
        obj = TRANS_LBC_COPY()
        return self.iAxis == obj.iAxis and \
            self.crCoord == obj.crCoord and \
            self.dlTransVec == obj.dlTransVec and \
            self.dMag == obj.dMag and \
            self.dOffset == obj.dOffset and \
            self.dTol == obj.dTol
    def fromList(self, param):
        obj = TRANS_LBC_COPY()
        self.iAxis = param[0] if len(param) > 0 else obj.iAxis
        self.crCoord = getCursorValue(param[1]) if len(param) > 1 else obj.crCoord
        self.dlTransVec = [normalizeDoubleType(tok) for tok in param[2]] if len(param) > 2 else obj.dlTransVec
        self.dMag = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dMag
        self.dOffset = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dOffset
        self.dTol = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dTol
        return self
    def __str__(self):
        obj = TRANS_LBC_COPY()
        paramArgs = []
        if self.iAxis != obj.iAxis:
            paramArgs.append('iAxis={0}'.format(getValueStr(self.iAxis)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        if self.dlTransVec != obj.dlTransVec:
            paramArgs.append('dlTransVec={0}'.format(getValueStr(self.dlTransVec)))
        if self.dMag != obj.dMag:
            paramArgs.append('dMag={0}'.format(getValueStr(self.dMag)))
        if self.dOffset != obj.dOffset:
            paramArgs.append('dOffset={0}'.format(getValueStr(self.dOffset)))
        if self.dTol != obj.dTol:
            paramArgs.append('dTol={0}'.format(getValueStr(self.dTol)))
        return 'TRANS_LBC_COPY({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            self.iAxis,
            str(self.crCoord) if self.crCoord is not None else '0:0',
            self.dlTransVec,
            self.dMag,
            self.dOffset,
            self.dTol) + rightBracket

class ROTATE_LBC_COPY:
    def __init__(self,
        iAxis=0,
        iCenter=2,
        dlCenterVec=[0,0,0],
        dlAxisVec=[0,0,0],
        crCoord=None,
        dAngle=0,
        dTol=0):
        self.iAxis = iAxis
        self.iCenter = iCenter
        self.dlCenterVec = dlCenterVec
        self.dlAxisVec = dlAxisVec
        self.crCoord = crCoord
        self.dAngle = dAngle
        self.dTol = dTol
    def isDefault(self):
        obj = ROTATE_LBC_COPY()
        return self.iAxis == obj.iAxis and \
            self.iCenter == obj.iCenter and \
            self.dlCenterVec == obj.dlCenterVec and \
            self.dlAxisVec == obj.dlAxisVec and \
            self.crCoord == obj.crCoord and \
            self.dAngle == obj.dAngle and \
            self.dTol == obj.dTol
    def fromList(self, param):
        obj = ROTATE_LBC_COPY()
        self.iAxis = param[0] if len(param) > 0 else obj.iAxis
        self.iCenter = param[1] if len(param) > 1 else obj.iCenter
        self.dlCenterVec = [normalizeDoubleType(tok) for tok in param[2]] if len(param) > 2 else obj.dlCenterVec
        self.dlAxisVec = [normalizeDoubleType(tok) for tok in param[3]] if len(param) > 3 else obj.dlAxisVec
        self.crCoord = getCursorValue(param[4]) if len(param) > 4 else obj.crCoord
        self.dAngle = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dAngle
        self.dTol = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dTol
        return self
    def __str__(self):
        obj = ROTATE_LBC_COPY()
        paramArgs = []
        if self.iAxis != obj.iAxis:
            paramArgs.append('iAxis={0}'.format(getValueStr(self.iAxis)))
        if self.iCenter != obj.iCenter:
            paramArgs.append('iCenter={0}'.format(getValueStr(self.iCenter)))
        if self.dlCenterVec != obj.dlCenterVec:
            paramArgs.append('dlCenterVec={0}'.format(getValueStr(self.dlCenterVec)))
        if self.dlAxisVec != obj.dlAxisVec:
            paramArgs.append('dlAxisVec={0}'.format(getValueStr(self.dlAxisVec)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        if self.dAngle != obj.dAngle:
            paramArgs.append('dAngle={0}'.format(getValueStr(self.dAngle)))
        if self.dTol != obj.dTol:
            paramArgs.append('dTol={0}'.format(getValueStr(self.dTol)))
        return 'ROTATE_LBC_COPY({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            self.iAxis,
            self.iCenter,
            self.dlCenterVec,
            self.dlAxisVec,
            str(self.crCoord) if self.crCoord is not None else '0:0',
            self.dAngle,
            self.dTol) + rightBracket

class MIRRO_LBC_COPY:
    def __init__(self,
        dOffset=0,
        dTol=0.1,
        veclPoint=[]):
        self.dOffset = dOffset
        self.dTol = dTol
        self.veclPoint = veclPoint
    def isDefault(self):
        obj = MIRRO_LBC_COPY()
        return self.dOffset == obj.dOffset and \
            self.dTol == obj.dTol and \
            self.veclPoint == obj.veclPoint
    def fromList(self, param):
        obj = MIRRO_LBC_COPY()
        self.dOffset = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dOffset
        self.dTol = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dTol
        self.veclPoint = [[normalizeDoubleType(v) for v in tok] for tok in param[2]] if len(param) > 2 else obj.veclPoint
        return self
    def __str__(self):
        obj = MIRRO_LBC_COPY()
        paramArgs = []
        if self.dOffset != obj.dOffset:
            paramArgs.append('dOffset={0}'.format(getValueStr(self.dOffset)))
        if self.dTol != obj.dTol:
            paramArgs.append('dTol={0}'.format(getValueStr(self.dTol)))
        if self.veclPoint != obj.veclPoint:
            paramArgs.append('veclPoint={0}'.format([[getValueStr(v) for v in tok] for tok in self.veclPoint]))
        return 'MIRRO_LBC_COPY({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.dOffset,
            self.dTol,
            self.veclPoint) + rightBracket

class ADVC_EXPLICIT_DYNAMIC:
    def __init__(self,
        iLogMessageInterval=DFLT_INT,
        iLinearApproximation=-1,
        dBulkViscosityCoef1=DFLT_DBL,
        dBulkViscosityCoef2=DFLT_DBL,
        dMassScalingdt=DFLT_DBL,
        dDtScaleFactor=DFLT_DBL,
        dPenaltyScaleFactor=DFLT_DBL,
        iContactSearchInterval=DFLT_INT):
        self.iLogMessageInterval = iLogMessageInterval
        self.iLinearApproximation = iLinearApproximation
        self.dBulkViscosityCoef1 = dBulkViscosityCoef1
        self.dBulkViscosityCoef2 = dBulkViscosityCoef2
        self.dMassScalingdt = dMassScalingdt
        self.dDtScaleFactor = dDtScaleFactor
        self.dPenaltyScaleFactor = dPenaltyScaleFactor
        self.iContactSearchInterval = iContactSearchInterval
    def isDefault(self):
        obj = ADVC_EXPLICIT_DYNAMIC()
        return self.iLogMessageInterval == obj.iLogMessageInterval and \
            self.iLinearApproximation == obj.iLinearApproximation and \
            self.dBulkViscosityCoef1 == obj.dBulkViscosityCoef1 and \
            self.dBulkViscosityCoef2 == obj.dBulkViscosityCoef2 and \
            self.dMassScalingdt == obj.dMassScalingdt and \
            self.dDtScaleFactor == obj.dDtScaleFactor and \
            self.dPenaltyScaleFactor == obj.dPenaltyScaleFactor and \
            self.iContactSearchInterval == obj.iContactSearchInterval
    def fromList(self, param):
        obj = ADVC_EXPLICIT_DYNAMIC()
        self.iLogMessageInterval = param[0] if len(param) > 0 else obj.iLogMessageInterval
        self.iLinearApproximation = param[1] if len(param) > 1 else obj.iLinearApproximation
        self.dBulkViscosityCoef1 = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dBulkViscosityCoef1
        self.dBulkViscosityCoef2 = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dBulkViscosityCoef2
        self.dMassScalingdt = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dMassScalingdt
        self.dDtScaleFactor = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dDtScaleFactor
        self.dPenaltyScaleFactor = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dPenaltyScaleFactor
        self.iContactSearchInterval = param[7] if len(param) > 7 else obj.iContactSearchInterval
        return self
    def __str__(self):
        obj = ADVC_EXPLICIT_DYNAMIC()
        paramArgs = []
        if self.iLogMessageInterval != obj.iLogMessageInterval:
            paramArgs.append('iLogMessageInterval={0}'.format(getValueStr(self.iLogMessageInterval)))
        if self.iLinearApproximation != obj.iLinearApproximation:
            paramArgs.append('iLinearApproximation={0}'.format(getValueStr(self.iLinearApproximation)))
        if self.dBulkViscosityCoef1 != obj.dBulkViscosityCoef1:
            paramArgs.append('dBulkViscosityCoef1={0}'.format(getValueStr(self.dBulkViscosityCoef1)))
        if self.dBulkViscosityCoef2 != obj.dBulkViscosityCoef2:
            paramArgs.append('dBulkViscosityCoef2={0}'.format(getValueStr(self.dBulkViscosityCoef2)))
        if self.dMassScalingdt != obj.dMassScalingdt:
            paramArgs.append('dMassScalingdt={0}'.format(getValueStr(self.dMassScalingdt)))
        if self.dDtScaleFactor != obj.dDtScaleFactor:
            paramArgs.append('dDtScaleFactor={0}'.format(getValueStr(self.dDtScaleFactor)))
        if self.dPenaltyScaleFactor != obj.dPenaltyScaleFactor:
            paramArgs.append('dPenaltyScaleFactor={0}'.format(getValueStr(self.dPenaltyScaleFactor)))
        if self.iContactSearchInterval != obj.iContactSearchInterval:
            paramArgs.append('iContactSearchInterval={0}'.format(getValueStr(self.iContactSearchInterval)))
        return 'ADVC_EXPLICIT_DYNAMIC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(
            self.iLogMessageInterval,
            self.iLinearApproximation,
            self.dBulkViscosityCoef1,
            self.dBulkViscosityCoef2,
            self.dMassScalingdt,
            self.dDtScaleFactor,
            self.dPenaltyScaleFactor,
            self.iContactSearchInterval) + rightBracket

class ENFORCED_VELOCITY_LBC:
    def __init__(self,
        iDwDof=0,
        dVelocityTX=DFLT_DBL,
        dVelocityTY=DFLT_DBL,
        dVelocityTZ=DFLT_DBL,
        dVelocityRX=DFLT_DBL,
        dVelocityRY=DFLT_DBL,
        dVelocityRZ=DFLT_DBL,
        crCurCoord=None,
        iEndArrowDir=0,
        crTable=None,
        crNodeSet=None,
        dPhase=DFLT_DBL,
        dDelay=DFLT_DBL,
        crPhaseTable=None,
        iVelocityUnit=0,
        iRotUnit=0,
        bExport=False,
        crExportDataTX=None,
        crExportDataTY=None,
        crExportDataTZ=None,
        crExportDataRX=None,
        crExportDataRY=None,
        crExportDataRZ=None):
        self.iDwDof = iDwDof
        self.dVelocityTX = dVelocityTX
        self.dVelocityTY = dVelocityTY
        self.dVelocityTZ = dVelocityTZ
        self.dVelocityRX = dVelocityRX
        self.dVelocityRY = dVelocityRY
        self.dVelocityRZ = dVelocityRZ
        self.crCurCoord = crCurCoord
        self.iEndArrowDir = iEndArrowDir
        self.crTable = crTable
        self.crNodeSet = crNodeSet
        self.dPhase = dPhase
        self.dDelay = dDelay
        self.crPhaseTable = crPhaseTable
        self.iVelocityUnit = iVelocityUnit
        self.iRotUnit = iRotUnit
        self.bExport = bExport
        self.crExportDataTX = crExportDataTX
        self.crExportDataTY = crExportDataTY
        self.crExportDataTZ = crExportDataTZ
        self.crExportDataRX = crExportDataRX
        self.crExportDataRY = crExportDataRY
        self.crExportDataRZ = crExportDataRZ
    def isDefault(self):
        obj = ENFORCED_VELOCITY_LBC()
        return self.iDwDof == obj.iDwDof and \
            self.dVelocityTX == obj.dVelocityTX and \
            self.dVelocityTY == obj.dVelocityTY and \
            self.dVelocityTZ == obj.dVelocityTZ and \
            self.dVelocityRX == obj.dVelocityRX and \
            self.dVelocityRY == obj.dVelocityRY and \
            self.dVelocityRZ == obj.dVelocityRZ and \
            self.crCurCoord == obj.crCurCoord and \
            self.iEndArrowDir == obj.iEndArrowDir and \
            self.crTable == obj.crTable and \
            self.crNodeSet == obj.crNodeSet and \
            self.dPhase == obj.dPhase and \
            self.dDelay == obj.dDelay and \
            self.crPhaseTable == obj.crPhaseTable and \
            self.iVelocityUnit == obj.iVelocityUnit and \
            self.iRotUnit == obj.iRotUnit and \
            self.bExport == obj.bExport and \
            self.crExportDataTX == obj.crExportDataTX and \
            self.crExportDataTY == obj.crExportDataTY and \
            self.crExportDataTZ == obj.crExportDataTZ and \
            self.crExportDataRX == obj.crExportDataRX and \
            self.crExportDataRY == obj.crExportDataRY and \
            self.crExportDataRZ == obj.crExportDataRZ
    def fromList(self, param):
        obj = ENFORCED_VELOCITY_LBC()
        self.iDwDof = param[0] if len(param) > 0 else obj.iDwDof
        self.dVelocityTX = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dVelocityTX
        self.dVelocityTY = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dVelocityTY
        self.dVelocityTZ = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dVelocityTZ
        self.dVelocityRX = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dVelocityRX
        self.dVelocityRY = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dVelocityRY
        self.dVelocityRZ = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dVelocityRZ
        self.crCurCoord = getCursorValue(param[7]) if len(param) > 7 else obj.crCurCoord
        self.iEndArrowDir = param[8] if len(param) > 8 else obj.iEndArrowDir
        self.crTable = getCursorValue(param[9]) if len(param) > 9 else obj.crTable
        self.crNodeSet = getCursorValue(param[10]) if len(param) > 10 else obj.crNodeSet
        self.dPhase = normalizeDoubleType(param[11]) if len(param) > 11 else obj.dPhase
        self.dDelay = normalizeDoubleType(param[12]) if len(param) > 12 else obj.dDelay
        self.crPhaseTable = getCursorValue(param[13]) if len(param) > 13 else obj.crPhaseTable
        self.iVelocityUnit = param[14] if len(param) > 14 else obj.iVelocityUnit
        self.iRotUnit = param[15] if len(param) > 15 else obj.iRotUnit
        self.bExport = getBoolValue(param[16]) if len(param) > 16 else obj.bExport
        self.crExportDataTX = getCursorValue(param[17]) if len(param) > 17 else obj.crExportDataTX
        self.crExportDataTY = getCursorValue(param[18]) if len(param) > 18 else obj.crExportDataTY
        self.crExportDataTZ = getCursorValue(param[19]) if len(param) > 19 else obj.crExportDataTZ
        self.crExportDataRX = getCursorValue(param[20]) if len(param) > 20 else obj.crExportDataRX
        self.crExportDataRY = getCursorValue(param[21]) if len(param) > 21 else obj.crExportDataRY
        self.crExportDataRZ = getCursorValue(param[22]) if len(param) > 22 else obj.crExportDataRZ
        return self
    def __str__(self):
        obj = ENFORCED_VELOCITY_LBC()
        paramArgs = []
        if self.iDwDof != obj.iDwDof:
            paramArgs.append('iDwDof={0}'.format(getValueStr(self.iDwDof)))
        if self.dVelocityTX != obj.dVelocityTX:
            paramArgs.append('dVelocityTX={0}'.format(getValueStr(self.dVelocityTX)))
        if self.dVelocityTY != obj.dVelocityTY:
            paramArgs.append('dVelocityTY={0}'.format(getValueStr(self.dVelocityTY)))
        if self.dVelocityTZ != obj.dVelocityTZ:
            paramArgs.append('dVelocityTZ={0}'.format(getValueStr(self.dVelocityTZ)))
        if self.dVelocityRX != obj.dVelocityRX:
            paramArgs.append('dVelocityRX={0}'.format(getValueStr(self.dVelocityRX)))
        if self.dVelocityRY != obj.dVelocityRY:
            paramArgs.append('dVelocityRY={0}'.format(getValueStr(self.dVelocityRY)))
        if self.dVelocityRZ != obj.dVelocityRZ:
            paramArgs.append('dVelocityRZ={0}'.format(getValueStr(self.dVelocityRZ)))
        if self.crCurCoord != obj.crCurCoord:
            paramArgs.append('crCurCoord={0}'.format(getCursorValueStr(self.crCurCoord)))
        if self.iEndArrowDir != obj.iEndArrowDir:
            paramArgs.append('iEndArrowDir={0}'.format(getValueStr(self.iEndArrowDir)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        if self.crNodeSet != obj.crNodeSet:
            paramArgs.append('crNodeSet={0}'.format(getCursorValueStr(self.crNodeSet)))
        if self.dPhase != obj.dPhase:
            paramArgs.append('dPhase={0}'.format(getValueStr(self.dPhase)))
        if self.dDelay != obj.dDelay:
            paramArgs.append('dDelay={0}'.format(getValueStr(self.dDelay)))
        if self.crPhaseTable != obj.crPhaseTable:
            paramArgs.append('crPhaseTable={0}'.format(getCursorValueStr(self.crPhaseTable)))
        if self.iVelocityUnit != obj.iVelocityUnit:
            paramArgs.append('iVelocityUnit={0}'.format(getValueStr(self.iVelocityUnit)))
        if self.iRotUnit != obj.iRotUnit:
            paramArgs.append('iRotUnit={0}'.format(getValueStr(self.iRotUnit)))
        if self.bExport != obj.bExport:
            paramArgs.append('bExport={0}'.format(getBoolStr(self.bExport)))
        if self.crExportDataTX != obj.crExportDataTX:
            paramArgs.append('crExportDataTX={0}'.format(getCursorValueStr(self.crExportDataTX)))
        if self.crExportDataTY != obj.crExportDataTY:
            paramArgs.append('crExportDataTY={0}'.format(getCursorValueStr(self.crExportDataTY)))
        if self.crExportDataTZ != obj.crExportDataTZ:
            paramArgs.append('crExportDataTZ={0}'.format(getCursorValueStr(self.crExportDataTZ)))
        if self.crExportDataRX != obj.crExportDataRX:
            paramArgs.append('crExportDataRX={0}'.format(getCursorValueStr(self.crExportDataRX)))
        if self.crExportDataRY != obj.crExportDataRY:
            paramArgs.append('crExportDataRY={0}'.format(getCursorValueStr(self.crExportDataRY)))
        if self.crExportDataRZ != obj.crExportDataRZ:
            paramArgs.append('crExportDataRZ={0}'.format(getCursorValueStr(self.crExportDataRZ)))
        return 'ENFORCED_VELOCITY_LBC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}'.format(
            self.iDwDof,
            self.dVelocityTX,
            self.dVelocityTY,
            self.dVelocityTZ,
            self.dVelocityRX,
            self.dVelocityRY,
            self.dVelocityRZ,
            str(self.crCurCoord) if self.crCurCoord is not None else '0:0',
            self.iEndArrowDir,
            str(self.crTable) if self.crTable is not None else '0:0',
            str(self.crNodeSet) if self.crNodeSet is not None else '0:0',
            self.dPhase,
            self.dDelay,
            str(self.crPhaseTable) if self.crPhaseTable is not None else '0:0',
            self.iVelocityUnit,
            self.iRotUnit,
            1 if self.bExport else 0,
            str(self.crExportDataTX) if self.crExportDataTX is not None else '0:0',
            str(self.crExportDataTY) if self.crExportDataTY is not None else '0:0',
            str(self.crExportDataTZ) if self.crExportDataTZ is not None else '0:0',
            str(self.crExportDataRX) if self.crExportDataRX is not None else '0:0',
            str(self.crExportDataRY) if self.crExportDataRY is not None else '0:0',
            str(self.crExportDataRZ) if self.crExportDataRZ is not None else '0:0') + rightBracket

class FORCE_ND_LBC:
    def __init__(self,
        ParamGeneralForce=FORCE_LBC(),
        dValueForND=1.0,
        strFormulaValue="",
        crElementForND=None):
        self.ParamGeneralForce = ParamGeneralForce
        self.dValueForND = dValueForND
        self.strFormulaValue = strFormulaValue
        self.crElementForND = crElementForND
    def isDefault(self):
        obj = FORCE_ND_LBC()
        return self.ParamGeneralForce == obj.ParamGeneralForce and \
            self.dValueForND == obj.dValueForND and \
            self.strFormulaValue == obj.strFormulaValue and \
            self.crElementForND == obj.crElementForND
    def fromList(self, param):
        obj = FORCE_ND_LBC()
        self.ParamGeneralForce = param[0] if len(param) > 0 else obj.ParamGeneralForce
        self.dValueForND = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dValueForND
        self.strFormulaValue = param[2] if len(param) > 2 else obj.strFormulaValue
        self.crElementForND = getCursorValue(param[3]) if len(param) > 3 else obj.crElementForND
        return self
    def __str__(self):
        obj = FORCE_ND_LBC()
        paramArgs = []
        if self.ParamGeneralForce != obj.ParamGeneralForce:
            paramArgs.append('ParamGeneralForce={0}'.format(self.ParamGeneralForce))
        if self.dValueForND != obj.dValueForND:
            paramArgs.append('dValueForND={0}'.format(getValueStr(self.dValueForND)))
        if self.strFormulaValue != obj.strFormulaValue:
            paramArgs.append('strFormulaValue={0}'.format('"' + self.strFormulaValue + '"'))
        if self.crElementForND != obj.crElementForND:
            paramArgs.append('crElementForND={0}'.format(getCursorValueStr(self.crElementForND)))
        return 'FORCE_ND_LBC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.ParamGeneralForce,
            self.dValueForND,
            '"' + self.strFormulaValue + '"',
            str(self.crElementForND) if self.crElementForND is not None else '0:0') + rightBracket

class SUBMODEL_FORCED_TEMP_LBC:
    def __init__(self,
        iSolver=0,
        strFilePathName="/home/",
        iProcessNo=0,
        iReferType=0,
        dExtensionRange=DFLT_DBL,
        dExtensionTol=DFLT_DBL,
        dExtensionLimitTol=DFLT_DBL,
        strGlobalElementSet="",
        iUseBucket=-1,
        iNumBucketMaxX=DFLT_INT,
        iNumBucketMaxY=DFLT_INT,
        iNumBucketMaxZ=DFLT_INT,
        iPrevBc=-1):
        self.iSolver = iSolver
        self.strFilePathName = strFilePathName
        self.iProcessNo = iProcessNo
        self.iReferType = iReferType
        self.dExtensionRange = dExtensionRange
        self.dExtensionTol = dExtensionTol
        self.dExtensionLimitTol = dExtensionLimitTol
        self.strGlobalElementSet = strGlobalElementSet
        self.iUseBucket = iUseBucket
        self.iNumBucketMaxX = iNumBucketMaxX
        self.iNumBucketMaxY = iNumBucketMaxY
        self.iNumBucketMaxZ = iNumBucketMaxZ
        self.iPrevBc = iPrevBc
    def isDefault(self):
        obj = SUBMODEL_FORCED_TEMP_LBC()
        return self.iSolver == obj.iSolver and \
            self.strFilePathName == obj.strFilePathName and \
            self.iProcessNo == obj.iProcessNo and \
            self.iReferType == obj.iReferType and \
            self.dExtensionRange == obj.dExtensionRange and \
            self.dExtensionTol == obj.dExtensionTol and \
            self.dExtensionLimitTol == obj.dExtensionLimitTol and \
            self.strGlobalElementSet == obj.strGlobalElementSet and \
            self.iUseBucket == obj.iUseBucket and \
            self.iNumBucketMaxX == obj.iNumBucketMaxX and \
            self.iNumBucketMaxY == obj.iNumBucketMaxY and \
            self.iNumBucketMaxZ == obj.iNumBucketMaxZ and \
            self.iPrevBc == obj.iPrevBc
    def fromList(self, param):
        obj = SUBMODEL_FORCED_TEMP_LBC()
        self.iSolver = param[0] if len(param) > 0 else obj.iSolver
        self.strFilePathName = param[1] if len(param) > 1 else obj.strFilePathName
        self.iProcessNo = param[2] if len(param) > 2 else obj.iProcessNo
        self.iReferType = param[3] if len(param) > 3 else obj.iReferType
        self.dExtensionRange = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dExtensionRange
        self.dExtensionTol = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dExtensionTol
        self.dExtensionLimitTol = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dExtensionLimitTol
        self.strGlobalElementSet = param[7] if len(param) > 7 else obj.strGlobalElementSet
        self.iUseBucket = param[8] if len(param) > 8 else obj.iUseBucket
        self.iNumBucketMaxX = param[9] if len(param) > 9 else obj.iNumBucketMaxX
        self.iNumBucketMaxY = param[10] if len(param) > 10 else obj.iNumBucketMaxY
        self.iNumBucketMaxZ = param[11] if len(param) > 11 else obj.iNumBucketMaxZ
        self.iPrevBc = param[12] if len(param) > 12 else obj.iPrevBc
        return self
    def __str__(self):
        obj = SUBMODEL_FORCED_TEMP_LBC()
        paramArgs = []
        if self.iSolver != obj.iSolver:
            paramArgs.append('iSolver={0}'.format(getValueStr(self.iSolver)))
        if self.strFilePathName != obj.strFilePathName:
            paramArgs.append('strFilePathName={0}'.format('"' + self.strFilePathName + '"'))
        if self.iProcessNo != obj.iProcessNo:
            paramArgs.append('iProcessNo={0}'.format(getValueStr(self.iProcessNo)))
        if self.iReferType != obj.iReferType:
            paramArgs.append('iReferType={0}'.format(getValueStr(self.iReferType)))
        if self.dExtensionRange != obj.dExtensionRange:
            paramArgs.append('dExtensionRange={0}'.format(getValueStr(self.dExtensionRange)))
        if self.dExtensionTol != obj.dExtensionTol:
            paramArgs.append('dExtensionTol={0}'.format(getValueStr(self.dExtensionTol)))
        if self.dExtensionLimitTol != obj.dExtensionLimitTol:
            paramArgs.append('dExtensionLimitTol={0}'.format(getValueStr(self.dExtensionLimitTol)))
        if self.strGlobalElementSet != obj.strGlobalElementSet:
            paramArgs.append('strGlobalElementSet={0}'.format('"' + self.strGlobalElementSet + '"'))
        if self.iUseBucket != obj.iUseBucket:
            paramArgs.append('iUseBucket={0}'.format(getValueStr(self.iUseBucket)))
        if self.iNumBucketMaxX != obj.iNumBucketMaxX:
            paramArgs.append('iNumBucketMaxX={0}'.format(getValueStr(self.iNumBucketMaxX)))
        if self.iNumBucketMaxY != obj.iNumBucketMaxY:
            paramArgs.append('iNumBucketMaxY={0}'.format(getValueStr(self.iNumBucketMaxY)))
        if self.iNumBucketMaxZ != obj.iNumBucketMaxZ:
            paramArgs.append('iNumBucketMaxZ={0}'.format(getValueStr(self.iNumBucketMaxZ)))
        if self.iPrevBc != obj.iPrevBc:
            paramArgs.append('iPrevBc={0}'.format(getValueStr(self.iPrevBc)))
        return 'SUBMODEL_FORCED_TEMP_LBC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}'.format(
            self.iSolver,
            '"' + self.strFilePathName + '"',
            self.iProcessNo,
            self.iReferType,
            self.dExtensionRange,
            self.dExtensionTol,
            self.dExtensionLimitTol,
            '"' + self.strGlobalElementSet + '"',
            self.iUseBucket,
            self.iNumBucketMaxX,
            self.iNumBucketMaxY,
            self.iNumBucketMaxZ,
            self.iPrevBc) + rightBracket

class FIND_OPTION_UTIL:
    def __init__(self,
        bFindMatch = False):
        self.bFindMatch = bFindMatch
    def isDefault(self):
        obj = FIND_OPTION_UTIL()
        return self.bFindMatch == obj.bFindMatch
    def fromList(self, param):
        obj = FIND_OPTION_UTIL()
        self.bFindMatch = getBoolValue(param[0]) if len(param) > 0 else obj.bFindMatch
        return self
    def __str__(self):
        obj = FIND_OPTION_UTIL()
        paramArgs = []
        if self.bFindMatch != obj.bFindMatch:
            paramArgs.append('bFindMatch={0}'.format(getBoolStr(self.bFindMatch)))
        return 'FIND_OPTION_UTIL({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}'.format(
            1 if self.bFindMatch else 0) + rightBracket

class MMC_ACMODEL_MESH:
    def __init__(self,
        crlPart=[],
        crlItem1=[],
        crlItem2=[],
        crlItem3=[],
        iType=-1,
        bMergeTol=False,
        dTol=0.01,
        dMeshSise=0.1,
        bCreatePart=False):
        self.crlPart = crlPart
        self.crlItem1 = crlItem1
        self.crlItem2 = crlItem2
        self.crlItem3 = crlItem3
        self.iType = iType
        self.bMergeTol = bMergeTol
        self.dTol = dTol
        self.dMeshSise = dMeshSise
        self.bCreatePart = bCreatePart
    def isDefault(self):
        obj = MMC_ACMODEL_MESH()
        return self.crlPart == obj.crlPart and \
            self.crlItem1 == obj.crlItem1 and \
            self.crlItem2 == obj.crlItem2 and \
            self.crlItem3 == obj.crlItem3 and \
            self.iType == obj.iType and \
            self.bMergeTol == obj.bMergeTol and \
            self.dTol == obj.dTol and \
            self.dMeshSise == obj.dMeshSise and \
            self.bCreatePart == obj.bCreatePart
    def fromList(self, param):
        obj = MMC_ACMODEL_MESH()
        self.crlPart = getCursorListValue(param[0]) if len(param) > 0 else obj.crlPart
        self.crlItem1 = getCursorListValue(param[1]) if len(param) > 1 else obj.crlItem1
        self.crlItem2 = getCursorListValue(param[2]) if len(param) > 2 else obj.crlItem2
        self.crlItem3 = getCursorListValue(param[3]) if len(param) > 3 else obj.crlItem3
        self.iType = param[4] if len(param) > 4 else obj.iType
        self.bMergeTol = getBoolValue(param[5]) if len(param) > 5 else obj.bMergeTol
        self.dTol = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dTol
        self.dMeshSise = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dMeshSise
        self.bCreatePart = getBoolValue(param[8]) if len(param) > 8 else obj.bCreatePart
        return self
    def __str__(self):
        obj = MMC_ACMODEL_MESH()
        paramArgs = []
        if self.crlPart != obj.crlPart:
            paramArgs.append('crlPart={0}'.format(getCursorListValueStr(self.crlPart)))
        if self.crlItem1 != obj.crlItem1:
            paramArgs.append('crlItem1={0}'.format(getCursorListValueStr(self.crlItem1)))
        if self.crlItem2 != obj.crlItem2:
            paramArgs.append('crlItem2={0}'.format(getCursorListValueStr(self.crlItem2)))
        if self.crlItem3 != obj.crlItem3:
            paramArgs.append('crlItem3={0}'.format(getCursorListValueStr(self.crlItem3)))
        if self.iType != obj.iType:
            paramArgs.append('iType={0}'.format(getValueStr(self.iType)))
        if self.bMergeTol != obj.bMergeTol:
            paramArgs.append('bMergeTol={0}'.format(getBoolStr(self.bMergeTol)))
        if self.dTol != obj.dTol:
            paramArgs.append('dTol={0}'.format(getValueStr(self.dTol)))
        if self.dMeshSise != obj.dMeshSise:
            paramArgs.append('dMeshSise={0}'.format(getValueStr(self.dMeshSise)))
        if self.bCreatePart != obj.bCreatePart:
            paramArgs.append('bCreatePart={0}'.format(getBoolStr(self.bCreatePart)))
        return 'MMC_ACMODEL_MESH({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            str(self.crlPart) if self.crlPart != [None] else '[0:0]',
            str(self.crlItem1) if self.crlItem1 != [None] else '[0:0]',
            str(self.crlItem2) if self.crlItem2 != [None] else '[0:0]',
            str(self.crlItem3) if self.crlItem3 != [None] else '[0:0]',
            self.iType,
            1 if self.bMergeTol else 0,
            self.dTol,
            self.dMeshSise,
            1 if self.bCreatePart else 0) + rightBracket

class BEAM_1D_PROP:
    def __init__(self,
        crMat=None,
        dArea=DFLT_DBL,
        iOrientType=DFLT_INT,
        vecOrient=[DFLT_DBL, DFLT_DBL, DFLT_DBL],
        iOrientNodeId=DFLT_INT,
        vecInertia=[DFLT_DBL, DFLT_DBL, DFLT_DBL],
        dTorConst=DFLT_DBL,
        dNSM=DFLT_DBL,
        dlDnsmAB=[DFLT_DBL, DFLT_DBL],
        listDnsmNode=[[DFLT_DBL, DFLT_DBL], [DFLT_DBL, DFLT_DBL]],
        dlShearStiffness=[DFLT_DBL, DFLT_DBL],
        dlShearAreaRelief=[DFLT_DBL, DFLT_DBL],
        dlWrapCoeff=[DFLT_DBL, DFLT_DBL],
        listNA=[[DFLT_DBL, DFLT_DBL], [DFLT_DBL, DFLT_DBL]],
        dlStressRecoveryCoeff=[DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL],
        bTapped=False,
        dTapDarea=DFLT_DBL,
        vecTapInertia=[DFLT_DBL, DFLT_DBL, DFLT_DBL],
        dTapDtorconst=DFLT_DBL,
        dTapDnsm=DFLT_DBL,
        dlTapStressrecoverycoeff=[DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL],
        iIntePtNum=DFLT_INT,
        blPinA=[False, False, False, False, False, False],
        blPinB=[False, False, False, False, False, False],
        veclOffset=[ [DFLT_DBL, DFLT_DBL, DFLT_DBL], [DFLT_DBL, DFLT_DBL, DFLT_DBL]]):
        self.crMat = crMat
        self.dArea = dArea
        self.iOrientType = iOrientType
        self.vecOrient = vecOrient
        self.iOrientNodeId = iOrientNodeId
        self.vecInertia = vecInertia
        self.dTorConst = dTorConst
        self.dNSM = dNSM
        self.dlDnsmAB = dlDnsmAB
        self.listDnsmNode = listDnsmNode
        self.dlShearStiffness = dlShearStiffness
        self.dlShearAreaRelief = dlShearAreaRelief
        self.dlWrapCoeff = dlWrapCoeff
        self.listNA = listNA
        self.dlStressRecoveryCoeff = dlStressRecoveryCoeff
        self.bTapped = bTapped
        self.dTapDarea = dTapDarea
        self.vecTapInertia = vecTapInertia
        self.dTapDtorconst = dTapDtorconst
        self.dTapDnsm = dTapDnsm
        self.dlTapStressrecoverycoeff = dlTapStressrecoverycoeff
        self.iIntePtNum = iIntePtNum
        self.blPinA = blPinA
        self.blPinB = blPinB
        self.veclOffset = veclOffset
    def isDefault(self):
        obj = BEAM_1D_PROP()
        return self.crMat == obj.crMat and \
            self.dArea == obj.dArea and \
            self.iOrientType == obj.iOrientType and \
            self.vecOrient == obj.vecOrient and \
            self.iOrientNodeId == obj.iOrientNodeId and \
            self.vecInertia == obj.vecInertia and \
            self.dTorConst == obj.dTorConst and \
            self.dNSM == obj.dNSM and \
            self.dlDnsmAB == obj.dlDnsmAB and \
            self.listDnsmNode == obj.listDnsmNode and \
            self.dlShearStiffness == obj.dlShearStiffness and \
            self.dlShearAreaRelief == obj.dlShearAreaRelief and \
            self.dlWrapCoeff == obj.dlWrapCoeff and \
            self.listNA == obj.listNA and \
            self.dlStressRecoveryCoeff == obj.dlStressRecoveryCoeff and \
            self.bTapped == obj.bTapped and \
            self.dTapDarea == obj.dTapDarea and \
            self.vecTapInertia == obj.vecTapInertia and \
            self.dTapDtorconst == obj.dTapDtorconst and \
            self.dTapDnsm == obj.dTapDnsm and \
            self.dlTapStressrecoverycoeff == obj.dlTapStressrecoverycoeff and \
            self.iIntePtNum == obj.iIntePtNum and \
            self.blPinA == obj.blPinA and \
            self.blPinB == obj.blPinB and \
            self.veclOffset == obj.veclOffset
    def fromList(self, param):
        obj = BEAM_1D_PROP()
        self.crMat = getCursorValue(param[0]) if len(param) > 0 else obj.crMat
        self.dArea = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dArea
        self.iOrientType = param[2] if len(param) > 2 else obj.iOrientType
        self.vecOrient = [normalizeDoubleType(tok) for tok in param[3]] if len(param) > 3 else obj.vecOrient
        self.iOrientNodeId = param[4] if len(param) > 4 else obj.iOrientNodeId
        self.vecInertia = [normalizeDoubleType(tok) for tok in param[5]] if len(param) > 5 else obj.vecInertia
        self.dTorConst = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dTorConst
        self.dNSM = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dNSM
        self.dlDnsmAB = [normalizeDoubleType(tok) for tok in param[8]] if len(param) > 8 else obj.dlDnsmAB
        self.listDnsmNode = param[9] if len(param) > 9 else obj.listDnsmNode
        self.dlShearStiffness = [normalizeDoubleType(tok) for tok in param[10]] if len(param) > 10 else obj.dlShearStiffness
        self.dlShearAreaRelief = [normalizeDoubleType(tok) for tok in param[11]] if len(param) > 11 else obj.dlShearAreaRelief
        self.dlWrapCoeff = [normalizeDoubleType(tok) for tok in param[12]] if len(param) > 12 else obj.dlWrapCoeff
        self.listNA = param[13] if len(param) > 13 else obj.listNA
        self.dlStressRecoveryCoeff = [normalizeDoubleType(tok) for tok in param[14]] if len(param) > 14 else obj.dlStressRecoveryCoeff
        self.bTapped = getBoolValue(param[15]) if len(param) > 15 else obj.bTapped
        self.dTapDarea = normalizeDoubleType(param[16]) if len(param) > 16 else obj.dTapDarea
        self.vecTapInertia = [normalizeDoubleType(tok) for tok in param[17]] if len(param) > 17 else obj.vecTapInertia
        self.dTapDtorconst = normalizeDoubleType(param[18]) if len(param) > 18 else obj.dTapDtorconst
        self.dTapDnsm = normalizeDoubleType(param[19]) if len(param) > 19 else obj.dTapDnsm
        self.dlTapStressrecoverycoeff = [normalizeDoubleType(tok) for tok in param[20]] if len(param) > 20 else obj.dlTapStressrecoverycoeff
        self.iIntePtNum = param[21] if len(param) > 21 else obj.iIntePtNum
        self.blPinA = param[22] if len(param) > 22 else obj.blPinA
        self.blPinB = param[23] if len(param) > 23 else obj.blPinB
        self.veclOffset = [[normalizeDoubleType(v) for v in tok] for tok in param[24]] if len(param) > 24 else obj.veclOffset
        return self
    def __str__(self):
        obj = BEAM_1D_PROP()
        paramArgs = []
        if self.crMat != obj.crMat:
            paramArgs.append('crMat={0}'.format(getCursorValueStr(self.crMat)))
        if self.dArea != obj.dArea:
            paramArgs.append('dArea={0}'.format(getValueStr(self.dArea)))
        if self.iOrientType != obj.iOrientType:
            paramArgs.append('iOrientType={0}'.format(getValueStr(self.iOrientType)))
        if self.vecOrient != obj.vecOrient:
            paramArgs.append('vecOrient={0}'.format(getValueStr(self.vecOrient)))
        if self.iOrientNodeId != obj.iOrientNodeId:
            paramArgs.append('iOrientNodeId={0}'.format(getValueStr(self.iOrientNodeId)))
        if self.vecInertia != obj.vecInertia:
            paramArgs.append('vecInertia={0}'.format(getValueStr(self.vecInertia)))
        if self.dTorConst != obj.dTorConst:
            paramArgs.append('dTorConst={0}'.format(getValueStr(self.dTorConst)))
        if self.dNSM != obj.dNSM:
            paramArgs.append('dNSM={0}'.format(getValueStr(self.dNSM)))
        if self.dlDnsmAB != obj.dlDnsmAB:
            paramArgs.append('dlDnsmAB={0}'.format(getValueStr(self.dlDnsmAB)))
        if self.listDnsmNode != obj.listDnsmNode:
            paramArgs.append('listDnsmNode={0}'.format(self.listDnsmNode))
        if self.dlShearStiffness != obj.dlShearStiffness:
            paramArgs.append('dlShearStiffness={0}'.format(getValueStr(self.dlShearStiffness)))
        if self.dlShearAreaRelief != obj.dlShearAreaRelief:
            paramArgs.append('dlShearAreaRelief={0}'.format(getValueStr(self.dlShearAreaRelief)))
        if self.dlWrapCoeff != obj.dlWrapCoeff:
            paramArgs.append('dlWrapCoeff={0}'.format(getValueStr(self.dlWrapCoeff)))
        if self.listNA != obj.listNA:
            paramArgs.append('listNA={0}'.format(self.listNA))
        if self.dlStressRecoveryCoeff != obj.dlStressRecoveryCoeff:
            paramArgs.append('dlStressRecoveryCoeff={0}'.format(getValueStr(self.dlStressRecoveryCoeff)))
        if self.bTapped != obj.bTapped:
            paramArgs.append('bTapped={0}'.format(getBoolStr(self.bTapped)))
        if self.dTapDarea != obj.dTapDarea:
            paramArgs.append('dTapDarea={0}'.format(getValueStr(self.dTapDarea)))
        if self.vecTapInertia != obj.vecTapInertia:
            paramArgs.append('vecTapInertia={0}'.format(getValueStr(self.vecTapInertia)))
        if self.dTapDtorconst != obj.dTapDtorconst:
            paramArgs.append('dTapDtorconst={0}'.format(getValueStr(self.dTapDtorconst)))
        if self.dTapDnsm != obj.dTapDnsm:
            paramArgs.append('dTapDnsm={0}'.format(getValueStr(self.dTapDnsm)))
        if self.dlTapStressrecoverycoeff != obj.dlTapStressrecoverycoeff:
            paramArgs.append('dlTapStressrecoverycoeff={0}'.format(getValueStr(self.dlTapStressrecoverycoeff)))
        if self.iIntePtNum != obj.iIntePtNum:
            paramArgs.append('iIntePtNum={0}'.format(getValueStr(self.iIntePtNum)))
        if self.blPinA != obj.blPinA:
            paramArgs.append('blPinA={0}'.format(self.blPinA))
        if self.blPinB != obj.blPinB:
            paramArgs.append('blPinB={0}'.format(self.blPinB))
        if self.veclOffset != obj.veclOffset:
            paramArgs.append('veclOffset={0}'.format([[getValueStr(v) for v in tok] for tok in self.veclOffset]))
        return 'BEAM_1D_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}'.format(
            str(self.crMat) if self.crMat is not None else '0:0',
            self.dArea,
            self.iOrientType,
            self.vecOrient,
            self.iOrientNodeId,
            self.vecInertia,
            self.dTorConst,
            self.dNSM,
            self.dlDnsmAB,
            self.listDnsmNode,
            self.dlShearStiffness,
            self.dlShearAreaRelief,
            self.dlWrapCoeff,
            self.listNA,
            self.dlStressRecoveryCoeff,
            1 if self.bTapped else 0,
            self.dTapDarea,
            self.vecTapInertia,
            self.dTapDtorconst,
            self.dTapDnsm,
            self.dlTapStressrecoverycoeff,
            self.iIntePtNum,
            1 if self.blPinA else 0,
            1 if self.blPinB else 0,
            self.veclOffset) + rightBracket

class CONNECT_RENUMBER_TOOL:
    def __init__(self,
        iItemType=0,
        iKConn=0,
        iSolver=0,
        iStartID=0):
        self.iItemType = iItemType
        self.iKConn = iKConn
        self.iSolver = iSolver
        self.iStartID = iStartID
    def isDefault(self):
        obj = CONNECT_RENUMBER_TOOL()
        return self.iItemType == obj.iItemType and \
            self.iKConn == obj.iKConn and \
            self.iSolver == obj.iSolver and \
            self.iStartID == obj.iStartID
    def fromList(self, param):
        obj = CONNECT_RENUMBER_TOOL()
        self.iItemType = param[0] if len(param) > 0 else obj.iItemType
        self.iKConn = param[1] if len(param) > 1 else obj.iKConn
        self.iSolver = param[2] if len(param) > 2 else obj.iSolver
        self.iStartID = param[3] if len(param) > 3 else obj.iStartID
        return self
    def __str__(self):
        obj = CONNECT_RENUMBER_TOOL()
        paramArgs = []
        if self.iItemType != obj.iItemType:
            paramArgs.append('iItemType={0}'.format(getValueStr(self.iItemType)))
        if self.iKConn != obj.iKConn:
            paramArgs.append('iKConn={0}'.format(getValueStr(self.iKConn)))
        if self.iSolver != obj.iSolver:
            paramArgs.append('iSolver={0}'.format(getValueStr(self.iSolver)))
        if self.iStartID != obj.iStartID:
            paramArgs.append('iStartID={0}'.format(getValueStr(self.iStartID)))
        return 'CONNECT_RENUMBER_TOOL({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.iItemType,
            self.iKConn,
            self.iSolver,
            self.iStartID) + rightBracket

class ERICONT_END_PROP:
    def __init__(self,
        iConnId=0,
        iEndA=0,
        iEndB=0):
        self.iConnId = iConnId
        self.iEndA = iEndA
        self.iEndB = iEndB
    def isDefault(self):
        obj = ERICONT_END_PROP()
        return self.iConnId == obj.iConnId and \
            self.iEndA == obj.iEndA and \
            self.iEndB == obj.iEndB
    def fromList(self, param):
        obj = ERICONT_END_PROP()
        self.iConnId = param[0] if len(param) > 0 else obj.iConnId
        self.iEndA = param[1] if len(param) > 1 else obj.iEndA
        self.iEndB = param[2] if len(param) > 2 else obj.iEndB
        return self
    def __str__(self):
        obj = ERICONT_END_PROP()
        paramArgs = []
        if self.iConnId != obj.iConnId:
            paramArgs.append('iConnId={0}'.format(getValueStr(self.iConnId)))
        if self.iEndA != obj.iEndA:
            paramArgs.append('iEndA={0}'.format(getValueStr(self.iEndA)))
        if self.iEndB != obj.iEndB:
            paramArgs.append('iEndB={0}'.format(getValueStr(self.iEndB)))
        return 'ERICONT_END_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iConnId,
            self.iEndA,
            self.iEndB) + rightBracket

class ERICONT_ORI_VEC_PROP:
    def __init__(self,
        iConnId=0,
        iEndA=0,
        iEndB=0,
        dOrientVecX=0.0,
        dOrientVecY=0.0,
        dOrientVecZ=0.0):
        self.iConnId = iConnId
        self.iEndA = iEndA
        self.iEndB = iEndB
        self.dOrientVecX = dOrientVecX
        self.dOrientVecY = dOrientVecY
        self.dOrientVecZ = dOrientVecZ
    def isDefault(self):
        obj = ERICONT_ORI_VEC_PROP()
        return self.iConnId == obj.iConnId and \
            self.iEndA == obj.iEndA and \
            self.iEndB == obj.iEndB and \
            self.dOrientVecX == obj.dOrientVecX and \
            self.dOrientVecY == obj.dOrientVecY and \
            self.dOrientVecZ == obj.dOrientVecZ
    def fromList(self, param):
        obj = ERICONT_ORI_VEC_PROP()
        self.iConnId = param[0] if len(param) > 0 else obj.iConnId
        self.iEndA = param[1] if len(param) > 1 else obj.iEndA
        self.iEndB = param[2] if len(param) > 2 else obj.iEndB
        self.dOrientVecX = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dOrientVecX
        self.dOrientVecY = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dOrientVecY
        self.dOrientVecZ = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dOrientVecZ
        return self
    def __str__(self):
        obj = ERICONT_ORI_VEC_PROP()
        paramArgs = []
        if self.iConnId != obj.iConnId:
            paramArgs.append('iConnId={0}'.format(getValueStr(self.iConnId)))
        if self.iEndA != obj.iEndA:
            paramArgs.append('iEndA={0}'.format(getValueStr(self.iEndA)))
        if self.iEndB != obj.iEndB:
            paramArgs.append('iEndB={0}'.format(getValueStr(self.iEndB)))
        if self.dOrientVecX != obj.dOrientVecX:
            paramArgs.append('dOrientVecX={0}'.format(getValueStr(self.dOrientVecX)))
        if self.dOrientVecY != obj.dOrientVecY:
            paramArgs.append('dOrientVecY={0}'.format(getValueStr(self.dOrientVecY)))
        if self.dOrientVecZ != obj.dOrientVecZ:
            paramArgs.append('dOrientVecZ={0}'.format(getValueStr(self.dOrientVecZ)))
        return 'ERICONT_ORI_VEC_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            self.iConnId,
            self.iEndA,
            self.iEndB,
            self.dOrientVecX,
            self.dOrientVecY,
            self.dOrientVecZ) + rightBracket

class ERICONT_NODEID_PROP:
    def __init__(self,
        iConnId=0,
        iEndA=0,
        iEndB=0,
        iNodeID=0):
        self.iConnId = iConnId
        self.iEndA = iEndA
        self.iEndB = iEndB
        self.iNodeID = iNodeID
    def isDefault(self):
        obj = ERICONT_NODEID_PROP()
        return self.iConnId == obj.iConnId and \
            self.iEndA == obj.iEndA and \
            self.iEndB == obj.iEndB and \
            self.iNodeID == obj.iNodeID
    def fromList(self, param):
        obj = ERICONT_NODEID_PROP()
        self.iConnId = param[0] if len(param) > 0 else obj.iConnId
        self.iEndA = param[1] if len(param) > 1 else obj.iEndA
        self.iEndB = param[2] if len(param) > 2 else obj.iEndB
        self.iNodeID = param[3] if len(param) > 3 else obj.iNodeID
        return self
    def __str__(self):
        obj = ERICONT_NODEID_PROP()
        paramArgs = []
        if self.iConnId != obj.iConnId:
            paramArgs.append('iConnId={0}'.format(getValueStr(self.iConnId)))
        if self.iEndA != obj.iEndA:
            paramArgs.append('iEndA={0}'.format(getValueStr(self.iEndA)))
        if self.iEndB != obj.iEndB:
            paramArgs.append('iEndB={0}'.format(getValueStr(self.iEndB)))
        if self.iNodeID != obj.iNodeID:
            paramArgs.append('iNodeID={0}'.format(getValueStr(self.iNodeID)))
        return 'ERICONT_NODEID_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.iConnId,
            self.iEndA,
            self.iEndB,
            self.iNodeID) + rightBracket

class ERICONT_CID_PROP:
    def __init__(self,
        iConnId=0,
        iEndA=0,
        iEndB=0,
        iCid=0):
        self.iConnId = iConnId
        self.iEndA = iEndA
        self.iEndB = iEndB
        self.iCid = iCid
    def isDefault(self):
        obj = ERICONT_CID_PROP()
        return self.iConnId == obj.iConnId and \
            self.iEndA == obj.iEndA and \
            self.iEndB == obj.iEndB and \
            self.iCid == obj.iCid
    def fromList(self, param):
        obj = ERICONT_CID_PROP()
        self.iConnId = param[0] if len(param) > 0 else obj.iConnId
        self.iEndA = param[1] if len(param) > 1 else obj.iEndA
        self.iEndB = param[2] if len(param) > 2 else obj.iEndB
        self.iCid = param[3] if len(param) > 3 else obj.iCid
        return self
    def __str__(self):
        obj = ERICONT_CID_PROP()
        paramArgs = []
        if self.iConnId != obj.iConnId:
            paramArgs.append('iConnId={0}'.format(getValueStr(self.iConnId)))
        if self.iEndA != obj.iEndA:
            paramArgs.append('iEndA={0}'.format(getValueStr(self.iEndA)))
        if self.iEndB != obj.iEndB:
            paramArgs.append('iEndB={0}'.format(getValueStr(self.iEndB)))
        if self.iCid != obj.iCid:
            paramArgs.append('iCid={0}'.format(getValueStr(self.iCid)))
        return 'ERICONT_CID_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.iConnId,
            self.iEndA,
            self.iEndB,
            self.iCid) + rightBracket

class ERICONT_DAMPER_LOC_PROP:
    def __init__(self,
        iConnId=0,
        iEndA=0,
        iEndB=0,
        dAmperLoc=0.0):
        self.iConnId = iConnId
        self.iEndA = iEndA
        self.iEndB = iEndB
        self.dAmperLoc = dAmperLoc
    def isDefault(self):
        obj = ERICONT_DAMPER_LOC_PROP()
        return self.iConnId == obj.iConnId and \
            self.iEndA == obj.iEndA and \
            self.iEndB == obj.iEndB and \
            self.dAmperLoc == obj.dAmperLoc
    def fromList(self, param):
        obj = ERICONT_DAMPER_LOC_PROP()
        self.iConnId = param[0] if len(param) > 0 else obj.iConnId
        self.iEndA = param[1] if len(param) > 1 else obj.iEndA
        self.iEndB = param[2] if len(param) > 2 else obj.iEndB
        self.dAmperLoc = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dAmperLoc
        return self
    def __str__(self):
        obj = ERICONT_DAMPER_LOC_PROP()
        paramArgs = []
        if self.iConnId != obj.iConnId:
            paramArgs.append('iConnId={0}'.format(getValueStr(self.iConnId)))
        if self.iEndA != obj.iEndA:
            paramArgs.append('iEndA={0}'.format(getValueStr(self.iEndA)))
        if self.iEndB != obj.iEndB:
            paramArgs.append('iEndB={0}'.format(getValueStr(self.iEndB)))
        if self.dAmperLoc != obj.dAmperLoc:
            paramArgs.append('dAmperLoc={0}'.format(getValueStr(self.dAmperLoc)))
        return 'ERICONT_DAMPER_LOC_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.iConnId,
            self.iEndA,
            self.iEndB,
            self.dAmperLoc) + rightBracket

class ERICONT_OCID_PROP:
    def __init__(self,
        iConnId=0,
        iEndA=0,
        iEndB=0,
        iOcid=0):
        self.iConnId = iConnId
        self.iEndA = iEndA
        self.iEndB = iEndB
        self.iOcid = iOcid
    def isDefault(self):
        obj = ERICONT_OCID_PROP()
        return self.iConnId == obj.iConnId and \
            self.iEndA == obj.iEndA and \
            self.iEndB == obj.iEndB and \
            self.iOcid == obj.iOcid
    def fromList(self, param):
        obj = ERICONT_OCID_PROP()
        self.iConnId = param[0] if len(param) > 0 else obj.iConnId
        self.iEndA = param[1] if len(param) > 1 else obj.iEndA
        self.iEndB = param[2] if len(param) > 2 else obj.iEndB
        self.iOcid = param[3] if len(param) > 3 else obj.iOcid
        return self
    def __str__(self):
        obj = ERICONT_OCID_PROP()
        paramArgs = []
        if self.iConnId != obj.iConnId:
            paramArgs.append('iConnId={0}'.format(getValueStr(self.iConnId)))
        if self.iEndA != obj.iEndA:
            paramArgs.append('iEndA={0}'.format(getValueStr(self.iEndA)))
        if self.iEndB != obj.iEndB:
            paramArgs.append('iEndB={0}'.format(getValueStr(self.iEndB)))
        if self.iOcid != obj.iOcid:
            paramArgs.append('iOcid={0}'.format(getValueStr(self.iOcid)))
        return 'ERICONT_OCID_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.iConnId,
            self.iEndA,
            self.iEndB,
            self.iOcid) + rightBracket

class ERICONT_DAMPER_OFFSET_VEC_PROP:
    def __init__(self,
        iConnId=0,
        iEndA=0,
        iEndB=0,
        dAmperOffsetVecX=0.0,
        dAmperOffsetVecY=0.0,
        dAmperOffsetVecZ=0.0):
        self.iConnId = iConnId
        self.iEndA = iEndA
        self.iEndB = iEndB
        self.dAmperOffsetVecX = dAmperOffsetVecX
        self.dAmperOffsetVecY = dAmperOffsetVecY
        self.dAmperOffsetVecZ = dAmperOffsetVecZ
    def isDefault(self):
        obj = ERICONT_DAMPER_OFFSET_VEC_PROP()
        return self.iConnId == obj.iConnId and \
            self.iEndA == obj.iEndA and \
            self.iEndB == obj.iEndB and \
            self.dAmperOffsetVecX == obj.dAmperOffsetVecX and \
            self.dAmperOffsetVecY == obj.dAmperOffsetVecY and \
            self.dAmperOffsetVecZ == obj.dAmperOffsetVecZ
    def fromList(self, param):
        obj = ERICONT_DAMPER_OFFSET_VEC_PROP()
        self.iConnId = param[0] if len(param) > 0 else obj.iConnId
        self.iEndA = param[1] if len(param) > 1 else obj.iEndA
        self.iEndB = param[2] if len(param) > 2 else obj.iEndB
        self.dAmperOffsetVecX = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dAmperOffsetVecX
        self.dAmperOffsetVecY = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dAmperOffsetVecY
        self.dAmperOffsetVecZ = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dAmperOffsetVecZ
        return self
    def __str__(self):
        obj = ERICONT_DAMPER_OFFSET_VEC_PROP()
        paramArgs = []
        if self.iConnId != obj.iConnId:
            paramArgs.append('iConnId={0}'.format(getValueStr(self.iConnId)))
        if self.iEndA != obj.iEndA:
            paramArgs.append('iEndA={0}'.format(getValueStr(self.iEndA)))
        if self.iEndB != obj.iEndB:
            paramArgs.append('iEndB={0}'.format(getValueStr(self.iEndB)))
        if self.dAmperOffsetVecX != obj.dAmperOffsetVecX:
            paramArgs.append('dAmperOffsetVecX={0}'.format(getValueStr(self.dAmperOffsetVecX)))
        if self.dAmperOffsetVecY != obj.dAmperOffsetVecY:
            paramArgs.append('dAmperOffsetVecY={0}'.format(getValueStr(self.dAmperOffsetVecY)))
        if self.dAmperOffsetVecZ != obj.dAmperOffsetVecZ:
            paramArgs.append('dAmperOffsetVecZ={0}'.format(getValueStr(self.dAmperOffsetVecZ)))
        return 'ERICONT_DAMPER_OFFSET_VEC_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            self.iConnId,
            self.iEndA,
            self.iEndB,
            self.dAmperOffsetVecX,
            self.dAmperOffsetVecY,
            self.dAmperOffsetVecZ) + rightBracket

class VOLUME_MESH:
    def __init__(self,
        bTet10=False,
        dGradingFactor=0,
        bGravCenter=False,
        dStretchLimit=0,
        iSpeedVsQual=0,
        iSpeedVsMem=0,
        iRegion=0,
        bInternalNodes=True,
        bSafeMode=True,
        iParallel=0,
        bSurfaceNodes=True,
        bEdgeNodes=True,
        bPreservation=True,
        bInternalMeshOnly=True):
        self.bTet10 = bTet10
        self.dGradingFactor = dGradingFactor
        self.bGravCenter = bGravCenter
        self.dStretchLimit = dStretchLimit
        self.iSpeedVsQual = iSpeedVsQual
        self.iSpeedVsMem = iSpeedVsMem
        self.iRegion = iRegion
        self.bInternalNodes = bInternalNodes
        self.bSafeMode = bSafeMode
        self.iParallel = iParallel
        self.bSurfaceNodes = bSurfaceNodes
        self.bEdgeNodes = bEdgeNodes
        self.bPreservation = bPreservation
        self.bInternalMeshOnly = bInternalMeshOnly
    def isDefault(self):
        obj = VOLUME_MESH()
        return self.bTet10 == obj.bTet10 and \
            self.dGradingFactor == obj.dGradingFactor and \
            self.bGravCenter == obj.bGravCenter and \
            self.dStretchLimit == obj.dStretchLimit and \
            self.iSpeedVsQual == obj.iSpeedVsQual and \
            self.iSpeedVsMem == obj.iSpeedVsMem and \
            self.iRegion == obj.iRegion and \
            self.bInternalNodes == obj.bInternalNodes and \
            self.bSafeMode == obj.bSafeMode and \
            self.iParallel == obj.iParallel and \
            self.bSurfaceNodes == obj.bSurfaceNodes and \
            self.bEdgeNodes == obj.bEdgeNodes and \
            self.bPreservation == obj.bPreservation and \
            self.bInternalMeshOnly == obj.bInternalMeshOnly
    def fromList(self, volumeMesh):
        obj = VOLUME_MESH()
        self.bTet10 = getBoolValue(volumeMesh[0]) if len(volumeMesh) > 0 else obj.bTet10
        self.dGradingFactor = normalizeDoubleType(volumeMesh[1]) if len(volumeMesh) > 1 else obj.dGradingFactor
        self.bGravCenter = getBoolValue(volumeMesh[2]) if len(volumeMesh) > 2 else obj.bGravCenter
        self.dStretchLimit = normalizeDoubleType(volumeMesh[3]) if len(volumeMesh) > 3 else obj.dStretchLimit
        self.iSpeedVsQual = volumeMesh[4] if len(volumeMesh) > 4 else obj.iSpeedVsQual
        self.iSpeedVsMem = volumeMesh[5] if len(volumeMesh) > 5 else obj.iSpeedVsMem
        self.iRegion = volumeMesh[6] if len(volumeMesh) > 6 else obj.iRegion
        self.bInternalNodes = getBoolValue(volumeMesh[7]) if len(volumeMesh) > 7 else obj.bInternalNodes
        self.bSafeMode = getBoolValue(volumeMesh[8]) if len(volumeMesh) > 8 else obj.bSafeMode
        self.iParallel = volumeMesh[9] if len(volumeMesh) > 9 else obj.iParallel
        self.bSurfaceNodes = getBoolValue(volumeMesh[10]) if len(volumeMesh) > 10 else obj.bSurfaceNodes
        self.bEdgeNodes = getBoolValue(volumeMesh[11]) if len(volumeMesh) > 11 else obj.bEdgeNodes
        self.bPreservation = getBoolValue(volumeMesh[12]) if len(volumeMesh) > 12 else obj.bPreservation
        self.bInternalMeshOnly = getBoolValue(volumeMesh[13]) if len(volumeMesh) > 13 else obj.bInternalMeshOnly
        return self
    def __str__(self):
        obj = VOLUME_MESH()
        paramArgs = []
        if self.bTet10 != obj.bTet10:
            paramArgs.append('bTet10={0}'.format(getBoolStr(self.bTet10)))
        if self.dGradingFactor != obj.dGradingFactor:
            paramArgs.append('dGradingFactor={0}'.format(getValueStr(self.dGradingFactor)))
        if self.bGravCenter != obj.bGravCenter:
            paramArgs.append('bGravCenter={0}'.format(getBoolStr(self.bGravCenter)))
        if self.dStretchLimit != obj.dStretchLimit:
            paramArgs.append('dStretchLimit={0}'.format(getValueStr(self.dStretchLimit)))
        if self.iSpeedVsQual != obj.iSpeedVsQual:
            paramArgs.append('iSpeedVsQual={0}'.format(getValueStr(self.iSpeedVsQual)))
        if self.iSpeedVsMem != obj.iSpeedVsMem:
            paramArgs.append('iSpeedVsMem={0}'.format(getValueStr(self.iSpeedVsMem)))
        if self.iRegion != obj.iRegion:
            paramArgs.append('iRegion={0}'.format(getValueStr(self.iRegion)))
        if self.bInternalNodes != obj.bInternalNodes:
            paramArgs.append('bInternalNodes={0}'.format(getBoolStr(self.bInternalNodes)))
        if self.bSafeMode != obj.bSafeMode:
            paramArgs.append('bSafeMode={0}'.format(getBoolStr(self.bSafeMode)))
        if self.iParallel != obj.iParallel:
            paramArgs.append('iParallel={0}'.format(getValueStr(self.iParallel)))
        if self.bSurfaceNodes != obj.bSurfaceNodes:
            paramArgs.append('bSurfaceNodes={0}'.format(getBoolStr(self.bSurfaceNodes)))
        if self.bEdgeNodes != obj.bEdgeNodes:
            paramArgs.append('bEdgeNodes={0}'.format(getBoolStr(self.bEdgeNodes)))
        if self.bPreservation != obj.bPreservation:
            paramArgs.append('bPreservation={0}'.format(getBoolStr(self.bPreservation)))
        if self.bInternalMeshOnly != obj.bInternalMeshOnly:
            paramArgs.append('bInternalMeshOnly={0}'.format(getBoolStr(self.bInternalMeshOnly)))
        return 'VOLUME_MESH({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '{' if isOneParam else ''
        rightBracket = '}' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}'.format(
            1 if self.bTet10 else 0,
            self.dGradingFactor,
            1 if self.bGravCenter else 0,
            self.dStretchLimit,
            self.iSpeedVsQual,
            self.iSpeedVsMem,
            self.iRegion,
            1 if self.bInternalNodes else 0,
            1 if self.bSafeMode else 0,
            self.iParallel,
            1 if self.bSurfaceNodes else 0,
            1 if self.bEdgeNodes else 0,
            1 if self.bPreservation else 0,
            1 if self.bInternalMeshOnly else 0) + rightBracket

class RBE3_TERM_CONNECTION:
    def __init__(self,
        dCoef=0,
        iDof=0,
        iTarCnt=0):
        self.dCoef = dCoef
        self.iDof = iDof
        self.iTarCnt = iTarCnt
    def isDefault(self):
        obj = RBE3_TERM_CONNECTION()
        return self.dCoef == obj.dCoef and \
            self.iDof == obj.iDof and \
            self.iTarCnt == obj.iTarCnt
    def fromList(self, param):
        obj = RBE3_TERM_CONNECTION()
        self.dCoef = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dCoef
        self.iDof = param[1] if len(param) > 1 else obj.iDof
        self.iTarCnt = param[2] if len(param) > 2 else obj.iTarCnt
        return self
    def __str__(self):
        obj = RBE3_TERM_CONNECTION()
        paramArgs = []
        if self.dCoef != obj.dCoef:
            paramArgs.append('dCoef={0}'.format(getValueStr(self.dCoef)))
        if self.iDof != obj.iDof:
            paramArgs.append('iDof={0}'.format(getValueStr(self.iDof)))
        if self.iTarCnt != obj.iTarCnt:
            paramArgs.append('iTarCnt={0}'.format(getValueStr(self.iTarCnt)))
        return 'RBE3_TERM_CONNECTION({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.dCoef,
            self.iDof,
            self.iTarCnt) + rightBracket

class FIXED_CONTRAINT_LBC:
    def __init__(self,
        iDwDof=7,
        crCurCoord=None,
        iType=0,
        iUsetType=0,
        crTable=None,
        bAbaqusFixed=False):
        self.iDwDof = iDwDof
        self.crCurCoord = crCurCoord
        self.iType = iType
        self.iUsetType = iUsetType
        self.crTable = crTable
        self.bAbaqusFixed = bAbaqusFixed
    def isDefault(self):
        obj = FIXED_CONTRAINT_LBC()
        return self.iDwDof == obj.iDwDof and \
            self.crCurCoord == obj.crCurCoord and \
            self.iType == obj.iType and \
            self.iUsetType == obj.iUsetType and \
            self.crTable == obj.crTable and \
            self.bAbaqusFixed == obj.bAbaqusFixed
    def fromList(self, param):
        obj = FIXED_CONTRAINT_LBC()
        self.iDwDof = param[0] if len(param) > 0 else obj.iDwDof
        self.crCurCoord = getCursorValue(param[1]) if len(param) > 1 else obj.crCurCoord
        self.iType = param[2] if len(param) > 2 else obj.iType
        self.iUsetType = param[3] if len(param) > 3 else obj.iUsetType
        self.crTable = getCursorValue(param[4]) if len(param) > 4 else obj.crTable
        self.bAbaqusFixed = getBoolValue(param[5]) if len(param) > 5 else obj.bAbaqusFixed
        return self
    def __str__(self):
        obj = FIXED_CONTRAINT_LBC()
        paramArgs = []
        if self.iDwDof != obj.iDwDof:
            paramArgs.append('iDwDof={0}'.format(getValueStr(self.iDwDof)))
        if self.crCurCoord != obj.crCurCoord:
            paramArgs.append('crCurCoord={0}'.format(getCursorValueStr(self.crCurCoord)))
        if self.iType != obj.iType:
            paramArgs.append('iType={0}'.format(getValueStr(self.iType)))
        if self.iUsetType != obj.iUsetType:
            paramArgs.append('iUsetType={0}'.format(getValueStr(self.iUsetType)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        if self.bAbaqusFixed != obj.bAbaqusFixed:
            paramArgs.append('bAbaqusFixed={0}'.format(getBoolStr(self.bAbaqusFixed)))
        return 'FIXED_CONTRAINT_LBC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            self.iDwDof,
            str(self.crCurCoord) if self.crCurCoord is not None else '0:0',
            self.iType,
            self.iUsetType,
            str(self.crTable) if self.crTable is not None else '0:0',
            1 if self.bAbaqusFixed else 0) + rightBracket

class SURFACE_MESH:
    def __init__(self,
        dAvgElemSize=0.005,
        dMaxElemSize=0.01,
        dMinElemSize=0.001,
        dReductionFactor=1.0,
        dGeomAngle=0.785398,
        dGeomMinSize=0.001,
        dGradingFactor=1.250000,
        dMinStretchVal=0.100000,
        dGeomEdgeDev=0.100000,
        dGeomQualRatio=0.700000,
        dGeomCntRatio=0.500000,
        iPerformanceMode=0,
        iOptLevel=3,
        bAutoMergeEdges=False,
        bAutoMergeFaces=False,
        dAutoMeshPatternMinElemAngle=0,
        dAutoMergeTinyFacesAngle=0.523598756,
        bOutputQuadMesh=False,
        bPureQuad=False,
        bBadInputModel=False,
        bCloseGaps=False,
        bLocalRemesh=False,
        bGeomApprox=False,
        bCurvatureControl=False,
        bDeleteCircChamfer=False,
        bTinyCylinderMesh=False,
        iNextEntityOffsetId=10000000,
        iNextElemOffsetId=0,
        iNextNodeOffsetId=0):
        self.dAvgElemSize = dAvgElemSize
        self.dMaxElemSize = dMaxElemSize
        self.dMinElemSize = dMinElemSize
        self.dReductionFactor = dReductionFactor
        self.dGeomAngle = dGeomAngle
        self.dGeomMinSize = dGeomMinSize
        self.dGradingFactor = dGradingFactor
        self.dMinStretchVal = dMinStretchVal
        self.dGeomEdgeDev = dGeomEdgeDev
        self.dGeomQualRatio = dGeomQualRatio
        self.dGeomCntRatio = dGeomCntRatio
        self.iPerformanceMode = iPerformanceMode
        self.iOptLevel = iOptLevel
        self.bAutoMergeEdges = bAutoMergeEdges
        self.bAutoMergeFaces = bAutoMergeFaces
        self.dAutoMeshPatternMinElemAngle = dAutoMeshPatternMinElemAngle
        self.dAutoMergeTinyFacesAngle = dAutoMergeTinyFacesAngle
        self.bOutputQuadMesh = bOutputQuadMesh
        self.bPureQuad = bPureQuad
        self.bBadInputModel = bBadInputModel
        self.bCloseGaps = bCloseGaps
        self.bLocalRemesh = bLocalRemesh
        self.bGeomApprox = bGeomApprox
        self.bCurvatureControl = bCurvatureControl
        self.bDeleteCircChamfer = bDeleteCircChamfer
        self.bTinyCylinderMesh = bTinyCylinderMesh
        self.iNextEntityOffsetId = iNextEntityOffsetId
        self.iNextElemOffsetId = iNextElemOffsetId
        self.iNextNodeOffsetId = iNextNodeOffsetId
    def isDefault(self):
        obj = SURFACE_MESH()
        return self.dAvgElemSize == obj.dAvgElemSize and \
            self.dMaxElemSize == obj.dMaxElemSize and \
            self.dMinElemSize == obj.dMinElemSize and \
            self.dReductionFactor == obj.dReductionFactor and \
            self.dGeomAngle == obj.dGeomAngle and \
            self.dGeomMinSize == obj.dGeomMinSize and \
            self.dGradingFactor == obj.dGradingFactor and \
            self.dMinStretchVal == obj.dMinStretchVal and \
            self.dGeomEdgeDev == obj.dGeomEdgeDev and \
            self.dGeomQualRatio == obj.dGeomQualRatio and \
            self.dGeomCntRatio == obj.dGeomCntRatio and \
            self.iPerformanceMode == obj.iPerformanceMode and \
            self.iOptLevel == obj.iOptLevel and \
            self.bAutoMergeEdges == obj.bAutoMergeEdges and \
            self.bAutoMergeFaces == obj.bAutoMergeFaces and \
            self.dAutoMeshPatternMinElemAngle == obj.dAutoMeshPatternMinElemAngle and \
            self.dAutoMergeTinyFacesAngle == obj.dAutoMergeTinyFacesAngle and \
            self.bOutputQuadMesh == obj.bOutputQuadMesh and \
            self.bPureQuad == obj.bPureQuad and \
            self.bBadInputModel == obj.bBadInputModel and \
            self.bCloseGaps == obj.bCloseGaps and \
            self.bLocalRemesh == obj.bLocalRemesh and \
            self.bGeomApprox == obj.bGeomApprox and \
            self.bCurvatureControl == obj.bCurvatureControl and \
            self.bDeleteCircChamfer == obj.bDeleteCircChamfer and \
            self.bTinyCylinderMesh == obj.bTinyCylinderMesh and \
            self.iNextEntityOffsetId == obj.iNextEntityOffsetId and \
            self.iNextElemOffsetId == obj.iNextElemOffsetId and \
            self.iNextNodeOffsetId == obj.iNextNodeOffsetId
    def fromList(self, param):
        obj = SURFACE_MESH()
        self.dAvgElemSize = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dAvgElemSize
        self.dMaxElemSize = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dMaxElemSize
        self.dMinElemSize = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dMinElemSize
        self.dReductionFactor = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dReductionFactor
        self.dGeomAngle = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dGeomAngle
        self.dGeomMinSize = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dGeomMinSize
        self.dGradingFactor = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dGradingFactor
        self.dMinStretchVal = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dMinStretchVal
        self.dGeomEdgeDev = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dGeomEdgeDev
        self.dGeomQualRatio = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dGeomQualRatio
        self.dGeomCntRatio = normalizeDoubleType(param[10]) if len(param) > 10 else obj.dGeomCntRatio
        self.iPerformanceMode = param[11] if len(param) > 11 else obj.iPerformanceMode
        self.iOptLevel = param[12] if len(param) > 12 else obj.iOptLevel
        self.bAutoMergeEdges = getBoolValue(param[13]) if len(param) > 13 else obj.bAutoMergeEdges
        self.bAutoMergeFaces = getBoolValue(param[14]) if len(param) > 14 else obj.bAutoMergeFaces
        self.dAutoMeshPatternMinElemAngle = normalizeDoubleType(param[15]) if len(param) > 15 else obj.dAutoMeshPatternMinElemAngle
        self.dAutoMergeTinyFacesAngle = normalizeDoubleType(param[16]) if len(param) > 16 else obj.dAutoMergeTinyFacesAngle
        self.bOutputQuadMesh = getBoolValue(param[17]) if len(param) > 17 else obj.bOutputQuadMesh
        self.bPureQuad = getBoolValue(param[18]) if len(param) > 18 else obj.bPureQuad
        self.bBadInputModel = getBoolValue(param[19]) if len(param) > 19 else obj.bBadInputModel
        self.bCloseGaps = getBoolValue(param[20]) if len(param) > 20 else obj.bCloseGaps
        self.bLocalRemesh = getBoolValue(param[21]) if len(param) > 21 else obj.bLocalRemesh
        self.bGeomApprox = getBoolValue(param[22]) if len(param) > 22 else obj.bGeomApprox
        self.bCurvatureControl = getBoolValue(param[23]) if len(param) > 23 else obj.bCurvatureControl
        self.bDeleteCircChamfer = getBoolValue(param[24]) if len(param) > 24 else obj.bDeleteCircChamfer
        self.bTinyCylinderMesh = getBoolValue(param[25]) if len(param) > 25 else obj.bTinyCylinderMesh
        self.iNextEntityOffsetId = param[26] if len(param) > 26 else obj.iNextEntityOffsetId
        self.iNextElemOffsetId = param[27] if len(param) > 27 else obj.iNextElemOffsetId
        self.iNextNodeOffsetId = param[28] if len(param) > 28 else obj.iNextNodeOffsetId
        return self
    def __str__(self):
        obj = SURFACE_MESH()
        paramArgs = []
        if self.dAvgElemSize != obj.dAvgElemSize:
            paramArgs.append('dAvgElemSize={0}'.format(getValueStr(self.dAvgElemSize)))
        if self.dMaxElemSize != obj.dMaxElemSize:
            paramArgs.append('dMaxElemSize={0}'.format(getValueStr(self.dMaxElemSize)))
        if self.dMinElemSize != obj.dMinElemSize:
            paramArgs.append('dMinElemSize={0}'.format(getValueStr(self.dMinElemSize)))
        if self.dReductionFactor != obj.dReductionFactor:
            paramArgs.append('dReductionFactor={0}'.format(getValueStr(self.dReductionFactor)))
        if self.dGeomAngle != obj.dGeomAngle:
            paramArgs.append('dGeomAngle={0}'.format(getValueStr(self.dGeomAngle)))
        if self.dGeomMinSize != obj.dGeomMinSize:
            paramArgs.append('dGeomMinSize={0}'.format(getValueStr(self.dGeomMinSize)))
        if self.dGradingFactor != obj.dGradingFactor:
            paramArgs.append('dGradingFactor={0}'.format(getValueStr(self.dGradingFactor)))
        if self.dMinStretchVal != obj.dMinStretchVal:
            paramArgs.append('dMinStretchVal={0}'.format(getValueStr(self.dMinStretchVal)))
        if self.dGeomEdgeDev != obj.dGeomEdgeDev:
            paramArgs.append('dGeomEdgeDev={0}'.format(getValueStr(self.dGeomEdgeDev)))
        if self.dGeomQualRatio != obj.dGeomQualRatio:
            paramArgs.append('dGeomQualRatio={0}'.format(getValueStr(self.dGeomQualRatio)))
        if self.dGeomCntRatio != obj.dGeomCntRatio:
            paramArgs.append('dGeomCntRatio={0}'.format(getValueStr(self.dGeomCntRatio)))
        if self.iPerformanceMode != obj.iPerformanceMode:
            paramArgs.append('iPerformanceMode={0}'.format(getValueStr(self.iPerformanceMode)))
        if self.iOptLevel != obj.iOptLevel:
            paramArgs.append('iOptLevel={0}'.format(getValueStr(self.iOptLevel)))
        if self.bAutoMergeEdges != obj.bAutoMergeEdges:
            paramArgs.append('bAutoMergeEdges={0}'.format(getBoolStr(self.bAutoMergeEdges)))
        if self.bAutoMergeFaces != obj.bAutoMergeFaces:
            paramArgs.append('bAutoMergeFaces={0}'.format(getBoolStr(self.bAutoMergeFaces)))
        if self.dAutoMeshPatternMinElemAngle != obj.dAutoMeshPatternMinElemAngle:
            paramArgs.append('dAutoMeshPatternMinElemAngle={0}'.format(getValueStr(self.dAutoMeshPatternMinElemAngle)))
        if self.dAutoMergeTinyFacesAngle != obj.dAutoMergeTinyFacesAngle:
            paramArgs.append('dAutoMergeTinyFacesAngle={0}'.format(getValueStr(self.dAutoMergeTinyFacesAngle)))
        if self.bOutputQuadMesh != obj.bOutputQuadMesh:
            paramArgs.append('bOutputQuadMesh={0}'.format(getBoolStr(self.bOutputQuadMesh)))
        if self.bPureQuad != obj.bPureQuad:
            paramArgs.append('bPureQuad={0}'.format(getBoolStr(self.bPureQuad)))
        if self.bBadInputModel != obj.bBadInputModel:
            paramArgs.append('bBadInputModel={0}'.format(getBoolStr(self.bBadInputModel)))
        if self.bCloseGaps != obj.bCloseGaps:
            paramArgs.append('bCloseGaps={0}'.format(getBoolStr(self.bCloseGaps)))
        if self.bLocalRemesh != obj.bLocalRemesh:
            paramArgs.append('bLocalRemesh={0}'.format(getBoolStr(self.bLocalRemesh)))
        if self.bGeomApprox != obj.bGeomApprox:
            paramArgs.append('bGeomApprox={0}'.format(getBoolStr(self.bGeomApprox)))
        if self.bCurvatureControl != obj.bCurvatureControl:
            paramArgs.append('bCurvatureControl={0}'.format(getBoolStr(self.bCurvatureControl)))
        if self.bDeleteCircChamfer != obj.bDeleteCircChamfer:
            paramArgs.append('bDeleteCircChamfer={0}'.format(getBoolStr(self.bDeleteCircChamfer)))
        #if self.bTinyCylinderMesh != obj.bTinyCylinderMesh:
          #  paramArgs.append('bTinyCylinderMesh={0}'.format(getBoolStr(self.bTinyCylinderMesh)))
        if self.iNextEntityOffsetId != obj.iNextEntityOffsetId:
            paramArgs.append('iNextEntityOffsetId={0}'.format(getValueStr(self.iNextEntityOffsetId)))
        if self.iNextElemOffsetId != obj.iNextElemOffsetId:
            paramArgs.append('iNextElemOffsetId={0}'.format(getValueStr(self.iNextElemOffsetId)))
        if self.iNextNodeOffsetId != obj.iNextNodeOffsetId:
            paramArgs.append('iNextNodeOffsetId={0}'.format(getValueStr(self.iNextNodeOffsetId)))
        return 'SURFACE_MESH({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '{' if isOneParam else ''
        rightBracket = '}' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}'.format(
            self.dAvgElemSize,
            self.dMaxElemSize,
            self.dMinElemSize,
            self.dReductionFactor,
            self.dGeomAngle,
            self.dGeomMinSize,
            self.dGradingFactor,
            self.dMinStretchVal,
            self.dGeomEdgeDev,
            self.dGeomQualRatio,
            self.dGeomCntRatio,
            self.iPerformanceMode,
            self.iOptLevel,
            1 if self.bAutoMergeEdges else 0,
            1 if self.bAutoMergeFaces else 0,
            self.dAutoMeshPatternMinElemAngle,
            self.dAutoMergeTinyFacesAngle,
            1 if self.bOutputQuadMesh else 0,
            1 if self.bPureQuad else 0,
            1 if self.bBadInputModel else 0,
            1 if self.bCloseGaps else 0,
            1 if self.bLocalRemesh else 0,
            1 if self.bGeomApprox else 0,
            1 if self.bCurvatureControl else 0,
            1 if self.bDeleteCircChamfer else 0,
            #1 if self.bTinyCylinderMesh else 0,
            self.iNextEntityOffsetId,
            self.iNextElemOffsetId,
            self.iNextNodeOffsetId) + rightBracket

class NASTRAN_NONLINEAR:
    def __init__(self,
        iNINC=1,
        iKMETHOD=3,
        iMAXITER=1,
        bUseEPSU=False,
        bUseEPSP=False,
        bUseEPSW=False,
        dEPSU=1.0E-2,
        dEPSP=1.0E-2,
        dEPSW=1.0E-2):
        self.iNINC = iNINC
        self.iKMETHOD = iKMETHOD
        self.iMAXITER = iMAXITER
        self.bUseEPSU = bUseEPSU
        self.bUseEPSP = bUseEPSP
        self.bUseEPSW = bUseEPSW
        self.dEPSU = dEPSU
        self.dEPSP = dEPSP
        self.dEPSW = dEPSW
    def isDefault(self):
        obj = NASTRAN_NONLINEAR()
        return self.iNINC == obj.iNINC and \
            self.iKMETHOD == obj.iKMETHOD and \
            self.iMAXITER == obj.iMAXITER and \
            self.bUseEPSU == obj.bUseEPSU and \
            self.bUseEPSP == obj.bUseEPSP and \
            self.bUseEPSW == obj.bUseEPSW and \
            self.dEPSU == obj.dEPSU and \
            self.dEPSP == obj.dEPSP and \
            self.dEPSW == obj.dEPSW
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_NONLINEAR()
        self.iNINC = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iNINC
        self.iKMETHOD = nastranAnalysis[1] if len(nastranAnalysis) > 1 else obj.iKMETHOD
        self.iMAXITER = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.iMAXITER
        self.bUseEPSU = getBoolValue(nastranAnalysis[3]) if len(nastranAnalysis) > 3 else obj.bUseEPSU
        self.bUseEPSP = getBoolValue(nastranAnalysis[4]) if len(nastranAnalysis) > 4 else obj.bUseEPSP
        self.bUseEPSW = getBoolValue(nastranAnalysis[5]) if len(nastranAnalysis) > 5 else obj.bUseEPSW
        self.dEPSU = normalizeDoubleType(nastranAnalysis[6]) if len(nastranAnalysis) > 6 else obj.dEPSU
        self.dEPSP = normalizeDoubleType(nastranAnalysis[7]) if len(nastranAnalysis) > 7 else obj.dEPSP
        self.dEPSW = normalizeDoubleType(nastranAnalysis[8]) if len(nastranAnalysis) > 8 else obj.dEPSW
        return self
    def __str__(self):
        obj = NASTRAN_NONLINEAR()
        paramArgs = []
        if self.iNINC != obj.iNINC:
            paramArgs.append('iNINC={0}'.format(getValueStr(self.iNINC)))
        if self.iKMETHOD != obj.iKMETHOD:
            paramArgs.append('iKMETHOD={0}'.format(getValueStr(self.iKMETHOD)))
        if self.iMAXITER != obj.iMAXITER:
            paramArgs.append('iMAXITER={0}'.format(getValueStr(self.iMAXITER)))
        if self.bUseEPSU != obj.bUseEPSU:
            paramArgs.append('bUseEPSU={0}'.format(getBoolStr(self.bUseEPSU)))
        if self.bUseEPSP != obj.bUseEPSP:
            paramArgs.append('bUseEPSP={0}'.format(getBoolStr(self.bUseEPSP)))
        if self.bUseEPSW != obj.bUseEPSW:
            paramArgs.append('bUseEPSW={0}'.format(getBoolStr(self.bUseEPSW)))
        if self.dEPSU != obj.dEPSU:
            paramArgs.append('dEPSU={0}'.format(getValueStr(self.dEPSU)))
        if self.dEPSP != obj.dEPSP:
            paramArgs.append('dEPSP={0}'.format(getValueStr(self.dEPSP)))
        if self.dEPSW != obj.dEPSW:
            paramArgs.append('dEPSW={0}'.format(getValueStr(self.dEPSW)))
        return 'NASTRAN_NONLINEAR({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            self.iNINC,
            self.iKMETHOD,
            self.iMAXITER,
            1 if self.bUseEPSU else 0,
            1 if self.bUseEPSP else 0,
            1 if self.bUseEPSW else 0,
            self.dEPSU,
            self.dEPSP,
            self.dEPSW) + rightBracket

    def __eq__(self, other):
        return self.iNINC == other.iNINC and \
            self.iKMETHOD == other.iKMETHOD and \
            self.iMAXITER == other.iMAXITER and \
            self.bUseEPSU == other.bUseEPSU and \
            self.bUseEPSP == other.bUseEPSP and \
            self.bUseEPSW == other.bUseEPSW and \
            self.dEPSU == other.dEPSU and \
            self.dEPSP == other.dEPSP and \
            self.dEPSW == other.dEPSW

    def __ne__(self, other):
        return self.iNINC != other.iNINC or \
            self.iKMETHOD != other.iKMETHOD or \
            self.iMAXITER != other.iMAXITER or \
            self.bUseEPSU != other.bUseEPSU or \
            self.bUseEPSP != other.bUseEPSP or \
            self.bUseEPSW != other.bUseEPSW or \
            self.dEPSU != other.dEPSU or \
            self.dEPSP != other.dEPSP or \
            self.dEPSW != other.dEPSW

class NASTRAN_NONLINEAR_TIMESTEP:
    def __init__(self,
        iNDT=DFLT_INT,
        dDT=DFLT_DBL,
        iMAXITER=DFLT_INT):
        self.iNDT = iNDT
        self.dDT = dDT
        self.iMAXITER = iMAXITER
    def isDefault(self):
        obj = NASTRAN_NONLINEAR_TIMESTEP()
        return self.iNDT == obj.iNDT and \
            self.dDT == obj.dDT and \
            self.iMAXITER == obj.iMAXITER
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_NONLINEAR_TIMESTEP()
        self.iNDT = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iNDT
        self.dDT = normalizeDoubleType(nastranAnalysis[1]) if len(nastranAnalysis) > 1 else obj.dDT
        self.iMAXITER = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.iMAXITER
        return self
    def __str__(self):
        obj = NASTRAN_NONLINEAR_TIMESTEP()
        paramArgs = []
        if self.iNDT != obj.iNDT:
            paramArgs.append('iNDT={0}'.format(getValueStr(self.iNDT)))
        if self.dDT != obj.dDT:
            paramArgs.append('dDT={0}'.format(getValueStr(self.dDT)))
        if self.iMAXITER != obj.iMAXITER:
            paramArgs.append('iMAXITER={0}'.format(getValueStr(self.iMAXITER)))
        return 'NASTRAN_NONLINEAR_TIMESTEP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iNDT,
            self.dDT,
            self.iMAXITER) + rightBracket

    def __eq__(self, other):
        return self.iNDT == other.iNDT and \
            self.dDT == other.dDT and \
            self.iMAXITER == other.iMAXITER

    def __ne__(self, other):
        return self.iNDT != other.iNDT or \
            self.dDT != other.dDT or \
            self.iMAXITER != other.iMAXITER

class NASTRAN_EIGEN:
    def __init__(self,
        dStartFreq=DFLT_DBL,
        dEndFreq=DFLT_DBL,
        iNoOfModes=DFLT_INT):
        self.dStartFreq = dStartFreq
        self.dEndFreq = dEndFreq
        self.iNoOfModes = iNoOfModes
    def isDefault(self):
        obj = NASTRAN_EIGEN()
        return self.dStartFreq == obj.dStartFreq and \
            self.dEndFreq == obj.dEndFreq and \
            self.iNoOfModes == obj.iNoOfModes
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_EIGEN()
        self.dStartFreq = normalizeDoubleType(nastranAnalysis[0]) if len(nastranAnalysis) > 0 else obj.dStartFreq
        self.dEndFreq = normalizeDoubleType(nastranAnalysis[1]) if len(nastranAnalysis) > 1 else obj.dEndFreq
        self.iNoOfModes = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.iNoOfModes
        return self
    def __str__(self):
        obj = NASTRAN_EIGEN()
        paramArgs = []
        if self.dStartFreq != obj.dStartFreq:
            paramArgs.append('dStartFreq={0}'.format(getValueStr(self.dStartFreq)))
        if self.dEndFreq != obj.dEndFreq:
            paramArgs.append('dEndFreq={0}'.format(getValueStr(self.dEndFreq)))
        if self.iNoOfModes != obj.iNoOfModes:
            paramArgs.append('iNoOfModes={0}'.format(getValueStr(self.iNoOfModes)))
        return 'NASTRAN_EIGEN({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.dStartFreq,
            self.dEndFreq,
            self.iNoOfModes) + rightBracket

    def __eq__(self, other):
        return self.dStartFreq == other.dStartFreq and \
            self.dEndFreq == other.dEndFreq and \
            self.iNoOfModes == other.iNoOfModes
    def __ne__(self, other):
        return self.dStartFreq != other.dStartFreq or \
            self.dEndFreq != other.dEndFreq or \
            self.iNoOfModes != other.iNoOfModes

class NASTRAN_EIGEN126:
    def __init__(self,
        iModalExtractionMethod=0,
        dModalStartFreq=DFLT_DBL,
        dModalEndFreq=DFLT_DBL,
        iModalNoOfModes=DFLT_INT,
        iBRsvec=0,
        iMLDSExtractionMethod=0,
        dMLDSStartFreq=DFLT_DBL,
        dMLDSEndFreq=DFLT_DBL,
        iMLDSNoOfModes=DFLT_INT):
        self.iModalExtractionMethod = iModalExtractionMethod
        self.dModalStartFreq = dModalStartFreq
        self.dModalEndFreq = dModalEndFreq
        self.iModalNoOfModes = iModalNoOfModes
        self.iBRsvec = iBRsvec
        self.iMLDSExtractionMethod = iMLDSExtractionMethod
        self.dMLDSStartFreq = dMLDSStartFreq
        self.dMLDSEndFreq = dMLDSEndFreq
        self.iMLDSNoOfModes = iMLDSNoOfModes
    def isDefault(self):
        obj = NASTRAN_EIGEN126()
        return self.iModalExtractionMethod == obj.iModalExtractionMethod and \
            self.dModalStartFreq == obj.dModalStartFreq and \
            self.dModalEndFreq == obj.dModalEndFreq and \
            self.iModalNoOfModes == obj.iModalNoOfModes and \
            self.iBRsvec == obj.iBRsvec and \
            self.iMLDSExtractionMethod == obj.iMLDSExtractionMethod and \
            self.dMLDSStartFreq == obj.dMLDSStartFreq and \
            self.dMLDSEndFreq == obj.dMLDSEndFreq and \
            self.iMLDSNoOfModes == obj.iMLDSNoOfModes
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_EIGEN126()
        self.iModalExtractionMethod = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iModalExtractionMethod
        self.dModalStartFreq = normalizeDoubleType(nastranAnalysis[1]) if len(nastranAnalysis) > 1 else obj.dModalStartFreq
        self.dModalEndFreq = normalizeDoubleType(nastranAnalysis[2]) if len(nastranAnalysis) > 2 else obj.dModalEndFreq
        self.iModalNoOfModes = nastranAnalysis[3] if len(nastranAnalysis) > 3 else obj.iModalNoOfModes
        self.iBRsvec = nastranAnalysis[4] if len(nastranAnalysis) > 4 else obj.iBRsvec
        self.iMLDSExtractionMethod = nastranAnalysis[5] if len(nastranAnalysis) > 5 else obj.iMLDSExtractionMethod
        self.dMLDSStartFreq = normalizeDoubleType(nastranAnalysis[6]) if len(nastranAnalysis) > 6 else obj.dMLDSStartFreq
        self.dMLDSEndFreq = normalizeDoubleType(nastranAnalysis[7]) if len(nastranAnalysis) > 7 else obj.dMLDSEndFreq
        self.iMLDSNoOfModes = nastranAnalysis[8] if len(nastranAnalysis) > 8 else obj.iMLDSNoOfModes
        return self
    def __str__(self):
        obj = NASTRAN_EIGEN126()
        paramArgs = []
        if self.iModalExtractionMethod != obj.iModalExtractionMethod:
            paramArgs.append('iModalExtractionMethod={0}'.format(getValueStr(self.iModalExtractionMethod)))
        if self.dModalStartFreq != obj.dModalStartFreq:
            paramArgs.append('dModalStartFreq={0}'.format(getValueStr(self.dModalStartFreq)))
        if self.dModalEndFreq != obj.dModalEndFreq:
            paramArgs.append('dModalEndFreq={0}'.format(getValueStr(self.dModalEndFreq)))
        if self.iModalNoOfModes != obj.iModalNoOfModes:
            paramArgs.append('iModalNoOfModes={0}'.format(getValueStr(self.iModalNoOfModes)))
        if self.iBRsvec != obj.iBRsvec:
            paramArgs.append('iBRsvec={0}'.format(getValueStr(self.iBRsvec)))
        if self.iMLDSExtractionMethod != obj.iMLDSExtractionMethod:
            paramArgs.append('iMLDSExtractionMethod={0}'.format(getValueStr(self.iMLDSExtractionMethod)))
        if self.dMLDSStartFreq != obj.dMLDSStartFreq:
            paramArgs.append('dMLDSStartFreq={0}'.format(getValueStr(self.dMLDSStartFreq)))
        if self.dMLDSEndFreq != obj.dMLDSEndFreq:
            paramArgs.append('dMLDSEndFreq={0}'.format(getValueStr(self.dMLDSEndFreq)))
        if self.iMLDSNoOfModes != obj.iMLDSNoOfModes:
            paramArgs.append('iMLDSNoOfModes={0}'.format(getValueStr(self.iMLDSNoOfModes)))
        return 'NASTRAN_EIGEN126({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            self.iModalExtractionMethod,
            self.dModalStartFreq,
            self.dModalEndFreq,
            self.iModalNoOfModes,
            self.iBRsvec,
            self.iMLDSExtractionMethod,
            self.dMLDSStartFreq,
            self.dMLDSEndFreq,
            self.iMLDSNoOfModes) + rightBracket

    def __eq__(self, other):
        return self.iModalExtractionMethod == other.iModalExtractionMethod and \
            self.dModalStartFreq == other.dModalStartFreq and \
            self.dModalEndFreq == other.dModalEndFreq and \
            self.iModalNoOfModes == other.iModalNoOfModes and \
            self.iBRsvec == other.iBRsvec and \
            self.iMLDSExtractionMethod == other.iMLDSExtractionMethod and \
            self.dMLDSStartFreq == other.dMLDSStartFreq and \
            self.dMLDSEndFreq == other.dMLDSEndFreq and \
            self.iMLDSNoOfModes == other.iMLDSNoOfModes
    def __ne__(self, other):
        return self.iModalExtractionMethod != other.iModalExtractionMethod or \
            self.dModalStartFreq != other.dModalStartFreq or \
            self.dModalEndFreq != other.dModalEndFreq or \
            self.iModalNoOfModes != other.iModalNoOfModes or \
            self.iBRsvec != other.iBRsvec or \
            self.iMLDSExtractionMethod != other.iMLDSExtractionMethod or \
            self.dMLDSStartFreq != other.dMLDSStartFreq or \
            self.dMLDSEndFreq != other.dMLDSEndFreq or \
            self.iMLDSNoOfModes != other.iMLDSNoOfModes

class NASTRAN_FREQUENCY:
    def __init__(self,
        dStartFrequency=DFLT_DBL,
        dIncrement=DFLT_DBL,
        iumOfInc=DFLT_INT,
        iTableId=0):
        self.dStartFrequency = dStartFrequency
        self.dIncrement = dIncrement
        self.iumOfInc = iumOfInc
        self.iTableId = iTableId
    def isDefault(self):
        obj = NASTRAN_FREQUENCY()
        return self.dStartFrequency == obj.dStartFrequency and \
            self.dIncrement == obj.dIncrement and \
            self.iumOfInc == obj.iumOfInc and \
            self.iTableId == obj.iTableId
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_FREQUENCY()
        self.dStartFrequency = normalizeDoubleType(nastranAnalysis[0]) if len(nastranAnalysis) > 0 else obj.dStartFrequency
        self.dIncrement = normalizeDoubleType(nastranAnalysis[1]) if len(nastranAnalysis) > 1 else obj.dIncrement
        self.iumOfInc = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.iumOfInc
        self.iTableId = nastranAnalysis[3] if len(nastranAnalysis) > 3 else obj.iTableId
        return self
    def __str__(self):
        obj = NASTRAN_FREQUENCY()
        paramArgs = []
        if self.dStartFrequency != obj.dStartFrequency:
            paramArgs.append('dStartFrequency={0}'.format(getValueStr(self.dStartFrequency)))
        if self.dIncrement != obj.dIncrement:
            paramArgs.append('dIncrement={0}'.format(getValueStr(self.dIncrement)))
        if self.iumOfInc != obj.iumOfInc:
            paramArgs.append('iumOfInc={0}'.format(getValueStr(self.iumOfInc)))
        if self.iTableId != obj.iTableId:
            paramArgs.append('iTableId={0}'.format(getValueStr(self.iTableId)))
        return 'NASTRAN_FREQUENCY({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.dStartFrequency,
            self.dIncrement,
            self.iumOfInc,
            self.iTableId) + rightBracket

    def __eq__(self, other):
        return self.dStartFrequency == other.dStartFrequency and \
            self.dIncrement == other.dIncrement and \
            self.iumOfInc == other.iumOfInc and \
            self.iTableId == other.iTableId

    def __ne__(self, other):
        return self.dStartFrequency != other.dStartFrequency or \
            self.dIncrement != other.dIncrement or \
            self.iumOfInc != other.iumOfInc or \
            self.iTableId != other.iTableId

class NASTRAN_FREQ_TIMESTEP:
    def __init__(self,
        iumOfSteps=DFLT_INT,
        dTimeIncrement=DFLT_DBL,
        iOutputInterval=DFLT_INT,
        iDampingType=2,
        iModalDampingTableId=0):
        self.iumOfSteps = iumOfSteps
        self.dTimeIncrement = dTimeIncrement
        self.iOutputInterval = iOutputInterval
        self.iDampingType = iDampingType
        self.iModalDampingTableId = iModalDampingTableId
    def isDefault(self):
        obj = NASTRAN_FREQ_TIMESTEP()
        return self.iumOfSteps == obj.iumOfSteps and \
            self.dTimeIncrement == obj.dTimeIncrement and \
            self.iOutputInterval == obj.iOutputInterval and \
            self.iDampingType == obj.iDampingType and \
            self.iModalDampingTableId == obj.iModalDampingTableId
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_FREQ_TIMESTEP()
        self.iumOfSteps = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iumOfSteps
        self.dTimeIncrement = normalizeDoubleType(nastranAnalysis[1]) if len(nastranAnalysis) > 1 else obj.dTimeIncrement
        self.iOutputInterval = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.iOutputInterval
        self.iDampingType = nastranAnalysis[3] if len(nastranAnalysis) > 3 else obj.iDampingType
        self.iModalDampingTableId = nastranAnalysis[4] if len(nastranAnalysis) > 4 else obj.iModalDampingTableId
        return self
    def __str__(self):
        obj = NASTRAN_FREQ_TIMESTEP()
        paramArgs = []
        if self.iumOfSteps != obj.iumOfSteps:
            paramArgs.append('iumOfSteps={0}'.format(getValueStr(self.iumOfSteps)))
        if self.dTimeIncrement != obj.dTimeIncrement:
            paramArgs.append('dTimeIncrement={0}'.format(getValueStr(self.dTimeIncrement)))
        if self.iOutputInterval != obj.iOutputInterval:
            paramArgs.append('iOutputInterval={0}'.format(getValueStr(self.iOutputInterval)))
        if self.iDampingType != obj.iDampingType:
            paramArgs.append('iDampingType={0}'.format(getValueStr(self.iDampingType)))
        if self.iModalDampingTableId != obj.iModalDampingTableId:
            paramArgs.append('iModalDampingTableId={0}'.format(getValueStr(self.iModalDampingTableId)))
        return 'NASTRAN_FREQ_TIMESTEP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            self.iumOfSteps,
            self.dTimeIncrement,
            self.iOutputInterval,
            self.iDampingType,
            self.iModalDampingTableId) + rightBracket

    def __eq__(self, other):
        return self.iumOfSteps == other.iumOfSteps and \
            self.dTimeIncrement == other.dTimeIncrement and \
            self.iOutputInterval == other.iOutputInterval and \
            self.iDampingType == other.iDampingType and \
            self.iModalDampingTableId == other.iModalDampingTableId

    def __ne__(self, other):
        return self.iumOfSteps != other.iumOfSteps or \
            self.dTimeIncrement != other.dTimeIncrement or \
            self.iOutputInterval != other.iOutputInterval or \
            self.iDampingType != other.iDampingType or \
            self.iModalDampingTableId != other.iModalDampingTableId

class NASTRAN_OUTPUT_REQUEST:
    def __init__(self,
        iValueDisplacement=DFLT_INT,
        iValueSpcforces=DFLT_INT,
        iValueOload=DFLT_INT,
        iValueMpcforces=DFLT_INT,
        iValueStress=DFLT_INT,
        iValueStrain=DFLT_INT,
        iValueForce=DFLT_INT,
        iValueGpforces=0,
        iValueNlstress=0,
        iValueStrainenergy=DFLT_INT,
        iValueKineticenergy=0,
        iValueBcresults=0,
        iValueBgresults=0,
        iValueSdisplacement=0,
        iValueAcceleration=0,
        iValueVelocity=0,
        iValueMeffmass=0,
        iValueThermal=DFLT_INT,
        iValueFlux=DFLT_INT,
        iTypeDisplacement=1,
        iTypeSpcforces=0,
        iTypeOload=0,
        iTypeMpcforces=0,
        iTypeStress=1,
        iTypeStrain=1,
        iTypeForce=0,
        iTypeGpforces=0,
        iTypeNlstress=0,
        iTypeStrainenergy=0,
        iTypeKineticenergy=0,
        iTypeBcresults=0,
        iTypeBgresults=0,
        iTypeSdisplacement=0,
        iTypeAcceleration=0,
        iTypeVelocity=0,
        iTypeMeffmass=0,
        iTypeThermal=0,
        iTypeFlux=0):
        self.iValueDisplacement = iValueDisplacement
        self.iValueSpcforces = iValueSpcforces
        self.iValueOload = iValueOload
        self.iValueMpcforces = iValueMpcforces
        self.iValueStress = iValueStress
        self.iValueStrain = iValueStrain
        self.iValueForce = iValueForce
        self.iValueGpforces = iValueGpforces
        self.iValueNlstress = iValueNlstress
        self.iValueStrainenergy = iValueStrainenergy
        self.iValueKineticenergy = iValueKineticenergy
        self.iValueBcresults = iValueBcresults
        self.iValueBgresults = iValueBgresults
        self.iValueSdisplacement = iValueSdisplacement
        self.iValueAcceleration = iValueAcceleration
        self.iValueVelocity = iValueVelocity
        self.iValueMeffmass = iValueMeffmass
        self.iValueThermal = iValueThermal
        self.iValueFlux = iValueFlux
        self.iTypeDisplacement = iTypeDisplacement
        self.iTypeSpcforces = iTypeSpcforces
        self.iTypeOload = iTypeOload
        self.iTypeMpcforces = iTypeMpcforces
        self.iTypeStress = iTypeStress
        self.iTypeStrain = iTypeStrain
        self.iTypeForce = iTypeForce
        self.iTypeGpforces = iTypeGpforces
        self.iTypeNlstress = iTypeNlstress
        self.iTypeStrainenergy = iTypeStrainenergy
        self.iTypeKineticenergy = iTypeKineticenergy
        self.iTypeBcresults = iTypeBcresults
        self.iTypeBgresults = iTypeBgresults
        self.iTypeSdisplacement = iTypeSdisplacement
        self.iTypeAcceleration = iTypeAcceleration
        self.iTypeVelocity = iTypeVelocity
        self.iTypeMeffmass = iTypeMeffmass
        self.iTypeThermal = iTypeThermal
        self.iTypeFlux = iTypeFlux
    def isDefault(self):
        obj = NASTRAN_OUTPUT_REQUEST()
        return self.iValueDisplacement == obj.iValueDisplacement and \
            self.iValueSpcforces == obj.iValueSpcforces and \
            self.iValueOload == obj.iValueOload and \
            self.iValueMpcforces == obj.iValueMpcforces and \
            self.iValueStress == obj.iValueStress and \
            self.iValueStrain == obj.iValueStrain and \
            self.iValueForce == obj.iValueForce and \
            self.iValueGpforces == obj.iValueGpforces and \
            self.iValueNlstress == obj.iValueNlstress and \
            self.iValueStrainenergy == obj.iValueStrainenergy and \
            self.iValueKineticenergy == obj.iValueKineticenergy and \
            self.iValueBcresults == obj.iValueBcresults and \
            self.iValueBgresults == obj.iValueBgresults and \
            self.iValueSdisplacement == obj.iValueSdisplacement and \
            self.iValueAcceleration == obj.iValueAcceleration and \
            self.iValueVelocity == obj.iValueVelocity and \
            self.iValueMeffmass == obj.iValueMeffmass and \
            self.iValueThermal == obj.iValueThermal and \
            self.iValueFlux == obj.iValueFlux and \
            self.iTypeDisplacement == obj.iTypeDisplacement and \
            self.iTypeSpcforces == obj.iTypeSpcforces and \
            self.iTypeOload == obj.iTypeOload and \
            self.iTypeMpcforces == obj.iTypeMpcforces and \
            self.iTypeStress == obj.iTypeStress and \
            self.iTypeStrain == obj.iTypeStrain and \
            self.iTypeForce == obj.iTypeForce and \
            self.iTypeGpforces == obj.iTypeGpforces and \
            self.iTypeNlstress == obj.iTypeNlstress and \
            self.iTypeStrainenergy == obj.iTypeStrainenergy and \
            self.iTypeKineticenergy == obj.iTypeKineticenergy and \
            self.iTypeBcresults == obj.iTypeBcresults and \
            self.iTypeBgresults == obj.iTypeBgresults and \
            self.iTypeSdisplacement == obj.iTypeSdisplacement and \
            self.iTypeAcceleration == obj.iTypeAcceleration and \
            self.iTypeVelocity == obj.iTypeVelocity and \
            self.iTypeMeffmass == obj.iTypeMeffmass and \
            self.iTypeThermal == obj.iTypeThermal and \
            self.iTypeFlux == obj.iTypeFlux
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_OUTPUT_REQUEST()
        self.iValueDisplacement = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iValueDisplacement
        self.iValueSpcforces = nastranAnalysis[1] if len(nastranAnalysis) > 1 else obj.iValueSpcforces
        self.iValueOload = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.iValueOload
        self.iValueMpcforces = nastranAnalysis[3] if len(nastranAnalysis) > 3 else obj.iValueMpcforces
        self.iValueStress = nastranAnalysis[4] if len(nastranAnalysis) > 4 else obj.iValueStress
        self.iValueStrain = nastranAnalysis[5] if len(nastranAnalysis) > 5 else obj.iValueStrain
        self.iValueForce = nastranAnalysis[6] if len(nastranAnalysis) > 6 else obj.iValueForce
        self.iValueGpforces = nastranAnalysis[7] if len(nastranAnalysis) > 7 else obj.iValueGpforces
        self.iValueNlstress = nastranAnalysis[8] if len(nastranAnalysis) > 8 else obj.iValueNlstress
        self.iValueStrainenergy = nastranAnalysis[9] if len(nastranAnalysis) > 9 else obj.iValueStrainenergy
        self.iValueKineticenergy = nastranAnalysis[10] if len(nastranAnalysis) > 10 else obj.iValueKineticenergy
        self.iValueBcresults = nastranAnalysis[11] if len(nastranAnalysis) > 11 else obj.iValueBcresults
        self.iValueBgresults = nastranAnalysis[12] if len(nastranAnalysis) > 12 else obj.iValueBgresults
        self.iValueSdisplacement = nastranAnalysis[13] if len(nastranAnalysis) > 13 else obj.iValueSdisplacement
        self.iValueAcceleration = nastranAnalysis[14] if len(nastranAnalysis) > 14 else obj.iValueAcceleration
        self.iValueVelocity = nastranAnalysis[15] if len(nastranAnalysis) > 15 else obj.iValueVelocity
        self.iValueMeffmass = nastranAnalysis[16] if len(nastranAnalysis) > 16 else obj.iValueMeffmass
        self.iValueThermal = nastranAnalysis[17] if len(nastranAnalysis) > 17 else obj.iValueThermal
        self.iValueFlux = nastranAnalysis[18] if len(nastranAnalysis) > 18 else obj.iValueFlux
        self.iTypeDisplacement = nastranAnalysis[19] if len(nastranAnalysis) > 19 else obj.iTypeDisplacement
        self.iTypeSpcforces = nastranAnalysis[20] if len(nastranAnalysis) > 20 else obj.iTypeSpcforces
        self.iTypeOload = nastranAnalysis[21] if len(nastranAnalysis) > 21 else obj.iTypeOload
        self.iTypeMpcforces = nastranAnalysis[22] if len(nastranAnalysis) > 22 else obj.iTypeMpcforces
        self.iTypeStress = nastranAnalysis[23] if len(nastranAnalysis) > 23 else obj.iTypeStress
        self.iTypeStrain = nastranAnalysis[24] if len(nastranAnalysis) > 24 else obj.iTypeStrain
        self.iTypeForce = nastranAnalysis[25] if len(nastranAnalysis) > 25 else obj.iTypeForce
        self.iTypeGpforces = nastranAnalysis[26] if len(nastranAnalysis) > 26 else obj.iTypeGpforces
        self.iTypeNlstress = nastranAnalysis[27] if len(nastranAnalysis) > 27 else obj.iTypeNlstress
        self.iTypeStrainenergy = nastranAnalysis[28] if len(nastranAnalysis) > 28 else obj.iTypeStrainenergy
        self.iTypeKineticenergy = nastranAnalysis[29] if len(nastranAnalysis) > 29 else obj.iTypeKineticenergy
        self.iTypeBcresults = nastranAnalysis[30] if len(nastranAnalysis) > 30 else obj.iTypeBcresults
        self.iTypeBgresults = nastranAnalysis[31] if len(nastranAnalysis) > 31 else obj.iTypeBgresults
        self.iTypeSdisplacement = nastranAnalysis[32] if len(nastranAnalysis) > 32 else obj.iTypeSdisplacement
        self.iTypeAcceleration = nastranAnalysis[33] if len(nastranAnalysis) > 33 else obj.iTypeAcceleration
        self.iTypeVelocity = nastranAnalysis[34] if len(nastranAnalysis) > 34 else obj.iTypeVelocity
        self.iTypeMeffmass = nastranAnalysis[35] if len(nastranAnalysis) > 35 else obj.iTypeMeffmass
        self.iTypeThermal = nastranAnalysis[36] if len(nastranAnalysis) > 36 else obj.iTypeThermal
        self.iTypeFlux = nastranAnalysis[37] if len(nastranAnalysis) > 37 else obj.iTypeFlux
        return self
    def __str__(self):
        obj = NASTRAN_OUTPUT_REQUEST()
        paramArgs = []
        if self.iValueDisplacement != obj.iValueDisplacement:
            paramArgs.append('iValueDisplacement={0}'.format(getValueStr(self.iValueDisplacement)))
        if self.iValueSpcforces != obj.iValueSpcforces:
            paramArgs.append('iValueSpcforces={0}'.format(getValueStr(self.iValueSpcforces)))
        if self.iValueOload != obj.iValueOload:
            paramArgs.append('iValueOload={0}'.format(getValueStr(self.iValueOload)))
        if self.iValueMpcforces != obj.iValueMpcforces:
            paramArgs.append('iValueMpcforces={0}'.format(getValueStr(self.iValueMpcforces)))
        if self.iValueStress != obj.iValueStress:
            paramArgs.append('iValueStress={0}'.format(getValueStr(self.iValueStress)))
        if self.iValueStrain != obj.iValueStrain:
            paramArgs.append('iValueStrain={0}'.format(getValueStr(self.iValueStrain)))
        if self.iValueForce != obj.iValueForce:
            paramArgs.append('iValueForce={0}'.format(getValueStr(self.iValueForce)))
        if self.iValueGpforces != obj.iValueGpforces:
            paramArgs.append('iValueGpforces={0}'.format(getValueStr(self.iValueGpforces)))
        if self.iValueNlstress != obj.iValueNlstress:
            paramArgs.append('iValueNlstress={0}'.format(getValueStr(self.iValueNlstress)))
        if self.iValueStrainenergy != obj.iValueStrainenergy:
            paramArgs.append('iValueStrainenergy={0}'.format(getValueStr(self.iValueStrainenergy)))
        if self.iValueKineticenergy != obj.iValueKineticenergy:
            paramArgs.append('iValueKineticenergy={0}'.format(getValueStr(self.iValueKineticenergy)))
        if self.iValueBcresults != obj.iValueBcresults:
            paramArgs.append('iValueBcresults={0}'.format(getValueStr(self.iValueBcresults)))
        if self.iValueBgresults != obj.iValueBgresults:
            paramArgs.append('iValueBgresults={0}'.format(getValueStr(self.iValueBgresults)))
        if self.iValueSdisplacement != obj.iValueSdisplacement:
            paramArgs.append('iValueSdisplacement={0}'.format(getValueStr(self.iValueSdisplacement)))
        if self.iValueAcceleration != obj.iValueAcceleration:
            paramArgs.append('iValueAcceleration={0}'.format(getValueStr(self.iValueAcceleration)))
        if self.iValueVelocity != obj.iValueVelocity:
            paramArgs.append('iValueVelocity={0}'.format(getValueStr(self.iValueVelocity)))
        if self.iValueMeffmass != obj.iValueMeffmass:
            paramArgs.append('iValueMeffmass={0}'.format(getValueStr(self.iValueMeffmass)))
        if self.iValueThermal != obj.iValueThermal:
            paramArgs.append('iValueThermal={0}'.format(getValueStr(self.iValueThermal)))
        if self.iValueFlux != obj.iValueFlux:
            paramArgs.append('iValueFlux={0}'.format(getValueStr(self.iValueFlux)))
        if self.iTypeDisplacement != obj.iTypeDisplacement:
            paramArgs.append('iTypeDisplacement={0}'.format(getValueStr(self.iTypeDisplacement)))
        if self.iTypeSpcforces != obj.iTypeSpcforces:
            paramArgs.append('iTypeSpcforces={0}'.format(getValueStr(self.iTypeSpcforces)))
        if self.iTypeOload != obj.iTypeOload:
            paramArgs.append('iTypeOload={0}'.format(getValueStr(self.iTypeOload)))
        if self.iTypeMpcforces != obj.iTypeMpcforces:
            paramArgs.append('iTypeMpcforces={0}'.format(getValueStr(self.iTypeMpcforces)))
        if self.iTypeStress != obj.iTypeStress:
            paramArgs.append('iTypeStress={0}'.format(getValueStr(self.iTypeStress)))
        if self.iTypeStrain != obj.iTypeStrain:
            paramArgs.append('iTypeStrain={0}'.format(getValueStr(self.iTypeStrain)))
        if self.iTypeForce != obj.iTypeForce:
            paramArgs.append('iTypeForce={0}'.format(getValueStr(self.iTypeForce)))
        if self.iTypeGpforces != obj.iTypeGpforces:
            paramArgs.append('iTypeGpforces={0}'.format(getValueStr(self.iTypeGpforces)))
        if self.iTypeNlstress != obj.iTypeNlstress:
            paramArgs.append('iTypeNlstress={0}'.format(getValueStr(self.iTypeNlstress)))
        if self.iTypeStrainenergy != obj.iTypeStrainenergy:
            paramArgs.append('iTypeStrainenergy={0}'.format(getValueStr(self.iTypeStrainenergy)))
        if self.iTypeKineticenergy != obj.iTypeKineticenergy:
            paramArgs.append('iTypeKineticenergy={0}'.format(getValueStr(self.iTypeKineticenergy)))
        if self.iTypeBcresults != obj.iTypeBcresults:
            paramArgs.append('iTypeBcresults={0}'.format(getValueStr(self.iTypeBcresults)))
        if self.iTypeBgresults != obj.iTypeBgresults:
            paramArgs.append('iTypeBgresults={0}'.format(getValueStr(self.iTypeBgresults)))
        if self.iTypeSdisplacement != obj.iTypeSdisplacement:
            paramArgs.append('iTypeSdisplacement={0}'.format(getValueStr(self.iTypeSdisplacement)))
        if self.iTypeAcceleration != obj.iTypeAcceleration:
            paramArgs.append('iTypeAcceleration={0}'.format(getValueStr(self.iTypeAcceleration)))
        if self.iTypeVelocity != obj.iTypeVelocity:
            paramArgs.append('iTypeVelocity={0}'.format(getValueStr(self.iTypeVelocity)))
        if self.iTypeMeffmass != obj.iTypeMeffmass:
            paramArgs.append('iTypeMeffmass={0}'.format(getValueStr(self.iTypeMeffmass)))
        if self.iTypeThermal != obj.iTypeThermal:
            paramArgs.append('iTypeThermal={0}'.format(getValueStr(self.iTypeThermal)))
        if self.iTypeFlux != obj.iTypeFlux:
            paramArgs.append('iTypeFlux={0}'.format(getValueStr(self.iTypeFlux)))
        return 'NASTRAN_OUTPUT_REQUEST({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}'.format(
            self.iValueDisplacement,
            self.iValueSpcforces,
            self.iValueOload,
            self.iValueMpcforces,
            self.iValueStress,
            self.iValueStrain,
            self.iValueForce,
            self.iValueGpforces,
            self.iValueNlstress,
            self.iValueStrainenergy,
            self.iValueKineticenergy,
            self.iValueBcresults,
            self.iValueBgresults,
            self.iValueSdisplacement,
            self.iValueAcceleration,
            self.iValueVelocity,
            self.iValueMeffmass,
            self.iValueThermal,
            self.iValueFlux,
            self.iTypeDisplacement,
            self.iTypeSpcforces,
            self.iTypeOload,
            self.iTypeMpcforces,
            self.iTypeStress,
            self.iTypeStrain,
            self.iTypeForce,
            self.iTypeGpforces,
            self.iTypeNlstress,
            self.iTypeStrainenergy,
            self.iTypeKineticenergy,
            self.iTypeBcresults,
            self.iTypeBgresults,
            self.iTypeSdisplacement,
            self.iTypeAcceleration,
            self.iTypeVelocity,
            self.iTypeMeffmass,
            self.iTypeThermal,
            self.iTypeFlux) + rightBracket

class NASTRAN_SETTINGS:
    def __init__(self,
        iPOST=-1,
        iOGEOM=0,
        iAUTOSPC=0,
        strGRDPNT="",
        strWTMASS="",
        strK6ROT="",
        strMAXRATIO="",
        iBAILOUT=DFLT_INT,
        iPRGPST=2,
        iRESVEC=0,
        dG=DFLT_DBL,
        dHFREQ=DFLT_DBL,
        dLFREQ=DFLT_DBL,
        dW3=DFLT_DBL,
        dW4=DFLT_DBL,
        iMEFFMASS=0,
        MEFFMASS_GRID_ID=DFLT_INT,
        iMLDS=1,
        iMLDSRCV=0):
        self.iPOST = iPOST
        self.iOGEOM = iOGEOM
        self.iAUTOSPC = iAUTOSPC
        self.strGRDPNT = strGRDPNT
        self.strWTMASS = strWTMASS
        self.strK6ROT = strK6ROT
        self.strMAXRATIO = strMAXRATIO
        self.iBAILOUT = iBAILOUT
        self.iPRGPST = iPRGPST
        self.iRESVEC = iRESVEC
        self.dG = dG
        self.dHFREQ = dHFREQ
        self.dLFREQ = dLFREQ
        self.dW3 = dW3
        self.dW4 = dW4
        self.iMEFFMASS = iMEFFMASS
        self.MEFFMASS_GRID_ID = MEFFMASS_GRID_ID
        self.iMLDS = iMLDS
        self.iMLDSRCV = iMLDSRCV
    def isDefault(self):
        obj = NASTRAN_SETTINGS()
        return self.iPOST == obj.iPOST and \
            self.iOGEOM == obj.iOGEOM and \
            self.iAUTOSPC == obj.iAUTOSPC and \
            self.strGRDPNT == obj.strGRDPNT and \
            self.strWTMASS == obj.strWTMASS and \
            self.strK6ROT == obj.strK6ROT and \
            self.strMAXRATIO == obj.strMAXRATIO and \
            self.iBAILOUT == obj.iBAILOUT and \
            self.iPRGPST == obj.iPRGPST and \
            self.iRESVEC == obj.iRESVEC and \
            self.dG == obj.dG and \
            self.dHFREQ == obj.dHFREQ and \
            self.dLFREQ == obj.dLFREQ and \
            self.dW3 == obj.dW3 and \
            self.dW4 == obj.dW4 and \
            self.iMEFFMASS == obj.iMEFFMASS and \
            self.MEFFMASS_GRID_ID == obj.MEFFMASS_GRID_ID and \
            self.iMLDS == obj.iMLDS and \
            self.iMLDSRCV == obj.iMLDSRCV
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_SETTINGS()
        self.iPOST = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iPOST
        self.iOGEOM = nastranAnalysis[1] if len(nastranAnalysis) > 1 else obj.iOGEOM
        self.iAUTOSPC = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.iAUTOSPC
        self.strGRDPNT = nastranAnalysis[3] if len(nastranAnalysis) > 3 else obj.strGRDPNT
        self.strWTMASS = nastranAnalysis[4] if len(nastranAnalysis) > 4 else obj.strWTMASS
        self.strK6ROT = nastranAnalysis[5] if len(nastranAnalysis) > 5 else obj.strK6ROT
        self.strMAXRATIO = nastranAnalysis[6] if len(nastranAnalysis) > 6 else obj.strMAXRATIO
        self.iBAILOUT = nastranAnalysis[7] if len(nastranAnalysis) > 7 else obj.iBAILOUT
        self.iPRGPST = nastranAnalysis[8] if len(nastranAnalysis) > 8 else obj.iPRGPST
        self.iRESVEC = nastranAnalysis[9] if len(nastranAnalysis) > 9 else obj.iRESVEC
        self.dG = normalizeDoubleType(nastranAnalysis[10]) if len(nastranAnalysis) > 10 else obj.dG
        self.dHFREQ = normalizeDoubleType(nastranAnalysis[11]) if len(nastranAnalysis) > 11 else obj.dHFREQ
        self.dLFREQ = normalizeDoubleType(nastranAnalysis[12]) if len(nastranAnalysis) > 12 else obj.dLFREQ
        self.dW3 = normalizeDoubleType(nastranAnalysis[13]) if len(nastranAnalysis) > 13 else obj.dW3
        self.dW4 = normalizeDoubleType(nastranAnalysis[14]) if len(nastranAnalysis) > 14 else obj.dW4
        self.iMEFFMASS = nastranAnalysis[15] if len(nastranAnalysis) > 15 else obj.iMEFFMASS
        self.MEFFMASS_GRID_ID = nastranAnalysis[16] if len(nastranAnalysis) > 16 else obj.MEFFMASS_GRID_ID
        self.iMLDS = nastranAnalysis[17] if len(nastranAnalysis) > 17 else obj.iMLDS
        self.iMLDSRCV = nastranAnalysis[18] if len(nastranAnalysis) > 18 else obj.iMLDSRCV
        return self
    def __str__(self):
        obj = NASTRAN_SETTINGS()
        paramArgs = []
        if self.iPOST != obj.iPOST:
            paramArgs.append('iPOST={0}'.format(getValueStr(self.iPOST)))
        if self.iOGEOM != obj.iOGEOM:
            paramArgs.append('iOGEOM={0}'.format(getValueStr(self.iOGEOM)))
        if self.iAUTOSPC != obj.iAUTOSPC:
            paramArgs.append('iAUTOSPC={0}'.format(getValueStr(self.iAUTOSPC)))
        if self.strGRDPNT != obj.strGRDPNT:
            paramArgs.append('strGRDPNT={0}'.format('"' + self.strGRDPNT + '"'))
        if self.strWTMASS != obj.strWTMASS:
            paramArgs.append('strWTMASS={0}'.format('"' + self.strWTMASS + '"'))
        if self.strK6ROT != obj.strK6ROT:
            paramArgs.append('strK6ROT={0}'.format('"' + self.strK6ROT + '"'))
        if self.strMAXRATIO != obj.strMAXRATIO:
            paramArgs.append('strMAXRATIO={0}'.format('"' + self.strMAXRATIO + '"'))
        if self.iBAILOUT != obj.iBAILOUT:
            paramArgs.append('iBAILOUT={0}'.format(getValueStr(self.iBAILOUT)))
        if self.iPRGPST != obj.iPRGPST:
            paramArgs.append('iPRGPST={0}'.format(getValueStr(self.iPRGPST)))
        if self.iRESVEC != obj.iRESVEC:
            paramArgs.append('iRESVEC={0}'.format(getValueStr(self.iRESVEC)))
        if self.dG != obj.dG:
            paramArgs.append('dG={0}'.format(getValueStr(self.dG)))
        if self.dHFREQ != obj.dHFREQ:
            paramArgs.append('dHFREQ={0}'.format(getValueStr(self.dHFREQ)))
        if self.dLFREQ != obj.dLFREQ:
            paramArgs.append('dLFREQ={0}'.format(getValueStr(self.dLFREQ)))
        if self.dW3 != obj.dW3:
            paramArgs.append('dW3={0}'.format(getValueStr(self.dW3)))
        if self.dW4 != obj.dW4:
            paramArgs.append('dW4={0}'.format(getValueStr(self.dW4)))
        if self.iMEFFMASS != obj.iMEFFMASS:
            paramArgs.append('iMEFFMASS={0}'.format(getValueStr(self.iMEFFMASS)))
        if self.MEFFMASS_GRID_ID != obj.MEFFMASS_GRID_ID:
            paramArgs.append('MEFFMASS_GRID_ID={0}'.format(getValueStr(self.MEFFMASS_GRID_ID)))
        if self.iMLDS != obj.iMLDS:
            paramArgs.append('iMLDS={0}'.format(getValueStr(self.iMLDS)))
        if self.iMLDSRCV != obj.iMLDSRCV:
            paramArgs.append('iMLDSRCV={0}'.format(getValueStr(self.iMLDSRCV)))
        return 'NASTRAN_SETTINGS({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}'.format(
            self.iPOST,
            self.iOGEOM,
            self.iAUTOSPC,
            '"' + self.strGRDPNT + '"',
            '"' + self.strWTMASS + '"',
            '"' + self.strK6ROT + '"',
            '"' + self.strMAXRATIO + '"',
            self.iBAILOUT,
            self.iPRGPST,
            self.iRESVEC,
            self.dG,
            self.dHFREQ,
            self.dLFREQ,
            self.dW3,
            self.dW4,
            self.iMEFFMASS,
            self.MEFFMASS_GRID_ID,
            self.iMLDS,
            self.iMLDSRCV) + rightBracket

    def __eq__(self, other):
        return self.iPOST == other.iPOST and \
            self.iOGEOM == other.iOGEOM and \
            self.iAUTOSPC == other.iAUTOSPC and \
            self.strGRDPNT == other.strGRDPNT and \
            self.strWTMASS == other.strWTMASS and \
            self.strK6ROT == other.strK6ROT and \
            self.strMAXRATIO == other.strMAXRATIO and \
            self.iBAILOUT == other.iBAILOUT and \
            self.iPRGPST == other.iPRGPST and \
            self.iRESVEC == other.iRESVEC and \
            self.dG == other.dG and \
            self.dHFREQ == other.dHFREQ and \
            self.dLFREQ == other.dLFREQ and \
            self.dW3 == other.dW3 and \
            self.dW4 == other.dW4 and \
            self.iMEFFMASS == other.iMEFFMASS and \
            self.MEFFMASS_GRID_ID == other.MEFFMASS_GRID_ID and \
            self.iMLDS == other.iMLDS and \
            self.iMLDSRCV == other.iMLDSRCV

    def __ne__(self, other):
        return self.iPOST != other.iPOST or \
            self.iOGEOM != other.iOGEOM or \
            self.iAUTOSPC != other.iAUTOSPC or \
            self.strGRDPNT != other.strGRDPNT or \
            self.strWTMASS != other.strWTMASS or \
            self.strK6ROT != other.strK6ROT or \
            self.strMAXRATIO != other.strMAXRATIO or \
            self.iBAILOUT != other.iBAILOUT or \
            self.iPRGPST != other.iPRGPST or \
            self.iRESVEC != other.iRESVEC or \
            self.dG != other.dG or \
            self.dHFREQ != other.dHFREQ or \
            self.dLFREQ != other.dLFREQ or \
            self.dW3 != other.dW3 or \
            self.dW4 != other.dW4 or \
            self.iMEFFMASS != other.iMEFFMASS or \
            self.MEFFMASS_GRID_ID != other.MEFFMASS_GRID_ID or \
            self.iMLDS != other.iMLDS or \
            self.iMLDSRCV != other.iMLDSRCV

class NASTRAN_CASE_CONTROL:
    def __init__(self,
        iECHO=0,
        strTitle=""):
        self.iECHO = iECHO
        self.strTitle = strTitle
    def isDefault(self):
        obj = NASTRAN_CASE_CONTROL()
        return self.iECHO == obj.iECHO and \
            self.strTitle == obj.strTitle
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_CASE_CONTROL()
        self.iECHO = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iECHO
        self.strTitle = nastranAnalysis[1] if len(nastranAnalysis) > 1 else obj.strTitle
        return self
    def __str__(self):
        obj = NASTRAN_CASE_CONTROL()
        paramArgs = []
        if self.iECHO != obj.iECHO:
            paramArgs.append('iECHO={0}'.format(getValueStr(self.iECHO)))
        if self.strTitle != obj.strTitle:
            paramArgs.append('strTitle={0}'.format('"' + self.strTitle + '"'))
        return 'NASTRAN_CASE_CONTROL({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            self.iECHO,
            '"' + self.strTitle + '"') + rightBracket

    def __eq__(self, other):
        return self.iECHO == other.iECHO and \
            self.strTitle == other.strTitle

    def __ne__(self, other):
        return self.iECHO != other.iECHO or \
            self.strTitle != other.strTitle

class NASTRAN_MAIN_LBC_SET:
    def __init__(self,
        iSubcaseIdForLoad=DFLT_INT,
        iSubcaseIdForDload=DFLT_INT,
        iSubcaseIdForSpc=DFLT_INT,
        iSubcaseIdForMpc=DFLT_INT,
        iSubcaseIdForTempInit=DFLT_INT,
        iSubcaseIdForTempLoad=DFLT_INT):
        self.iSubcaseIdForLoad = iSubcaseIdForLoad
        self.iSubcaseIdForDload = iSubcaseIdForDload
        self.iSubcaseIdForSpc = iSubcaseIdForSpc
        self.iSubcaseIdForMpc = iSubcaseIdForMpc
        self.iSubcaseIdForTempInit = iSubcaseIdForTempInit
        self.iSubcaseIdForTempLoad = iSubcaseIdForTempLoad
    def isDefault(self):
        obj = NASTRAN_MAIN_LBC_SET()
        return self.iSubcaseIdForLoad == obj.iSubcaseIdForLoad and \
            self.iSubcaseIdForDload == obj.iSubcaseIdForDload and \
            self.iSubcaseIdForSpc == obj.iSubcaseIdForSpc and \
            self.iSubcaseIdForMpc == obj.iSubcaseIdForMpc and \
            self.iSubcaseIdForTempInit == obj.iSubcaseIdForTempInit and \
            self.iSubcaseIdForTempLoad == obj.iSubcaseIdForTempLoad
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_MAIN_LBC_SET()
        self.iSubcaseIdForLoad = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iSubcaseIdForLoad
        self.iSubcaseIdForDload = nastranAnalysis[1] if len(nastranAnalysis) > 1 else obj.iSubcaseIdForDload
        self.iSubcaseIdForSpc = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.iSubcaseIdForSpc
        self.iSubcaseIdForMpc = nastranAnalysis[3] if len(nastranAnalysis) > 3 else obj.iSubcaseIdForMpc
        self.iSubcaseIdForTempInit = nastranAnalysis[4] if len(nastranAnalysis) > 4 else obj.iSubcaseIdForTempInit
        self.iSubcaseIdForTempLoad = nastranAnalysis[5] if len(nastranAnalysis) > 5 else obj.iSubcaseIdForTempLoad
        return self
    def __str__(self):
        obj = NASTRAN_MAIN_LBC_SET()
        paramArgs = []
        if self.iSubcaseIdForLoad != obj.iSubcaseIdForLoad:
            paramArgs.append('iSubcaseIdForLoad={0}'.format(getValueStr(self.iSubcaseIdForLoad)))
        if self.iSubcaseIdForDload != obj.iSubcaseIdForDload:
            paramArgs.append('iSubcaseIdForDload={0}'.format(getValueStr(self.iSubcaseIdForDload)))
        if self.iSubcaseIdForSpc != obj.iSubcaseIdForSpc:
            paramArgs.append('iSubcaseIdForSpc={0}'.format(getValueStr(self.iSubcaseIdForSpc)))
        if self.iSubcaseIdForMpc != obj.iSubcaseIdForMpc:
            paramArgs.append('iSubcaseIdForMpc={0}'.format(getValueStr(self.iSubcaseIdForMpc)))
        if self.iSubcaseIdForTempInit != obj.iSubcaseIdForTempInit:
            paramArgs.append('iSubcaseIdForTempInit={0}'.format(getValueStr(self.iSubcaseIdForTempInit)))
        if self.iSubcaseIdForTempLoad != obj.iSubcaseIdForTempLoad:
            paramArgs.append('iSubcaseIdForTempLoad={0}'.format(getValueStr(self.iSubcaseIdForTempLoad)))
        return 'NASTRAN_MAIN_LBC_SET({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            self.iSubcaseIdForLoad,
            self.iSubcaseIdForDload,
            self.iSubcaseIdForSpc,
            self.iSubcaseIdForMpc,
            self.iSubcaseIdForTempInit,
            self.iSubcaseIdForTempLoad) + rightBracket

    def __eq__(self, other):
        return self.iSubcaseIdForLoad == other.iSubcaseIdForLoad and \
            self.iSubcaseIdForDload == other.iSubcaseIdForDload and \
            self.iSubcaseIdForSpc == other.iSubcaseIdForSpc and \
            self.iSubcaseIdForMpc == other.iSubcaseIdForMpc and \
            self.iSubcaseIdForTempInit == other.iSubcaseIdForTempInit and \
            self.iSubcaseIdForTempLoad == other.iSubcaseIdForTempLoad

    def __ne__(self, other):
        return self.iSubcaseIdForLoad != other.iSubcaseIdForLoad or \
            self.iSubcaseIdForDload != other.iSubcaseIdForDload or \
            self.iSubcaseIdForSpc != other.iSubcaseIdForSpc or \
            self.iSubcaseIdForMpc != other.iSubcaseIdForMpc or \
            self.iSubcaseIdForTempInit != other.iSubcaseIdForTempInit or \
            self.iSubcaseIdForTempLoad != other.iSubcaseIdForTempLoad

class NASTRAN_SUBCASE:
    def __init__(self,
        iId=0,
        strTitle="",
        strArbitraryText="",
        iSubcaseIdForLoad=0,
        iSubcaseIdForDload=0,
        iSubcaseIdForSpc=0,
        iSubcaseIdForMpc=0,
        iSubcaseIdForBcontact=0,
        iSubcaseIdForTempInit=0,
        iSubcaseIdForTempLoad=0,
        iOutputreqDisplacement=0,
        iOutputreqStress=0,
        iOutputreqStrain=0,
        iOutputreqAcceleration=0,
        iOutputreqVelocity=0,
        nastranNonlinear=DFLT_INT):
        self.iId = iId
        self.strTitle = strTitle
        self.strArbitraryText = strArbitraryText
        self.iSubcaseIdForLoad = iSubcaseIdForLoad
        self.iSubcaseIdForDload = iSubcaseIdForDload
        self.iSubcaseIdForSpc = iSubcaseIdForSpc
        self.iSubcaseIdForMpc = iSubcaseIdForMpc
        self.iSubcaseIdForBcontact = iSubcaseIdForBcontact
        self.iSubcaseIdForTempInit = iSubcaseIdForTempInit
        self.iSubcaseIdForTempLoad = iSubcaseIdForTempLoad
        self.iOutputreqDisplacement = iOutputreqDisplacement
        self.iOutputreqStress = iOutputreqStress
        self.iOutputreqStrain = iOutputreqStrain
        self.iOutputreqAcceleration = iOutputreqAcceleration
        self.iOutputreqVelocity = iOutputreqVelocity
        self.nastranNonlinear = nastranNonlinear
    def isDefault(self):
        obj = NASTRAN_SUBCASE()
        return self.iId == obj.iId and \
            self.strTitle == obj.strTitle and \
            self.strArbitraryText == obj.strArbitraryText and \
            self.iSubcaseIdForLoad == obj.iSubcaseIdForLoad and \
            self.iSubcaseIdForDload == obj.iSubcaseIdForDload and \
            self.iSubcaseIdForSpc == obj.iSubcaseIdForSpc and \
            self.iSubcaseIdForMpc == obj.iSubcaseIdForMpc and \
            self.iSubcaseIdForBcontact == obj.iSubcaseIdForBcontact and \
            self.iSubcaseIdForTempInit == obj.iSubcaseIdForTempInit and \
            self.iSubcaseIdForTempLoad == obj.iSubcaseIdForTempLoad and \
            self.iOutputreqDisplacement == obj.iOutputreqDisplacement and \
            self.iOutputreqStress == obj.iOutputreqStress and \
            self.iOutputreqStrain == obj.iOutputreqStrain and \
            self.iOutputreqAcceleration == obj.iOutputreqAcceleration and \
            self.iOutputreqVelocity == obj.iOutputreqVelocity and \
            self.nastranNonlinear == obj.nastranNonlinear
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_SUBCASE()
        self.iId = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iId
        self.strTitle = nastranAnalysis[1] if len(nastranAnalysis) > 1 else obj.strTitle
        self.strArbitraryText = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.strArbitraryText
        self.iSubcaseIdForLoad = nastranAnalysis[3] if len(nastranAnalysis) > 3 else obj.iSubcaseIdForLoad
        self.iSubcaseIdForDload = nastranAnalysis[4] if len(nastranAnalysis) > 4 else obj.iSubcaseIdForDload
        self.iSubcaseIdForSpc = nastranAnalysis[5] if len(nastranAnalysis) > 5 else obj.iSubcaseIdForSpc
        self.iSubcaseIdForMpc = nastranAnalysis[6] if len(nastranAnalysis) > 6 else obj.iSubcaseIdForMpc
        self.iSubcaseIdForBcontact = nastranAnalysis[7] if len(nastranAnalysis) > 7 else obj.iSubcaseIdForBcontact
        self.iSubcaseIdForTempInit = nastranAnalysis[8] if len(nastranAnalysis) > 8 else obj.iSubcaseIdForTempInit
        self.iSubcaseIdForTempLoad = nastranAnalysis[9] if len(nastranAnalysis) > 9 else obj.iSubcaseIdForTempLoad
        self.iOutputreqDisplacement = nastranAnalysis[10] if len(nastranAnalysis) > 10 else obj.iOutputreqDisplacement
        self.iOutputreqStress = nastranAnalysis[11] if len(nastranAnalysis) > 11 else obj.iOutputreqStress
        self.iOutputreqStrain = nastranAnalysis[12] if len(nastranAnalysis) > 12 else obj.iOutputreqStrain
        self.iOutputreqAcceleration = nastranAnalysis[13] if len(nastranAnalysis) > 13 else obj.iOutputreqAcceleration
        self.iOutputreqVelocity = nastranAnalysis[14] if len(nastranAnalysis) > 14 else obj.iOutputreqVelocity
        self.nastranNonlinear = nastranAnalysis[15] if len(nastranAnalysis) > 15 else obj.nastranNonlinear
        return self
    def __str__(self):
        obj = NASTRAN_SUBCASE()
        paramArgs = []
        if self.iId != obj.iId:
            paramArgs.append('iId={0}'.format(getValueStr(self.iId)))
        if self.strTitle != obj.strTitle:
            paramArgs.append('strTitle={0}'.format('"' + self.strTitle + '"'))
        if self.strArbitraryText != obj.strArbitraryText:
            paramArgs.append('strArbitraryText={0}'.format('"' + self.strArbitraryText + '"'))
        if self.iSubcaseIdForLoad != obj.iSubcaseIdForLoad:
            paramArgs.append('iSubcaseIdForLoad={0}'.format(getValueStr(self.iSubcaseIdForLoad)))
        if self.iSubcaseIdForDload != obj.iSubcaseIdForDload:
            paramArgs.append('iSubcaseIdForDload={0}'.format(getValueStr(self.iSubcaseIdForDload)))
        if self.iSubcaseIdForSpc != obj.iSubcaseIdForSpc:
            paramArgs.append('iSubcaseIdForSpc={0}'.format(getValueStr(self.iSubcaseIdForSpc)))
        if self.iSubcaseIdForMpc != obj.iSubcaseIdForMpc:
            paramArgs.append('iSubcaseIdForMpc={0}'.format(getValueStr(self.iSubcaseIdForMpc)))
        if self.iSubcaseIdForBcontact != obj.iSubcaseIdForBcontact:
            paramArgs.append('iSubcaseIdForBcontact={0}'.format(getValueStr(self.iSubcaseIdForBcontact)))
        if self.iSubcaseIdForTempInit != obj.iSubcaseIdForTempInit:
            paramArgs.append('iSubcaseIdForTempInit={0}'.format(getValueStr(self.iSubcaseIdForTempInit)))
        if self.iSubcaseIdForTempLoad != obj.iSubcaseIdForTempLoad:
            paramArgs.append('iSubcaseIdForTempLoad={0}'.format(getValueStr(self.iSubcaseIdForTempLoad)))
        if self.iOutputreqDisplacement != obj.iOutputreqDisplacement:
            paramArgs.append('iOutputreqDisplacement={0}'.format(getValueStr(self.iOutputreqDisplacement)))
        if self.iOutputreqStress != obj.iOutputreqStress:
            paramArgs.append('iOutputreqStress={0}'.format(getValueStr(self.iOutputreqStress)))
        if self.iOutputreqStrain != obj.iOutputreqStrain:
            paramArgs.append('iOutputreqStrain={0}'.format(getValueStr(self.iOutputreqStrain)))
        if self.iOutputreqAcceleration != obj.iOutputreqAcceleration:
            paramArgs.append('iOutputreqAcceleration={0}'.format(getValueStr(self.iOutputreqAcceleration)))
        if self.iOutputreqVelocity != obj.iOutputreqVelocity:
            paramArgs.append('iOutputreqVelocity={0}'.format(getValueStr(self.iOutputreqVelocity)))
        if self.nastranNonlinear != obj.nastranNonlinear:
            paramArgs.append('nastranNonlinear={0}'.format(getValueStr(self.nastranNonlinear)))
        return 'NASTRAN_SUBCASE({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}'.format(
            self.iId,
            '"' + self.strTitle + '"',
            '"' + self.strArbitraryText + '"',
            self.iSubcaseIdForLoad,
            self.iSubcaseIdForDload,
            self.iSubcaseIdForSpc,
            self.iSubcaseIdForMpc,
            self.iSubcaseIdForBcontact,
            self.iSubcaseIdForTempInit,
            self.iSubcaseIdForTempLoad,
            self.iOutputreqDisplacement,
            self.iOutputreqStress,
            self.iOutputreqStrain,
            self.iOutputreqAcceleration,
            self.iOutputreqVelocity,
            self.nastranNonlinear) + rightBracket

    def __eq__(self, other):
        return self.iId == other.iId and \
            self.strTitle == other.strTitle and \
            self.strArbitraryText == other.strArbitraryText and \
            self.iSubcaseIdForLoad == other.iSubcaseIdForLoad and \
            self.iSubcaseIdForDload == other.iSubcaseIdForDload and \
            self.iSubcaseIdForSpc == other.iSubcaseIdForSpc and \
            self.iSubcaseIdForMpc == other.iSubcaseIdForMpc and \
            self.iSubcaseIdForBcontact == other.iSubcaseIdForBcontact and \
            self.iSubcaseIdForTempInit == other.iSubcaseIdForTempInit and \
            self.iSubcaseIdForTempLoad == other.iSubcaseIdForTempLoad and \
            self.iOutputreqDisplacement == other.iOutputreqDisplacement and \
            self.iOutputreqStress == other.iOutputreqStress and \
            self.iOutputreqStrain == other.iOutputreqStrain and \
            self.iOutputreqAcceleration == other.iOutputreqAcceleration and \
            self.iOutputreqVelocity == other.iOutputreqVelocity and \
            self.nastranNonlinear == other.nastranNonlinear

    def __ne__(self, other):
        return self.iId != other.iId or \
            self.strTitle != other.strTitle or \
            self.strArbitraryText != other.strArbitraryText or \
            self.iSubcaseIdForLoad != other.iSubcaseIdForLoad or \
            self.iSubcaseIdForDload != other.iSubcaseIdForDload or \
            self.iSubcaseIdForSpc != other.iSubcaseIdForSpc or \
            self.iSubcaseIdForMpc != other.iSubcaseIdForMpc or \
            self.iSubcaseIdForBcontact != other.iSubcaseIdForBcontact or \
            self.iSubcaseIdForTempInit != other.iSubcaseIdForTempInit or \
            self.iSubcaseIdForTempLoad != other.iSubcaseIdForTempLoad or \
            self.iOutputreqDisplacement != other.iOutputreqDisplacement or \
            self.iOutputreqStress != other.iOutputreqStress or \
            self.iOutputreqStrain != other.iOutputreqStrain or \
            self.iOutputreqAcceleration != other.iOutputreqAcceleration or \
            self.iOutputreqVelocity != other.iOutputreqVelocity or \
            self.nastranNonlinear != other.nastranNonlinear

class Nastran_Psd_Data:
    def __init__(self,
        iMasterID=0,
        iSlaveID=0,
        dRealX=1.0,
        dImagY=0.0,
        iTableID=0):
        self.iMasterID = iMasterID
        self.iSlaveID = iSlaveID
        self.dRealX = dRealX
        self.dImagY = dImagY
        self.iTableID = iTableID
    def isDefault(self):
        obj = Nastran_Psd_Data()
        return self.iMasterID == obj.iMasterID and \
            self.iSlaveID == obj.iSlaveID and \
            self.dRealX == obj.dRealX and \
            self.dImagY == obj.dImagY and \
            self.iTableID == obj.iTableID
    def fromList(self, param):
        obj = Nastran_Psd_Data()
        self.iMasterID = param[0] if len(param) > 0 else obj.iMasterID
        self.iSlaveID = param[1] if len(param) > 1 else obj.iSlaveID
        self.dRealX = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dRealX
        self.dImagY = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dImagY
        self.iTableID = param[4] if len(param) > 4 else obj.iTableID
        return self
    def __str__(self):
        obj = Nastran_Psd_Data()
        paramArgs = []
        if self.iMasterID != obj.iMasterID:
            paramArgs.append('iMasterID={0}'.format(getValueStr(self.iMasterID)))
        if self.iSlaveID != obj.iSlaveID:
            paramArgs.append('iSlaveID={0}'.format(getValueStr(self.iSlaveID)))
        if self.dRealX != obj.dRealX:
            paramArgs.append('dRealX={0}'.format(getValueStr(self.dRealX)))
        if self.dImagY != obj.dImagY:
            paramArgs.append('dImagY={0}'.format(getValueStr(self.dImagY)))
        if self.iTableID != obj.iTableID:
            paramArgs.append('iTableID={0}'.format(getValueStr(self.iTableID)))
        return 'Nastran_Psd_Data({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            self.iMasterID,
            self.iSlaveID,
            self.dRealX,
            self.dImagY,
            self.iTableID) + rightBracket

    def __eq__(self, other):
        return self.iMasterID == other.iMasterID and \
            self.iSlaveID == other.iSlaveID and \
            self.dRealX == other.dRealX and \
            self.dImagY == other.dImagY and \
            self.iTableID == other.iTableID

    def __ne__(self, other):
        return self.iMasterID != other.iMasterID or \
            self.iSlaveID != other.iSlaveID or \
            self.dRealX != other.dRealX or \
            self.dImagY != other.dImagY or \
            self.iTableID != other.iTableID

class Nastran_Psd_Opt:
    def __init__(self,
        iNodeSetID=0,
        bDofT1=False,
        bDofT2=False,
        bDofT3=False,
        bDofR1=False,
        bDofR2=False,
        bDofR3=False,
        iOutputType=0,
        iDispType=0,
        iVelocityType=0,
        iAcceType=0,
        dStartFreq=0.0,
        dEndFreq=0.0):
        self.iNodeSetID = iNodeSetID
        self.bDofT1 = bDofT1
        self.bDofT2 = bDofT2
        self.bDofT3 = bDofT3
        self.bDofR1 = bDofR1
        self.bDofR2 = bDofR2
        self.bDofR3 = bDofR3
        self.iOutputType = iOutputType
        self.iDispType = iDispType
        self.iVelocityType = iVelocityType
        self.iAcceType = iAcceType
        self.dStartFreq = dStartFreq
        self.dEndFreq = dEndFreq
    def isDefault(self):
        obj = Nastran_Psd_Opt()
        return self.iNodeSetID == obj.iNodeSetID and \
            self.bDofT1 == obj.bDofT1 and \
            self.bDofT2 == obj.bDofT2 and \
            self.bDofT3 == obj.bDofT3 and \
            self.bDofR1 == obj.bDofR1 and \
            self.bDofR2 == obj.bDofR2 and \
            self.bDofR3 == obj.bDofR3 and \
            self.iOutputType == obj.iOutputType and \
            self.iDispType == obj.iDispType and \
            self.iVelocityType == obj.iVelocityType and \
            self.iAcceType == obj.iAcceType and \
            self.dStartFreq == obj.dStartFreq and \
            self.dEndFreq == obj.dEndFreq
    def fromList(self, param):
        obj = Nastran_Psd_Opt()
        self.iNodeSetID = param[0] if len(param) > 0 else obj.iNodeSetID
        self.bDofT1 = getBoolValue(param[1]) if len(param) > 1 else obj.bDofT1
        self.bDofT2 = getBoolValue(param[2]) if len(param) > 2 else obj.bDofT2
        self.bDofT3 = getBoolValue(param[3]) if len(param) > 3 else obj.bDofT3
        self.bDofR1 = getBoolValue(param[4]) if len(param) > 4 else obj.bDofR1
        self.bDofR2 = getBoolValue(param[5]) if len(param) > 5 else obj.bDofR2
        self.bDofR3 = getBoolValue(param[6]) if len(param) > 6 else obj.bDofR3
        self.iOutputType = param[7] if len(param) > 7 else obj.iOutputType
        self.iDispType = param[8] if len(param) > 8 else obj.iDispType
        self.iVelocityType = param[9] if len(param) > 9 else obj.iVelocityType
        self.iAcceType = param[10] if len(param) > 10 else obj.iAcceType
        self.dStartFreq = normalizeDoubleType(param[11]) if len(param) > 11 else obj.dStartFreq
        self.dEndFreq = normalizeDoubleType(param[12]) if len(param) > 12 else obj.dEndFreq
        return self
    def __str__(self):
        obj = Nastran_Psd_Opt()
        paramArgs = []
        if self.iNodeSetID != obj.iNodeSetID:
            paramArgs.append('iNodeSetID={0}'.format(getValueStr(self.iNodeSetID)))
        if self.bDofT1 != obj.bDofT1:
            paramArgs.append('bDofT1={0}'.format(getBoolStr(self.bDofT1)))
        if self.bDofT2 != obj.bDofT2:
            paramArgs.append('bDofT2={0}'.format(getBoolStr(self.bDofT2)))
        if self.bDofT3 != obj.bDofT3:
            paramArgs.append('bDofT3={0}'.format(getBoolStr(self.bDofT3)))
        if self.bDofR1 != obj.bDofR1:
            paramArgs.append('bDofR1={0}'.format(getBoolStr(self.bDofR1)))
        if self.bDofR2 != obj.bDofR2:
            paramArgs.append('bDofR2={0}'.format(getBoolStr(self.bDofR2)))
        if self.bDofR3 != obj.bDofR3:
            paramArgs.append('bDofR3={0}'.format(getBoolStr(self.bDofR3)))
        if self.iOutputType != obj.iOutputType:
            paramArgs.append('iOutputType={0}'.format(getValueStr(self.iOutputType)))
        if self.iDispType != obj.iDispType:
            paramArgs.append('iDispType={0}'.format(getValueStr(self.iDispType)))
        if self.iVelocityType != obj.iVelocityType:
            paramArgs.append('iVelocityType={0}'.format(getValueStr(self.iVelocityType)))
        if self.iAcceType != obj.iAcceType:
            paramArgs.append('iAcceType={0}'.format(getValueStr(self.iAcceType)))
        if self.dStartFreq != obj.dStartFreq:
            paramArgs.append('dStartFreq={0}'.format(getValueStr(self.dStartFreq)))
        if self.dEndFreq != obj.dEndFreq:
            paramArgs.append('dEndFreq={0}'.format(getValueStr(self.dEndFreq)))
        return 'Nastran_Psd_Opt({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}'.format(
            self.iNodeSetID,
            1 if self.bDofT1 else 0,
            1 if self.bDofT2 else 0,
            1 if self.bDofT3 else 0,
            1 if self.bDofR1 else 0,
            1 if self.bDofR2 else 0,
            1 if self.bDofR3 else 0,
            self.iOutputType,
            self.iDispType,
            self.iVelocityType,
            self.iAcceType,
            self.dStartFreq,
            self.dEndFreq) + rightBracket

    def __eq__(self, other):
        return self.iNodeSetID == other.iNodeSetID and \
            self.bDofT1 == other.bDofT1 and \
            self.bDofT2 == other.bDofT2 and \
            self.bDofT3 == other.bDofT3 and \
            self.bDofR1 == other.bDofR1 and \
            self.bDofR2 == other.bDofR2 and \
            self.bDofR3 == other.bDofR3 and \
            self.iOutputType == other.iOutputType and \
            self.iDispType == other.iDispType and \
            self.iVelocityType == other.iVelocityType and \
            self.iAcceType == other.iAcceType and \
            self.dStartFreq == other.dStartFreq and \
            self.dEndFreq == other.dEndFreq

    def __ne__(self, other):
        return self.iNodeSetID != other.iNodeSetID or \
            self.bDofT1 != other.bDofT1 or \
            self.bDofT2 != other.bDofT2 or \
            self.bDofT3 != other.bDofT3 or \
            self.bDofR1 != other.bDofR1 or \
            self.bDofR2 != other.bDofR2 or \
            self.bDofR3 != other.bDofR3 or \
            self.iOutputType != other.iOutputType or \
            self.iDispType != other.iDispType or \
            self.iVelocityType != other.iVelocityType or \
            self.iAcceType != other.iAcceType or \
            self.dStartFreq != other.dStartFreq or \
            self.dEndFreq != other.dEndFreq

class NASTRAN_EXEC_CONTROL:
    def __init__(self,
        bGeometrycheck=False):
        self.bGeometrycheck = bGeometrycheck
    def isDefault(self):
        obj = NASTRAN_EXEC_CONTROL()
        return self.bGeometrycheck == obj.bGeometrycheck
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_EXEC_CONTROL()
        self.bGeometrycheck = getBoolValue(nastranAnalysis[0]) if len(nastranAnalysis) > 0 else obj.bGeometrycheck
        return self
    def __str__(self):
        obj = NASTRAN_EXEC_CONTROL()
        paramArgs = []
        if self.bGeometrycheck != obj.bGeometrycheck:
            paramArgs.append('bGeometrycheck={0}'.format(getBoolStr(self.bGeometrycheck)))
        return 'NASTRAN_EXEC_CONTROL({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}'.format(
            1 if self.bGeometrycheck else 0) + rightBracket

    def __eq__(self, other):
        return self.bGeometrycheck == other.bGeometrycheck

    def __ne__(self, other):
        return self.bGeometrycheck != other.bGeometrycheck

class NASTRAN_ANALYSIS:
    def __init__(self,
        iSolverType=0,
        iWriteType=0,
        iGridFormatType=0,
        bDeleteFloatingNodes=False,
        bContinuanceMarker=False,
        bDefineLbcId=False,
        iDefinedLoadId=0,
        iDefinedSpcId=0,
        iDefinedMpcId=0,
        bUniqueLbcId=False,
        bUseCASI=False,
        dEpsilon=0.0,
        iMaxNumOfIter=0,
        iNumberOfThreads=0,
        iMemory=0,
        bParamInrel=False,
        iNcpu=0,
        iSolNo=0,
        strIncludeFilePath="",
        nastranEigen=NASTRAN_EIGEN(),
        nastranEigen126=NASTRAN_EIGEN126(),
        nastranFrequency=NASTRAN_FREQUENCY(),
        nastranFreqTimestep=NASTRAN_FREQ_TIMESTEP(),
        nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(),
        nastranExecControl=NASTRAN_EXEC_CONTROL(),
        nastranCaseControl=NASTRAN_CASE_CONTROL(),
        nastranMainLbcSet=NASTRAN_MAIN_LBC_SET(),
        nastranSettings=NASTRAN_SETTINGS(),
        nastranNonlinear=NASTRAN_NONLINEAR(),
        nastranNonlinearTimestep=NASTRAN_NONLINEAR_TIMESTEP(),
        nastranSubcase=[],
        strSystemCellText="",
        strFileManagementText="",
        strExecutiveControlText="",
        strGlobalCaseControlText="",
        strBulkDataText="",
        iExportModelUnitSystem=0):
        self.iSolverType = iSolverType
        self.iWriteType = iWriteType
        self.iGridFormatType = iGridFormatType
        self.bDeleteFloatingNodes = bDeleteFloatingNodes
        self.bContinuanceMarker = bContinuanceMarker
        self.bDefineLbcId = bDefineLbcId
        self.iDefinedLoadId = iDefinedLoadId
        self.iDefinedSpcId = iDefinedSpcId
        self.iDefinedMpcId = iDefinedMpcId
        self.bUniqueLbcId = bUniqueLbcId
        self.bUseCASI = bUseCASI
        self.dEpsilon = dEpsilon
        self.iMaxNumOfIter = iMaxNumOfIter
        self.iNumberOfThreads = iNumberOfThreads
        self.iMemory = iMemory
        self.bParamInrel = bParamInrel
        self.iNcpu = iNcpu
        self.iSolNo = iSolNo
        self.strIncludeFilePath = strIncludeFilePath
        self.nastranEigen = nastranEigen
        self.nastranEigen126 = nastranEigen126
        self.nastranFrequency = nastranFrequency
        self.nastranFreqTimestep = nastranFreqTimestep
        self.nastranOutputRequest = nastranOutputRequest
        self.nastranExecControl = nastranExecControl
        self.nastranCaseControl = nastranCaseControl
        self.nastranMainLbcSet = nastranMainLbcSet
        self.nastranSettings = nastranSettings
        self.nastranNonlinear = nastranNonlinear
        self.nastranNonlinearTimestep = nastranNonlinearTimestep
        self.nastranSubcase = nastranSubcase
        self.strSystemCellText = strSystemCellText
        self.strFileManagementText = strFileManagementText
        self.strExecutiveControlText = strExecutiveControlText
        self.strGlobalCaseControlText = strGlobalCaseControlText
        self.strBulkDataText = strBulkDataText
        self.iExportModelUnitSystem = iExportModelUnitSystem
    def isDefault(self):
        obj = NASTRAN_ANALYSIS()
        return self.iSolverType == obj.iSolverType and \
            self.iWriteType == obj.iWriteType and \
            self.iGridFormatType == obj.iGridFormatType and \
            self.bDeleteFloatingNodes == obj.bDeleteFloatingNodes and \
            self.bContinuanceMarker == obj.bContinuanceMarker and \
            self.bDefineLbcId == obj.bDefineLbcId and \
            self.iDefinedLoadId == obj.iDefinedLoadId and \
            self.iDefinedSpcId == obj.iDefinedSpcId and \
            self.iDefinedMpcId == obj.iDefinedMpcId and \
            self.bUniqueLbcId == obj.bUniqueLbcId and \
            self.bUseCASI == obj.bUseCASI and \
            self.dEpsilon == obj.dEpsilon and \
            self.iMaxNumOfIter == obj.iMaxNumOfIter and \
            self.iNumberOfThreads == obj.iNumberOfThreads and \
            self.iMemory == obj.iMemory and \
            self.bParamInrel == obj.bParamInrel and \
            self.iNcpu == obj.iNcpu and \
            self.iSolNo == obj.iSolNo and \
            self.strIncludeFilePath == obj.strIncludeFilePath and \
            self.nastranEigen == obj.nastranEigen and \
            self.nastranEigen126 == obj.nastranEigen126 and \
            self.nastranFrequency == obj.nastranFrequency and \
            self.nastranFreqTimestep == obj.nastranFreqTimestep and \
            self.nastranOutputRequest == obj.nastranOutputRequest and \
            self.nastranExecControl == obj.nastranExecControl and \
            self.nastranCaseControl == obj.nastranCaseControl and \
            self.nastranMainLbcSet == obj.nastranMainLbcSet and \
            self.nastranSettings == obj.nastranSettings and \
            self.nastranNonlinear == obj.nastranNonlinear and \
            self.nastranNonlinearTimestep == obj.nastranNonlinearTimestep and \
            self.nastranSubcase == obj.nastranSubcase and \
            self.strSystemCellText == obj.strSystemCellText and \
            self.strFileManagementText == obj.strFileManagementText and \
            self.strExecutiveControlText == obj.strExecutiveControlText and \
            self.strGlobalCaseControlText == obj.strGlobalCaseControlText and \
            self.strBulkDataText == obj.strBulkDataText and \
            self.iExportModelUnitSystem == obj.iExportModelUnitSystem
    def fromList(self, nastranAnalysis):
        obj = NASTRAN_ANALYSIS()
        self.iSolverType = nastranAnalysis[0] if len(nastranAnalysis) > 0 else obj.iSolverType
        self.iWriteType = nastranAnalysis[1] if len(nastranAnalysis) > 1 else obj.iWriteType
        self.iGridFormatType = nastranAnalysis[2] if len(nastranAnalysis) > 2 else obj.iGridFormatType
        self.bDeleteFloatingNodes = getBoolValue(nastranAnalysis[3]) if len(nastranAnalysis) > 3 else obj.bDeleteFloatingNodes
        self.bContinuanceMarker = getBoolValue(nastranAnalysis[4]) if len(nastranAnalysis) > 4 else obj.bContinuanceMarker
        self.bDefineLbcId = getBoolValue(nastranAnalysis[5]) if len(nastranAnalysis) > 5 else obj.bDefineLbcId
        self.iDefinedLoadId = nastranAnalysis[6] if len(nastranAnalysis) > 6 else obj.iDefinedLoadId
        self.iDefinedSpcId = nastranAnalysis[7] if len(nastranAnalysis) > 7 else obj.iDefinedSpcId
        self.iDefinedMpcId = nastranAnalysis[8] if len(nastranAnalysis) > 8 else obj.iDefinedMpcId
        self.bUniqueLbcId = getBoolValue(nastranAnalysis[9]) if len(nastranAnalysis) > 9 else obj.bUniqueLbcId
        self.bUseCASI = getBoolValue(nastranAnalysis[10]) if len(nastranAnalysis) > 10 else obj.bUseCASI
        self.dEpsilon = normalizeDoubleType(nastranAnalysis[11]) if len(nastranAnalysis) > 11 else obj.dEpsilon
        self.iMaxNumOfIter = nastranAnalysis[12] if len(nastranAnalysis) > 12 else obj.iMaxNumOfIter
        self.iNumberOfThreads = nastranAnalysis[13] if len(nastranAnalysis) > 13 else obj.iNumberOfThreads
        self.iMemory = nastranAnalysis[14] if len(nastranAnalysis) > 14 else obj.iMemory
        self.bParamInrel = getBoolValue(nastranAnalysis[15]) if len(nastranAnalysis) > 15 else obj.bParamInrel
        self.iNcpu = nastranAnalysis[16] if len(nastranAnalysis) > 16 else obj.iNcpu
        self.iSolNo = nastranAnalysis[17] if len(nastranAnalysis) > 17 else obj.iSolNo
        self.strIncludeFilePath = nastranAnalysis[18] if len(nastranAnalysis) > 18 else obj.strIncludeFilePath
        self.nastranEigen = NASTRAN_EIGEN().fromList(nastranAnalysis[19]) if len(nastranAnalysis) > 19 else obj.nastranEigen
        self.nastranEigen126 = NASTRAN_EIGEN126().fromList(nastranAnalysis[20]) if len(nastranAnalysis) > 20 else obj.nastranEigen126
        self.nastranFrequency = NASTRAN_FREQUENCY().fromList(nastranAnalysis[21]) if len(nastranAnalysis) > 21 else obj.nastranFrequency
        self.nastranFreqTimestep = NASTRAN_FREQ_TIMESTEP().fromList(nastranAnalysis[22]) if len(nastranAnalysis) > 22 else obj.nastranFreqTimestep
        self.nastranOutputRequest = NASTRAN_OUTPUT_REQUEST().fromList(nastranAnalysis[23]) if len(nastranAnalysis) > 23 else obj.nastranOutputRequest
        self.nastranExecControl = NASTRAN_EXEC_CONTROL().fromList(nastranAnalysis[24]) if len(nastranAnalysis) > 24 else obj.nastranExecControl
        self.nastranCaseControl = NASTRAN_CASE_CONTROL().fromList(nastranAnalysis[25]) if len(nastranAnalysis) > 25 else obj.nastranCaseControl
        self.nastranMainLbcSet = NASTRAN_MAIN_LBC_SET().fromList(nastranAnalysis[26]) if len(nastranAnalysis) > 26 else obj.nastranMainLbcSet
        self.nastranSettings = NASTRAN_SETTINGS().fromList(nastranAnalysis[27]) if len(nastranAnalysis) > 27 else obj.nastranSettings
        self.nastranNonlinear = NASTRAN_NONLINEAR().fromList(nastranAnalysis[28]) if len(nastranAnalysis) > 28 else obj.nastranNonlinear
        self.nastranNonlinearTimestep = NASTRAN_NONLINEAR_TIMESTEP().fromList(nastranAnalysis[29]) if len(nastranAnalysis) > 29 else obj.nastranNonlinearTimestep
        self.nastranSubcase = [NASTRAN_SUBCASE().fromList(tok) for tok in nastranAnalysis[30]] if len(nastranAnalysis) > 30 else obj.nastranSubcase
        self.strSystemCellText = nastranAnalysis[31] if len(nastranAnalysis) > 31 else obj.strSystemCellText
        self.strFileManagementText = nastranAnalysis[32] if len(nastranAnalysis) > 32 else obj.strFileManagementText
        self.strExecutiveControlText = nastranAnalysis[33] if len(nastranAnalysis) > 33 else obj.strExecutiveControlText
        self.strGlobalCaseControlText = nastranAnalysis[34] if len(nastranAnalysis) > 34 else obj.strGlobalCaseControlText
        self.strBulkDataText = nastranAnalysis[35] if len(nastranAnalysis) > 35 else obj.strBulkDataText
        self.iExportModelUnitSystem = nastranAnalysis[36] if len(nastranAnalysis) > 36 else obj.iExportModelUnitSystem
        return self
    def __str__(self):
        obj = NASTRAN_ANALYSIS()
        paramArgs = []
        if self.iSolverType != obj.iSolverType:
            paramArgs.append('iSolverType={0}'.format(getValueStr(self.iSolverType)))
        if self.iWriteType != obj.iWriteType:
            paramArgs.append('iWriteType={0}'.format(getValueStr(self.iWriteType)))
        if self.iGridFormatType != obj.iGridFormatType:
            paramArgs.append('iGridFormatType={0}'.format(getValueStr(self.iGridFormatType)))
        if self.bDeleteFloatingNodes != obj.bDeleteFloatingNodes:
            paramArgs.append('bDeleteFloatingNodes={0}'.format(getBoolStr(self.bDeleteFloatingNodes)))
        if self.bContinuanceMarker != obj.bContinuanceMarker:
            paramArgs.append('bContinuanceMarker={0}'.format(getBoolStr(self.bContinuanceMarker)))
        if self.bDefineLbcId != obj.bDefineLbcId:
            paramArgs.append('bDefineLbcId={0}'.format(getBoolStr(self.bDefineLbcId)))
        if self.iDefinedLoadId != obj.iDefinedLoadId:
            paramArgs.append('iDefinedLoadId={0}'.format(getValueStr(self.iDefinedLoadId)))
        if self.iDefinedSpcId != obj.iDefinedSpcId:
            paramArgs.append('iDefinedSpcId={0}'.format(getValueStr(self.iDefinedSpcId)))
        if self.iDefinedMpcId != obj.iDefinedMpcId:
            paramArgs.append('iDefinedMpcId={0}'.format(getValueStr(self.iDefinedMpcId)))
        if self.bUniqueLbcId != obj.bUniqueLbcId:
            paramArgs.append('bUniqueLbcId={0}'.format(getBoolStr(self.bUniqueLbcId)))
        if self.bUseCASI != obj.bUseCASI:
            paramArgs.append('bUseCASI={0}'.format(getBoolStr(self.bUseCASI)))
        if self.dEpsilon != obj.dEpsilon:
            paramArgs.append('dEpsilon={0}'.format(getValueStr(self.dEpsilon)))
        if self.iMaxNumOfIter != obj.iMaxNumOfIter:
            paramArgs.append('iMaxNumOfIter={0}'.format(getValueStr(self.iMaxNumOfIter)))
        if self.iNumberOfThreads != obj.iNumberOfThreads:
            paramArgs.append('iNumberOfThreads={0}'.format(getValueStr(self.iNumberOfThreads)))
        if self.iMemory != obj.iMemory:
            paramArgs.append('iMemory={0}'.format(getValueStr(self.iMemory)))
        if self.bParamInrel != obj.bParamInrel:
            paramArgs.append('bParamInrel={0}'.format(getBoolStr(self.bParamInrel)))
        if self.iNcpu != obj.iNcpu:
            paramArgs.append('iNcpu={0}'.format(getValueStr(self.iNcpu)))
        if self.iSolNo != obj.iSolNo:
            paramArgs.append('iSolNo={0}'.format(getValueStr(self.iSolNo)))
        if self.strIncludeFilePath != obj.strIncludeFilePath:
            paramArgs.append('strIncludeFilePath={0}'.format('"' + self.strIncludeFilePath + '"'))
        if self.nastranEigen != obj.nastranEigen:
            paramArgs.append('nastranEigen={0}'.format(self.nastranEigen))
        if self.nastranEigen126 != obj.nastranEigen126:
            paramArgs.append('nastranEigen126={0}'.format(self.nastranEigen126))
        if self.nastranFrequency != obj.nastranFrequency:
            paramArgs.append('nastranFrequency={0}'.format(self.nastranFrequency))
        if self.nastranFreqTimestep != obj.nastranFreqTimestep:
            paramArgs.append('nastranFreqTimestep={0}'.format(self.nastranFreqTimestep))
        if self.nastranOutputRequest != obj.nastranOutputRequest:
            paramArgs.append('nastranOutputRequest={0}'.format(self.nastranOutputRequest))
        if self.nastranExecControl != obj.nastranExecControl:
            paramArgs.append('nastranExecControl={0}'.format(self.nastranExecControl))
        if self.nastranCaseControl != obj.nastranCaseControl:
            paramArgs.append('nastranCaseControl={0}'.format(self.nastranCaseControl))
        if self.nastranMainLbcSet != obj.nastranMainLbcSet:
            paramArgs.append('nastranMainLbcSet={0}'.format(self.nastranMainLbcSet))
        if self.nastranSettings != obj.nastranSettings:
            paramArgs.append('nastranSettings={0}'.format(self.nastranSettings))
        if self.nastranNonlinear != obj.nastranNonlinear:
            paramArgs.append('nastranNonlinear={0}'.format(self.nastranNonlinear))
        if self.nastranNonlinearTimestep != obj.nastranNonlinearTimestep:
            paramArgs.append('nastranNonlinearTimestep={0}'.format(self.nastranNonlinearTimestep))
        if self.nastranSubcase != obj.nastranSubcase:
            paramArgs.append('nastranSubcase={0}'.format(self.nastranSubcase))
        if self.strSystemCellText != obj.strSystemCellText:
            paramArgs.append('strSystemCellText={0}'.format('"' + self.strSystemCellText + '"'))
        if self.strFileManagementText != obj.strFileManagementText:
            paramArgs.append('strFileManagementText={0}'.format('"' + self.strFileManagementText + '"'))
        if self.strExecutiveControlText != obj.strExecutiveControlText:
            paramArgs.append('strExecutiveControlText={0}'.format('"' + self.strExecutiveControlText + '"'))
        if self.strGlobalCaseControlText != obj.strGlobalCaseControlText:
            paramArgs.append('strGlobalCaseControlText={0}'.format('"' + self.strGlobalCaseControlText + '"'))
        if self.strBulkDataText != obj.strBulkDataText:
            paramArgs.append('strBulkDataText={0}'.format('"' + self.strBulkDataText + '"'))
        if self.iExportModelUnitSystem != obj.iExportModelUnitSystem:
            paramArgs.append('iExportModelUnitSystem={0}'.format(getValueStr(self.iExportModelUnitSystem)))
        return 'NASTRAN_ANALYSIS({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}'.format(
            self.iSolverType,
            self.iWriteType,
            self.iGridFormatType,
            1 if self.bDeleteFloatingNodes else 0,
            1 if self.bContinuanceMarker else 0,
            1 if self.bDefineLbcId else 0,
            self.iDefinedLoadId,
            self.iDefinedSpcId,
            self.iDefinedMpcId,
            1 if self.bUniqueLbcId else 0,
            1 if self.bUseCASI else 0,
            self.dEpsilon,
            self.iMaxNumOfIter,
            self.iNumberOfThreads,
            self.iMemory,
            1 if self.bParamInrel else 0,
            self.iNcpu,
            self.iSolNo,
            '"' + self.strIncludeFilePath + '"',
            self.nastranEigen.toNativeStr(isOneParam=True),
            self.nastranEigen126.toNativeStr(isOneParam=True),
            self.nastranFrequency.toNativeStr(isOneParam=True),
            self.nastranFreqTimestep.toNativeStr(isOneParam=True),
            self.nastranOutputRequest.toNativeStr(isOneParam=True),
            self.nastranExecControl.toNativeStr(isOneParam=True),
            self.nastranCaseControl.toNativeStr(isOneParam=True),
            self.nastranMainLbcSet.toNativeStr(isOneParam=True),
            self.nastranSettings.toNativeStr(isOneParam=True),
            self.nastranNonlinear.toNativeStr(isOneParam=True),
            self.nastranNonlinearTimestep.toNativeStr(isOneParam=True),
            '[' + ', '.join([tok.toNativeStr(isOneParam=True) for tok in self.nastranSubcase]) + ']',
            '"' + self.strSystemCellText + '"',
            '"' + self.strFileManagementText + '"',
            '"' + self.strExecutiveControlText + '"',
            '"' + self.strGlobalCaseControlText + '"',
            '"' + self.strBulkDataText + '"',
            self.iExportModelUnitSystem) + rightBracket

class TIME_POINTS:
    def __init__(self,
        crCrtimePoint=None,
        bSpecify=False):
        self.crCrtimePoint = crCrtimePoint
        self.bSpecify = bSpecify
    def isDefault(self):
        obj = TIME_POINTS()
        return self.crCrtimePoint == obj.crCrtimePoint and \
            self.bSpecify == obj.bSpecify
    def fromList(self, param):
        obj = TIME_POINTS()
        self.crCrtimePoint = getCursorValue(param[0]) if len(param) > 0 else obj.crCrtimePoint
        self.bSpecify = getBoolValue(param[1]) if len(param) > 1 else obj.bSpecify
        return self
    def __str__(self):
        obj = TIME_POINTS()
        paramArgs = []
        if self.crCrtimePoint != obj.crCrtimePoint:
            paramArgs.append('crCrtimePoint={0}'.format(getCursorValueStr(self.crCrtimePoint)))
        if self.bSpecify != obj.bSpecify:
            paramArgs.append('bSpecify={0}'.format(getBoolStr(self.bSpecify)))
        return 'TIME_POINTS({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            str(self.crCrtimePoint) if self.crCrtimePoint is not None else '0:0',
            1 if self.bSpecify else 0) + rightBracket

class ABAQUS_OUTPUT_REQUEST:
    def __init__(self,
        strName="",
        strDescription="",
        iId=0,
        iOutputFiletype=0,
        iDomainType=0,
        iDomainId=0,
        iFrequencyType=0,
        dFrequency=0.0,
        ParamTimePoint=TIME_POINTS(),
        iTiming=0,
        strlOutputVariables=[]):
        self.strName = strName
        self.strDescription = strDescription
        self.iId = iId
        self.iOutputFiletype = iOutputFiletype
        self.iDomainType = iDomainType
        self.iDomainId = iDomainId
        self.iFrequencyType = iFrequencyType
        self.dFrequency = dFrequency
        self.iTiming = iTiming
        self.strlOutputVariables = strlOutputVariables
    def isDefault(self):
        obj = ABAQUS_OUTPUT_REQUEST()
        return self.strName == obj.strName and \
            self.strDescription == obj.strDescription and \
            self.iId == obj.iId and \
            self.iOutputFiletype == obj.iOutputFiletype and \
            self.iDomainType == obj.iDomainType and \
            self.iDomainId == obj.iDomainId and \
            self.iFrequencyType == obj.iFrequencyType and \
            self.dFrequency == obj.dFrequency and \
            self.iTiming == obj.iTiming and \
            self.strlOutputVariables == obj.strlOutputVariables
    def fromList(self, param):
        obj = ABAQUS_OUTPUT_REQUEST()
        self.strName = param[0] if len(param) > 0 else obj.strName
        self.strDescription = param[1] if len(param) > 1 else obj.strDescription
        self.iId = param[2] if len(param) > 2 else obj.iId
        self.iOutputFiletype = param[3] if len(param) > 3 else obj.iOutputFiletype
        self.iDomainType = param[4] if len(param) > 4 else obj.iDomainType
        self.iDomainId = param[5] if len(param) > 5 else obj.iDomainId
        self.iFrequencyType = param[6] if len(param) > 6 else obj.iFrequencyType
        self.dFrequency = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dFrequency
        self.iTiming = param[8] if len(param) > 8 else obj.iTiming
        self.strlOutputVariables = param[9] if len(param) > 9 else obj.strlOutputVariables
        return self
    def __str__(self):
        obj = ABAQUS_OUTPUT_REQUEST()
        paramArgs = []
        if self.strName != obj.strName:
            paramArgs.append('strName={0}'.format('"' + self.strName + '"'))
        if self.strDescription != obj.strDescription:
            paramArgs.append('strDescription={0}'.format('"' + self.strDescription + '"'))
        if self.iId != obj.iId:
            paramArgs.append('iId={0}'.format(getValueStr(self.iId)))
        if self.iOutputFiletype != obj.iOutputFiletype:
            paramArgs.append('iOutputFiletype={0}'.format(getValueStr(self.iOutputFiletype)))
        if self.iDomainType != obj.iDomainType:
            paramArgs.append('iDomainType={0}'.format(getValueStr(self.iDomainType)))
        if self.iDomainId != obj.iDomainId:
            paramArgs.append('iDomainId={0}'.format(getValueStr(self.iDomainId)))
        if self.iFrequencyType != obj.iFrequencyType:
            paramArgs.append('iFrequencyType={0}'.format(getValueStr(self.iFrequencyType)))
        if self.dFrequency != obj.dFrequency:
            paramArgs.append('dFrequency={0}'.format(getValueStr(self.dFrequency)))
        if self.iTiming != obj.iTiming:
            paramArgs.append('iTiming={0}'.format(getValueStr(self.iTiming)))
        if self.strlOutputVariables != obj.strlOutputVariables:
            paramArgs.append('strlOutputVariables={0}'.format(self.strlOutputVariables))
        return 'ABAQUS_OUTPUT_REQUEST({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}'.format(
            '"' + self.strName + '"',
            '"' + self.strDescription + '"',
            self.iId,
            self.iOutputFiletype,
            self.iDomainType,
            self.iDomainId,
            self.iFrequencyType,
            self.dFrequency,
            self.iTiming,
            '[' + ', '.join('"' + tok + '"' for tok in self.strlOutputVariables) + ']') + rightBracket

class ABAQUS_DYNAMIC:
    def __init__(self,
        strName="",
        strDescription="",
        bAutomatic=True,
        iMaxInc=0,
        iInitialSize=0,
        iMinSize=0.0,
        iMaxSize=0.0,
        iSuppressHalfRescal=0,
        dHalfStepResTol=DFLT_DBL,
        iMethod=0,
        iMatrixStorage=0,
        iSolutionTechnique=0,
        iAllowedIters=0,
        iAdjustFactor=0,
        iMaxContactIter=0,
        dDampingControl=DFLT_DBL,
        iPassCalInitialAcceleration=0,
        INlgeom=1,
        dTimePeriod=DFLT_DBL,
        iIncludeHeatEffect=0,
        iConvertDscntIter=0,
        iRamp=0,
        iAcceptByMaxIters=0,
        outputRequestParams = []):
        self.strName = strName
        self.desp = strDescription
        self.bAutomatic = bAutomatic
        self.iMaxInc = iMaxInc
        self.iInitialSize = iInitialSize
        self.iMinSize = iMinSize
        self.iMaxSize = iMaxSize
        self.iSuppressHalfRescal = iSuppressHalfRescal
        self.dHalfStepResTol = dHalfStepResTol
        self.iMethod = iMethod
        self.iMatrixStorage = iMatrixStorage
        self.iSolutionTechnique = iSolutionTechnique
        self.iAllowedIters = iAllowedIters
        self.iAdjustFactor = iAdjustFactor
        self.iMaxContactIter = iMaxContactIter
        self.damping_control = dDampingControl
        self.iPassCalInitialAcceleration = iPassCalInitialAcceleration
        self.INlgeom = INlgeom
        self.dTimePeriod = dTimePeriod
        self.iIncludeHeatEffect = iIncludeHeatEffect
        self.iConvertDscntIter = iConvertDscntIter
        self.iRamp = iRamp
        self.iAcceptByMaxIters = iAcceptByMaxIters
        self.outputRequestParams = outputRequestParams
    def isDefault(self):
        obj = ABAQUS_DYNAMIC()
        return self.strName == obj.strName and \
            self.strDescription == obj.strDescription and \
            self.bAutomatic == obj.bAutomatic and \
            self.iMaxInc == obj.iMaxInc and \
            self.iInitialSize == obj.iInitialSize and \
            self.iMinSize == obj.iMinSize and \
            self.iMaxSize == obj.iMaxSize and \
            self.iSuppressHalfRescal == obj.iSuppressHalfRescal and \
            self.dHalfStepResTol == obj.dHalfStepResTol and \
            self.iMethod == obj.iMethod and \
            self.iMatrixStorage == obj.iMatrixStorage and \
            self.iSolutionTechnique == obj.iSolutionTechnique and \
            self.iAllowedIters == obj.iAllowedIters and \
            self.iAdjustFactor == obj.iAdjustFactor and \
            self.iMaxContactIter == obj.iMaxContactIter and \
            self.dDampingControl == obj.dDampingControl and \
            self.iPassCalInitialAcceleration == obj.iPassCalInitialAcceleration and \
            self.INlgeom == obj.INlgeom and \
            self.dTimePeriod == obj.dTimePeriod and \
            self.iIncludeHeatEffect == obj.iIncludeHeatEffect and \
            self.iConvertDscntIter == obj.iConvertDscntIter and \
            self.iRamp == obj.iRamp and \
            self.iAcceptByMaxIters == obj.iAcceptByMaxIters and \
            self.outputRequestParams == obj.outputRequestParams
    def fromList(self, param):
        obj = ABAQUS_DYNAMIC()
        self.strName = param[0] if len(param) > 0 else obj.strName
        self.strDescription = param[1] if len(param) > 1 else obj.strDescription
        self.bAutomatic = getBoolValue(param[2]) if len(param) > 2 else obj.bAutomatic
        self.iMaxInc = param[3] if len(param) > 3 else obj.iMaxInc
        self.iInitialSize = param[4] if len(param) > 4 else obj.iInitialSize
        self.iMinSize = normalizeDoubleType(param[5]) if len(param) > 5 else obj.iMinSize
        self.iMaxSize = normalizeDoubleType(param[6]) if len(param) > 6 else obj.iMaxSize
        self.iSuppressHalfRescal = param[7] if len(param) > 7 else obj.iSuppressHalfRescal
        self.dHalfStepResTol = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dHalfStepResTol
        self.iMethod = param[9] if len(param) > 9 else obj.iMethod
        self.iMatrixStorage = param[10] if len(param) > 10 else obj.iMatrixStorage
        self.iSolutionTechnique = param[11] if len(param) > 11 else obj.iSolutionTechnique
        self.iAllowedIters = param[12] if len(param) > 12 else obj.iAllowedIters
        self.iAdjustFactor = param[13] if len(param) > 13 else obj.iAdjustFactor
        self.iMaxContactIter = param[14] if len(param) > 14 else obj.iMaxContactIter
        self.dDampingControl = normalizeDoubleType(param[15]) if len(param) > 15 else obj.dDampingControl
        self.iPassCalInitialAcceleration = param[16] if len(param) > 16 else obj.iPassCalInitialAcceleration
        self.INlgeom = param[17] if len(param) > 17 else obj.INlgeom
        self.dTimePeriod = normalizeDoubleType(param[18]) if len(param) > 18 else obj.dTimePeriod
        self.iIncludeHeatEffect = param[19] if len(param) > 19 else obj.iIncludeHeatEffect
        self.iConvertDscntIter = param[20] if len(param) > 20 else obj.iConvertDscntIter
        self.iRamp = param[21] if len(param) > 21 else obj.iRamp
        self.iAcceptByMaxIters = param[22] if len(param) > 22 else obj.iAcceptByMaxIters
        self.outputRequestParams = param[23] if len(param) > 23 else obj.outputRequestParams
        return self
    def __str__(self):
        obj = ABAQUS_DYNAMIC()
        paramArgs = []
        if self.strName != obj.strName:
            paramArgs.append('strName={0}'.format('"' + self.strName + '"'))
        if self.strDescription != obj.strDescription:
            paramArgs.append('strDescription={0}'.format('"' + self.strDescription + '"'))
        if self.bAutomatic != obj.bAutomatic:
            paramArgs.append('bAutomatic={0}'.format(getBoolStr(self.bAutomatic)))
        if self.iMaxInc != obj.iMaxInc:
            paramArgs.append('iMaxInc={0}'.format(getValueStr(self.iMaxInc)))
        if self.iInitialSize != obj.iInitialSize:
            paramArgs.append('iInitialSize={0}'.format(getValueStr(self.iInitialSize)))
        if self.iMinSize != obj.iMinSize:
            paramArgs.append('iMinSize={0}'.format(getValueStr(self.iMinSize)))
        if self.iMaxSize != obj.iMaxSize:
            paramArgs.append('iMaxSize={0}'.format(getValueStr(self.iMaxSize)))
        if self.iSuppressHalfRescal != obj.iSuppressHalfRescal:
            paramArgs.append('iSuppressHalfRescal={0}'.format(getValueStr(self.iSuppressHalfRescal)))
        if self.dHalfStepResTol != obj.dHalfStepResTol:
            paramArgs.append('dHalfStepResTol={0}'.format(getValueStr(self.dHalfStepResTol)))
        if self.iMethod != obj.iMethod:
            paramArgs.append('iMethod={0}'.format(getValueStr(self.iMethod)))
        if self.iMatrixStorage != obj.iMatrixStorage:
            paramArgs.append('iMatrixStorage={0}'.format(getValueStr(self.iMatrixStorage)))
        if self.iSolutionTechnique != obj.iSolutionTechnique:
            paramArgs.append('iSolutionTechnique={0}'.format(getValueStr(self.iSolutionTechnique)))
        if self.iAllowedIters != obj.iAllowedIters:
            paramArgs.append('iAllowedIters={0}'.format(getValueStr(self.iAllowedIters)))
        if self.iAdjustFactor != obj.iAdjustFactor:
            paramArgs.append('iAdjustFactor={0}'.format(getValueStr(self.iAdjustFactor)))
        if self.iMaxContactIter != obj.iMaxContactIter:
            paramArgs.append('iMaxContactIter={0}'.format(getValueStr(self.iMaxContactIter)))
        if self.dDampingControl != obj.dDampingControl:
            paramArgs.append('dDampingControl={0}'.format(getValueStr(self.dDampingControl)))
        if self.iPassCalInitialAcceleration != obj.iPassCalInitialAcceleration:
            paramArgs.append('iPassCalInitialAcceleration={0}'.format(getValueStr(self.iPassCalInitialAcceleration)))
        if self.INlgeom != obj.INlgeom:
            paramArgs.append('INlgeom={0}'.format(getValueStr(self.INlgeom)))
        if self.dTimePeriod != obj.dTimePeriod:
            paramArgs.append('dTimePeriod={0}'.format(getValueStr(self.dTimePeriod)))
        if self.iIncludeHeatEffect != obj.iIncludeHeatEffect:
            paramArgs.append('iIncludeHeatEffect={0}'.format(getValueStr(self.iIncludeHeatEffect)))
        if self.iConvertDscntIter != obj.iConvertDscntIter:
            paramArgs.append('iConvertDscntIter={0}'.format(getValueStr(self.iConvertDscntIter)))
        if self.iRamp != obj.iRamp:
            paramArgs.append('iRamp={0}'.format(getValueStr(self.iRamp)))
        if self.iAcceptByMaxIters != obj.iAcceptByMaxIters:
            paramArgs.append('iAcceptByMaxIters={0}'.format(getValueStr(self.iAcceptByMaxIters)))
        if self.outputRequestParams != obj.outputRequestParams:
            paramArgs.append('outputRequestParams={0}'.format(self.outputRequestParams))    
        return 'ABAQUS_DYNAMIC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}'.format(
            '"' + self.strName + '"',
            '"' + self.strDescription + '"',
            1 if self.bAutomatic else 0,
            self.iMaxInc,
            self.iInitialSize,
            self.iMinSize,
            self.iMaxSize,
            self.iSuppressHalfRescal,
            self.dHalfStepResTol,
            self.iMethod,
            self.iMatrixStorage,
            self.iSolutionTechnique,
            self.iAllowedIters,
            self.iAdjustFactor,
            self.iMaxContactIter,
            self.dDampingControl,
            self.iPassCalInitialAcceleration,
            self.INlgeom,
            self.dTimePeriod,
            self.iIncludeHeatEffect,
            self.iConvertDscntIter,
            self.iRamp,
            self.iAcceptByMaxIters,
            '[' + ', '.join(tok.toNativeStr(True) for tok in self.outputRequestParams) +']',) + rightBracket

class LBC_SUBMODEL_FORCED_DISP_DATA:
    def __init__(self,
        iSolver=0,
        strFilePathName="/home/",
        iProcessNo=0,
        bTranslationX=True,
        bTranslationY=True,
        bTranslationZ=True,
        iReferType=-1,
        dExtensionRange=DFLT_DBL,
        dExtensionTol=DFLT_DBL,
        dExtensionLimitTol=DFLT_DBL,
        strGlobalElementSet="",
        iUseBucket=-1,
        iNumBucketMaxX=DFLT_INT,
        iNumBucketMaxY=DFLT_INT,
        iNumBucketMaxZ=DFLT_INT,
        iPrevBc=-1):
        self.iSolver = iSolver
        self.strFilePathName = strFilePathName
        self.iProcessNo = iProcessNo
        self.bTranslationX = bTranslationX
        self.bTranslationY = bTranslationY
        self.bTranslationZ = bTranslationZ
        self.iReferType = iReferType
        self.dExtensionRange = dExtensionRange
        self.dExtensionTol = dExtensionTol
        self.dExtensionLimitTol = dExtensionLimitTol
        self.strGlobalElementSet = strGlobalElementSet
        self.iUseBucket = iUseBucket
        self.iNumBucketMaxX = iNumBucketMaxX
        self.iNumBucketMaxY = iNumBucketMaxY
        self.iNumBucketMaxZ = iNumBucketMaxZ
        self.iPrevBc = iPrevBc
    def isDefault(self):
        obj = LBC_SUBMODEL_FORCED_DISP_DATA()
        return self.iSolver == obj.iSolver and \
            self.strFilePathName == obj.strFilePathName and \
            self.iProcessNo == obj.iProcessNo and \
            self.bTranslationX == obj.bTranslationX and \
            self.bTranslationY == obj.bTranslationY and \
            self.bTranslationZ == obj.bTranslationZ and \
            self.iReferType == obj.iReferType and \
            self.dExtensionRange == obj.dExtensionRange and \
            self.dExtensionTol == obj.dExtensionTol and \
            self.dExtensionLimitTol == obj.dExtensionLimitTol and \
            self.strGlobalElementSet == obj.strGlobalElementSet and \
            self.iUseBucket == obj.iUseBucket and \
            self.iNumBucketMaxX == obj.iNumBucketMaxX and \
            self.iNumBucketMaxY == obj.iNumBucketMaxY and \
            self.iNumBucketMaxZ == obj.iNumBucketMaxZ and \
            self.iPrevBc == obj.iPrevBc
    def fromList(self, param):
        obj = LBC_SUBMODEL_FORCED_DISP_DATA()
        self.iSolver = param[0] if len(param) > 0 else obj.iSolver
        self.strFilePathName = param[1] if len(param) > 1 else obj.strFilePathName
        self.iProcessNo = param[2] if len(param) > 2 else obj.iProcessNo
        self.bTranslationX = getBoolValue(param[3]) if len(param) > 3 else obj.bTranslationX
        self.bTranslationY = getBoolValue(param[4]) if len(param) > 4 else obj.bTranslationY
        self.bTranslationZ = getBoolValue(param[5]) if len(param) > 5 else obj.bTranslationZ
        self.iReferType = param[6] if len(param) > 6 else obj.iReferType
        self.dExtensionRange = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dExtensionRange
        self.dExtensionTol = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dExtensionTol
        self.dExtensionLimitTol = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dExtensionLimitTol
        self.strGlobalElementSet = param[10] if len(param) > 10 else obj.strGlobalElementSet
        self.iUseBucket = param[11] if len(param) > 11 else obj.iUseBucket
        self.iNumBucketMaxX = param[12] if len(param) > 12 else obj.iNumBucketMaxX
        self.iNumBucketMaxY = param[13] if len(param) > 13 else obj.iNumBucketMaxY
        self.iNumBucketMaxZ = param[14] if len(param) > 14 else obj.iNumBucketMaxZ
        self.iPrevBc = param[15] if len(param) > 15 else obj.iPrevBc
        return self
    def __str__(self):
        obj = LBC_SUBMODEL_FORCED_DISP_DATA()
        paramArgs = []
        if self.iSolver != obj.iSolver:
            paramArgs.append('iSolver={0}'.format(getValueStr(self.iSolver)))
        if self.strFilePathName != obj.strFilePathName:
            paramArgs.append('strFilePathName={0}'.format('"' + self.strFilePathName + '"'))
        if self.iProcessNo != obj.iProcessNo:
            paramArgs.append('iProcessNo={0}'.format(getValueStr(self.iProcessNo)))
        if self.bTranslationX != obj.bTranslationX:
            paramArgs.append('bTranslationX={0}'.format(getBoolStr(self.bTranslationX)))
        if self.bTranslationY != obj.bTranslationY:
            paramArgs.append('bTranslationY={0}'.format(getBoolStr(self.bTranslationY)))
        if self.bTranslationZ != obj.bTranslationZ:
            paramArgs.append('bTranslationZ={0}'.format(getBoolStr(self.bTranslationZ)))
        if self.iReferType != obj.iReferType:
            paramArgs.append('iReferType={0}'.format(getValueStr(self.iReferType)))
        if self.dExtensionRange != obj.dExtensionRange:
            paramArgs.append('dExtensionRange={0}'.format(getValueStr(self.dExtensionRange)))
        if self.dExtensionTol != obj.dExtensionTol:
            paramArgs.append('dExtensionTol={0}'.format(getValueStr(self.dExtensionTol)))
        if self.dExtensionLimitTol != obj.dExtensionLimitTol:
            paramArgs.append('dExtensionLimitTol={0}'.format(getValueStr(self.dExtensionLimitTol)))
        if self.strGlobalElementSet != obj.strGlobalElementSet:
            paramArgs.append('strGlobalElementSet={0}'.format('"' + self.strGlobalElementSet + '"'))
        if self.iUseBucket != obj.iUseBucket:
            paramArgs.append('iUseBucket={0}'.format(getValueStr(self.iUseBucket)))
        if self.iNumBucketMaxX != obj.iNumBucketMaxX:
            paramArgs.append('iNumBucketMaxX={0}'.format(getValueStr(self.iNumBucketMaxX)))
        if self.iNumBucketMaxY != obj.iNumBucketMaxY:
            paramArgs.append('iNumBucketMaxY={0}'.format(getValueStr(self.iNumBucketMaxY)))
        if self.iNumBucketMaxZ != obj.iNumBucketMaxZ:
            paramArgs.append('iNumBucketMaxZ={0}'.format(getValueStr(self.iNumBucketMaxZ)))
        if self.iPrevBc != obj.iPrevBc:
            paramArgs.append('iPrevBc={0}'.format(getValueStr(self.iPrevBc)))
        return 'LBC_SUBMODEL_FORCED_DISP_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}'.format(
            self.iSolver,
            '"' + self.strFilePathName + '"',
            self.iProcessNo,
            1 if self.bTranslationX else 0,
            1 if self.bTranslationY else 0,
            1 if self.bTranslationZ else 0,
            self.iReferType,
            self.dExtensionRange,
            self.dExtensionTol,
            self.dExtensionLimitTol,
            '"' + self.strGlobalElementSet + '"',
            self.iUseBucket,
            self.iNumBucketMaxX,
            self.iNumBucketMaxY,
            self.iNumBucketMaxZ,
            self.iPrevBc) + rightBracket

class LBC_PRETENSION_ADVC_DATA:
    def __init__(self,
        bfixedLength=False,
        crEnforcedVelocity=None,
        dvalue=DFLT_DBL,
        dirUpdateType=0,
        vnormal=[DFLT_DBL,DFLT_DBL,DFLT_DBL],
        vCtrolNodePos=[DFLT_DBL,DFLT_DBL,DFLT_DBL],
        refNodeId=0):
        self.bfixedLength = bfixedLength
        self.crEnforcedVelocity = crEnforcedVelocity
        self.dvalue = dvalue
        self.dirUpdateType = dirUpdateType
        self.vnormal = vnormal
        self.vCtrolNodePos = vCtrolNodePos
        self.refNodeId = refNodeId
    def isDefault(self):
        obj = LBC_PRETENSION_ADVC_DATA()
        return self.bfixedLength == obj.bfixedLength and \
            self.crEnforcedVelocity == obj.crEnforcedVelocity and \
            self.dvalue == obj.dvalue and \
            self.dirUpdateType == obj.dirUpdateType and \
            self.vnormal == obj.vnormal and \
            self.vCtrolNodePos == obj.vCtrolNodePos and \
            self.refNodeId == obj.refNodeId
    def fromList(self, param):
        obj = LBC_PRETENSION_ADVC_DATA()
        self.bfixedLength = getBoolValue(param[0]) if len(param) > 0 else obj.bfixedLength
        self.crEnforcedVelocity = getCursorValue(param[1]) if len(param) > 1 else obj.crEnforcedVelocity
        self.dvalue = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dvalue
        self.dirUpdateType = param[3] if len(param) > 3 else obj.dirUpdateType
        self.vnormal = [normalizeDoubleType(tok) for tok in param[4]] if len(param) > 4 else obj.vnormal
        self.vCtrolNodePos = [normalizeDoubleType(tok) for tok in param[5]] if len(param) > 5 else obj.vCtrolNodePos
        self.refNodeId = param[6] if len(param) > 6 else obj.refNodeId
        return self
    def __str__(self):
        obj = LBC_PRETENSION_ADVC_DATA()
        paramArgs = []
        if self.bfixedLength != obj.bfixedLength:
            paramArgs.append('bfixedLength={0}'.format(getBoolStr(self.bfixedLength)))
        if self.crEnforcedVelocity != obj.crEnforcedVelocity:
            paramArgs.append('crEnforcedVelocity={0}'.format(getCursorValueStr(self.crEnforcedVelocity)))
        if self.dvalue != obj.dvalue:
            paramArgs.append('dvalue={0}'.format(getValueStr(self.dvalue)))
        if self.dirUpdateType != obj.dirUpdateType:
            paramArgs.append('dirUpdateType={0}'.format(getValueStr(self.dirUpdateType)))
        if self.vnormal != obj.vnormal:
            paramArgs.append('vnormal={0}'.format(getValueStr(self.vnormal)))
        if self.vCtrolNodePos != obj.vCtrolNodePos:
            paramArgs.append('vCtrolNodePos={0}'.format(getValueStr(self.vCtrolNodePos)))
        if self.refNodeId != obj.refNodeId:
            paramArgs.append('refNodeId={0}'.format(getValueStr(self.refNodeId)))
        return 'LBC_PRETENSION_ADVC_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            1 if self.bfixedLength else 0,
            str(self.crEnforcedVelocity) if self.crEnforcedVelocity is not None else '0:0',
            self.dvalue,
            self.dirUpdateType,
            self.vnormal,
            self.vCtrolNodePos,
            self.refNodeId) + rightBracket

class LBC_PRETENSION_ABAQUS_DATA:
    def __init__(self,
        bFixedLenght=False,
        crTable=None,
        dValue=DFLT_DBL,
        iLocalUnit=0,
        stNormal="",
        NodePos=[DFLT_DBL,DFLT_DBL,DFLT_DBL]):
        self.bFixedLenght = bFixedLenght
        self.crTable = crTable
        self.dValue = dValue
        self.iLocalUnit = iLocalUnit
        self.stNormal = stNormal
        self.NodePos = NodePos
    def isDefault(self):
        obj = LBC_PRETENSION_ABAQUS_DATA()
        return self.bFixedLenght == obj.bFixedLenght and \
            self.crTable == obj.crTable and \
            self.dValue == obj.dValue and \
            self.iLocalUnit == obj.iLocalUnit and \
            self.stNormal == obj.stNormal and \
            self.NodePos == obj.NodePos
    def fromList(self, param):
        obj = LBC_PRETENSION_ABAQUS_DATA()
        self.bFixedLenght = getBoolValue(param[0]) if len(param) > 0 else obj.bFixedLenght
        self.crTable = getCursorValue(param[1]) if len(param) > 1 else obj.crTable
        self.dValue = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dValue
        self.iLocalUnit = param[3] if len(param) > 3 else obj.iLocalUnit
        self.stNormal = param[4] if len(param) > 4 else obj.stNormal
        self.NodePos = [normalizeDoubleType(tok) for tok in param[5]] if len(param) > 5 else obj.NodePos
        return self
    def __str__(self):
        obj = LBC_PRETENSION_ABAQUS_DATA()
        paramArgs = []
        if self.bFixedLenght != obj.bFixedLenght:
            paramArgs.append('bFixedLenght={0}'.format(getBoolStr(self.bFixedLenght)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        if self.dValue != obj.dValue:
            paramArgs.append('dValue={0}'.format(getValueStr(self.dValue)))
        if self.iLocalUnit != obj.iLocalUnit:
            paramArgs.append('iLocalUnit={0}'.format(getValueStr(self.iLocalUnit)))
        if self.stNormal != obj.stNormal:
            paramArgs.append('stNormal={0}'.format('"' + self.stNormal + '"'))
        if self.NodePos != obj.NodePos:
            paramArgs.append('NodePos={0}'.format(getValueStr(self.NodePos)))
        return 'LBC_PRETENSION_ABAQUS_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            1 if self.bFixedLenght else 0,
            str(self.crTable) if self.crTable is not None else '0:0',
            self.dValue,
            self.iLocalUnit,
            '"' + self.stNormal + '"',
            self.NodePos) + rightBracket

class LBC_PRETENSION_DATA:
    def __init__(self,
        iDir=0,
        dValue=DFLT_DBL,
        bFixLength=False,
        crTable=None,
        crCoord=None,
        iLocalUnit=0):
        self.iDir = iDir
        self.dValue = dValue
        self.bFixLength = bFixLength
        self.crTable = crTable
        self.crCoord = crCoord
        self.iLocalUnit = iLocalUnit
    def isDefault(self):
        obj = LBC_PRETENSION_DATA()
        return self.iDir == obj.iDir and \
            self.dValue == obj.dValue and \
            self.bFixLength == obj.bFixLength and \
            self.crTable == obj.crTable and \
            self.crCoord == obj.crCoord and \
            self.iLocalUnit == obj.iLocalUnit
    def fromList(self, param):
        obj = LBC_PRETENSION_DATA()
        self.iDir = param[0] if len(param) > 0 else obj.iDir
        self.dValue = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dValue
        self.bFixLength = getBoolValue(param[2]) if len(param) > 2 else obj.bFixLength
        self.crTable = getCursorValue(param[3]) if len(param) > 3 else obj.crTable
        self.crCoord = getCursorValue(param[4]) if len(param) > 4 else obj.crCoord
        self.iLocalUnit = param[5] if len(param) > 5 else obj.iLocalUnit
        return self
    def __str__(self):
        obj = LBC_PRETENSION_DATA()
        paramArgs = []
        if self.iDir != obj.iDir:
            paramArgs.append('iDir={0}'.format(getValueStr(self.iDir)))
        if self.dValue != obj.dValue:
            paramArgs.append('dValue={0}'.format(getValueStr(self.dValue)))
        if self.bFixLength != obj.bFixLength:
            paramArgs.append('bFixLength={0}'.format(getBoolStr(self.bFixLength)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        if self.iLocalUnit != obj.iLocalUnit:
            paramArgs.append('iLocalUnit={0}'.format(getValueStr(self.iLocalUnit)))
        return 'LBC_PRETENSION_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            self.iDir,
            self.dValue,
            1 if self.bFixLength else 0,
            str(self.crTable) if self.crTable is not None else '0:0',
            str(self.crCoord) if self.crCoord is not None else '0:0',
            self.iLocalUnit) + rightBracket

class LBC_PRESSURE_SINE_DATA:
    def __init__(self,
        a=0.0,
        crCoordinate=None,
        angleRange=0.0,
        distributionAxis=False,
        pressureDirectionMode=0,
        isTotalForceAdjustment=False,
        totalForce=0.0,
        pressureDirection=[0.0,0.0,0.0],
        crCoordinateSystemForDirection=None,
        isCornerNodesDistribution=False,
        formulaForA=""):
        self.a = a
        self.crCoordinate = crCoordinate
        self.angleRange = angleRange
        self.distributionAxis = distributionAxis
        self.pressureDirectionMode = pressureDirectionMode
        self.isTotalForceAdjustment = isTotalForceAdjustment
        self.totalForce = totalForce
        self.pressureDirection = pressureDirection
        self.crCoordinateSystemForDirection = crCoordinateSystemForDirection
        self.isCornerNodesDistribution = isCornerNodesDistribution
        self.formulaForA = formulaForA
    def isDefault(self):
        obj = LBC_PRESSURE_SINE_DATA()
        return self.a == obj.a and \
            self.crCoordinate == obj.crCoordinate and \
            self.angleRange == obj.angleRange and \
            self.distributionAxis == obj.distributionAxis and \
            self.pressureDirectionMode == obj.pressureDirectionMode and \
            self.isTotalForceAdjustment == obj.isTotalForceAdjustment and \
            self.totalForce == obj.totalForce and \
            self.pressureDirection == obj.pressureDirection and \
            self.crCoordinateSystemForDirection == obj.crCoordinateSystemForDirection and \
            self.isCornerNodesDistribution == obj.isCornerNodesDistribution and \
            self.formulaForA == obj.formulaForA
    def fromList(self, param):
        obj = LBC_PRESSURE_SINE_DATA()
        self.a = normalizeDoubleType(param[0]) if len(param) > 0 else obj.a
        self.crCoordinate = getCursorValue(param[1]) if len(param) > 1 else obj.crCoordinate
        self.angleRange = normalizeDoubleType(param[2]) if len(param) > 2 else obj.angleRange
        self.distributionAxis = getBoolValue(param[3]) if len(param) > 3 else obj.distributionAxis
        self.pressureDirectionMode = param[4] if len(param) > 4 else obj.pressureDirectionMode
        self.isTotalForceAdjustment = getBoolValue(param[5]) if len(param) > 5 else obj.isTotalForceAdjustment
        self.totalForce = normalizeDoubleType(param[6]) if len(param) > 6 else obj.totalForce
        self.pressureDirection = [normalizeDoubleType(tok) for tok in param[7]] if len(param) > 7 else obj.pressureDirection
        self.crCoordinateSystemForDirection = getCursorValue(param[8]) if len(param) > 8 else obj.crCoordinateSystemForDirection
        self.isCornerNodesDistribution = getBoolValue(param[9]) if len(param) > 9 else obj.isCornerNodesDistribution
        self.formulaForA = param[10] if len(param) > 10 else obj.formulaForA
        return self
    def __str__(self):
        obj = LBC_PRESSURE_SINE_DATA()
        paramArgs = []
        if self.a != obj.a:
            paramArgs.append('a={0}'.format(getValueStr(self.a)))
        if self.crCoordinate != obj.crCoordinate:
            paramArgs.append('crCoordinate={0}'.format(getCursorValueStr(self.crCoordinate)))
        if self.angleRange != obj.angleRange:
            paramArgs.append('angleRange={0}'.format(getValueStr(self.angleRange)))
        if self.distributionAxis != obj.distributionAxis:
            paramArgs.append('distributionAxis={0}'.format(getBoolStr(self.distributionAxis)))
        if self.pressureDirectionMode != obj.pressureDirectionMode:
            paramArgs.append('pressureDirectionMode={0}'.format(getValueStr(self.pressureDirectionMode)))
        if self.isTotalForceAdjustment != obj.isTotalForceAdjustment:
            paramArgs.append('isTotalForceAdjustment={0}'.format(getBoolStr(self.isTotalForceAdjustment)))
        if self.totalForce != obj.totalForce:
            paramArgs.append('totalForce={0}'.format(getValueStr(self.totalForce)))
        if self.pressureDirection != obj.pressureDirection:
            paramArgs.append('pressureDirection={0}'.format(getValueStr(self.pressureDirection)))
        if self.crCoordinateSystemForDirection != obj.crCoordinateSystemForDirection:
            paramArgs.append('crCoordinateSystemForDirection={0}'.format(getCursorValueStr(self.crCoordinateSystemForDirection)))
        if self.isCornerNodesDistribution != obj.isCornerNodesDistribution:
            paramArgs.append('isCornerNodesDistribution={0}'.format(getBoolStr(self.isCornerNodesDistribution)))
        if self.formulaForA != obj.formulaForA:
            paramArgs.append('formulaForA={0}'.format('"' + self.formulaForA + '"'))
        return 'LBC_PRESSURE_SINE_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(
            self.a,
            str(self.crCoordinate) if self.crCoordinate is not None else '0:0',
            self.angleRange,
            1 if self.distributionAxis else 0,
            self.pressureDirectionMode,
            1 if self.isTotalForceAdjustment else 0,
            self.totalForce,
            self.pressureDirection,
            str(self.crCoordinateSystemForDirection) if self.crCoordinateSystemForDirection is not None else '0:0',
            1 if self.isCornerNodesDistribution else 0,
            '"' + self.formulaForA + '"') + rightBracket

class LBC_NOLIN1_DATA:
    def __init__(self,
        dForceScale=0.0,
        dMomentScale=0.0,
        iForcDir=0,
        iForceDepends=0,
        iMomentDir=0,
        iMomentDepends=0,
        crCoord=None,
        crForceTable=None,
        crMomentTable=None):
        self.dForceScale = dForceScale
        self.dMomentScale = dMomentScale
        self.iForcDir = iForcDir
        self.iForceDepends = iForceDepends
        self.iMomentDir = iMomentDir
        self.iMomentDepends = iMomentDepends
        self.crCoord = crCoord
        self.crForceTable = crForceTable
        self.crMomentTable = crMomentTable
    def isDefault(self):
        obj = LBC_NOLIN1_DATA()
        return self.dForceScale == obj.dForceScale and \
            self.dMomentScale == obj.dMomentScale and \
            self.iForcDir == obj.iForcDir and \
            self.iForceDepends == obj.iForceDepends and \
            self.iMomentDir == obj.iMomentDir and \
            self.iMomentDepends == obj.iMomentDepends and \
            self.crCoord == obj.crCoord and \
            self.crForceTable == obj.crForceTable and \
            self.crMomentTable == obj.crMomentTable
    def fromList(self, param):
        obj = LBC_NOLIN1_DATA()
        self.dForceScale = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dForceScale
        self.dMomentScale = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dMomentScale
        self.iForcDir = param[2] if len(param) > 2 else obj.iForcDir
        self.iForceDepends = param[3] if len(param) > 3 else obj.iForceDepends
        self.iMomentDir = param[4] if len(param) > 4 else obj.iMomentDir
        self.iMomentDepends = param[5] if len(param) > 5 else obj.iMomentDepends
        self.crCoord = getCursorValue(param[6]) if len(param) > 6 else obj.crCoord
        self.crForceTable = getCursorValue(param[7]) if len(param) > 7 else obj.crForceTable
        self.crMomentTable = getCursorValue(param[8]) if len(param) > 8 else obj.crMomentTable
        return self
    def __str__(self):
        obj = LBC_NOLIN1_DATA()
        paramArgs = []
        if self.dForceScale != obj.dForceScale:
            paramArgs.append('dForceScale={0}'.format(getValueStr(self.dForceScale)))
        if self.dMomentScale != obj.dMomentScale:
            paramArgs.append('dMomentScale={0}'.format(getValueStr(self.dMomentScale)))
        if self.iForcDir != obj.iForcDir:
            paramArgs.append('iForcDir={0}'.format(getValueStr(self.iForcDir)))
        if self.iForceDepends != obj.iForceDepends:
            paramArgs.append('iForceDepends={0}'.format(getValueStr(self.iForceDepends)))
        if self.iMomentDir != obj.iMomentDir:
            paramArgs.append('iMomentDir={0}'.format(getValueStr(self.iMomentDir)))
        if self.iMomentDepends != obj.iMomentDepends:
            paramArgs.append('iMomentDepends={0}'.format(getValueStr(self.iMomentDepends)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        if self.crForceTable != obj.crForceTable:
            paramArgs.append('crForceTable={0}'.format(getCursorValueStr(self.crForceTable)))
        if self.crMomentTable != obj.crMomentTable:
            paramArgs.append('crMomentTable={0}'.format(getCursorValueStr(self.crMomentTable)))
        return 'LBC_NOLIN1_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            self.dForceScale,
            self.dMomentScale,
            self.iForcDir,
            self.iForceDepends,
            self.iMomentDir,
            self.iMomentDepends,
            str(self.crCoord) if self.crCoord is not None else '0:0',
            str(self.crForceTable) if self.crForceTable is not None else '0:0',
            str(self.crMomentTable) if self.crMomentTable is not None else '0:0') + rightBracket

class LBC_INSIDE_HEAT_GENERATION_DATA:
    def __init__(self,
        dInsideFlux=DFLT_DBL,
        crTable=None):
        self.dInsideFlux = dInsideFlux
        self.crTable = crTable
    def isDefault(self):
        obj = LBC_INSIDE_HEAT_GENERATION_DATA()
        return self.dInsideFlux == obj.dInsideFlux and \
            self.crTable == obj.crTable
    def fromList(self, param):
        obj = LBC_INSIDE_HEAT_GENERATION_DATA()
        self.dInsideFlux = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dInsideFlux
        self.crTable = getCursorValue(param[1]) if len(param) > 1 else obj.crTable
        return self
    def __str__(self):
        obj = LBC_INSIDE_HEAT_GENERATION_DATA()
        paramArgs = []
        if self.dInsideFlux != obj.dInsideFlux:
            paramArgs.append('dInsideFlux={0}'.format(getValueStr(self.dInsideFlux)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        return 'LBC_INSIDE_HEAT_GENERATION_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            self.dInsideFlux,
            str(self.crTable) if self.crTable is not None else '0:0') + rightBracket

class LBC_INITSTRESS_GENERAL_DATA:
    def __init__(self,
        dimension=2,
        elemCs=0,
        sXX=DFLT_DBL,
        sYY=DFLT_DBL,
        sXY=DFLT_DBL,
        crTable=None):
        self.dimension = dimension
        self.elemCs = elemCs
        self.sXX = sXX
        self.sYY = sYY
        self.sXY = sXY
        self.crTable = crTable
    def isDefault(self):
        obj = LBC_INITSTRESS_GENERAL_DATA()
        return self.dimension == obj.dimension and \
            self.elemCs == obj.elemCs and \
            self.sXX == obj.sXX and \
            self.sYY == obj.sYY and \
            self.sXY == obj.sXY and \
            self.crTable == obj.crTable
    def fromList(self, param):
        obj = LBC_INITSTRESS_GENERAL_DATA()
        self.dimension = param[0] if len(param) > 0 else obj.dimension
        self.elemCs = param[1] if len(param) > 1 else obj.elemCs
        self.sXX = normalizeDoubleType(param[2]) if len(param) > 2 else obj.sXX
        self.sYY = normalizeDoubleType(param[3]) if len(param) > 3 else obj.sYY
        self.sXY = normalizeDoubleType(param[4]) if len(param) > 4 else obj.sXY
        self.crTable = getCursorValue(param[5]) if len(param) > 5 else obj.crTable
        return self
    def __str__(self):
        obj = LBC_INITSTRESS_GENERAL_DATA()
        paramArgs = []
        if self.dimension != obj.dimension:
            paramArgs.append('dimension={0}'.format(getValueStr(self.dimension)))
        if self.elemCs != obj.elemCs:
            paramArgs.append('elemCs={0}'.format(getValueStr(self.elemCs)))
        if self.sXX != obj.sXX:
            paramArgs.append('sXX={0}'.format(getValueStr(self.sXX)))
        if self.sYY != obj.sYY:
            paramArgs.append('sYY={0}'.format(getValueStr(self.sYY)))
        if self.sXY != obj.sXY:
            paramArgs.append('sXY={0}'.format(getValueStr(self.sXY)))             
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        return 'LBC_INITSTRESS_GENERAL_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            self.dimension,
            self.elemCs,
            self.sXX,
            self.sYY,
            self.sXY,
            str(self.crTable) if self.crTable is not None else '0:0') + rightBracket
class LBC_INITIAL_ROTVEL_ABAQUS_DATA:
    def __init__(self,
        dVelocity=DFLT_DBL,
        strFirstCoord="",
        strSecondCoord=""):
        self.dVelocity = dVelocity
        self.strFirstCoord = strFirstCoord
        self.strSecondCoord = strSecondCoord
    def isDefault(self):
        obj = LBC_INITIAL_ROTVEL_ABAQUS_DATA()
        return self.dVelocity == obj.dVelocity and \
            self.strFirstCoord == obj.strFirstCoord and \
            self.strSecondCoord == obj.strSecondCoord
    def fromList(self, param):
        obj = LBC_INITIAL_ROTVEL_ABAQUS_DATA()
        self.dVelocity = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dVelocity
        self.strFirstCoord = param[1] if len(param) > 1 else obj.strFirstCoord
        self.strSecondCoord = param[2] if len(param) > 2 else obj.strSecondCoord
        return self
    def __str__(self):
        obj = LBC_INITIAL_ROTVEL_ABAQUS_DATA()
        paramArgs = []
        if self.dVelocity != obj.dVelocity:
            paramArgs.append('dVelocity={0}'.format(getValueStr(self.dVelocity)))
        if self.strFirstCoord != obj.strFirstCoord:
            paramArgs.append('strFirstCoord={0}'.format('"' + self.strFirstCoord + '"'))
        if self.strSecondCoord != obj.strSecondCoord:
            paramArgs.append('strSecondCoord={0}'.format('"' + self.strSecondCoord + '"'))
        return 'LBC_INITIAL_ROTVEL_ABAQUS_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.dVelocity,
            '"' + self.strFirstCoord + '"',
            '"' + self.strSecondCoord + '"') + rightBracket

class LBC_PRESSURE_G_DATA:
    def __init__(self,
        fpressure=0.0,
        idistribute=0,
        crtable=None,
        dphase=0.0,
        ddelay=0.0,
        crphaseTable=None,
        strformularValue="",
        crcoord=None,
        vdirection=[DFLT_DBL,DFLT_DBL,DFLT_DBL],
        formularDirX="",
        formularDirY="",
        formularDirZ="",
        arrowDir=1):
        self.fpressure = fpressure
        self.idistribute = idistribute
        self.crtable = crtable
        self.dphase = dphase
        self.ddelay = ddelay
        self.crphaseTable = crphaseTable
        self.strformularValue = strformularValue
        self.crcoord = crcoord
        self.vdirection = vdirection
        self.formularDirX = formularDirX
        self.formularDirY = formularDirY
        self.formularDirZ = formularDirZ
        self.arrowDir = arrowDir
    def isDefault(self):
        obj = LBC_PRESSURE_G_DATA()
        return self.fpressure == obj.fpressure and \
            self.idistribute == obj.idistribute and \
            self.crtable == obj.crtable and \
            self.dphase == obj.dphase and \
            self.ddelay == obj.ddelay and \
            self.crphaseTable == obj.crphaseTable and \
            self.strformularValue == obj.strformularValue and \
            self.crcoord == obj.crcoord and \
            self.vdirection == obj.vdirection and \
            self.formularDirX == obj.formularDirX and \
            self.formularDirY == obj.formularDirY and \
            self.formularDirZ == obj.formularDirZ and \
            self.arrowDir == obj.arrowDir
    def fromList(self, param):
        obj = LBC_PRESSURE_G_DATA()
        self.fpressure = normalizeDoubleType(param[0]) if len(param) > 0 else obj.fpressure
        self.idistribute = param[1] if len(param) > 1 else obj.idistribute
        self.crtable = getCursorValue(param[2]) if len(param) > 2 else obj.crtable
        self.dphase = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dphase
        self.ddelay = normalizeDoubleType(param[4]) if len(param) > 4 else obj.ddelay
        self.crphaseTable = getCursorValue(param[5]) if len(param) > 5 else obj.crphaseTable
        self.strformularValue = param[6] if len(param) > 6 else obj.strformularValue
        self.crcoord = getCursorValue(param[7]) if len(param) > 7 else obj.crcoord
        self.vdirection = [normalizeDoubleType(tok) for tok in param[8]] if len(param) > 8 else obj.vdirection
        self.formularDirX = param[9] if len(param) > 9 else obj.formularDirX
        self.formularDirY = param[10] if len(param) > 10 else obj.formularDirY
        self.formularDirZ = param[11] if len(param) > 11 else obj.formularDirZ
        self.arrowDir = param[12] if len(param) > 12 else obj.arrowDir
        return self
    def __str__(self):
        obj = LBC_PRESSURE_G_DATA()
        paramArgs = []
        if self.fpressure != obj.fpressure:
            paramArgs.append('fpressure={0}'.format(getValueStr(self.fpressure)))
        if self.idistribute != obj.idistribute:
            paramArgs.append('idistribute={0}'.format(getValueStr(self.idistribute)))
        if self.crtable != obj.crtable:
            paramArgs.append('crtable={0}'.format(getCursorValueStr(self.crtable)))
        if self.dphase != obj.dphase:
            paramArgs.append('dphase={0}'.format(getValueStr(self.dphase)))
        if self.ddelay != obj.ddelay:
            paramArgs.append('ddelay={0}'.format(getValueStr(self.ddelay)))
        if self.crphaseTable != obj.crphaseTable:
            paramArgs.append('crphaseTable={0}'.format(getCursorValueStr(self.crphaseTable)))
        if self.strformularValue != obj.strformularValue:
            paramArgs.append('strformularValue={0}'.format('"' + self.strformularValue + '"'))
        if self.crcoord != obj.crcoord:
            paramArgs.append('crcoord={0}'.format(getCursorValueStr(self.crcoord)))
        if self.vdirection != obj.vdirection:
            paramArgs.append('vdirection={0}'.format(getValueStr(self.vdirection)))
        if self.formularDirX != obj.formularDirX:
            paramArgs.append('formularDirX={0}'.format('"' + self.formularDirX + '"'))
        if self.formularDirY != obj.formularDirY:
            paramArgs.append('formularDirY={0}'.format('"' + self.formularDirY + '"'))
        if self.formularDirZ != obj.formularDirZ:
            paramArgs.append('formularDirZ={0}'.format('"' + self.formularDirZ + '"'))
        if self.arrowDir != obj.arrowDir:
            paramArgs.append('arrowDir={0}'.format(getValueStr(self.arrowDir)))
        return 'LBC_PRESSURE_G_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}'.format(
            self.fpressure,
            self.idistribute,
            str(self.crtable) if self.crtable is not None else '0:0',
            self.dphase,
            self.ddelay,
            str(self.crphaseTable) if self.crphaseTable is not None else '0:0',
            '"' + self.strformularValue + '"',
            str(self.crcoord) if self.crcoord is not None else '0:0',
            self.vdirection,
            '"' + self.formularDirX + '"',
            '"' + self.formularDirY + '"',
            '"' + self.formularDirZ + '"',
            self.arrowDir) + rightBracket

class LBC_PRESSURE_H_DATA:
    def __init__(self,
        fHPressure=0.0,
        fDensity=0.0,
        iDensityUnit=0,
        fGravity=0.0,
        iGravityUnit=0,
        iGravityDir=0,
        fWaterSuface=0.0,
        iSufaceUnit=0,
        enDistrbute=0):
        self.fHPressure = fHPressure
        self.fDensity = fDensity
        self.iDensityUnit = iDensityUnit
        self.fGravity = fGravity
        self.iGravityUnit = iGravityUnit
        self.iGravityDir = iGravityDir
        self.fWaterSuface = fWaterSuface
        self.iSufaceUnit = iSufaceUnit
        self.enDistrbute = enDistrbute
    def isDefault(self):
        obj = LBC_PRESSURE_H_DATA()
        return self.fHPressure == obj.fHPressure and \
            self.fDensity == obj.fDensity and \
            self.iDensityUnit == obj.iDensityUnit and \
            self.fGravity == obj.fGravity and \
            self.iGravityUnit == obj.iGravityUnit and \
            self.iGravityDir == obj.iGravityDir and \
            self.fWaterSuface == obj.fWaterSuface and \
            self.iSufaceUnit == obj.iSufaceUnit and \
            self.enDistrbute == obj.enDistrbute
    def fromList(self, param):
        obj = LBC_PRESSURE_H_DATA()
        self.fHPressure = normalizeDoubleType(param[0]) if len(param) > 0 else obj.fHPressure
        self.fDensity = normalizeDoubleType(param[1]) if len(param) > 1 else obj.fDensity
        self.iDensityUnit = param[2] if len(param) > 2 else obj.iDensityUnit
        self.fGravity = normalizeDoubleType(param[3]) if len(param) > 3 else obj.fGravity
        self.iGravityUnit = param[4] if len(param) > 4 else obj.iGravityUnit
        self.iGravityDir = param[5] if len(param) > 5 else obj.iGravityDir
        self.fWaterSuface = normalizeDoubleType(param[6]) if len(param) > 6 else obj.fWaterSuface
        self.iSufaceUnit = param[7] if len(param) > 7 else obj.iSufaceUnit
        self.enDistrbute = param[8] if len(param) > 8 else obj.enDistrbute
        return self
    def __str__(self):
        obj = LBC_PRESSURE_H_DATA()
        paramArgs = []
        if self.fHPressure != obj.fHPressure:
            paramArgs.append('fHPressure={0}'.format(getValueStr(self.fHPressure)))
        if self.fDensity != obj.fDensity:
            paramArgs.append('fDensity={0}'.format(getValueStr(self.fDensity)))
        if self.iDensityUnit != obj.iDensityUnit:
            paramArgs.append('iDensityUnit={0}'.format(getValueStr(self.iDensityUnit)))
        if self.fGravity != obj.fGravity:
            paramArgs.append('fGravity={0}'.format(getValueStr(self.fGravity)))
        if self.iGravityUnit != obj.iGravityUnit:
            paramArgs.append('iGravityUnit={0}'.format(getValueStr(self.iGravityUnit)))
        if self.iGravityDir != obj.iGravityDir:
            paramArgs.append('iGravityDir={0}'.format(getValueStr(self.iGravityDir)))
        if self.fWaterSuface != obj.fWaterSuface:
            paramArgs.append('fWaterSuface={0}'.format(getValueStr(self.fWaterSuface)))
        if self.iSufaceUnit != obj.iSufaceUnit:
            paramArgs.append('iSufaceUnit={0}'.format(getValueStr(self.iSufaceUnit)))
        if self.enDistrbute != obj.enDistrbute:
            paramArgs.append('enDistrbute={0}'.format(getValueStr(self.enDistrbute)))
        return 'LBC_PRESSURE_H_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            self.fHPressure,
            self.fDensity,
            self.iDensityUnit,
            self.fGravity,
            self.iGravityUnit,
            self.iGravityDir,
            self.fWaterSuface,
            self.iSufaceUnit,
            self.enDistrbute) + rightBracket

class LBC_FORCE_VECTOR_DATA:
    def __init__(self,
        fTotalForce=DFLT_DBL,
        a=DFLT_DBL,
        x=DFLT_DBL,
        y=DFLT_DBL,
        crCoord=None,
        enDirection=0,
        angleRange=0.0,
        arrowDir=0,
        bdistributeInAxis=False):
        self.fTotalForce = fTotalForce
        self.a = a
        self.x = x
        self.y = y
        self.crCoord = crCoord
        self.enDirection = enDirection
        self.angleRange = angleRange
        self.arrowDir = arrowDir
        self.bdistributeInAxis = bdistributeInAxis
    def isDefault(self):
        obj = LBC_FORCE_VECTOR_DATA()
        return self.fTotalForce == obj.fTotalForce and \
            self.a == obj.a and \
            self.x == obj.x and \
            self.y == obj.y and \
            self.crCoord == obj.crCoord and \
            self.enDirection == obj.enDirection and \
            self.angleRange == obj.angleRange and \
            self.arrowDir == obj.arrowDir and \
            self.bdistributeInAxis == obj.bdistributeInAxis
    def fromList(self, param):
        obj = LBC_FORCE_VECTOR_DATA()
        self.fTotalForce = normalizeDoubleType(param[0]) if len(param) > 0 else obj.fTotalForce
        self.a = normalizeDoubleType(param[1]) if len(param) > 1 else obj.a
        self.x = normalizeDoubleType(param[2]) if len(param) > 2 else obj.x
        self.y = normalizeDoubleType(param[3]) if len(param) > 3 else obj.y
        self.crCoord = getCursorValue(param[4]) if len(param) > 4 else obj.crCoord
        self.enDirection = param[5] if len(param) > 5 else obj.enDirection
        self.angleRange = normalizeDoubleType(param[6]) if len(param) > 6 else obj.angleRange
        self.arrowDir = param[7] if len(param) > 7 else obj.arrowDir
        self.bdistributeInAxis = getBoolValue(param[8]) if len(param) > 8 else obj.bdistributeInAxis
        return self
    def __str__(self):
        obj = LBC_FORCE_VECTOR_DATA()
        paramArgs = []
        if self.fTotalForce != obj.fTotalForce:
            paramArgs.append('fTotalForce={0}'.format(getValueStr(self.fTotalForce)))
        if self.a != obj.a:
            paramArgs.append('a={0}'.format(getValueStr(self.a)))
        if self.x != obj.x:
            paramArgs.append('x={0}'.format(getValueStr(self.x)))
        if self.y != obj.y:
            paramArgs.append('y={0}'.format(getValueStr(self.y)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        if self.enDirection != obj.enDirection:
            paramArgs.append('enDirection={0}'.format(getValueStr(self.enDirection)))
        if self.angleRange != obj.angleRange:
            paramArgs.append('angleRange={0}'.format(getValueStr(self.angleRange)))
        if self.arrowDir != obj.arrowDir:
            paramArgs.append('arrowDir={0}'.format(getValueStr(self.arrowDir)))
        if self.bdistributeInAxis != obj.bdistributeInAxis:
            paramArgs.append('bdistributeInAxis={0}'.format(getBoolStr(self.bdistributeInAxis)))
        return 'LBC_FORCE_VECTOR_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            self.fTotalForce,
            self.a,
            self.x,
            self.y,
            str(self.crCoord) if self.crCoord is not None else '0:0',
            self.enDirection,
            self.angleRange,
            self.arrowDir,
            1 if self.bdistributeInAxis else 0) + rightBracket

class LBC_FORCE_QUADRATIC_DATA:
    def __init__(self,
        fTotalForce=0.0,
        a=0.0,
        b=0.0,
        crCoord=None,
        angleBase=0,
        angleRange=0.0,
        enArrowDir=0):
        self.fTotalForce = fTotalForce
        self.a = a
        self.b = b
        self.crCoord = crCoord
        self.angleBase = angleBase
        self.angleRange = angleRange
        self.enArrowDir = enArrowDir
    def isDefault(self):
        obj = LBC_FORCE_QUADRATIC_DATA()
        return self.fTotalForce == obj.fTotalForce and \
            self.a == obj.a and \
            self.b == obj.b and \
            self.crCoord == obj.crCoord and \
            self.angleBase == obj.angleBase and \
            self.angleRange == obj.angleRange and \
            self.enArrowDir == obj.enArrowDir
    def fromList(self, param):
        obj = LBC_FORCE_QUADRATIC_DATA()
        self.fTotalForce = normalizeDoubleType(param[0]) if len(param) > 0 else obj.fTotalForce
        self.a = normalizeDoubleType(param[1]) if len(param) > 1 else obj.a
        self.b = normalizeDoubleType(param[2]) if len(param) > 2 else obj.b
        self.crCoord = getCursorValue(param[3]) if len(param) > 3 else obj.crCoord
        self.angleBase = param[4] if len(param) > 4 else obj.angleBase
        self.angleRange = normalizeDoubleType(param[5]) if len(param) > 5 else obj.angleRange
        self.enArrowDir = param[6] if len(param) > 6 else obj.enArrowDir
        return self
    def __str__(self):
        obj = LBC_FORCE_QUADRATIC_DATA()
        paramArgs = []
        if self.fTotalForce != obj.fTotalForce:
            paramArgs.append('fTotalForce={0}'.format(getValueStr(self.fTotalForce)))
        if self.a != obj.a:
            paramArgs.append('a={0}'.format(getValueStr(self.a)))
        if self.b != obj.b:
            paramArgs.append('b={0}'.format(getValueStr(self.b)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        if self.angleBase != obj.angleBase:
            paramArgs.append('angleBase={0}'.format(getValueStr(self.angleBase)))
        if self.angleRange != obj.angleRange:
            paramArgs.append('angleRange={0}'.format(getValueStr(self.angleRange)))
        if self.enArrowDir != obj.enArrowDir:
            paramArgs.append('enArrowDir={0}'.format(getValueStr(self.enArrowDir)))
        return 'LBC_FORCE_QUADRATIC_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            self.fTotalForce,
            self.a,
            self.b,
            str(self.crCoord) if self.crCoord is not None else '0:0',
            self.angleBase,
            self.angleRange,
            self.enArrowDir) + rightBracket

class LBC_FORCE_SINE_DATA:
    def __init__(self,
        fTotalForce=0.0,
        a=0.0,
        crCoord=None,
        angleBase=0,
        angleRange=0.0,
        enArrowDir=0,
        bdistributeInAxis=False):
        self.fTotalForce = fTotalForce
        self.a = a
        self.crCoord = crCoord
        self.angleBase = angleBase
        self.angleRange = angleRange
        self.enArrowDir = enArrowDir
        self.bdistributeInAxis = bdistributeInAxis
    def isDefault(self):
        obj = LBC_FORCE_SINE_DATA()
        return self.fTotalForce == obj.fTotalForce and \
            self.a == obj.a and \
            self.crCoord == obj.crCoord and \
            self.angleBase == obj.angleBase and \
            self.angleRange == obj.angleRange and \
            self.enArrowDir == obj.enArrowDir and \
            self.bdistributeInAxis == obj.bdistributeInAxis
    def fromList(self, param):
        obj = LBC_FORCE_SINE_DATA()
        self.fTotalForce = normalizeDoubleType(param[0]) if len(param) > 0 else obj.fTotalForce
        self.a = normalizeDoubleType(param[1]) if len(param) > 1 else obj.a
        self.crCoord = getCursorValue(param[2]) if len(param) > 2 else obj.crCoord
        self.angleBase = param[3] if len(param) > 3 else obj.angleBase
        self.angleRange = normalizeDoubleType(param[4]) if len(param) > 4 else obj.angleRange
        self.enArrowDir = param[5] if len(param) > 5 else obj.enArrowDir
        self.bdistributeInAxis = getBoolValue(param[6]) if len(param) > 6 else obj.bdistributeInAxis
        return self
    def __str__(self):
        obj = LBC_FORCE_SINE_DATA()
        paramArgs = []
        if self.fTotalForce != obj.fTotalForce:
            paramArgs.append('fTotalForce={0}'.format(getValueStr(self.fTotalForce)))
        if self.a != obj.a:
            paramArgs.append('a={0}'.format(getValueStr(self.a)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        if self.angleBase != obj.angleBase:
            paramArgs.append('angleBase={0}'.format(getValueStr(self.angleBase)))
        if self.angleRange != obj.angleRange:
            paramArgs.append('angleRange={0}'.format(getValueStr(self.angleRange)))
        if self.enArrowDir != obj.enArrowDir:
            paramArgs.append('enArrowDir={0}'.format(getValueStr(self.enArrowDir)))
        if self.bdistributeInAxis != obj.bdistributeInAxis:
            paramArgs.append('bdistributeInAxis={0}'.format(getBoolStr(self.bdistributeInAxis)))
        return 'LBC_FORCE_SINE_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            self.fTotalForce,
            self.a,
            str(self.crCoord) if self.crCoord is not None else '0:0',
            self.angleBase,
            self.angleRange,
            self.enArrowDir,
            1 if self.bdistributeInAxis else 0) + rightBracket

class LBC_RIGIDWALL_DATA:
    def __init__(self,
        m_nObject=0,
        m_nType=0,
        m_nMotion=0,
        m_nFriction=0,
        m_nOrtho=0,
        m_nForces=0,
        m_Finite=[DFLT_DBL,DFLT_DBL],
        m_MotionMass=DFLT_DBL,
        m_MotionInitVelo=DFLT_DBL,
        m_FricCoulombCoeff=DFLT_DBL,
        m_FricWeldVelo=DFLT_DBL,
        m_ForcesCirclesNum=0,
        m_OrthoStaticCoeff=[DFLT_DBL,DFLT_DBL],
        m_OrthoDynamicCoeff=[DFLT_DBL,DFLT_DBL],
        m_OrthoDecayConst=[DFLT_DBL,DFLT_DBL],
        m_OrthoFricVector=[DFLT_DBL,DFLT_DBL,DFLT_DBL],
        m_bAllNodeSlave=False,
        crCoord=None,
        crAreaFaceSet=None,
        crVisualNodeSet=None):
        self.m_nObject = m_nObject
        self.m_nType = m_nType
        self.m_nMotion = m_nMotion
        self.m_nFriction = m_nFriction
        self.m_nOrtho = m_nOrtho
        self.m_nForces = m_nForces
        self.m_Finite = m_Finite
        self.m_MotionMass = m_MotionMass
        self.m_MotionInitVelo = m_MotionInitVelo
        self.m_FricCoulombCoeff = m_FricCoulombCoeff
        self.m_FricWeldVelo = m_FricWeldVelo
        self.m_ForcesCirclesNum = m_ForcesCirclesNum
        self.m_OrthoStaticCoeff = m_OrthoStaticCoeff
        self.m_OrthoDynamicCoeff = m_OrthoDynamicCoeff
        self.m_OrthoDecayConst = m_OrthoDecayConst
        self.m_OrthoFricVector = m_OrthoFricVector
        self.m_bAllNodeSlave = m_bAllNodeSlave
        self.crCoord = crCoord
        self.crAreaFaceSet = crAreaFaceSet
        self.crVisualNodeSet = crVisualNodeSet
    def isDefault(self):
        obj = LBC_RIGIDWALL_DATA()
        return self.m_nObject == obj.m_nObject and \
            self.m_nType == obj.m_nType and \
            self.m_nMotion == obj.m_nMotion and \
            self.m_nFriction == obj.m_nFriction and \
            self.m_nOrtho == obj.m_nOrtho and \
            self.m_nForces == obj.m_nForces and \
            self.m_Finite == obj.m_Finite and \
            self.m_MotionMass == obj.m_MotionMass and \
            self.m_MotionInitVelo == obj.m_MotionInitVelo and \
            self.m_FricCoulombCoeff == obj.m_FricCoulombCoeff and \
            self.m_FricWeldVelo == obj.m_FricWeldVelo and \
            self.m_ForcesCirclesNum == obj.m_ForcesCirclesNum and \
            self.m_OrthoStaticCoeff == obj.m_OrthoStaticCoeff and \
            self.m_OrthoDynamicCoeff == obj.m_OrthoDynamicCoeff and \
            self.m_OrthoDecayConst == obj.m_OrthoDecayConst and \
            self.m_OrthoFricVector == obj.m_OrthoFricVector and \
            self.m_bAllNodeSlave == obj.m_bAllNodeSlave and \
            self.crCoord == obj.crCoord and \
            self.crAreaFaceSet == obj.crAreaFaceSet and \
            self.crVisualNodeSet == obj.crVisualNodeSet
    def fromList(self, param):
        obj = LBC_RIGIDWALL_DATA()
        self.m_nObject = param[0] if len(param) > 0 else obj.m_nObject
        self.m_nType = param[1] if len(param) > 1 else obj.m_nType
        self.m_nMotion = param[2] if len(param) > 2 else obj.m_nMotion
        self.m_nFriction = param[3] if len(param) > 3 else obj.m_nFriction
        self.m_nOrtho = param[4] if len(param) > 4 else obj.m_nOrtho
        self.m_nForces = param[5] if len(param) > 5 else obj.m_nForces
        self.m_Finite = [normalizeDoubleType(tok) for tok in param[6]] if len(param) > 6 else obj.m_Finite
        self.m_MotionMass = normalizeDoubleType(param[7]) if len(param) > 7 else obj.m_MotionMass
        self.m_MotionInitVelo = normalizeDoubleType(param[8]) if len(param) > 8 else obj.m_MotionInitVelo
        self.m_FricCoulombCoeff = normalizeDoubleType(param[9]) if len(param) > 9 else obj.m_FricCoulombCoeff
        self.m_FricWeldVelo = normalizeDoubleType(param[10]) if len(param) > 10 else obj.m_FricWeldVelo
        self.m_ForcesCirclesNum = normalizeDoubleType(param[11]) if len(param) > 11 else obj.m_ForcesCirclesNum
        self.m_OrthoStaticCoeff = [normalizeDoubleType(tok) for tok in param[12]] if len(param) > 12 else obj.m_OrthoStaticCoeff
        self.m_OrthoDynamicCoeff = [normalizeDoubleType(tok) for tok in param[13]] if len(param) > 13 else obj.m_OrthoDynamicCoeff
        self.m_OrthoDecayConst = [normalizeDoubleType(tok) for tok in param[14]] if len(param) > 14 else obj.m_OrthoDecayConst
        self.m_OrthoFricVector = [normalizeDoubleType(tok) for tok in param[15]] if len(param) > 15 else obj.m_OrthoFricVector
        self.m_bAllNodeSlave = getBoolValue(param[16]) if len(param) > 16 else obj.m_bAllNodeSlave
        self.crCoord = getCursorValue(param[17]) if len(param) > 17 else obj.crCoord
        self.crAreaFaceSet = getCursorValue(param[18]) if len(param) > 18 else obj.crAreaFaceSet
        self.crVisualNodeSet = getCursorValue(param[19]) if len(param) > 19 else obj.crVisualNodeSet
        return self
    def __str__(self):
        obj = LBC_RIGIDWALL_DATA()
        paramArgs = []
        if self.m_nObject != obj.m_nObject:
            paramArgs.append('m_nObject={0}'.format(getValueStr(self.m_nObject)))
        if self.m_nType != obj.m_nType:
            paramArgs.append('m_nType={0}'.format(getValueStr(self.m_nType)))
        if self.m_nMotion != obj.m_nMotion:
            paramArgs.append('m_nMotion={0}'.format(getValueStr(self.m_nMotion)))
        if self.m_nFriction != obj.m_nFriction:
            paramArgs.append('m_nFriction={0}'.format(getValueStr(self.m_nFriction)))
        if self.m_nOrtho != obj.m_nOrtho:
            paramArgs.append('m_nOrtho={0}'.format(getValueStr(self.m_nOrtho)))
        if self.m_nForces != obj.m_nForces:
            paramArgs.append('m_nForces={0}'.format(getValueStr(self.m_nForces)))
        if self.m_Finite != obj.m_Finite:
            paramArgs.append('m_Finite={0}'.format(getValueStr(self.m_Finite)))
        if self.m_MotionMass != obj.m_MotionMass:
            paramArgs.append('m_MotionMass={0}'.format(getValueStr(self.m_MotionMass)))
        if self.m_MotionInitVelo != obj.m_MotionInitVelo:
            paramArgs.append('m_MotionInitVelo={0}'.format(getValueStr(self.m_MotionInitVelo)))
        if self.m_FricCoulombCoeff != obj.m_FricCoulombCoeff:
            paramArgs.append('m_FricCoulombCoeff={0}'.format(getValueStr(self.m_FricCoulombCoeff)))
        if self.m_FricWeldVelo != obj.m_FricWeldVelo:
            paramArgs.append('m_FricWeldVelo={0}'.format(getValueStr(self.m_FricWeldVelo)))
        if self.m_ForcesCirclesNum != obj.m_ForcesCirclesNum:
            paramArgs.append('m_ForcesCirclesNum={0}'.format(getValueStr(self.m_ForcesCirclesNum)))
        if self.m_OrthoStaticCoeff != obj.m_OrthoStaticCoeff:
            paramArgs.append('m_OrthoStaticCoeff={0}'.format(getValueStr(self.m_OrthoStaticCoeff)))
        if self.m_OrthoDynamicCoeff != obj.m_OrthoDynamicCoeff:
            paramArgs.append('m_OrthoDynamicCoeff={0}'.format(getValueStr(self.m_OrthoDynamicCoeff)))
        if self.m_OrthoDecayConst != obj.m_OrthoDecayConst:
            paramArgs.append('m_OrthoDecayConst={0}'.format(getValueStr(self.m_OrthoDecayConst)))
        if self.m_OrthoFricVector != obj.m_OrthoFricVector:
            paramArgs.append('m_OrthoFricVector={0}'.format(getValueStr(self.m_OrthoFricVector)))
        if self.m_bAllNodeSlave != obj.m_bAllNodeSlave:
            paramArgs.append('m_bAllNodeSlave={0}'.format(getBoolStr(self.m_bAllNodeSlave)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        if self.crAreaFaceSet != obj.crAreaFaceSet:
            paramArgs.append('crAreaFaceSet={0}'.format(getCursorValueStr(self.crAreaFaceSet)))
        if self.crVisualNodeSet != obj.crVisualNodeSet:
            paramArgs.append('crVisualNodeSet={0}'.format(getCursorValueStr(self.crVisualNodeSet)))
        return 'LBC_RIGIDWALL_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12},{13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}'.format(
            self.m_nObject,
            self.m_nType,
            self.m_nMotion,
            self.m_nFriction,
            self.m_nOrtho,
            self.m_nForces,
            self.m_Finite[0],
            self.m_Finite[1],
            self.m_MotionMass,
            self.m_MotionInitVelo,
            self.m_FricCoulombCoeff,
            self.m_FricWeldVelo,
            self.m_ForcesCirclesNum,
            self.m_OrthoStaticCoeff[0],
            self.m_OrthoStaticCoeff[1],
            self.m_OrthoDynamicCoeff[0],
            self.m_OrthoDynamicCoeff[1],
            self.m_OrthoDecayConst[0],
            self.m_OrthoDecayConst[1],
            self.m_OrthoFricVector[0],
            self.m_OrthoFricVector[1],
            self.m_OrthoFricVector[2],
            1 if self.m_bAllNodeSlave else 0,
            str(self.crCoord) if self.crCoord is not None else '0:0',
            str(self.crAreaFaceSet) if self.crAreaFaceSet is not None else '0:0',
            str(self.crVisualNodeSet) if self.crVisualNodeSet is not None else '0:0') + rightBracket

class LBC_ENFORCEDDISP_DATA:
    def __init__(self,
        dwDof=63,
        vTrans=[DFLT_DBL,DFLT_DBL,DFLT_DBL],
        vRot=[DFLT_DBL,DFLT_DBL,DFLT_DBL],
        curCoord=None,
        enArrowDir=0,
        crTable=None,
        crNodeSet=None,
        m_fPhase=DFLT_DBL,
        m_fDelay=DFLT_DBL,
        crPhaseTable=None):
        self.dwDof = dwDof
        self.vTrans = vTrans
        self.vRot = vRot
        self.curCoord = curCoord
        self.enArrowDir = enArrowDir
        self.crTable = crTable
        self.crNodeSet = crNodeSet
        self.m_fPhase = m_fPhase
        self.m_fDelay = m_fDelay
        self.crPhaseTable = crPhaseTable
    def isDefault(self):
        obj = LBC_ENFORCEDDISP_DATA()
        return self.dwDof == obj.dwDof and \
            self.vTrans == obj.vTrans and \
            self.vRot == obj.vRot and \
            self.curCoord == obj.curCoord and \
            self.enArrowDir == obj.enArrowDir and \
            self.crTable == obj.crTable and \
            self.crNodeSet == obj.crNodeSet and \
            self.m_fPhase == obj.m_fPhase and \
            self.m_fDelay == obj.m_fDelay and \
            self.crPhaseTable == obj.crPhaseTable
    def fromList(self, param):
        obj = LBC_ENFORCEDDISP_DATA()
        self.dwDof = param[0] if len(param) > 0 else obj.dwDof
        self.vTrans = [normalizeDoubleType(tok) for tok in param[1]] if len(param) > 1 else obj.vTrans
        self.vRot = [normalizeDoubleType(tok) for tok in param[2]] if len(param) > 2 else obj.vRot
        self.curCoord = getCursorValue(param[3]) if len(param) > 3 else obj.curCoord
        self.enArrowDir = param[4] if len(param) > 4 else obj.enArrowDir
        self.crTable = getCursorValue(param[5]) if len(param) > 5 else obj.crTable
        self.crNodeSet = getCursorValue(param[6]) if len(param) > 6 else obj.crNodeSet
        self.m_fPhase = normalizeDoubleType(param[7]) if len(param) > 7 else obj.m_fPhase
        self.m_fDelay = normalizeDoubleType(param[8]) if len(param) > 8 else obj.m_fDelay
        self.crPhaseTable = getCursorValue(param[9]) if len(param) > 9 else obj.crPhaseTable
        return self
    def __str__(self):
        obj = LBC_ENFORCEDDISP_DATA()
        paramArgs = []
        if self.dwDof != obj.dwDof:
            paramArgs.append('dwDof={0}'.format(getValueStr(self.dwDof)))
        if self.vTrans != obj.vTrans:
            paramArgs.append('vTrans={0}'.format(getValueStr(self.vTrans)))
        if self.vRot != obj.vRot:
            paramArgs.append('vRot={0}'.format(getValueStr(self.vRot)))
        if self.curCoord != obj.curCoord:
            paramArgs.append('curCoord={0}'.format(getCursorValueStr(self.curCoord)))
        if self.enArrowDir != obj.enArrowDir:
            paramArgs.append('enArrowDir={0}'.format(getValueStr(self.enArrowDir)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        if self.crNodeSet != obj.crNodeSet:
            paramArgs.append('crNodeSet={0}'.format(getCursorValueStr(self.crNodeSet)))
        if self.m_fPhase != obj.m_fPhase:
            paramArgs.append('m_fPhase={0}'.format(getValueStr(self.m_fPhase)))
        if self.m_fDelay != obj.m_fDelay:
            paramArgs.append('m_fDelay={0}'.format(getValueStr(self.m_fDelay)))
        if self.crPhaseTable != obj.crPhaseTable:
            paramArgs.append('crPhaseTable={0}'.format(getCursorValueStr(self.crPhaseTable)))
        return 'LBC_ENFORCEDDISP_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}'.format(
            self.dwDof,
            self.vTrans[0],
            self.vTrans[1],
            self.vTrans[2],
            self.vRot[0],
            self.vRot[1],
            self.vRot[2],
            str(self.curCoord) if self.curCoord is not None else '0:0',
            self.enArrowDir,
            str(self.crTable) if self.crTable is not None else '0:0',
            str(self.crNodeSet) if self.crNodeSet is not None else '0:0',
            self.m_fPhase,
            self.m_fDelay,
            str(self.crPhaseTable) if self.crPhaseTable is not None else '0:0') + rightBracket

class LBC_DYNAMIC_INITIAL_CONDITION_DATA:
    def __init__(self,
        vInit=[DFLT_DBL,DFLT_DBL,DFLT_DBL],
        bSelNode=False,
        crNodeSet=None,
        crTable=None,
        crCoord=None):
        self.vInit = vInit
        self.bSelNode = bSelNode
        self.crNodeSet = crNodeSet
        self.crTable = crTable
        self.crCoord = crCoord
    def isDefault(self):
        obj = LBC_DYNAMIC_INITIAL_CONDITION_DATA()
        return self.vInit == obj.vInit and \
            self.bSelNode == obj.bSelNode and \
            self.crNodeSet == obj.crNodeSet and \
            self.crTable == obj.crTable and \
            self.crCoord == obj.crCoord
    def fromList(self, param):
        obj = LBC_DYNAMIC_INITIAL_CONDITION_DATA()
        self.vInit = [normalizeDoubleType(tok) for tok in param[0]] if len(param) > 0 else obj.vInit
        self.bSelNode = getBoolValue(param[1]) if len(param) > 1 else obj.bSelNode
        self.crNodeSet = getCursorValue(param[2]) if len(param) > 2 else obj.crNodeSet
        self.crTable = getCursorValue(param[3]) if len(param) > 3 else obj.crTable
        self.crCoord = getCursorValue(param[4]) if len(param) > 4 else obj.crCoord
        return self
    def __str__(self):
        obj = LBC_DYNAMIC_INITIAL_CONDITION_DATA()
        paramArgs = []
        if self.vInit != obj.vInit:
            paramArgs.append('vInit={0}'.format(getValueStr(self.vInit)))
        if self.bSelNode != obj.bSelNode:
            paramArgs.append('bSelNode={0}'.format(getBoolStr(self.bSelNode)))
        if self.crNodeSet != obj.crNodeSet:
            paramArgs.append('crNodeSet={0}'.format(getCursorValueStr(self.crNodeSet)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        return 'LBC_DYNAMIC_INITIAL_CONDITION_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            self.vInit,
            1 if self.bSelNode else 0,
            str(self.crNodeSet) if self.crNodeSet is not None else '0:0',
            str(self.crTable) if self.crTable is not None else '0:0',
            str(self.crCoord) if self.crCoord is not None else '0:0') + rightBracket

class RenumberByConnData:
    def __init__(self,
        entityType=0,
        sortOrder=0,
        startId=1,
        incStep=1,
        layer1=100,
        layer2=100,
        layer3=100,
        offsetLayer12=DFLT_INT,
        offsetLayer23=DFLT_INT,
        bstopAtEdge=False):
        self.entityType = entityType
        self.sortOrder = sortOrder
        self.startId = startId
        self.incStep = incStep
        self.layer1 = layer1
        self.layer2 = layer2
        self.layer3 = layer3
        self.offsetLayer12 = offsetLayer12
        self.offsetLayer23 = offsetLayer23
        self.bstopAtEdge = bstopAtEdge
    def isDefault(self):
        obj = RenumberByConnData()
        return self.entityType == obj.entityType and \
            self.sortOrder == obj.sortOrder and \
            self.startId == obj.startId and \
            self.incStep == obj.incStep and \
            self.layer1 == obj.layer1 and \
            self.layer2 == obj.layer2 and \
            self.layer3 == obj.layer3 and \
            self.offsetLayer12 == obj.offsetLayer12 and \
            self.offsetLayer23 == obj.offsetLayer23 and \
            self.bstopAtEdge == obj.bstopAtEdge
    def fromList(self, param):
        obj = RenumberByConnData()
        self.entityType = param[0] if len(param) > 0 else obj.entityType
        self.sortOrder = param[1] if len(param) > 1 else obj.sortOrder
        self.startId = param[2] if len(param) > 2 else obj.startId
        self.incStep = param[3] if len(param) > 3 else obj.incStep
        self.layer1 = param[4] if len(param) > 4 else obj.layer1
        self.layer2 = param[5] if len(param) > 5 else obj.layer2
        self.layer3 = param[6] if len(param) > 6 else obj.layer3
        self.offsetLayer12 = param[7] if len(param) > 7 else obj.offsetLayer12
        self.offsetLayer23 = param[8] if len(param) > 8 else obj.offsetLayer23
        self.bstopAtEdge = getBoolValue(param[9]) if len(param) > 9 else obj.bstopAtEdge
        return self
    def __str__(self):
        obj = RenumberByConnData()
        paramArgs = []
        if self.entityType != obj.entityType:
            paramArgs.append('entityType={0}'.format(getValueStr(self.entityType)))
        if self.sortOrder != obj.sortOrder:
            paramArgs.append('sortOrder={0}'.format(getValueStr(self.sortOrder)))
        if self.startId != obj.startId:
            paramArgs.append('startId={0}'.format(getValueStr(self.startId)))
        if self.incStep != obj.incStep:
            paramArgs.append('incStep={0}'.format(getValueStr(self.incStep)))
        if self.layer1 != obj.layer1:
            paramArgs.append('layer1={0}'.format(getValueStr(self.layer1)))
        if self.layer2 != obj.layer2:
            paramArgs.append('layer2={0}'.format(getValueStr(self.layer2)))
        if self.layer3 != obj.layer3:
            paramArgs.append('layer3={0}'.format(getValueStr(self.layer3)))
        if self.offsetLayer12 != obj.offsetLayer12:
            paramArgs.append('offsetLayer12={0}'.format(getValueStr(self.offsetLayer12)))
        if self.offsetLayer23 != obj.offsetLayer23:
            paramArgs.append('offsetLayer23={0}'.format(getValueStr(self.offsetLayer23)))
        if self.bstopAtEdge != obj.bstopAtEdge:
            paramArgs.append('bstopAtEdge={0}'.format(getBoolStr(self.bstopAtEdge)))
        return 'RenumberByConnData({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}'.format(
            self.entityType,
            self.sortOrder,
            self.startId,
            self.incStep,
            self.layer1,
            self.layer2,
            self.layer3,
            self.offsetLayer12,
            self.offsetLayer23,
            1 if self.bstopAtEdge else 0) + rightBracket

class ACTRAN_DOMAIN:
    def __init__(self,
        iElemPID=0,
        strName="",
        strBdf=""):
        self.iElemPID = iElemPID
        self.strName = strName
        self.strBdf = strBdf
    def isDefault(self):
        obj = ACTRAN_DOMAIN()
        return self.iElemPID == obj.iElemPID and \
            self.strName == obj.strName and \
            self.strBdf == obj.strBdf
    def fromList(self, param):
        obj = ACTRAN_DOMAIN()
        self.iElemPID = param[0] if len(param) > 0 else obj.iElemPID
        self.strName = param[1] if len(param) > 1 else obj.strName
        self.strBdf = param[2] if len(param) > 2 else obj.strBdf
        return self
    def __str__(self):
        obj = ACTRAN_DOMAIN()
        paramArgs = []
        if self.iElemPID != obj.iElemPID:
            paramArgs.append('iElemPID={0}'.format(getValueStr(self.iElemPID)))
        if self.strName != obj.strName:
            paramArgs.append('strName={0}'.format('"' + self.strName + '"'))
        if self.strBdf != obj.strBdf:
            paramArgs.append('strBdf={0}'.format('"' + self.strBdf + '"'))
        return 'ACTRAN_DOMAIN({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iElemPID,
            '"' + self.strName + '"',
            '"' + self.strBdf + '"') + rightBracket

class ACTRAN_ANALYSIS:
    def __init__(self,
        strName="Job_1",
        strDescription="",
        iExeType=0,
        iAnaType=0,
        strEdatFile="",
        strAcousticFileName="",
        iNfSpaceType=0,
        iPML2DElemPID=0,
        iPML3DElemPID=0,
        iIFEM2DElemPID=0,
        iOrder=DFLT_INT,
        dlOrigin=[0.0,0.0,0.0],
        dlXAxis=[1.0,0.0,0.0],
        dlYAxis=[0.0,1.0,0.0],
        dlZAxis=[0.0,0.0,1.0],
        strReflection= "NOSYM, NOSYM, NOSYM",
        iProjectionSurface2DElemPID=0,
        dGapTol=0.01,
        dPlaneTol=0.0001,
        iFiniteDomain3DElemPID=0,
        iMatId=0,
        dAcousticSpeed=DFLT_DBL,
        dFluidDensity=DFLT_DBL,
        strStructuralModelBdfFile="",
        strStructuralModelOp2File="",
        strSubcase="1",
        iStateValue=1,
        iNumOfPanel=0,
        iSummationID=0,
        strStructuralModelPCHFile="",
        iLowerMode=DFLT_INT,
        iUpperMode=DFLT_INT,
        iSubcaseStart=DFLT_INT,
        iSubcaseStop=DFLT_INT,
        iStartRPM=DFLT_INT,
        iIncrementRPM=DFLT_INT,
        iFdmethod=0,
        dStartf=DFLT_DBL,
        dEndf=DFLT_DBL,
        dIncrtf=DFLT_DBL,
        iSolver=0,
        strGreenDBFile="Green_db",
        strPltfile="AUTO",
        bUseMapFile=False,
        iFormat=1,
        strMapFile="AUTO",
        iMethod=0,
        iNodeGroupID=0,
        tshTable=[],
        listActranDomain=[],
        iJobType=0,
        iInfiniteSpaceType=0,
        strInputFile1="",
        strInputFile2="",
        iMemory=500,
        iThreads=DFLT_INT):
        self.strName = strName
        self.strDescription = strDescription
        self.iExeType = iExeType
        self.iAnaType = iAnaType
        self.strEdatFile = strEdatFile
        self.strAcousticFileName = strAcousticFileName
        self.iNfSpaceType = iNfSpaceType
        self.iPML2DElemPID = iPML2DElemPID
        self.iPML3DElemPID = iPML3DElemPID
        self.iIFEM2DElemPID = iIFEM2DElemPID
        self.iOrder = iOrder
        self.dlOrigin = dlOrigin
        self.dlXAxis = dlXAxis
        self.dlYAxis = dlYAxis
        self.dlZAxis = dlZAxis
        self.strReflection = strReflection
        self.iProjectionSurface2DElemPID = iProjectionSurface2DElemPID
        self.dGapTol = dGapTol
        self.dPlaneTol = dPlaneTol
        self.iFiniteDomain3DElemPID = iFiniteDomain3DElemPID
        self.iMatId = iMatId
        self.dAcousticSpeed = dAcousticSpeed
        self.dFluidDensity = dFluidDensity
        self.strStructuralModelBdfFile = strStructuralModelBdfFile
        self.strStructuralModelOp2File = strStructuralModelOp2File
        self.strSubcase = strSubcase
        self.iStateValue = iStateValue
        self.iNumOfPanel = iNumOfPanel
        self.iSummationID = iSummationID
        self.strStructuralModelPCHFile = strStructuralModelPCHFile
        self.iLowerMode = iLowerMode
        self.iUpperMode = iUpperMode
        self.iSubcaseStart = iSubcaseStart
        self.iSubcaseStop = iSubcaseStop
        self.iStartRPM = iStartRPM
        self.iIncrementRPM = iIncrementRPM
        self.iFdmethod = iFdmethod
        self.dStartf = dStartf
        self.dEndf = dEndf
        self.dIncrtf = dIncrtf
        self.iSolver = iSolver
        self.strGreenDBFile = strGreenDBFile
        self.strPltfile = strPltfile
        self.bUseMapFile = bUseMapFile
        self.iFormat = iFormat
        self.strMapFile = strMapFile
        self.iMethod = iMethod
        self.iNodeGroupID = iNodeGroupID
        self.tshTable = tshTable
        self.listActranDomain = listActranDomain
        self.iJobType = iJobType
        self.iInfiniteSpaceType = iInfiniteSpaceType
        self.strInputFile1 = strInputFile1
        self.strInputFile2 = strInputFile2
        self.iMemory = iMemory
        self.iThreads = iThreads
    def isDefault(self):
        obj = ACTRAN_ANALYSIS()
        return self.strName == obj.strName and \
            self.strDescription == obj.strDescription and \
            self.iExeType == obj.iExeType and \
            self.iAnaType == obj.iAnaType and \
            self.strEdatFile == obj.strEdatFile and \
            self.strAcousticFileName == obj.strAcousticFileName and \
            self.iNfSpaceType == obj.iNfSpaceType and \
            self.iPML2DElemPID == obj.iPML2DElemPID and \
            self.iPML3DElemPID == obj.iPML3DElemPID and \
            self.iIFEM2DElemPID == obj.iIFEM2DElemPID and \
            self.iOrder == obj.iOrder and \
            self.dlOrigin == obj.dlOrigin and \
            self.dlXAxis == obj.dlXAxis and \
            self.dlYAxis == obj.dlYAxis and \
            self.dlZAxis == obj.dlZAxis and \
            self.strReflection == obj.strReflection and \
            self.iProjectionSurface2DElemPID == obj.iProjectionSurface2DElemPID and \
            self.dGapTol == obj.dGapTol and \
            self.dPlaneTol == obj.dPlaneTol and \
            self.iFiniteDomain3DElemPID == obj.iFiniteDomain3DElemPID and \
            self.iMatId == obj.iMatId and \
            self.dAcousticSpeed == obj.dAcousticSpeed and \
            self.dFluidDensity == obj.dFluidDensity and \
            self.strStructuralModelBdfFile == obj.strStructuralModelBdfFile and \
            self.strStructuralModelOp2File == obj.strStructuralModelOp2File and \
            self.strSubcase == obj.strSubcase and \
            self.iStateValue == obj.iStateValue and \
            self.iNumOfPanel == obj.iNumOfPanel and \
            self.iSummationID == obj.iSummationID and \
            self.strStructuralModelPCHFile == obj.strStructuralModelPCHFile and \
            self.iLowerMode == obj.iLowerMode and \
            self.iUpperMode == obj.iUpperMode and \
            self.iSubcaseStart == obj.iSubcaseStart and \
            self.iSubcaseStop == obj.iSubcaseStop and \
            self.iStartRPM == obj.iStartRPM and \
            self.iIncrementRPM == obj.iIncrementRPM and \
            self.iFdmethod == obj.iFdmethod and \
            self.dStartf == obj.dStartf and \
            self.dEndf == obj.dEndf and \
            self.dIncrtf == obj.dIncrtf and \
            self.iSolver == obj.iSolver and \
            self.strGreenDBFile == obj.strGreenDBFile and \
            self.strPltfile == obj.strPltfile and \
            self.bUseMapFile == obj.bUseMapFile and \
            self.iFormat == obj.iFormat and \
            self.strMapFile == obj.strMapFile and \
            self.iMethod == obj.iMethod and \
            self.iNodeGroupID == obj.iNodeGroupID and \
            self.tshTable == obj.tshTable and \
            self.listActranDomain == obj.listActranDomain and \
            self.iJobType == obj.iJobType and \
            self.iInfiniteSpaceType == obj.iInfiniteSpaceType and \
            self.strInputFile1 == obj.strInputFile1 and \
            self.strInputFile2 == obj.strInputFile2 and \
            self.iMemory == obj.iMemory and \
            self.iThreads == obj.iThreads
    def fromList(self, listActranDomain):
        obj = ACTRAN_ANALYSIS()
        self.strName = listActranDomain[0] if len(listActranDomain) > 0 else obj.strName
        self.strDescription = listActranDomain[1] if len(listActranDomain) > 1 else obj.strDescription
        self.iExeType = listActranDomain[2] if len(listActranDomain) > 2 else obj.iExeType
        self.iAnaType = listActranDomain[3] if len(listActranDomain) > 3 else obj.iAnaType
        self.strEdatFile = listActranDomain[4] if len(listActranDomain) > 4 else obj.strEdatFile
        self.strAcousticFileName = listActranDomain[5] if len(listActranDomain) > 5 else obj.strAcousticFileName
        self.iNfSpaceType = listActranDomain[6] if len(listActranDomain) > 6 else obj.iNfSpaceType
        self.iPML2DElemPID = listActranDomain[7] if len(listActranDomain) > 7 else obj.iPML2DElemPID
        self.iPML3DElemPID = listActranDomain[8] if len(listActranDomain) > 8 else obj.iPML3DElemPID
        self.iIFEM2DElemPID = listActranDomain[9] if len(listActranDomain) > 9 else obj.iIFEM2DElemPID
        self.iOrder = listActranDomain[10] if len(listActranDomain) > 10 else obj.iOrder
        self.dlOrigin = [normalizeDoubleType(tok) for tok in listActranDomain[11]] if len(listActranDomain) > 11 else obj.dlOrigin
        self.dlXAxis = [normalizeDoubleType(tok) for tok in listActranDomain[12]] if len(listActranDomain) > 12 else obj.dlXAxis
        self.dlYAxis = [normalizeDoubleType(tok) for tok in listActranDomain[13]] if len(listActranDomain) > 13 else obj.dlYAxis
        self.dlZAxis = [normalizeDoubleType(tok) for tok in listActranDomain[14]] if len(listActranDomain) > 14 else obj.dlZAxis
        self.strReflection = listActranDomain[15] if len(listActranDomain) > 15 else obj.strReflection
        self.iProjectionSurface2DElemPID = listActranDomain[16] if len(listActranDomain) > 16 else obj.iProjectionSurface2DElemPID
        self.dGapTol = normalizeDoubleType(listActranDomain[17]) if len(listActranDomain) > 17 else obj.dGapTol
        self.dPlaneTol = normalizeDoubleType(listActranDomain[18]) if len(listActranDomain) > 18 else obj.dPlaneTol
        self.iFiniteDomain3DElemPID = listActranDomain[19] if len(listActranDomain) > 19 else obj.iFiniteDomain3DElemPID
        self.iMatId = listActranDomain[20] if len(listActranDomain) > 20 else obj.iMatId
        self.dAcousticSpeed = normalizeDoubleType(listActranDomain[21]) if len(listActranDomain) > 21 else obj.dAcousticSpeed
        self.dFluidDensity = normalizeDoubleType(listActranDomain[22]) if len(listActranDomain) > 22 else obj.dFluidDensity
        self.strStructuralModelBdfFile = listActranDomain[23] if len(listActranDomain) > 23 else obj.strStructuralModelBdfFile
        self.strStructuralModelOp2File = listActranDomain[24] if len(listActranDomain) > 24 else obj.strStructuralModelOp2File
        self.strSubcase = listActranDomain[25] if len(listActranDomain) > 25 else obj.strSubcase
        self.iStateValue = listActranDomain[26] if len(listActranDomain) > 26 else obj.iStateValue
        self.iNumOfPanel = listActranDomain[27] if len(listActranDomain) > 27 else obj.iNumOfPanel
        self.iSummationID = listActranDomain[28] if len(listActranDomain) > 28 else obj.iSummationID
        self.strStructuralModelPCHFile = listActranDomain[29] if len(listActranDomain) > 29 else obj.strStructuralModelPCHFile
        self.iLowerMode = listActranDomain[30] if len(listActranDomain) > 30 else obj.iLowerMode
        self.iUpperMode = listActranDomain[31] if len(listActranDomain) > 31 else obj.iUpperMode
        self.iSubcaseStart = listActranDomain[32] if len(listActranDomain) > 32 else obj.iSubcaseStart
        self.iSubcaseStop = listActranDomain[33] if len(listActranDomain) > 33 else obj.iSubcaseStop
        self.iStartRPM = listActranDomain[34] if len(listActranDomain) > 34 else obj.iStartRPM
        self.iIncrementRPM = listActranDomain[35] if len(listActranDomain) > 35 else obj.iIncrementRPM
        self.iFdmethod = listActranDomain[36] if len(listActranDomain) > 36 else obj.iFdmethod
        self.dStartf = normalizeDoubleType(listActranDomain[37]) if len(listActranDomain) > 37 else obj.dStartf
        self.dEndf = normalizeDoubleType(listActranDomain[38]) if len(listActranDomain) > 38 else obj.dEndf
        self.dIncrtf = normalizeDoubleType(listActranDomain[39]) if len(listActranDomain) > 39 else obj.dIncrtf
        self.iSolver = listActranDomain[40] if len(listActranDomain) > 40 else obj.iSolver
        self.strGreenDBFile = listActranDomain[41] if len(listActranDomain) > 41 else obj.strGreenDBFile
        self.strPltfile = listActranDomain[42] if len(listActranDomain) > 42 else obj.strPltfile
        self.bUseMapFile = getBoolValue(listActranDomain[43]) if len(listActranDomain) > 43 else obj.bUseMapFile
        self.iFormat = listActranDomain[44] if len(listActranDomain) > 44 else obj.iFormat
        self.strMapFile = listActranDomain[45] if len(listActranDomain) > 45 else obj.strMapFile
        self.iMethod = listActranDomain[46] if len(listActranDomain) > 46 else obj.iMethod
        self.iNodeGroupID = listActranDomain[47] if len(listActranDomain) > 47 else obj.iNodeGroupID
        self.tshTable = listActranDomain[48] if len(listActranDomain) > 48 else obj.tshTable
        self.listActranDomain = [normalizeDoubleType(tok) for tok in listActranDomain[49]] if len(listActranDomain) > 49 else obj.listActranDomain
        self.iJobType = listActranDomain[50] if len(listActranDomain) > 50 else obj.iJobType
        self.iInfiniteSpaceType = listActranDomain[51] if len(listActranDomain) > 51 else obj.iInfiniteSpaceType
        self.strInputFile1 = listActranDomain[52] if len(listActranDomain) > 52 else obj.strInputFile1
        self.strInputFile2 = listActranDomain[53] if len(listActranDomain) > 53 else obj.strInputFile2
        self.iMemory = listActranDomain[54] if len(listActranDomain) > 54 else obj.iMemory
        self.iThreads = listActranDomain[55] if len(listActranDomain) > 55 else obj.iThreads
        return self
    def __str__(self):
        obj = ACTRAN_ANALYSIS()
        paramArgs = []
        if self.strName != obj.strName:
            paramArgs.append('strName={0}'.format('"' + self.strName + '"'))
        if self.strDescription != obj.strDescription:
            paramArgs.append('strDescription={0}'.format('"' + self.strDescription + '"'))
        if self.iExeType != obj.iExeType:
            paramArgs.append('iExeType={0}'.format(getValueStr(self.iExeType)))
        if self.iAnaType != obj.iAnaType:
            paramArgs.append('iAnaType={0}'.format(getValueStr(self.iAnaType)))
        if self.strEdatFile != obj.strEdatFile:
            paramArgs.append('strEdatFile={0}'.format('"' + self.strEdatFile + '"'))
        if self.strAcousticFileName != obj.strAcousticFileName:
            paramArgs.append('strAcousticFileName={0}'.format('"' + self.strAcousticFileName + '"'))
        if self.iNfSpaceType != obj.iNfSpaceType:
            paramArgs.append('iNfSpaceType={0}'.format(getValueStr(self.iNfSpaceType)))
        if self.iPML2DElemPID != obj.iPML2DElemPID:
            paramArgs.append('iPML2DElemPID={0}'.format(getValueStr(self.iPML2DElemPID)))
        if self.iPML3DElemPID != obj.iPML3DElemPID:
            paramArgs.append('iPML3DElemPID={0}'.format(getValueStr(self.iPML3DElemPID)))
        if self.iIFEM2DElemPID != obj.iIFEM2DElemPID:
            paramArgs.append('iIFEM2DElemPID={0}'.format(getValueStr(self.iIFEM2DElemPID)))
        if self.iOrder != obj.iOrder:
            paramArgs.append('iOrder={0}'.format(getValueStr(self.iOrder)))
        if self.dlOrigin != obj.dlOrigin:
            paramArgs.append('dlOrigin={0}'.format(getValueStr(self.dlOrigin)))
        if self.dlXAxis != obj.dlXAxis:
            paramArgs.append('dlXAxis={0}'.format(getValueStr(self.dlXAxis)))
        if self.dlYAxis != obj.dlYAxis:
            paramArgs.append('dlYAxis={0}'.format(getValueStr(self.dlYAxis)))
        if self.dlZAxis != obj.dlZAxis:
            paramArgs.append('dlZAxis={0}'.format(getValueStr(self.dlZAxis)))
        if self.strReflection != obj.strReflection:
            paramArgs.append('strReflection={0}'.format('"' + self.strReflection + '"'))
        if self.iProjectionSurface2DElemPID != obj.iProjectionSurface2DElemPID:
            paramArgs.append('iProjectionSurface2DElemPID={0}'.format(getValueStr(self.iProjectionSurface2DElemPID)))
        if self.dGapTol != obj.dGapTol:
            paramArgs.append('dGapTol={0}'.format(getValueStr(self.dGapTol)))
        if self.dPlaneTol != obj.dPlaneTol:
            paramArgs.append('dPlaneTol={0}'.format(getValueStr(self.dPlaneTol)))
        if self.iFiniteDomain3DElemPID != obj.iFiniteDomain3DElemPID:
            paramArgs.append('iFiniteDomain3DElemPID={0}'.format(getValueStr(self.iFiniteDomain3DElemPID)))
        if self.iMatId != obj.iMatId:
            paramArgs.append('iMatId={0}'.format(getValueStr(self.iMatId)))
        if self.dAcousticSpeed != obj.dAcousticSpeed:
            paramArgs.append('dAcousticSpeed={0}'.format(getValueStr(self.dAcousticSpeed)))
        if self.dFluidDensity != obj.dFluidDensity:
            paramArgs.append('dFluidDensity={0}'.format(getValueStr(self.dFluidDensity)))
        if self.strStructuralModelBdfFile != obj.strStructuralModelBdfFile:
            paramArgs.append('strStructuralModelBdfFile={0}'.format('"' + self.strStructuralModelBdfFile + '"'))
        if self.strStructuralModelOp2File != obj.strStructuralModelOp2File:
            paramArgs.append('strStructuralModelOp2File={0}'.format('"' + self.strStructuralModelOp2File + '"'))
        if self.strSubcase != obj.strSubcase:
            paramArgs.append('strSubcase={0}'.format('"' + self.strSubcase + '"'))
        if self.iStateValue != obj.iStateValue:
            paramArgs.append('iStateValue={0}'.format(getValueStr(self.iStateValue)))
        if self.iNumOfPanel != obj.iNumOfPanel:
            paramArgs.append('iNumOfPanel={0}'.format(getValueStr(self.iNumOfPanel)))
        if self.iSummationID != obj.iSummationID:
            paramArgs.append('iSummationID={0}'.format(getValueStr(self.iSummationID)))
        if self.strStructuralModelPCHFile != obj.strStructuralModelPCHFile:
            paramArgs.append('strStructuralModelPCHFile={0}'.format('"' + self.strStructuralModelPCHFile + '"'))
        if self.iLowerMode != obj.iLowerMode:
            paramArgs.append('iLowerMode={0}'.format(getValueStr(self.iLowerMode)))
        if self.iUpperMode != obj.iUpperMode:
            paramArgs.append('iUpperMode={0}'.format(getValueStr(self.iUpperMode)))
        if self.iSubcaseStart != obj.iSubcaseStart:
            paramArgs.append('iSubcaseStart={0}'.format(getValueStr(self.iSubcaseStart)))
        if self.iSubcaseStop != obj.iSubcaseStop:
            paramArgs.append('iSubcaseStop={0}'.format(getValueStr(self.iSubcaseStop)))
        if self.iStartRPM != obj.iStartRPM:
            paramArgs.append('iStartRPM={0}'.format(getValueStr(self.iStartRPM)))
        if self.iIncrementRPM != obj.iIncrementRPM:
            paramArgs.append('iIncrementRPM={0}'.format(getValueStr(self.iIncrementRPM)))
        if self.iFdmethod != obj.iFdmethod:
            paramArgs.append('iFdmethod={0}'.format(getValueStr(self.iFdmethod)))
        if self.dStartf != obj.dStartf:
            paramArgs.append('dStartf={0}'.format(getValueStr(self.dStartf)))
        if self.dEndf != obj.dEndf:
            paramArgs.append('dEndf={0}'.format(getValueStr(self.dEndf)))
        if self.dIncrtf != obj.dIncrtf:
            paramArgs.append('dIncrtf={0}'.format(getValueStr(self.dIncrtf)))
        if self.iSolver != obj.iSolver:
            paramArgs.append('iSolver={0}'.format(getValueStr(self.iSolver)))
        if self.strGreenDBFile != obj.strGreenDBFile:
            paramArgs.append('strGreenDBFile={0}'.format('"' + self.strGreenDBFile + '"'))
        if self.strPltfile != obj.strPltfile:
            paramArgs.append('strPltfile={0}'.format('"' + self.strPltfile + '"'))
        if self.bUseMapFile != obj.bUseMapFile:
            paramArgs.append('bUseMapFile={0}'.format(getBoolStr(self.bUseMapFile)))
        if self.iFormat != obj.iFormat:
            paramArgs.append('iFormat={0}'.format(getValueStr(self.iFormat)))
        if self.strMapFile != obj.strMapFile:
            paramArgs.append('strMapFile={0}'.format('"' + self.strMapFile + '"'))
        if self.iMethod != obj.iMethod:
            paramArgs.append('iMethod={0}'.format(getValueStr(self.iMethod)))
        if self.iNodeGroupID != obj.iNodeGroupID:
            paramArgs.append('iNodeGroupID={0}'.format(getValueStr(self.iNodeGroupID)))
        if self.tshTable != obj.tshTable:
            paramArgs.append('tshTable={0}'.format(getValueStr(self.tshTable)))
        if self.listActranDomain != obj.listActranDomain:
            paramArgs.append('listActranDomain={0}'.format(getValueStr(self.listActranDomain)))
        if self.iJobType != obj.iJobType:
            paramArgs.append('iJobType={0}'.format(getValueStr(self.iJobType)))
        if self.iInfiniteSpaceType != obj.iInfiniteSpaceType:
            paramArgs.append('iInfiniteSpaceType={0}'.format(getValueStr(self.iInfiniteSpaceType)))
        if self.strInputFile1 != obj.strInputFile1:
            paramArgs.append('strInputFile1={0}'.format('"' + self.strInputFile1 + '"'))
        if self.strInputFile2 != obj.strInputFile2:
            paramArgs.append('strInputFile2={0}'.format('"' + self.strInputFile2 + '"'))
        if self.iMemory != obj.iMemory:
            paramArgs.append('iMemory={0}'.format(getValueStr(self.iMemory)))
        if self.iThreads != obj.iThreads:
            paramArgs.append('iThreads={0}'.format(getValueStr(self.iThreads)))
        return 'ACTRAN_ANALYSIS({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}, {54}, {55}'.format(
            '"' + self.strName + '"',
            '"' + self.strDescription + '"',
            self.iExeType,
            self.iAnaType,
            '"' + self.strEdatFile + '"',
            '"' + self.strAcousticFileName + '"',
            self.iNfSpaceType,
            self.iPML2DElemPID,
            self.iPML3DElemPID,
            self.iIFEM2DElemPID,
            self.iOrder,
            self.dlOrigin,
            self.dlXAxis,
            self.dlYAxis,
            self.dlZAxis,
            '"' + self.strReflection + '"',
            self.iProjectionSurface2DElemPID,
            self.dGapTol,
            self.dPlaneTol,
            self.iFiniteDomain3DElemPID,
            self.iMatId,
            self.dAcousticSpeed,
            self.dFluidDensity,
            '"' + self.strStructuralModelBdfFile + '"',
            '"' + self.strStructuralModelOp2File + '"',
            '"' + self.strSubcase + '"',
            self.iStateValue,
            self.iNumOfPanel,
            self.iSummationID,
            '"' + self.strStructuralModelPCHFile + '"',
            self.iLowerMode,
            self.iUpperMode,
            self.iSubcaseStart,
            self.iSubcaseStop,
            self.iStartRPM,
            self.iIncrementRPM,
            self.iFdmethod,
            self.dStartf,
            self.dEndf,
            self.dIncrtf,
            self.iSolver,
            '"' + self.strGreenDBFile + '"',
            '"' + self.strPltfile + '"',
            1 if self.bUseMapFile else 0,
            self.iFormat,
            '"' + self.strMapFile + '"',
            self.iMethod,
            self.iNodeGroupID,
            self.tshTable,
            '[' + ', '.join(tok.toNativeStr(True) for tok in self.listActranDomain) +']',
            self.iJobType,
            self.iInfiniteSpaceType,
            '"' + self.strInputFile1 + '"',
            '"' + self.strInputFile2 + '"',
            self.iMemory,
            self.iThreads) + rightBracket

class ERIROD_END_PROP:
    def __init__(self,
        iElemId=0,
        iEndA=0,
        iEndB=0):
        self.iElemId = iElemId
        self.iEndA = iEndA
        self.iEndB = iEndB
    def isDefault(self):
        obj = ERIROD_END_PROP()
        return self.iElemId == obj.iElemId and \
            self.iEndA == obj.iEndA and \
            self.iEndB == obj.iEndB
    def fromList(self, param):
        obj = ERIROD_END_PROP()
        self.iElemId = param[0] if len(param) > 0 else obj.iElemId
        self.iEndA = param[1] if len(param) > 1 else obj.iEndA
        self.iEndB = param[2] if len(param) > 2 else obj.iEndB
        return self
    def __str__(self):
        obj = ERIROD_END_PROP()
        paramArgs = []
        if self.iElemId != obj.iElemId:
            paramArgs.append('iElemId={0}'.format(getValueStr(self.iElemId)))
        if self.iEndA != obj.iEndA:
            paramArgs.append('iEndA={0}'.format(getValueStr(self.iEndA)))
        if self.iEndB != obj.iEndB:
            paramArgs.append('iEndB={0}'.format(getValueStr(self.iEndB)))
        return 'ERIROD_END_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iElemId,
            self.iEndA,
            self.iEndB) + rightBracket

class ERIBEAM_END_PROP:
    def __init__(self,
        iElemId=0,
        iEndA=0,
        iEndB=0):
        self.iElemId = iElemId
        self.iEndA = iEndA
        self.iEndB = iEndB
    def isDefault(self):
        obj = ERIBEAM_END_PROP()
        return self.iElemId == obj.iElemId and \
            self.iEndA == obj.iEndA and \
            self.iEndB == obj.iEndB
    def fromList(self, param):
        obj = ERIBEAM_END_PROP()
        self.iElemId = param[0] if len(param) > 0 else obj.iElemId
        self.iEndA = param[1] if len(param) > 1 else obj.iEndA
        self.iEndB = param[2] if len(param) > 2 else obj.iEndB
        return self
    def __str__(self):
        obj = ERIBEAM_END_PROP()
        paramArgs = []
        if self.iElemId != obj.iElemId:
            paramArgs.append('iElemId={0}'.format(getValueStr(self.iElemId)))
        if self.iEndA != obj.iEndA:
            paramArgs.append('iEndA={0}'.format(getValueStr(self.iEndA)))
        if self.iEndB != obj.iEndB:
            paramArgs.append('iEndB={0}'.format(getValueStr(self.iEndB)))
        return 'ERIBEAM_END_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iElemId,
            self.iEndA,
            self.iEndB) + rightBracket

class ERIBEAM_ORI_VEC_PROP:
    def __init__(self,
        iPropId=0,
        iElemId=0,
        dlOrientVec=[0, 0, 0]):
        self.iPropId = iPropId
        self.iElemId = iElemId
        self.dlOrientVec = dlOrientVec
    def isDefault(self):
        obj = ERIBEAM_ORI_VEC_PROP()
        return self.iPropId == obj.iPropId and \
            self.iElemId == obj.iElemId and \
            self.dlOrientVec == obj.dlOrientVec
    def fromList(self, param):
        obj = ERIBEAM_ORI_VEC_PROP()
        self.iPropId = param[0] if len(param) > 0 else obj.iPropId
        self.iElemId = param[1] if len(param) > 1 else obj.iElemId
        self.dlOrientVec = [normalizeDoubleType(tok) for tok in param[2]] if len(param) > 2 else obj.dlOrientVec
        return self
    def __str__(self):
        obj = ERIBEAM_ORI_VEC_PROP()
        paramArgs = []
        if self.iPropId != obj.iPropId:
            paramArgs.append('iPropId={0}'.format(getValueStr(self.iPropId)))
        if self.iElemId != obj.iElemId:
            paramArgs.append('iElemId={0}'.format(getValueStr(self.iElemId)))
        if self.dlOrientVec != obj.dlOrientVec:
            paramArgs.append('dlOrientVec={0}'.format(getValueStr(self.dlOrientVec)))
        return 'ERIBEAM_ORI_VEC_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iPropId,
            self.iElemId,
            self.dlOrientVec) + rightBracket

class ERIBEAM_ORI_NODEID_PROP:
    def __init__(self,
        iPropId=0,
        iElemId=0,
        iOrientNodeId=0):
        self.iPropId = iPropId
        self.iElemId = iElemId
        self.iOrientNodeId = iOrientNodeId
    def isDefault(self):
        obj = ERIBEAM_ORI_NODEID_PROP()
        return self.iPropId == obj.iPropId and \
            self.iElemId == obj.iElemId and \
            self.iOrientNodeId == obj.iOrientNodeId
    def fromList(self, param):
        obj = ERIBEAM_ORI_NODEID_PROP()
        self.iPropId = param[0] if len(param) > 0 else obj.iPropId
        self.iElemId = param[1] if len(param) > 1 else obj.iElemId
        self.iOrientNodeId = param[2] if len(param) > 2 else obj.iOrientNodeId
        return self
    def __str__(self):
        obj = ERIBEAM_ORI_NODEID_PROP()
        paramArgs = []
        if self.iPropId != obj.iPropId:
            paramArgs.append('iPropId={0}'.format(getValueStr(self.iPropId)))
        if self.iElemId != obj.iElemId:
            paramArgs.append('iElemId={0}'.format(getValueStr(self.iElemId)))
        if self.iOrientNodeId != obj.iOrientNodeId:
            paramArgs.append('iOrientNodeId={0}'.format(getValueStr(self.iOrientNodeId)))
        return 'ERIBEAM_ORI_NODEID_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iPropId,
            self.iElemId,
            self.iOrientNodeId) + rightBracket

class ERIBEAM_OFFSET_VEC_PROP:
    def __init__(self,
        iPropId=0,
        iElemId=0,
        dlOffsetVec=[0, 0, 0]):
        self.iPropId = iPropId
        self.iElemId = iElemId
        self.dlOffsetVec = dlOffsetVec
    def isDefault(self):
        obj = ERIBEAM_OFFSET_VEC_PROP()
        return self.iPropId == obj.iPropId and \
            self.iElemId == obj.iElemId and \
            self.dlOffsetVec == obj.dlOffsetVec
    def fromList(self, param):
        obj = ERIBEAM_OFFSET_VEC_PROP()
        self.iPropId = param[0] if len(param) > 0 else obj.iPropId
        self.iElemId = param[1] if len(param) > 1 else obj.iElemId
        self.dlOffsetVec = [normalizeDoubleType(tok) for tok in param[2]] if len(param) > 2 else obj.dlOffsetVec
        return self
    def __str__(self):
        obj = ERIBEAM_OFFSET_VEC_PROP()
        paramArgs = []
        if self.iPropId != obj.iPropId:
            paramArgs.append('iPropId={0}'.format(getValueStr(self.iPropId)))
        if self.iElemId != obj.iElemId:
            paramArgs.append('iElemId={0}'.format(getValueStr(self.iElemId)))
        if self.dlOffsetVec != obj.dlOffsetVec:
            paramArgs.append('dlOffsetVec={0}'.format(getValueStr(self.dlOffsetVec)))
        return 'ERIBEAM_OFFSET_VEC_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iPropId,
            self.iElemId,
            self.dlOffsetVec) + rightBracket

class ERIBEAM_PIN_A_PROP:
    def __init__(self,
        iPropId=0,
        iElemId=0,
        iPinA=0):
        self.iPropId = iPropId
        self.iElemId = iElemId
        self.iPinA = iPinA
    def isDefault(self):
        obj = ERIBEAM_PIN_A_PROP()
        return self.iPropId == obj.iPropId and \
            self.iElemId == obj.iElemId and \
            self.iPinA == obj.iPinA
    def fromList(self, param):
        obj = ERIBEAM_PIN_A_PROP()
        self.iPropId = param[0] if len(param) > 0 else obj.iPropId
        self.iElemId = param[1] if len(param) > 1 else obj.iElemId
        self.iPinA = param[2] if len(param) > 2 else obj.iPinA
        return self
    def __str__(self):
        obj = ERIBEAM_PIN_A_PROP()
        paramArgs = []
        if self.iPropId != obj.iPropId:
            paramArgs.append('iPropId={0}'.format(getValueStr(self.iPropId)))
        if self.iElemId != obj.iElemId:
            paramArgs.append('iElemId={0}'.format(getValueStr(self.iElemId)))
        if self.iPinA != obj.iPinA:
            paramArgs.append('iPinA={0}'.format(getValueStr(self.iPinA)))
        return 'ERIBEAM_PIN_A_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iPropId,
            self.iElemId,
            self.iPinA) + rightBracket

class ERIBEAM_PIN_B_PROP:
    def __init__(self,
        iPropId=0,
        iElemId=0,
        iPinB=0):
        self.iPropId = iPropId
        self.iElemId = iElemId
        self.iPinB = iPinB
    def isDefault(self):
        obj = ERIBEAM_PIN_B_PROP()
        return self.iPropId == obj.iPropId and \
            self.iElemId == obj.iElemId and \
            self.iPinB == obj.iPinB
    def fromList(self, param):
        obj = ERIBEAM_PIN_B_PROP()
        self.iPropId = param[0] if len(param) > 0 else obj.iPropId
        self.iElemId = param[1] if len(param) > 1 else obj.iElemId
        self.iPinB = param[2] if len(param) > 2 else obj.iPinB
        return self
    def __str__(self):
        obj = ERIBEAM_PIN_B_PROP()
        paramArgs = []
        if self.iPropId != obj.iPropId:
            paramArgs.append('iPropId={0}'.format(getValueStr(self.iPropId)))
        if self.iElemId != obj.iElemId:
            paramArgs.append('iElemId={0}'.format(getValueStr(self.iElemId)))
        if self.iPinB != obj.iPinB:
            paramArgs.append('iPinB={0}'.format(getValueStr(self.iPinB)))
        return 'ERIBEAM_PIN_B_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iPropId,
            self.iElemId,
            self.iPinB) + rightBracket

class ERIBEAM_WARP_PROP:
    def __init__(self,
        iPropId=0,
        iElemId=0,
        dWarp=0):
        self.iPropId = iPropId
        self.iElemId = iElemId
        self.dWarp = dWarp
    def isDefault(self):
        obj = ERIBEAM_WARP_PROP()
        return self.iPropId == obj.iPropId and \
            self.iElemId == obj.iElemId and \
            self.dWarp == obj.dWarp
    def fromList(self, param):
        obj = ERIBEAM_WARP_PROP()
        self.iPropId = param[0] if len(param) > 0 else obj.iPropId
        self.iElemId = param[1] if len(param) > 1 else obj.iElemId
        self.dWarp = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dWarp
        return self
    def __str__(self):
        obj = ERIBEAM_WARP_PROP()
        paramArgs = []
        if self.iPropId != obj.iPropId:
            paramArgs.append('iPropId={0}'.format(getValueStr(self.iPropId)))
        if self.iElemId != obj.iElemId:
            paramArgs.append('iElemId={0}'.format(getValueStr(self.iElemId)))
        if self.dWarp != obj.dWarp:
            paramArgs.append('dWarp={0}'.format(getValueStr(self.dWarp)))
        return 'ERIBEAM_WARP_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iPropId,
            self.iElemId,
            self.dWarp) + rightBracket

class DOFSET_LBC:
    def __init__(self,
        iDwDof=0,
        crCurCoord=None,
        crTable=None):
        self.iDwDof = iDwDof
        self.crCurCoord = crCurCoord
        self.crTable = crTable
    def isDefault(self):
        obj = DOFSET_LBC()
        return self.iDwDof == obj.iDwDof and \
            self.crCurCoord == obj.crCurCoord and \
            self.crTable == obj.crTable
    def fromList(self, param):
        obj = DOFSET_LBC()
        self.iDwDof = param[0] if len(param) > 0 else obj.iDwDof
        self.crCurCoord = getCursorValue(param[1]) if len(param) > 1 else obj.crCurCoord
        self.crTable = getCursorValue(param[2]) if len(param) > 2 else obj.crTable
        return self
    def __str__(self):
        obj = DOFSET_LBC()
        paramArgs = []
        if self.iDwDof != obj.iDwDof:
            paramArgs.append('iDwDof={0}'.format(getValueStr(self.iDwDof)))
        if self.crCurCoord != obj.crCurCoord:
            paramArgs.append('crCurCoord={0}'.format(getCursorValueStr(self.crCurCoord)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        return 'DOFSET_LBC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iDwDof,
            str(self.crCurCoord) if self.crCurCoord is not None else '0:0',
            str(self.crTable) if self.crTable is not None else '0:0') + rightBracket

class TEMP_LOAD_LBC:
    def __init__(self,
        iType=0,
        dFTemp=0,
        strFilePathName="",
        crTable=None,
        bUseAsMaterialReferenceTemp=False):
        self.iType = iType
        self.dFTemp = dFTemp
        self.strFilePathName = strFilePathName
        self.crTable = crTable
        self.bUseAsMaterialReferenceTemp = bUseAsMaterialReferenceTemp
    def isDefault(self):
        obj = TEMP_LOAD_LBC()
        return self.iType == obj.iType and \
            self.dFTemp == obj.dFTemp and \
            self.strFilePathName == obj.strFilePathName and \
            self.crTable == obj.crTable and \
            self.bUseAsMaterialReferenceTemp == obj.bUseAsMaterialReferenceTemp
    def fromList(self, param):
        obj = TEMP_LOAD_LBC()
        self.iType = param[0] if len(param) > 0 else obj.iType
        self.dFTemp = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dFTemp
        self.strFilePathName = param[2] if len(param) > 2 else obj.strFilePathName
        self.crTable = getCursorValue(param[3]) if len(param) > 3 else obj.crTable
        self.bUseAsMaterialReferenceTemp = getBoolValue(param[4]) if len(param) > 4 else obj.bUseAsMaterialReferenceTemp
        return self
    def __str__(self):
        obj = TEMP_LOAD_LBC()
        paramArgs = []
        if self.iType != obj.iType:
            paramArgs.append('iType={0}'.format(getValueStr(self.iType)))
        if self.dFTemp != obj.dFTemp:
            paramArgs.append('dFTemp={0}'.format(getValueStr(self.dFTemp)))
        if self.strFilePathName != obj.strFilePathName:
            paramArgs.append('strFilePathName={0}'.format('"' + self.strFilePathName + '"'))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        if self.bUseAsMaterialReferenceTemp != obj.bUseAsMaterialReferenceTemp:
            paramArgs.append('bUseAsMaterialReferenceTemp={0}'.format(getBoolStr(self.bUseAsMaterialReferenceTemp)))
        return 'TEMP_LOAD_LBC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            self.iType,
            self.dFTemp,
            '"' + self.strFilePathName + '"',
            str(self.crTable) if self.crTable is not None else '0:0',
            1 if self.bUseAsMaterialReferenceTemp else 0) + rightBracket

class COMPOSITE_2D_SHELL_PROP:
    def __init__(self,
        iPID=0,
        dZ0=0,
        dNSM=0,
        dSB=0,
        iFT=0,
        dTREF=0,
        dGE=0,
        iLAM=0,
        iMID=0,
        iSOUT=0,
        dZOFF=0,
        iMatOrientType=0,
        vecMatOrient=[0, 0, 0],
        crLocalCS=None):
        self.iPID = iPID
        self.dZ0 = dZ0
        self.dNSM = dNSM
        self.dSB = dSB
        self.iFT = iFT
        self.dTREF = dTREF
        self.dGE = dGE
        self.iLAM = iLAM
        self.iMID = iMID
        self.iSOUT = iSOUT
        self.dZOFF = dZOFF
        self.iMatOrientType = iMatOrientType
        self.vecMatOrient = vecMatOrient
        self.crLocalCS = crLocalCS
    def isDefault(self):
        obj = COMPOSITE_2D_SHELL_PROP()
        return self.iPID == obj.iPID and \
            self.dZ0 == obj.dZ0 and \
            self.dNSM == obj.dNSM and \
            self.dSB == obj.dSB and \
            self.iFT == obj.iFT and \
            self.dTREF == obj.dTREF and \
            self.dGE == obj.dGE and \
            self.iLAM == obj.iLAM and \
            self.iMID == obj.iMID and \
            self.iSOUT == obj.iSOUT and \
            self.dZOFF == obj.dZOFF and \
            self.iMatOrientType == obj.iMatOrientType and \
            self.vecMatOrient == obj.vecMatOrient and \
            self.crLocalCS == obj.crLocalCS
    def fromList(self, param):
        obj = COMPOSITE_2D_SHELL_PROP()
        self.iPID = param[0] if len(param) > 0 else obj.iPID
        self.dZ0 = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dZ0
        self.dNSM = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dNSM
        self.dSB = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dSB
        self.iFT = param[4] if len(param) > 4 else obj.iFT
        self.dTREF = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dTREF
        self.dGE = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dGE
        self.iLAM = param[7] if len(param) > 7 else obj.iLAM
        self.iMID = param[8] if len(param) > 8 else obj.iMID
        self.iSOUT = param[9] if len(param) > 9 else obj.iSOUT
        self.dZOFF = normalizeDoubleType(param[10]) if len(param) > 10 else obj.dZOFF
        self.iMatOrientType = param[11] if len(param) > 11 else obj.iMatOrientType
        self.vecMatOrient = [normalizeDoubleType(tok) for tok in param[12]] if len(param) > 12 else obj.vecMatOrient
        self.crLocalCS = getCursorValue(param[13]) if len(param) > 13 else obj.crLocalCS
        return self
    def __str__(self):
        obj = COMPOSITE_2D_SHELL_PROP()
        paramArgs = []
        if self.iPID != obj.iPID:
            paramArgs.append('iPID={0}'.format(getValueStr(self.iPID)))
        if self.dZ0 != obj.dZ0:
            paramArgs.append('dZ0={0}'.format(getValueStr(self.dZ0)))
        if self.dNSM != obj.dNSM:
            paramArgs.append('dNSM={0}'.format(getValueStr(self.dNSM)))
        if self.dSB != obj.dSB:
            paramArgs.append('dSB={0}'.format(getValueStr(self.dSB)))
        if self.iFT != obj.iFT:
            paramArgs.append('iFT={0}'.format(getValueStr(self.iFT)))
        if self.dTREF != obj.dTREF:
            paramArgs.append('dTREF={0}'.format(getValueStr(self.dTREF)))
        if self.dGE != obj.dGE:
            paramArgs.append('dGE={0}'.format(getValueStr(self.dGE)))
        if self.iLAM != obj.iLAM:
            paramArgs.append('iLAM={0}'.format(getValueStr(self.iLAM)))
        if self.iMID != obj.iMID:
            paramArgs.append('iMID={0}'.format(getValueStr(self.iMID)))
        if self.iSOUT != obj.iSOUT:
            paramArgs.append('iSOUT={0}'.format(getValueStr(self.iSOUT)))
        if self.dZOFF != obj.dZOFF:
            paramArgs.append('dZOFF={0}'.format(getValueStr(self.dZOFF)))
        if self.iMatOrientType != obj.iMatOrientType:
            paramArgs.append('iMatOrientType={0}'.format(getValueStr(self.iMatOrientType)))
        if self.vecMatOrient != obj.vecMatOrient:
            paramArgs.append('vecMatOrient={0}'.format(getValueStr(self.vecMatOrient)))
        if self.crLocalCS != obj.crLocalCS:
            paramArgs.append('crLocalCS={0}'.format(getCursorValueStr(self.crLocalCS)))
        return 'COMPOSITE_2D_SHELL_PROP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}'.format(
            self.iPID,
            self.dZ0,
            self.dNSM,
            self.dSB,
            self.iFT,
            self.dTREF,
            self.dGE,
            self.iLAM,
            self.iMID,
            self.iSOUT,
            self.dZOFF,
            self.iMatOrientType,
            self.vecMatOrient,
            str(self.crLocalCS) if self.crLocalCS is not None else '0:0') + rightBracket

class LBC_CENTRIFUGAL_FORCE_CS_DATA:
    def __init__(self,
        fVelocity=DFLT_DBL,
        fAcceleration=DFLT_DBL,
        iAxisDirection=2,
        iVelocityUnit=0,
        iAccelerationUnit=0,
        curCoord=None):
        self.fVelocity = fVelocity
        self.fAcceleration = fAcceleration
        self.iAxisDirection = iAxisDirection
        self.iVelocityUnit = iVelocityUnit
        self.iAccelerationUnit = iAccelerationUnit
        self.curCoord = curCoord
    def isDefault(self):
        obj = LBC_CENTRIFUGAL_FORCE_CS_DATA()
        return self.fVelocity == obj.fVelocity and \
            self.fAcceleration == obj.fAcceleration and \
            self.iAxisDirection == obj.iAxisDirection and \
            self.iVelocityUnit == obj.iVelocityUnit and \
            self.iAccelerationUnit == obj.iAccelerationUnit and \
            self.curCoord == obj.curCoord
    def fromList(self, param):
        obj = LBC_CENTRIFUGAL_FORCE_CS_DATA()
        self.fVelocity = normalizeDoubleType(param[0]) if len(param) > 0 else obj.fVelocity
        self.fAcceleration = normalizeDoubleType(param[1]) if len(param) > 1 else obj.fAcceleration
        self.iAxisDirection = param[2] if len(param) > 2 else obj.iAxisDirection
        self.iVelocityUnit = param[3] if len(param) > 3 else obj.iVelocityUnit
        self.iAccelerationUnit = param[4] if len(param) > 4 else obj.iAccelerationUnit
        self.curCoord = getCursorValue(param[5]) if len(param) > 5 else obj.curCoord
        return self
    def __str__(self):
        obj = LBC_CENTRIFUGAL_FORCE_CS_DATA()
        paramArgs = []
        if self.fVelocity != obj.fVelocity:
            paramArgs.append('fVelocity={0}'.format(getValueStr(self.fVelocity)))
        if self.fAcceleration != obj.fAcceleration:
            paramArgs.append('fAcceleration={0}'.format(getValueStr(self.fAcceleration)))
        if self.iAxisDirection != obj.iAxisDirection:
            paramArgs.append('iAxisDirection={0}'.format(getValueStr(self.iAxisDirection)))
        if self.iVelocityUnit != obj.iVelocityUnit:
            paramArgs.append('iVelocityUnit={0}'.format(getValueStr(self.iVelocityUnit)))
        if self.iAccelerationUnit != obj.iAccelerationUnit:
            paramArgs.append('iAccelerationUnit={0}'.format(getValueStr(self.iAccelerationUnit)))
        if self.curCoord != obj.curCoord:
            paramArgs.append('curCoord={0}'.format(getCursorValueStr(self.curCoord)))
        return 'LBC_CENTRIFUGAL_FORCE_CS_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            self.fVelocity,
            self.fAcceleration,
            self.iAxisDirection,
            self.iVelocityUnit,
            self.iAccelerationUnit,
            str(self.curCoord) if self.curCoord is not None else '0:0') + rightBracket

class LBC_THERMAL_CONVECTION_DATA:
    def __init__(self,
        ExtTemp=DFLT_DBL,
        crTableTimeTemp=None,
        dcoef=DFLT_DBL,
        crTableTimeCoeff=None,
        crTableTempCoeff=None):
        self.ExtTemp = ExtTemp
        self.crTableTimeTemp = crTableTimeTemp
        self.dcoef = dcoef
        self.crTableTimeCoeff = crTableTimeCoeff
        self.crTableTempCoeff = crTableTempCoeff
    def isDefault(self):
        obj = LBC_THERMAL_CONVECTION_DATA()
        return self.ExtTemp == obj.ExtTemp and \
            self.crTableTimeTemp == obj.crTableTimeTemp and \
            self.dcoef == obj.dcoef and \
            self.crTableTimeCoeff == obj.crTableTimeCoeff and \
            self.crTableTempCoeff == obj.crTableTempCoeff
    def fromList(self, param):
        obj = LBC_THERMAL_CONVECTION_DATA()
        self.ExtTemp = normalizeDoubleType(param[0]) if len(param) > 0 else obj.ExtTemp
        self.crTableTimeTemp = getCursorValue(param[1]) if len(param) > 1 else obj.crTableTimeTemp
        self.dcoef = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dcoef
        self.crTableTimeCoeff = getCursorValue(param[3]) if len(param) > 3 else obj.crTableTimeCoeff
        self.crTableTempCoeff = getCursorValue(param[4]) if len(param) > 4 else obj.crTableTempCoeff
        return self
    def __str__(self):
        obj = LBC_THERMAL_CONVECTION_DATA()
        paramArgs = []
        if self.ExtTemp != obj.ExtTemp:
            paramArgs.append('ExtTemp={0}'.format(getValueStr(self.ExtTemp)))
        if self.crTableTimeTemp != obj.crTableTimeTemp:
            paramArgs.append('crTableTimeTemp={0}'.format(getCursorValueStr(self.crTableTimeTemp)))
        if self.dcoef != obj.dcoef:
            paramArgs.append('dcoef={0}'.format(getValueStr(self.dcoef)))
        if self.crTableTimeCoeff != obj.crTableTimeCoeff:
            paramArgs.append('crTableTimeCoeff={0}'.format(getCursorValueStr(self.crTableTimeCoeff)))
        if self.crTableTempCoeff != obj.crTableTempCoeff:
            paramArgs.append('crTableTempCoeff={0}'.format(getCursorValueStr(self.crTableTempCoeff)))
        return 'LBC_THERMAL_CONVECTION_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            self.ExtTemp,
            str(self.crTableTimeTemp) if self.crTableTimeTemp is not None else '0:0',
            self.dcoef,
            str(self.crTableTimeCoeff) if self.crTableTimeCoeff is not None else '0:0',
            str(self.crTableTempCoeff) if self.crTableTempCoeff is not None else '0:0') + rightBracket

class TSSOLVER_CONTACT:
    def __init__(self,
        iType=0,
        iAlg=0,
        dCINTERF=DFLT_DBL,
        dFRIC=DFLT_DBL,
        dSLIDE=DFLT_DBL,
        iICOORD=DFLT_INT,
        dSFACT=DFLT_DBL,
        iIshellelemfaceSlave=1,
        iIshellelemfaceMaster=1):
        self.iType = iType
        self.iAlg = iAlg
        self.dCINTERF = dCINTERF
        self.dFRIC = dFRIC
        self.dSLIDE = dSLIDE
        self.iICOORD = iICOORD
        self.dSFACT = dSFACT
        self.iIshellelemfaceSlave = iIshellelemfaceSlave
        self.iIshellelemfaceMaster = iIshellelemfaceMaster
    def isDefault(self):
        obj = TSSOLVER_CONTACT()
        return self.iType == obj.iType and \
            self.iAlg == obj.iAlg and \
            self.dCINTERF == obj.dCINTERF and \
            self.dFRIC == obj.dFRIC and \
            self.dSLIDE == obj.dSLIDE and \
            self.iICOORD == obj.iICOORD and \
            self.dSFACT == obj.dSFACT and \
            self.iIshellelemfaceSlave == obj.iIshellelemfaceSlave and \
            self.iIshellelemfaceMaster == obj.iIshellelemfaceMaster
    def fromList(self, param):
        obj = TSSOLVER_CONTACT()
        self.iType = param[0] if len(param) > 0 else obj.iType
        self.iAlg = param[1] if len(param) > 1 else obj.iAlg
        self.dCINTERF = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dCINTERF
        self.dFRIC = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dFRIC
        self.dSLIDE = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dSLIDE
        self.iICOORD = param[5] if len(param) > 5 else obj.iICOORD
        self.dSFACT = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dSFACT
        self.iIshellelemfaceSlave = param[7] if len(param) > 7 else obj.iIshellelemfaceSlave
        self.iIshellelemfaceMaster = param[8] if len(param) > 8 else obj.iIshellelemfaceMaster
        return self
    def __str__(self):
        obj = TSSOLVER_CONTACT()
        paramArgs = []
        if self.iType != obj.iType:
            paramArgs.append('iType={0}'.format(getValueStr(self.iType)))
        if self.iAlg != obj.iAlg:
            paramArgs.append('iAlg={0}'.format(getValueStr(self.iAlg)))
        if self.dCINTERF != obj.dCINTERF:
            paramArgs.append('dCINTERF={0}'.format(getValueStr(self.dCINTERF)))
        if self.dFRIC != obj.dFRIC:
            paramArgs.append('dFRIC={0}'.format(getValueStr(self.dFRIC)))
        if self.dSLIDE != obj.dSLIDE:
            paramArgs.append('dSLIDE={0}'.format(getValueStr(self.dSLIDE)))
        if self.iICOORD != obj.iICOORD:
            paramArgs.append('iICOORD={0}'.format(getValueStr(self.iICOORD)))
        if self.dSFACT != obj.dSFACT:
            paramArgs.append('dSFACT={0}'.format(getValueStr(self.dSFACT)))
        if self.iIshellelemfaceSlave != obj.iIshellelemfaceSlave:
            paramArgs.append('iIshellelemfaceSlave={0}'.format(getValueStr(self.iIshellelemfaceSlave)))
        if self.iIshellelemfaceMaster != obj.iIshellelemfaceMaster:
            paramArgs.append('iIshellelemfaceMaster={0}'.format(getValueStr(self.iIshellelemfaceMaster)))
        return 'TSSOLVER_CONTACT({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            self.iType,
            self.iAlg,
            self.dCINTERF,
            self.dFRIC,
            self.dSLIDE,
            self.iICOORD,
            self.dSFACT,
            self.iIshellelemfaceSlave,
            self.iIshellelemfaceMaster) + rightBracket

class ANSYS_CONTACT:
    def __init__(self,
        dFricCoef=DFLT_DBL,
        dPenaStiffness=DFLT_DBL,
        dPetrTolerance=DFLT_DBL,
        iStiffUpdate=2,
        iAlgorithm=2,
        iDetec=2,
        iBehavior=5,
        iIniPenetr=0):
        self.dFricCoef = dFricCoef
        self.dPenaStiffness = dPenaStiffness
        self.dPetrTolerance = dPetrTolerance
        self.iStiffUpdate = iStiffUpdate
        self.iAlgorithm = iAlgorithm
        self.iDetec = iDetec
        self.iBehavior = iBehavior
        self.iIniPenetr = iIniPenetr
    def isDefault(self):
        obj = ANSYS_CONTACT()
        return self.dFricCoef == obj.dFricCoef and \
            self.dPenaStiffness == obj.dPenaStiffness and \
            self.dPetrTolerance == obj.dPetrTolerance and \
            self.iStiffUpdate == obj.iStiffUpdate and \
            self.iAlgorithm == obj.iAlgorithm and \
            self.iDetec == obj.iDetec and \
            self.iBehavior == obj.iBehavior and \
            self.iIniPenetr == obj.iIniPenetr
    def fromList(self, param):
        obj = ANSYS_CONTACT()
        self.dFricCoef = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dFricCoef
        self.dPenaStiffness = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dPenaStiffness
        self.dPetrTolerance = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dPetrTolerance
        self.iStiffUpdate = param[3] if len(param) > 3 else obj.iStiffUpdate
        self.iAlgorithm = param[4] if len(param) > 4 else obj.iAlgorithm
        self.iDetec = param[5] if len(param) > 5 else obj.iDetec
        self.iBehavior = param[6] if len(param) > 6 else obj.iBehavior
        self.iIniPenetr = param[7] if len(param) > 7 else obj.iIniPenetr
        return self
    def __str__(self):
        obj = ANSYS_CONTACT()
        paramArgs = []
        if self.dFricCoef != obj.dFricCoef:
            paramArgs.append('dFricCoef={0}'.format(getValueStr(self.dFricCoef)))
        if self.dPenaStiffness != obj.dPenaStiffness:
            paramArgs.append('dPenaStiffness={0}'.format(getValueStr(self.dPenaStiffness)))
        if self.dPetrTolerance != obj.dPetrTolerance:
            paramArgs.append('dPetrTolerance={0}'.format(getValueStr(self.dPetrTolerance)))
        if self.iStiffUpdate != obj.iStiffUpdate:
            paramArgs.append('iStiffUpdate={0}'.format(getValueStr(self.iStiffUpdate)))
        if self.iAlgorithm != obj.iAlgorithm:
            paramArgs.append('iAlgorithm={0}'.format(getValueStr(self.iAlgorithm)))
        if self.iDetec != obj.iDetec:
            paramArgs.append('iDetec={0}'.format(getValueStr(self.iDetec)))
        if self.iBehavior != obj.iBehavior:
            paramArgs.append('iBehavior={0}'.format(getValueStr(self.iBehavior)))
        if self.iIniPenetr != obj.iIniPenetr:
            paramArgs.append('iIniPenetr={0}'.format(getValueStr(self.iIniPenetr)))
        return 'ANSYS_CONTACT({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(
            self.dFricCoef,
            self.dPenaStiffness,
            self.dPetrTolerance,
            self.iStiffUpdate,
            self.iAlgorithm,
            self.iDetec,
            self.iBehavior,
            self.iIniPenetr) + rightBracket

class CAD_ELYSIUM_PARAM_DATA:
    def __init__(self,
        chord_height_tolerance=1.0,
        angle_tolerance_degree=5.0,
        convert_isolated_curve=0,
        iges_fixedCurevePreference=0,
        iges_autoStitch=1,
        iges_stitchTolerance=0.1,
        catia_convertNotShowedElement=0,
        catia_convertNotShowedInstance=0,
        catia_convertAxis=1,
        step_createSeam=1,
        step_pointTolerance=0.0,
        acis_healAcisBeforeVersion=0,
        jt_convertGeometryType=2,
        jt_convertGeneralBody=1,
        jt_convertAxis=1,
        jt_convertCenterLine=0,
        dek_cleanSelfIntersectingLoop=2,
        point_coincident_tolerance=0.01,
        dek_volumeToBody=4):
        self.chord_height_tolerance = chord_height_tolerance
        self.angle_tolerance_degree = angle_tolerance_degree
        self.convert_isolated_curve = convert_isolated_curve
        self.iges_fixedCurevePreference = iges_fixedCurevePreference
        self.iges_autoStitch = iges_autoStitch
        self.iges_stitchTolerance = iges_stitchTolerance
        self.catia_convertNotShowedElement = catia_convertNotShowedElement
        self.catia_convertNotShowedInstance = catia_convertNotShowedInstance
        self.catia_convertAxis = catia_convertAxis
        self.step_createSeam = step_createSeam
        self.step_pointTolerance = step_pointTolerance
        self.acis_healAcisBeforeVersion = acis_healAcisBeforeVersion
        self.jt_convertGeometryType = jt_convertGeometryType
        self.jt_convertGeneralBody = jt_convertGeneralBody
        self.jt_convertAxis = jt_convertAxis
        self.jt_convertCenterLine = jt_convertCenterLine
        self.dek_cleanSelfIntersectingLoop = dek_cleanSelfIntersectingLoop
        self.point_coincident_tolerance = point_coincident_tolerance
        self.dek_volumeToBody = dek_volumeToBody
    def isDefault(self):
        obj = CAD_ELYSIUM_PARAM_DATA()
        return self.chord_height_tolerance == obj.chord_height_tolerance and \
            self.angle_tolerance_degree == obj.angle_tolerance_degree and \
            self.convert_isolated_curve == obj.convert_isolated_curve and \
            self.iges_fixedCurevePreference == obj.iges_fixedCurevePreference and \
            self.iges_autoStitch == obj.iges_autoStitch and \
            self.iges_stitchTolerance == obj.iges_stitchTolerance and \
            self.catia_convertNotShowedElement == obj.catia_convertNotShowedElement and \
            self.catia_convertNotShowedInstance == obj.catia_convertNotShowedInstance and \
            self.catia_convertAxis == obj.catia_convertAxis and \
            self.step_createSeam == obj.step_createSeam and \
            self.step_pointTolerance == obj.step_pointTolerance and \
            self.acis_healAcisBeforeVersion == obj.acis_healAcisBeforeVersion and \
            self.jt_convertGeometryType == obj.jt_convertGeometryType and \
            self.jt_convertGeneralBody == obj.jt_convertGeneralBody and \
            self.jt_convertAxis == obj.jt_convertAxis and \
            self.jt_convertCenterLine == obj.jt_convertCenterLine and \
            self.dek_cleanSelfIntersectingLoop == obj.dek_cleanSelfIntersectingLoop and \
            self.point_coincident_tolerance == obj.point_coincident_tolerance and \
            self.dek_volumeToBody == obj.dek_volumeToBody
    def fromList(self, cadElysiumParamData):
        obj = CAD_ELYSIUM_PARAM_DATA()
        self.chord_height_tolerance = normalizeDoubleType(cadElysiumParamData[0]) if len(cadElysiumParamData) > 0 else obj.chord_height_tolerance
        self.angle_tolerance_degree = normalizeDoubleType(cadElysiumParamData[1]) if len(cadElysiumParamData) > 1 else obj.angle_tolerance_degree
        self.convert_isolated_curve = cadElysiumParamData[2] if len(cadElysiumParamData) > 2 else obj.convert_isolated_curve
        self.iges_fixedCurevePreference = cadElysiumParamData[3] if len(cadElysiumParamData) > 3 else obj.iges_fixedCurevePreference
        self.iges_autoStitch = cadElysiumParamData[4] if len(cadElysiumParamData) > 4 else obj.iges_autoStitch
        self.iges_stitchTolerance = normalizeDoubleType(cadElysiumParamData[5]) if len(cadElysiumParamData) > 5 else obj.iges_stitchTolerance
        self.catia_convertNotShowedElement = cadElysiumParamData[6] if len(cadElysiumParamData) > 6 else obj.catia_convertNotShowedElement
        self.catia_convertNotShowedInstance = cadElysiumParamData[7] if len(cadElysiumParamData) > 7 else obj.catia_convertNotShowedInstance
        self.catia_convertAxis = cadElysiumParamData[8] if len(cadElysiumParamData) > 8 else obj.catia_convertAxis
        self.step_createSeam = cadElysiumParamData[9] if len(cadElysiumParamData) > 9 else obj.step_createSeam
        self.step_pointTolerance = normalizeDoubleType(cadElysiumParamData[10]) if len(cadElysiumParamData) > 10 else obj.step_pointTolerance
        self.acis_healAcisBeforeVersion = cadElysiumParamData[11] if len(cadElysiumParamData) > 11 else obj.acis_healAcisBeforeVersion
        self.jt_convertGeometryType = cadElysiumParamData[12] if len(cadElysiumParamData) > 12 else obj.jt_convertGeometryType
        self.jt_convertGeneralBody = cadElysiumParamData[13] if len(cadElysiumParamData) > 13 else obj.jt_convertGeneralBody
        self.jt_convertAxis = cadElysiumParamData[14] if len(cadElysiumParamData) > 14 else obj.jt_convertAxis
        self.jt_convertCenterLine = cadElysiumParamData[15] if len(cadElysiumParamData) > 15 else obj.jt_convertCenterLine
        self.dek_cleanSelfIntersectingLoop = cadElysiumParamData[16] if len(cadElysiumParamData) > 16 else obj.dek_cleanSelfIntersectingLoop
        self.point_coincident_tolerance = normalizeDoubleType(cadElysiumParamData[17]) if len(cadElysiumParamData) > 17 else obj.point_coincident_tolerance
        self.dek_volumeToBody = cadElysiumParamData[18] if len(cadElysiumParamData) > 18 else obj.dek_volumeToBody
        return self
    def __str__(self):
        obj = CAD_ELYSIUM_PARAM_DATA()
        paramArgs = []
        if self.chord_height_tolerance != obj.chord_height_tolerance:
            paramArgs.append('chord_height_tolerance={0}'.format(getValueStr(self.chord_height_tolerance)))
        if self.angle_tolerance_degree != obj.angle_tolerance_degree:
            paramArgs.append('angle_tolerance_degree={0}'.format(getValueStr(self.angle_tolerance_degree)))
        if self.convert_isolated_curve != obj.convert_isolated_curve:
            paramArgs.append('convert_isolated_curve={0}'.format(getValueStr(self.convert_isolated_curve)))
        if self.iges_fixedCurevePreference != obj.iges_fixedCurevePreference:
            paramArgs.append('iges_fixedCurevePreference={0}'.format(getValueStr(self.iges_fixedCurevePreference)))
        if self.iges_autoStitch != obj.iges_autoStitch:
            paramArgs.append('iges_autoStitch={0}'.format(getValueStr(self.iges_autoStitch)))
        if self.iges_stitchTolerance != obj.iges_stitchTolerance:
            paramArgs.append('iges_stitchTolerance={0}'.format(getValueStr(self.iges_stitchTolerance)))
        if self.catia_convertNotShowedElement != obj.catia_convertNotShowedElement:
            paramArgs.append('catia_convertNotShowedElement={0}'.format(getValueStr(self.catia_convertNotShowedElement)))
        if self.catia_convertNotShowedInstance != obj.catia_convertNotShowedInstance:
            paramArgs.append('catia_convertNotShowedInstance={0}'.format(getValueStr(self.catia_convertNotShowedInstance)))
        if self.catia_convertAxis != obj.catia_convertAxis:
            paramArgs.append('catia_convertAxis={0}'.format(getValueStr(self.catia_convertAxis)))
        if self.step_createSeam != obj.step_createSeam:
            paramArgs.append('step_createSeam={0}'.format(getValueStr(self.step_createSeam)))
        if self.step_pointTolerance != obj.step_pointTolerance:
            paramArgs.append('step_pointTolerance={0}'.format(getValueStr(self.step_pointTolerance)))
        if self.acis_healAcisBeforeVersion != obj.acis_healAcisBeforeVersion:
            paramArgs.append('acis_healAcisBeforeVersion={0}'.format(getValueStr(self.acis_healAcisBeforeVersion)))
        if self.jt_convertGeometryType != obj.jt_convertGeometryType:
            paramArgs.append('jt_convertGeometryType={0}'.format(getValueStr(self.jt_convertGeometryType)))
        if self.jt_convertGeneralBody != obj.jt_convertGeneralBody:
            paramArgs.append('jt_convertGeneralBody={0}'.format(getValueStr(self.jt_convertGeneralBody)))
        if self.jt_convertAxis != obj.jt_convertAxis:
            paramArgs.append('jt_convertAxis={0}'.format(getValueStr(self.jt_convertAxis)))
        if self.jt_convertCenterLine != obj.jt_convertCenterLine:
            paramArgs.append('jt_convertCenterLine={0}'.format(getValueStr(self.jt_convertCenterLine)))
        if self.dek_cleanSelfIntersectingLoop != obj.dek_cleanSelfIntersectingLoop:
            paramArgs.append('dek_cleanSelfIntersectingLoop={0}'.format(getValueStr(self.dek_cleanSelfIntersectingLoop)))
        if self.point_coincident_tolerance != obj.point_coincident_tolerance:
            paramArgs.append('point_coincident_tolerance={0}'.format(getValueStr(self.point_coincident_tolerance)))
        if self.dek_volumeToBody != obj.dek_volumeToBody:
            paramArgs.append('dek_volumeToBody={0}'.format(getValueStr(self.dek_volumeToBody)))
        return 'CAD_ELYSIUM_PARAM_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}'.format(
            self.chord_height_tolerance,
            self.angle_tolerance_degree,
            self.convert_isolated_curve,
            self.iges_fixedCurevePreference,
            self.iges_autoStitch,
            self.iges_stitchTolerance,
            self.catia_convertNotShowedElement,
            self.catia_convertNotShowedInstance,
            self.catia_convertAxis,
            self.step_createSeam,
            self.step_pointTolerance,
            self.acis_healAcisBeforeVersion,
            self.jt_convertGeometryType,
            self.jt_convertGeneralBody,
            self.jt_convertAxis,
            self.jt_convertCenterLine,
            self.dek_cleanSelfIntersectingLoop,
            self.point_coincident_tolerance,
            self.dek_volumeToBody) + rightBracket
    def toNativeStrSpecial(self, isOneParam=True, bSetFaceColor = True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}'.format(
            self.chord_height_tolerance,
            self.angle_tolerance_degree,
            self.convert_isolated_curve,
            self.iges_fixedCurevePreference,
            self.iges_autoStitch,
            self.iges_stitchTolerance,
            self.catia_convertNotShowedElement,
            self.catia_convertNotShowedInstance,
            self.catia_convertAxis,
            self.step_createSeam,
            self.step_pointTolerance,
            self.acis_healAcisBeforeVersion,
            self.jt_convertGeometryType,
            self.jt_convertGeneralBody,
            self.jt_convertAxis,
            self.jt_convertCenterLine,
            1 if bSetFaceColor else 0,
            self.dek_cleanSelfIntersectingLoop,
            self.point_coincident_tolerance,
            self.dek_volumeToBody) + rightBracket

class LOCAL_MESH:
    def __init__(self,
        iEntityType=0,
        bEnableSizeParams=False,
        dAvgElemSize=0.0,
        dMaxElemSize=0.0,
        dMinElemSize=0.0,
        bEnableTrimAngle=False,
        dTrimAngle=0.0,
        bEnableMeshCount=False,
        iNodeCount=0,
        iBiasNodeId=0,
        dBiasFactor=0.0,
        iBiasMethod=0,
        iBiasProgression=0,
        bEnableMeshPattern=False,
        iMeshPatternType=0,
        bEnableKeepEntity=False,
        dFixedPointX=0.0,
        dFixedPointY=0.0,
        dFixedPointZ=0.0,
        iFixedPointId=0,
        bEnableFreezeMesh=False):
        self.iEntityType = iEntityType
        self.bEnableSizeParams = bEnableSizeParams
        self.dAvgElemSize = dAvgElemSize
        self.dMaxElemSize = dMaxElemSize
        self.dMinElemSize = dMinElemSize
        self.bEnableTrimAngle = bEnableTrimAngle
        self.dTrimAngle = dTrimAngle
        self.bEnableMeshCount = bEnableMeshCount
        self.iNodeCount = iNodeCount
        self.iBiasNodeId = iBiasNodeId
        self.dBiasFactor = dBiasFactor
        self.iBiasMethod = iBiasMethod
        self.iBiasProgression = iBiasProgression
        self.bEnableMeshPattern = bEnableMeshPattern
        self.iMeshPatternType = iMeshPatternType
        self.bEnableKeepEntity = bEnableKeepEntity
        self.dFixedPointX = dFixedPointX
        self.dFixedPointY = dFixedPointY
        self.dFixedPointZ = dFixedPointZ
        self.iFixedPointId = iFixedPointId
        self.bEnableFreezeMesh = bEnableFreezeMesh
    def isDefault(self):
        obj = LOCAL_MESH()
        return self.iEntityType == obj.iEntityType and \
            self.bEnableSizeParams == obj.bEnableSizeParams and \
            self.dAvgElemSize == obj.dAvgElemSize and \
            self.dMaxElemSize == obj.dMaxElemSize and \
            self.dMinElemSize == obj.dMinElemSize and \
            self.bEnableTrimAngle == obj.bEnableTrimAngle and \
            self.dTrimAngle == obj.dTrimAngle and \
            self.bEnableMeshCount == obj.bEnableMeshCount and \
            self.iNodeCount == obj.iNodeCount and \
            self.iBiasNodeId == obj.iBiasNodeId and \
            self.dBiasFactor == obj.dBiasFactor and \
            self.iBiasMethod == obj.iBiasMethod and \
            self.iBiasProgression == obj.iBiasProgression and \
            self.bEnableMeshPattern == obj.bEnableMeshPattern and \
            self.iMeshPatternType == obj.iMeshPatternType and \
            self.bEnableKeepEntity == obj.bEnableKeepEntity and \
            self.dFixedPointX == obj.dFixedPointX and \
            self.dFixedPointY == obj.dFixedPointY and \
            self.dFixedPointZ == obj.dFixedPointZ and \
            self.iFixedPointId == obj.iFixedPointId and \
            self.bEnableFreezeMesh == obj.bEnableFreezeMesh
    def fromList(self, localMesh):
        obj = LOCAL_MESH()
        self.iEntityType = localMesh[0] if len(localMesh) > 0 else obj.iEntityType
        self.bEnableSizeParams = getBoolValue(localMesh[1]) if len(localMesh) > 1 else obj.bEnableSizeParams
        self.dAvgElemSize = normalizeDoubleType(localMesh[2]) if len(localMesh) > 2 else obj.dAvgElemSize
        self.dMaxElemSize = normalizeDoubleType(localMesh[3]) if len(localMesh) > 3 else obj.dMaxElemSize
        self.dMinElemSize = normalizeDoubleType(localMesh[4]) if len(localMesh) > 4 else obj.dMinElemSize
        self.bEnableTrimAngle = getBoolValue(localMesh[5]) if len(localMesh) > 5 else obj.bEnableTrimAngle
        self.dTrimAngle = normalizeDoubleType(localMesh[6]) if len(localMesh) > 6 else obj.dTrimAngle
        self.bEnableMeshCount = getBoolValue(localMesh[7]) if len(localMesh) > 7 else obj.bEnableMeshCount
        self.iNodeCount = localMesh[8] if len(localMesh) > 8 else obj.iNodeCount
        self.iBiasNodeId = localMesh[9] if len(localMesh) > 9 else obj.iBiasNodeId
        self.dBiasFactor = normalizeDoubleType(localMesh[10]) if len(localMesh) > 10 else obj.dBiasFactor
        self.iBiasMethod = localMesh[11] if len(localMesh) > 11 else obj.iBiasMethod
        self.iBiasProgression = localMesh[12] if len(localMesh) > 12 else obj.iBiasProgression
        self.bEnableMeshPattern = getBoolValue(localMesh[13]) if len(localMesh) > 13 else obj.bEnableMeshPattern
        self.iMeshPatternType = localMesh[14] if len(localMesh) > 14 else obj.iMeshPatternType
        self.bEnableKeepEntity = getBoolValue(localMesh[15]) if len(localMesh) > 15 else obj.bEnableKeepEntity
        self.dFixedPointX = normalizeDoubleType(localMesh[16]) if len(localMesh) > 16 else obj.dFixedPointX
        self.dFixedPointY = normalizeDoubleType(localMesh[17]) if len(localMesh) > 17 else obj.dFixedPointY
        self.dFixedPointZ = normalizeDoubleType(localMesh[18]) if len(localMesh) > 18 else obj.dFixedPointZ
        self.iFixedPointId = localMesh[19] if len(localMesh) > 19 else obj.iFixedPointId
        self.bEnableFreezeMesh = getBoolValue(localMesh[20]) if len(localMesh) > 20 else obj.bEnableFreezeMesh
        return self
    def __str__(self):
        obj = LOCAL_MESH()
        paramArgs = []
        if self.iEntityType != obj.iEntityType:
            paramArgs.append('iEntityType={0}'.format(getValueStr(self.iEntityType)))
        if self.bEnableSizeParams != obj.bEnableSizeParams:
            paramArgs.append('bEnableSizeParams={0}'.format(getBoolStr(self.bEnableSizeParams)))
        if self.dAvgElemSize != obj.dAvgElemSize:
            paramArgs.append('dAvgElemSize={0}'.format(getValueStr(self.dAvgElemSize)))
        if self.dMaxElemSize != obj.dMaxElemSize:
            paramArgs.append('dMaxElemSize={0}'.format(getValueStr(self.dMaxElemSize)))
        if self.dMinElemSize != obj.dMinElemSize:
            paramArgs.append('dMinElemSize={0}'.format(getValueStr(self.dMinElemSize)))
        if self.bEnableTrimAngle != obj.bEnableTrimAngle:
            paramArgs.append('bEnableTrimAngle={0}'.format(getBoolStr(self.bEnableTrimAngle)))
        if self.dTrimAngle != obj.dTrimAngle:
            paramArgs.append('dTrimAngle={0}'.format(getValueStr(self.dTrimAngle)))
        if self.bEnableMeshCount != obj.bEnableMeshCount:
            paramArgs.append('bEnableMeshCount={0}'.format(getBoolStr(self.bEnableMeshCount)))
        if self.iNodeCount != obj.iNodeCount:
            paramArgs.append('iNodeCount={0}'.format(getValueStr(self.iNodeCount)))
        if self.iBiasNodeId != obj.iBiasNodeId:
            paramArgs.append('iBiasNodeId={0}'.format(getValueStr(self.iBiasNodeId)))
        if self.dBiasFactor != obj.dBiasFactor:
            paramArgs.append('dBiasFactor={0}'.format(getValueStr(self.dBiasFactor)))
        if self.iBiasMethod != obj.iBiasMethod:
            paramArgs.append('iBiasMethod={0}'.format(getValueStr(self.iBiasMethod)))
        if self.iBiasProgression != obj.iBiasProgression:
            paramArgs.append('iBiasProgression={0}'.format(getValueStr(self.iBiasProgression)))
        if self.bEnableMeshPattern != obj.bEnableMeshPattern:
            paramArgs.append('bEnableMeshPattern={0}'.format(getBoolStr(self.bEnableMeshPattern)))
        if self.iMeshPatternType != obj.iMeshPatternType:
            paramArgs.append('iMeshPatternType={0}'.format(getValueStr(self.iMeshPatternType)))
        if self.bEnableKeepEntity != obj.bEnableKeepEntity:
            paramArgs.append('bEnableKeepEntity={0}'.format(getBoolStr(self.bEnableKeepEntity)))
        if self.dFixedPointX != obj.dFixedPointX:
            paramArgs.append('dFixedPointX={0}'.format(getValueStr(self.dFixedPointX)))
        if self.dFixedPointY != obj.dFixedPointY:
            paramArgs.append('dFixedPointY={0}'.format(getValueStr(self.dFixedPointY)))
        if self.dFixedPointZ != obj.dFixedPointZ:
            paramArgs.append('dFixedPointZ={0}'.format(getValueStr(self.dFixedPointZ)))
        if self.iFixedPointId != obj.iFixedPointId:
            paramArgs.append('iFixedPointId={0}'.format(getValueStr(self.iFixedPointId)))
        if self.bEnableFreezeMesh != obj.bEnableFreezeMesh:
            paramArgs.append('bEnableFreezeMesh={0}'.format(getBoolStr(self.bEnableFreezeMesh)))
        return 'LOCAL_MESH({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '{' if isOneParam else ''
        rightBracket = '}' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}'.format(
            self.iEntityType,
            1 if self.bEnableSizeParams else 0,
            self.dAvgElemSize,
            self.dMaxElemSize,
            self.dMinElemSize,
            1 if self.bEnableTrimAngle else 0,
            self.dTrimAngle,
            1 if self.bEnableMeshCount else 0,
            self.iNodeCount,
            self.iBiasNodeId,
            self.dBiasFactor,
            self.iBiasMethod,
            self.iBiasProgression,
            1 if self.bEnableMeshPattern else 0,
            self.iMeshPatternType,
            1 if self.bEnableKeepEntity else 0,
            self.dFixedPointX,
            self.dFixedPointY,
            self.dFixedPointZ,
            self.iFixedPointId,
            1 if self.bEnableFreezeMesh else 0) + rightBracket

class MPC_CONNECTION:
    def __init__(self,
        dCoef=0.0,
        iDof=0):
        self.dCoef = dCoef
        self.iDof = iDof
    def isDefault(self):
        obj = MPC_CONNECTION()
        return self.dCoef == obj.dCoef and \
            self.iDof == obj.iDof
    def fromList(self, param):
        obj = MPC_CONNECTION()
        self.dCoef = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dCoef
        self.iDof = param[1] if len(param) > 1 else obj.iDof
        return self
    def __str__(self):
        obj = MPC_CONNECTION()
        paramArgs = []
        if self.dCoef != obj.dCoef:
            paramArgs.append('dCoef={0}'.format(getValueStr(self.dCoef)))
        if self.iDof != obj.iDof:
            paramArgs.append('iDof={0}'.format(getValueStr(self.iDof)))
        return 'MPC_CONNECTION({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            self.dCoef,
            self.iDof) + rightBracket

class LBC_CONCENTRATE_FLUX_DATA:
    def __init__(self,
        dFluxValue=0.0,
        crTable=None):
        self.dFluxValue = dFluxValue
        self.crTable = crTable
    def isDefault(self):
        obj = LBC_CONCENTRATE_FLUX_DATA()
        return self.dFluxValue == obj.dFluxValue and \
            self.crTable == obj.crTable
    def fromList(self, param):
        obj = LBC_CONCENTRATE_FLUX_DATA()
        self.dFluxValue = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dFluxValue
        self.crTable = getCursorValue(param[1]) if len(param) > 1 else obj.crTable
        return self
    def __str__(self):
        obj = LBC_CONCENTRATE_FLUX_DATA()
        paramArgs = []
        if self.dFluxValue != obj.dFluxValue:
            paramArgs.append('dFluxValue={0}'.format(getValueStr(self.dFluxValue)))
        if self.crTable != obj.crTable:
            paramArgs.append('crTable={0}'.format(getCursorValueStr(self.crTable)))
        return 'LBC_CONCENTRATE_FLUX_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            self.dFluxValue,
            str(self.crTable) if self.crTable is not None else '0:0') + rightBracket

class ABAQUS_PAIR:
    def __init__(self,
        iEnableChecked=0,
        dlTList=[]):
        self.iEnableChecked = iEnableChecked
        self.dlTList = dlTList
    def isDefault(self):
        obj = ABAQUS_PAIR()
        return self.iEnableChecked == obj.iEnableChecked and \
            self.dlTList == obj.dlTList
    def fromList(self, param):
        obj = ABAQUS_PAIR()
        self.iEnableChecked = param[0] if len(param) > 0 else obj.iEnableChecked
        self.dlTList = [normalizeDoubleType(tok) for tok in param[1]] if len(param) > 1 else obj.dlTList
        return self
    def __str__(self):
        obj = ABAQUS_PAIR()
        paramArgs = []
        if self.iEnableChecked != obj.iEnableChecked:
            paramArgs.append('iEnableChecked={0}'.format(getValueStr(self.iEnableChecked)))
        if self.dlTList != obj.dlTList:
            paramArgs.append('dlTList={0}'.format(getValueStr(self.dlTList)))
        return 'ABAQUS_PAIR({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            self.iEnableChecked,
            self.dlTList) + rightBracket

class SUNSHINE_CONTACT:
    def __init__(self,
        iType=0,
        iAlg=0,
        dERROR=0.0,
        dFRIC=0.0,
        dSLIDE=0.0,
        iICOORD=0,
        dSFACT=0.0,
        dSFACTT=0.0,
        dCDAMP=0.0,
        iIshellelemfaceSlave=0,
        iIshellelemfaceMaster=0,
        dCINTERF=DFLT_DBL,
        iJGLUE=1,
        dSDIST=DFLT_DBL,
        iISTYP=DFLT_DBL,
        ):
        self.iType = iType
        self.iAlg = iAlg
        self.dERROR = dERROR
        self.dFRIC = dFRIC
        self.dSLIDE = dSLIDE
        self.iICOORD = iICOORD
        self.dSFACT = dSFACT
        self.dSFACTT = dSFACTT
        self.dCDAMP = dCDAMP
        self.iIshellelemfaceSlave = iIshellelemfaceSlave
        self.iIshellelemfaceMaster = iIshellelemfaceMaster
        self.dCINTERF = dCINTERF
        self.iJGLUE = iJGLUE
        self.dSDIST = dSDIST
        self.iISTYP = iISTYP
    def isDefault(self):
        obj = SUNSHINE_CONTACT()
        return self.iType == obj.iType and \
            self.iAlg == obj.iAlg and \
            self.dERROR == obj.dERROR and \
            self.dFRIC == obj.dFRIC and \
            self.dSLIDE == obj.dSLIDE and \
            self.iICOORD == obj.iICOORD and \
            self.dSFACT == obj.dSFACT and \
            self.dSFACTT == obj.dSFACTT and \
            self.dCDAMP == obj.dCDAMP and \
            self.iIshellelemfaceSlave == obj.iIshellelemfaceSlave and \
            self.iIshellelemfaceMaster == obj.iIshellelemfaceMaster and \
            self.dCINTERF == obj.dCINTERF and \
            self.iJGLUE == obj.iJGLUE and \
            self.dSDIST == obj.dSDIST and \
            self.iISTYP == obj.iISTYP
    def fromList(self, param):
        obj = SUNSHINE_CONTACT()
        self.iType = param[0] if len(param) > 0 else obj.iType
        self.iAlg = param[1] if len(param) > 1 else obj.iAlg
        self.dERROR = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dERROR
        self.dFRIC = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dFRIC
        self.dSLIDE = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dSLIDE
        self.iICOORD = param[5] if len(param) > 5 else obj.iICOORD
        self.dSFACT = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dSFACT
        self.dSFACTT = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dSFACTT
        self.dCDAMP = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dCDAMP
        self.iIshellelemfaceSlave = param[9] if len(param) > 9 else obj.iIshellelemfaceSlave
        self.iIshellelemfaceMaster = param[10] if len(param) > 10 else obj.iIshellelemfaceMaster
        self.dCINTERF = normalizeDoubleType(param[11]) if len(param) > 11 else obj.dCINTERF
        self.iJGLUE = param[12] if len(param) > 12 else obj.iJGLUE
        self.dSDIST = param[13] if len(param) > 13 else obj.dSDIST
        self.iISTYP = param[14] if len(param) > 14 else obj.iISTYP
        return self
    def __str__(self):
        obj = SUNSHINE_CONTACT()
        paramArgs = []
        if self.iType != obj.iType:
            paramArgs.append('iType={0}'.format(getValueStr(self.iType)))
        if self.iAlg != obj.iAlg:
            paramArgs.append('iAlg={0}'.format(getValueStr(self.iAlg)))
        if self.dERROR != obj.dERROR:
            paramArgs.append('dERROR={0}'.format(getValueStr(self.dERROR)))
        if self.dFRIC != obj.dFRIC:
            paramArgs.append('dFRIC={0}'.format(getValueStr(self.dFRIC)))
        if self.dSLIDE != obj.dSLIDE:
            paramArgs.append('dSLIDE={0}'.format(getValueStr(self.dSLIDE)))
        if self.iICOORD != obj.iICOORD:
            paramArgs.append('iICOORD={0}'.format(getValueStr(self.iICOORD)))
        if self.dSFACT != obj.dSFACT:
            paramArgs.append('dSFACT={0}'.format(getValueStr(self.dSFACT)))
        if self.dSFACTT != obj.dSFACTT:
            paramArgs.append('dSFACTT={0}'.format(getValueStr(self.dSFACTT)))
        if self.dCDAMP != obj.dCDAMP:
            paramArgs.append('dCDAMP={0}'.format(getValueStr(self.dCDAMP)))
        if self.iIshellelemfaceSlave != obj.iIshellelemfaceSlave:
            paramArgs.append('iIshellelemfaceSlave={0}'.format(getValueStr(self.iIshellelemfaceSlave)))
        if self.iIshellelemfaceMaster != obj.iIshellelemfaceMaster:
            paramArgs.append('iIshellelemfaceMaster={0}'.format(getValueStr(self.iIshellelemfaceMaster)))
        if self.dCINTERF != obj.dCINTERF:
            paramArgs.append('dCINTERF={0}'.format(getValueStr(self.dCINTERF)))
        if self.iJGLUE != obj.iJGLUE:
            paramArgs.append('iJGLUE={0}'.format(getValueStr(self.iJGLUE)))
        if self.dSDIST != obj.dSDIST:
            paramArgs.append('dSDIST={0}'.format(getValueStr(self.dSDIST)))
        if self.iISTYP != obj.iISTYP:
            paramArgs.append('iISTYP={0}'.format(getValueStr(self.iISTYP)))
        return 'SUNSHINE_CONTACT({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}'.format(
            self.iType,
            self.iAlg,
            self.dERROR,
            self.dFRIC,
            self.dSLIDE,
            self.iICOORD,
            self.dSFACT,
            self.dSFACTT,
            self.dCDAMP,
            self.iIshellelemfaceSlave,
            self.iIshellelemfaceMaster,
            self.dCINTERF,
            self.iJGLUE,
            self.dSDIST,
            self.iISTYP,
            ) + rightBracket

class MESH_PART_INFO_TOOL:
    def __init__(self,
        strPartName="",
        iPartID=0,
        strPropName="",
        iPropId=0,
        iPropType=0,
        strMatName="",
        iMatID=0,
        strMatType="",
        iPartNode=0,
        iNpartnodeWithprop=0,
        ilPartElement=[],
        ilNpartelementWithprop=[]):
        self.strPartName = strPartName
        self.iPartID = iPartID
        self.strPropName = strPropName
        self.iPropId = iPropId
        self.iPropType = iPropType
        self.strMatName = strMatName
        self.iMatID = iMatID
        self.strMatType = strMatType
        self.iPartNode = iPartNode
        self.iNpartnodeWithprop = iNpartnodeWithprop
        self.ilPartElement = ilPartElement
        self.ilNpartelementWithprop = ilNpartelementWithprop
    def isDefault(self):
        obj = MESH_PART_INFO_TOOL()
        return self.strPartName == obj.strPartName and \
            self.iPartID == obj.iPartID and \
            self.strPropName == obj.strPropName and \
            self.iPropId == obj.iPropId and \
            self.iPropType == obj.iPropType and \
            self.strMatName == obj.strMatName and \
            self.iMatID == obj.iMatID and \
            self.strMatType == obj.strMatType and \
            self.iPartNode == obj.iPartNode and \
            self.iNpartnodeWithprop == obj.iNpartnodeWithprop and \
            self.ilPartElement == obj.ilPartElement and \
            self.ilNpartelementWithprop == obj.ilNpartelementWithprop
    def fromList(self, param):
        obj = MESH_PART_INFO_TOOL()
        self.strPartName = param[0] if len(param) > 0 else obj.strPartName
        self.iPartID = param[1] if len(param) > 1 else obj.iPartID
        self.strPropName = param[2] if len(param) > 2 else obj.strPropName
        self.iPropId = param[3] if len(param) > 3 else obj.iPropId
        self.iPropType = param[4] if len(param) > 4 else obj.iPropType
        self.strMatName = param[5] if len(param) > 5 else obj.strMatName
        self.iMatID = param[6] if len(param) > 6 else obj.iMatID
        self.strMatType = param[7] if len(param) > 7 else obj.strMatType
        self.iPartNode = param[8] if len(param) > 8 else obj.iPartNode
        self.iNpartnodeWithprop = param[9] if len(param) > 9 else obj.iNpartnodeWithprop
        self.ilPartElement = param[10] if len(param) > 10 else obj.ilPartElement
        self.ilNpartelementWithprop = param[11] if len(param) > 11 else obj.ilNpartelementWithprop
        return self
    def __str__(self):
        obj = MESH_PART_INFO_TOOL()
        paramArgs = []
        if self.strPartName != obj.strPartName:
            paramArgs.append('strPartName={0}'.format('"' + self.strPartName + '"'))
        if self.iPartID != obj.iPartID:
            paramArgs.append('iPartID={0}'.format(getValueStr(self.iPartID)))
        if self.strPropName != obj.strPropName:
            paramArgs.append('strPropName={0}'.format('"' + self.strPropName + '"'))
        if self.iPropId != obj.iPropId:
            paramArgs.append('iPropId={0}'.format(getValueStr(self.iPropId)))
        if self.iPropType != obj.iPropType:
            paramArgs.append('iPropType={0}'.format(getValueStr(self.iPropType)))
        if self.strMatName != obj.strMatName:
            paramArgs.append('strMatName={0}'.format('"' + self.strMatName + '"'))
        if self.iMatID != obj.iMatID:
            paramArgs.append('iMatID={0}'.format(getValueStr(self.iMatID)))
        if self.strMatType != obj.strMatType:
            paramArgs.append('strMatType={0}'.format('"' + self.strMatType + '"'))
        if self.iPartNode != obj.iPartNode:
            paramArgs.append('iPartNode={0}'.format(getValueStr(self.iPartNode)))
        if self.iNpartnodeWithprop != obj.iNpartnodeWithprop:
            paramArgs.append('iNpartnodeWithprop={0}'.format(getValueStr(self.iNpartnodeWithprop)))
        if self.ilPartElement != obj.ilPartElement:
            paramArgs.append('ilPartElement={0}'.format(getValueStr(self.ilPartElement)))
        if self.ilNpartelementWithprop != obj.ilNpartelementWithprop:
            paramArgs.append('ilNpartelementWithprop={0}'.format(getValueStr(self.ilNpartelementWithprop)))
        return 'MESH_PART_INFO_TOOL({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}'.format(
            '"' + self.strPartName + '"',
            self.iPartID,
            '"' + self.strPropName + '"',
            self.iPropId,
            self.iPropType,
            '"' + self.strMatName + '"',
            self.iMatID,
            '"' + self.strMatType + '"',
            self.iPartNode,
            self.iNpartnodeWithprop,
            self.ilPartElement,
            self.ilNpartelementWithprop) + rightBracket

class PART_COLOR_PAIR:
    def __init__(self,
        crPart=None,
        iColor=65280):
        self.crPart = crPart
        self.iColor = iColor
    def isDefault(self):
        obj = PART_COLOR_PAIR()
        return self.crPart == obj.crPart and \
            self.iColor == obj.iColor
    def fromList(self, param):
        obj = PART_COLOR_PAIR()
        self.crPart = getCursorValue(param[0]) if len(param) > 0 else obj.crPart
        self.iColor = param[1] if len(param) > 1 else obj.iColor
        return self
    def __str__(self):
        obj = PART_COLOR_PAIR()
        paramArgs = []
        if self.crPart != obj.crPart:
            paramArgs.append('crPart={0}'.format(getCursorValueStr(self.crPart)))
        if self.iColor != obj.iColor:
            paramArgs.append('iColor={0}'.format(getValueStr(self.iColor)))
        return 'PART_COLOR_PAIR({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            str(self.crPart) if self.crPart is not None else '0:0',
            self.iColor) + rightBracket

class ABAQUS_LBC_STEP_INFO:
    def __init__(self,
        crStep=None,
        crLbc=None,
        iCurflag=0,
        iPreflag=0):
        self.crStep = crStep
        self.crLbc = crLbc
        self.iCurflag = iCurflag
        self.iPreflag = iPreflag
    def isDefault(self):
        obj = ABAQUS_LBC_STEP_INFO()
        return self.crStep == obj.crStep and \
            self.crLbc == obj.crLbc and \
            self.iCurflag == obj.iCurflag and \
            self.iPreflag == obj.iPreflag
    def fromList(self, param):
        obj = ABAQUS_LBC_STEP_INFO()
        self.crStep = getCursorValue(param[0]) if len(param) > 0 else obj.crStep
        self.crLbc = getCursorValue(param[1]) if len(param) > 1 else obj.crLbc
        self.iCurflag = param[2] if len(param) > 2 else obj.iCurflag
        self.iPreflag = param[3] if len(param) > 3 else obj.iPreflag
        return self
    def __str__(self):
        obj = ABAQUS_LBC_STEP_INFO()
        paramArgs = []
        if self.crStep != obj.crStep:
            paramArgs.append('crStep={0}'.format(getCursorValueStr(self.crStep)))
        if self.crLbc != obj.crLbc:
            paramArgs.append('crLbc={0}'.format(getCursorValueStr(self.crLbc)))
        if self.iCurflag != obj.iCurflag:
            paramArgs.append('iCurflag={0}'.format(getValueStr(self.iCurflag)))
        if self.iPreflag != obj.iPreflag:
            paramArgs.append('iPreflag={0}'.format(getValueStr(self.iPreflag)))
        return 'ABAQUS_LBC_STEP_INFO({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            str(self.crStep) if self.crStep is not None else '0:0',
            str(self.crLbc) if self.crLbc is not None else '0:0',
            self.iCurflag,
            self.iPreflag) + rightBracket

class ADVC_REF_STRESS_RESULT:
    def __init__(self,
        iProc=DFLT_INT,
        iStep=DFLT_INT,
        dFactor=DFLT_DBL):
        self.iProc = iProc
        self.iStep = iStep
        self.dFactor = dFactor
    def isDefault(self):
        obj = ADVC_REF_STRESS_RESULT()
        return self.iProc == obj.iProc and \
            self.iStep == obj.iStep and \
            self.dFactor == obj.dFactor
    def fromList(self, param):
        obj = ADVC_REF_STRESS_RESULT()
        self.iProc = param[0] if len(param) > 0 else obj.iProc
        self.iStep = param[1] if len(param) > 1 else obj.iStep
        self.dFactor = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dFactor
        return self
    def __str__(self):
        obj = ADVC_REF_STRESS_RESULT()
        paramArgs = []
        if self.iProc != obj.iProc:
            paramArgs.append('iProc={0}'.format(getValueStr(self.iProc)))
        if self.iStep != obj.iStep:
            paramArgs.append('iStep={0}'.format(getValueStr(self.iStep)))
        if self.dFactor != obj.dFactor:
            paramArgs.append('dFactor={0}'.format(getValueStr(self.dFactor)))
        return 'ADVC_REF_STRESS_RESULT({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}'.format(
            self.iProc,
            self.iStep,
            self.dFactor) + rightBracket

class RENUMBER_ITEM:
    def __init__(self,
        crTarget=None,
        iBeginID=0,
        iTargetType=0,
        iCount=0,
        iIncrement=0,
        iOrder=0,
        iMethod=0,
        crRefCoord=None,
        ilCoordOrder=[0, 0, 0],
        ilOffset=[0, 0, 0],
        dlCoordTolerance=[0.0, 0.0, 0.0],
        iConflictStrategy=0,
        iSolver=0,
        bEnable=False):
        self.crTarget = crTarget
        self.iBeginID = iBeginID
        self.iTargetType = iTargetType
        self.iCount = iCount
        self.iIncrement = iIncrement
        self.iOrder = iOrder
        self.iMethod = iMethod
        self.crRefCoord = crRefCoord
        self.ilCoordOrder = ilCoordOrder
        self.ilOffset = ilOffset
        self.dlCoordTolerance = dlCoordTolerance
        self.iConflictStrategy = iConflictStrategy
        self.iSolver = iSolver
        self.bEnable = bEnable
    def isDefault(self):
        obj = RENUMBER_ITEM()
        return self.crTarget == obj.crTarget and \
            self.iBeginID == obj.iBeginID and \
            self.iTargetType == obj.iTargetType and \
            self.iCount == obj.iCount and \
            self.iIncrement == obj.iIncrement and \
            self.iOrder == obj.iOrder and \
            self.iMethod == obj.iMethod and \
            self.crRefCoord == obj.crRefCoord and \
            self.ilCoordOrder == obj.ilCoordOrder and \
            self.ilOffset == obj.ilOffset and \
            self.dlCoordTolerance == obj.dlCoordTolerance and \
            self.iConflictStrategy == obj.iConflictStrategy and \
            self.iSolver == obj.iSolver and \
            self.bEnable == obj.bEnable
    def fromList(self, param):
        obj = RENUMBER_ITEM()
        self.crTarget = getCursorValue(param[0]) if len(param) > 0 else obj.crTarget
        self.iBeginID = param[1] if len(param) > 1 else obj.iBeginID
        self.iTargetType = param[2] if len(param) > 2 else obj.iTargetType
        self.iCount = param[3] if len(param) > 3 else obj.iCount
        self.iIncrement = param[4] if len(param) > 4 else obj.iIncrement
        self.iOrder = param[5] if len(param) > 5 else obj.iOrder
        self.iMethod = param[6] if len(param) > 6 else obj.iMethod
        self.crRefCoord = getCursorValue(param[7]) if len(param) > 7 else obj.crRefCoord
        self.ilCoordOrder = param[8] if len(param) > 8 else obj.ilCoordOrder
        self.ilOffset = param[9] if len(param) > 9 else obj.ilOffset
        self.dlCoordTolerance = [normalizeDoubleType(tok) for tok in param[10]] if len(param) > 10 else obj.dlCoordTolerance
        self.iConflictStrategy = param[11] if len(param) > 11 else obj.iConflictStrategy
        self.iSolver = param[12] if len(param) > 12 else obj.iSolver
        self.bEnable = getBoolValue(param[13]) if len(param) > 13 else obj.bEnable
        return self
    def __str__(self):
        obj = RENUMBER_ITEM()
        paramArgs = []
        if self.crTarget != obj.crTarget:
            paramArgs.append('crTarget={0}'.format(getCursorValueStr(self.crTarget)))
        if self.iBeginID != obj.iBeginID:
            paramArgs.append('iBeginID={0}'.format(getValueStr(self.iBeginID)))
        if self.iTargetType != obj.iTargetType:
            paramArgs.append('iTargetType={0}'.format(getValueStr(self.iTargetType)))
        if self.iCount != obj.iCount:
            paramArgs.append('iCount={0}'.format(getValueStr(self.iCount)))
        if self.iIncrement != obj.iIncrement:
            paramArgs.append('iIncrement={0}'.format(getValueStr(self.iIncrement)))
        if self.iOrder != obj.iOrder:
            paramArgs.append('iOrder={0}'.format(getValueStr(self.iOrder)))
        if self.iMethod != obj.iMethod:
            paramArgs.append('iMethod={0}'.format(getValueStr(self.iMethod)))
        if self.crRefCoord != obj.crRefCoord:
            paramArgs.append('crRefCoord={0}'.format(getCursorValueStr(self.crRefCoord)))
        if self.ilCoordOrder != obj.ilCoordOrder:
            paramArgs.append('ilCoordOrder={0}'.format(getValueStr(self.ilCoordOrder)))
        if self.ilOffset != obj.ilOffset:
            paramArgs.append('ilOffset={0}'.format(getValueStr(self.ilOffset)))
        if self.dlCoordTolerance != obj.dlCoordTolerance:
            paramArgs.append('dlCoordTolerance={0}'.format(getValueStr(self.dlCoordTolerance)))
        if self.iConflictStrategy != obj.iConflictStrategy:
            paramArgs.append('iConflictStrategy={0}'.format(getValueStr(self.iConflictStrategy)))
        if self.iSolver != obj.iSolver:
            paramArgs.append('iSolver={0}'.format(getValueStr(self.iSolver)))
        if self.bEnable != obj.bEnable:
            paramArgs.append('bEnable={0}'.format(getBoolStr(self.bEnable)))
        return 'RENUMBER_ITEM({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}'.format(
            str(self.crTarget) if self.crTarget is not None else '0:0',
            self.iBeginID,
            self.iTargetType,
            self.iCount,
            self.iIncrement,
            self.iOrder,
            self.iMethod,
            str(self.crRefCoord) if self.crRefCoord is not None else '0:0',
            self.ilCoordOrder,
            self.ilOffset,
            self.dlCoordTolerance,
            self.iConflictStrategy,
            self.iSolver,
            1 if self.bEnable else 0) + rightBracket

class SPACE_MESH:
    def __init__(self,
        iBodyType=0,
        bEnclosed=False,
        vOrigin=[0.0,0.0,0.0],
        vCenterPt=[0.0,0.0,0.0],
        vLength=[0.01,0.01,0.01],
        vAxisPt1=[0.0,0.0,0.01],
        vAxisPt2=[0.0,0.0,0.0],
        dMaxElemSize= DFLT_DBL,
        dMinElemSize=0.0):
        self.iBodyType = iBodyType
        self.bEnclosed = bEnclosed
        self.vOrigin = vOrigin
        self.vCenterPt = vCenterPt
        self.vLength = vLength
        self.vAxisPt1 = vAxisPt1
        self.vAxisPt2 = vAxisPt2
        self.dMaxElemSize = dMaxElemSize
        self.dMinElemSize = dMinElemSize
    def isDefault(self):
        obj = SPACE_MESH()
        return self.iBodyType == obj.iBodyType and \
            self.bEnclosed == obj.bEnclosed and \
            self.vOrigin == obj.vOrigin and \
            self.vCenterPt == obj.vCenterPt and \
            self.vLength == obj.vLength and \
            self.vAxisPt1 == obj.vAxisPt1 and \
            self.vAxisPt2 == obj.vAxisPt2 and \
            self.dMaxElemSize == obj.dMaxElemSize and \
            self.dMinElemSize == obj.dMinElemSize
    def fromList(self, param):
        obj = SPACE_MESH()
        self.iBodyType = param[0] if len(param) > 0 else obj.iBodyType
        self.bEnclosed = getBoolValue(param[1]) if len(param) > 1 else obj.bEnclosed
        self.vOrigin = [normalizeDoubleType(tok) for tok in param[2]] if len(param) > 2 else obj.vOrigin
        self.vCenterPt = [normalizeDoubleType(tok) for tok in param[3]] if len(param) > 3 else obj.vCenterPt
        self.vLength = [normalizeDoubleType(tok) for tok in param[4]] if len(param) > 4 else obj.vLength
        self.vAxisPt1 = [normalizeDoubleType(tok) for tok in param[5]] if len(param) > 5 else obj.vAxisPt1
        self.vAxisPt2 = [normalizeDoubleType(tok) for tok in param[6]] if len(param) > 6 else obj.vAxisPt2
        self.dMaxElemSize = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dMaxElemSize
        self.dMinElemSize = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dMinElemSize
        return self
    def __str__(self):
        obj = SPACE_MESH()
        paramArgs = []
        if self.iBodyType != obj.iBodyType:
            paramArgs.append('iBodyType={0}'.format(getValueStr(self.iBodyType)))
        if self.bEnclosed != obj.bEnclosed:
            paramArgs.append('bEnclosed={0}'.format(getBoolStr(self.bEnclosed)))
        if self.vOrigin != obj.vOrigin:
            paramArgs.append('vOrigin={0}'.format(getValueStr(self.vOrigin)))
        if self.vCenterPt != obj.vCenterPt:
            paramArgs.append('vCenterPt={0}'.format(getValueStr(self.vCenterPt)))
        if self.vLength != obj.vLength:
            paramArgs.append('vLength={0}'.format(getValueStr(self.vLength)))
        if self.vAxisPt1 != obj.vAxisPt1:
            paramArgs.append('vAxisPt1={0}'.format(getValueStr(self.vAxisPt1)))
        if self.vAxisPt2 != obj.vAxisPt2:
            paramArgs.append('vAxisPt2={0}'.format(getValueStr(self.vAxisPt2)))
        if self.dMaxElemSize != obj.dMaxElemSize:
            paramArgs.append('dMaxElemSize={0}'.format(getValueStr(self.dMaxElemSize)))
        if self.dMinElemSize != obj.dMinElemSize:
            paramArgs.append('dMinElemSize={0}'.format(getValueStr(self.dMinElemSize)))
        return 'SPACE_MESH({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '{' if isOneParam else ''
        rightBracket = '}' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            self.iBodyType,
            1 if self.bEnclosed else 0,
            self.vOrigin,
            self.vCenterPt,
            self.vLength,
            self.vAxisPt1,
            self.vAxisPt2,
            self.dMaxElemSize,
            self.dMinElemSize) + rightBracket

class BASIC:
    def __init__(self,
        bBasicOutputDisplacements=False,
        bOutputReactionLoad=False,
        bBasicOutputStrain=False,
        bBasicOutputStress=False,
        iAnalysisOption=0,
        bCalculatePrestressEffect=False,
        dUniformTemperature=0.0,
        dReferenceTemperature=0.0,
        dEndLoadTime=0.0,
        iTimeStep=0,
        iStepChosen=0,
        iSubStepNum=0,
        iMaxSubStep=0,
        iMinStepNum=0,
        dTimeStepSize=0.0,
        dMinTimeStep=0.0,
        dMaxTimeStep=0.0,
        iWriteResultFre=1,
        iNumber=1):
        self.bBasicOutputDisplacements = bBasicOutputDisplacements
        self.bOutputReactionLoad = bOutputReactionLoad
        self.bBasicOutputStrain = bBasicOutputStrain
        self.bBasicOutputStress = bBasicOutputStress
        self.iAnalysisOption = iAnalysisOption
        self.bCalculatePrestressEffect = bCalculatePrestressEffect
        self.dUniformTemperature = dUniformTemperature
        self.dReferenceTemperature = dReferenceTemperature
        self.dEndLoadTime = dEndLoadTime
        self.iTimeStep = iTimeStep
        self.iStepChosen = iStepChosen
        self.iSubStepNum = iSubStepNum
        self.iMaxSubStep = iMaxSubStep
        self.iMinStepNum = iMinStepNum
        self.dTimeStepSize = dTimeStepSize
        self.dMinTimeStep = dMinTimeStep
        self.dMaxTimeStep = dMaxTimeStep
        self.iWriteResultFre = iWriteResultFre
        self.iNumber = iNumber
    def isDefault(self):
        obj = BASIC()
        return self.bBasicOutputDisplacements == obj.bBasicOutputDisplacements and \
            self.bOutputReactionLoad == obj.bOutputReactionLoad and \
            self.bBasicOutputStrain == obj.bBasicOutputStrain and \
            self.bBasicOutputStress == obj.bBasicOutputStress and \
            self.iAnalysisOption == obj.iAnalysisOption and \
            self.bCalculatePrestressEffect == obj.bCalculatePrestressEffect and \
            self.dUniformTemperature == obj.dUniformTemperature and \
            self.dReferenceTemperature == obj.dReferenceTemperature and \
            self.dEndLoadTime == obj.dEndLoadTime and \
            self.iTimeStep == obj.iTimeStep and \
            self.iStepChosen == obj.iStepChosen and \
            self.iSubStepNum == obj.iSubStepNum and \
            self.iMaxSubStep == obj.iMaxSubStep and \
            self.iMinStepNum == obj.iMinStepNum and \
            self.dTimeStepSize == obj.dTimeStepSize and \
            self.dMinTimeStep == obj.dMinTimeStep and \
            self.dMaxTimeStep == obj.dMaxTimeStep and \
            self.iWriteResultFre == obj.iWriteResultFre and \
            self.iNumber == obj.iNumber
    def fromList(self, param):
        obj = BASIC()
        self.bBasicOutputDisplacements = getBoolValue(param[0]) if len(param) > 0 else obj.bBasicOutputDisplacements
        self.bOutputReactionLoad = getBoolValue(param[1]) if len(param) > 1 else obj.bOutputReactionLoad
        self.bBasicOutputStrain = getBoolValue(param[2]) if len(param) > 2 else obj.bBasicOutputStrain
        self.bBasicOutputStress = getBoolValue(param[3]) if len(param) > 3 else obj.bBasicOutputStress
        self.iAnalysisOption = param[4] if len(param) > 4 else obj.iAnalysisOption
        self.bCalculatePrestressEffect = getBoolValue(param[5]) if len(param) > 5 else obj.bCalculatePrestressEffect
        self.dUniformTemperature = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dUniformTemperature
        self.dReferenceTemperature = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dReferenceTemperature
        self.dEndLoadTime = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dEndLoadTime
        self.iTimeStep = param[9] if len(param) > 9 else obj.iTimeStep
        self.iStepChosen = param[10] if len(param) > 10 else obj.iStepChosen
        self.iSubStepNum = param[11] if len(param) > 11 else obj.iSubStepNum
        self.iMaxSubStep = param[12] if len(param) > 12 else obj.iMaxSubStep
        self.iMinStepNum = param[13] if len(param) > 13 else obj.iMinStepNum
        self.dTimeStepSize = normalizeDoubleType(param[14]) if len(param) > 14 else obj.dTimeStepSize
        self.dMinTimeStep = normalizeDoubleType(param[15]) if len(param) > 15 else obj.dMinTimeStep
        self.dMaxTimeStep = normalizeDoubleType(param[16]) if len(param) > 16 else obj.dMaxTimeStep
        self.iWriteResultFre = param[17] if len(param) > 17 else obj.iWriteResultFre
        self.iNumber = param[18] if len(param) > 18 else obj.iNumber
        return self
    def __str__(self):
        obj = BASIC()
        paramArgs = []
        if self.bBasicOutputDisplacements != obj.bBasicOutputDisplacements:
            paramArgs.append('bBasicOutputDisplacements={0}'.format(getBoolStr(self.bBasicOutputDisplacements)))
        if self.bOutputReactionLoad != obj.bOutputReactionLoad:
            paramArgs.append('bOutputReactionLoad={0}'.format(getBoolStr(self.bOutputReactionLoad)))
        if self.bBasicOutputStrain != obj.bBasicOutputStrain:
            paramArgs.append('bBasicOutputStrain={0}'.format(getBoolStr(self.bBasicOutputStrain)))
        if self.bBasicOutputStress != obj.bBasicOutputStress:
            paramArgs.append('bBasicOutputStress={0}'.format(getBoolStr(self.bBasicOutputStress)))
        if self.iAnalysisOption != obj.iAnalysisOption:
            paramArgs.append('iAnalysisOption={0}'.format(getValueStr(self.iAnalysisOption)))
        if self.bCalculatePrestressEffect != obj.bCalculatePrestressEffect:
            paramArgs.append('bCalculatePrestressEffect={0}'.format(getBoolStr(self.bCalculatePrestressEffect)))
        if self.dUniformTemperature != obj.dUniformTemperature:
            paramArgs.append('dUniformTemperature={0}'.format(getValueStr(self.dUniformTemperature)))
        if self.dReferenceTemperature != obj.dReferenceTemperature:
            paramArgs.append('dReferenceTemperature={0}'.format(getValueStr(self.dReferenceTemperature)))
        if self.dEndLoadTime != obj.dEndLoadTime:
            paramArgs.append('dEndLoadTime={0}'.format(getValueStr(self.dEndLoadTime)))
        if self.iTimeStep != obj.iTimeStep:
            paramArgs.append('iTimeStep={0}'.format(getValueStr(self.iTimeStep)))
        if self.iStepChosen != obj.iStepChosen:
            paramArgs.append('iStepChosen={0}'.format(getValueStr(self.iStepChosen)))
        if self.iSubStepNum != obj.iSubStepNum:
            paramArgs.append('iSubStepNum={0}'.format(getValueStr(self.iSubStepNum)))
        if self.iMaxSubStep != obj.iMaxSubStep:
            paramArgs.append('iMaxSubStep={0}'.format(getValueStr(self.iMaxSubStep)))
        if self.iMinStepNum != obj.iMinStepNum:
            paramArgs.append('iMinStepNum={0}'.format(getValueStr(self.iMinStepNum)))
        if self.dTimeStepSize != obj.dTimeStepSize:
            paramArgs.append('dTimeStepSize={0}'.format(getValueStr(self.dTimeStepSize)))
        if self.dMinTimeStep != obj.dMinTimeStep:
            paramArgs.append('dMinTimeStep={0}'.format(getValueStr(self.dMinTimeStep)))
        if self.dMaxTimeStep != obj.dMaxTimeStep:
            paramArgs.append('dMaxTimeStep={0}'.format(getValueStr(self.dMaxTimeStep)))
        if self.iWriteResultFre != obj.iWriteResultFre:
            paramArgs.append('iWriteResultFre={0}'.format(getValueStr(self.iWriteResultFre)))
        if self.iNumber != obj.iNumber:
            paramArgs.append('iNumber={0}'.format(getValueStr(self.iNumber)))
        return 'BASIC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}'.format(
            1 if self.bBasicOutputDisplacements else 0,
            1 if self.bOutputReactionLoad else 0,
            1 if self.bBasicOutputStrain else 0,
            1 if self.bBasicOutputStress else 0,
            self.iAnalysisOption,
            1 if self.bCalculatePrestressEffect else 0,
            self.dUniformTemperature,
            self.dReferenceTemperature,
            self.dEndLoadTime,
            self.iTimeStep,
            self.iStepChosen,
            self.iSubStepNum,
            self.iMaxSubStep,
            self.iMinStepNum,
            self.dTimeStepSize,
            self.dMinTimeStep,
            self.dMaxTimeStep,
            self.iWriteResultFre,
            self.iNumber) + rightBracket

class TRANSIENT:
    def __init__(self,
        bTransientEffect=True,
        iLoadingType=0,
        dMassMatrixMultiplier=0.0,
        dStiffMatrixMultiplier=0.0,
        bMidStep=False,
        dToleranceBisection=0.0,
        dToleranceTimeStep=0.0,
        iTimeInterAlgorithm=0,
        iTimeInter=0,
        dGamma=0.005,
        dAlpha=0.25250625,
        dDelta=0.505,
        dAlphaF=0.005,
        dAlphaM=0.0,
        bTransientOutputTemperature=False,
        bTransientOutputHeatFlux=False):
        self.bTransientEffect = bTransientEffect
        self.iLoadingType = iLoadingType
        self.dMassMatrixMultiplier = dMassMatrixMultiplier
        self.dStiffMatrixMultiplier = dStiffMatrixMultiplier
        self.bMidStep = bMidStep
        self.dToleranceBisection = dToleranceBisection
        self.dToleranceTimeStep = dToleranceTimeStep
        self.iTimeInterAlgorithm = iTimeInterAlgorithm
        self.iTimeInter = iTimeInter
        self.dGamma = dGamma
        self.dAlpha = dAlpha
        self.dDelta = dDelta
        self.dAlphaF = dAlphaF
        self.dAlphaM = dAlphaM
        self.bTransientOutputTemperature = bTransientOutputTemperature
        self.bTransientOutputHeatFlux = bTransientOutputHeatFlux
    def isDefault(self):
        obj = TRANSIENT()
        return self.bTransientEffect == obj.bTransientEffect and \
            self.iLoadingType == obj.iLoadingType and \
            self.dMassMatrixMultiplier == obj.dMassMatrixMultiplier and \
            self.dStiffMatrixMultiplier == obj.dStiffMatrixMultiplier and \
            self.bMidStep == obj.bMidStep and \
            self.dToleranceBisection == obj.dToleranceBisection and \
            self.dToleranceTimeStep == obj.dToleranceTimeStep and \
            self.iTimeInterAlgorithm == obj.iTimeInterAlgorithm and \
            self.iTimeInter == obj.iTimeInter and \
            self.dGamma == obj.dGamma and \
            self.dAlpha == obj.dAlpha and \
            self.dDelta == obj.dDelta and \
            self.dAlphaF == obj.dAlphaF and \
            self.dAlphaM == obj.dAlphaM and \
            self.bTransientOutputTemperature == obj.bTransientOutputTemperature and \
            self.bTransientOutputHeatFlux == obj.bTransientOutputHeatFlux
    def fromList(self, param):
        obj = TRANSIENT()
        self.bTransientEffect = getBoolValue(param[0]) if len(param) > 0 else obj.bTransientEffect
        self.iLoadingType = param[1] if len(param) > 1 else obj.iLoadingType
        self.dMassMatrixMultiplier = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dMassMatrixMultiplier
        self.dStiffMatrixMultiplier = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dStiffMatrixMultiplier
        self.bMidStep = getBoolValue(param[4]) if len(param) > 4 else obj.bMidStep
        self.dToleranceBisection = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dToleranceBisection
        self.dToleranceTimeStep = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dToleranceTimeStep
        self.iTimeInterAlgorithm = param[7] if len(param) > 7 else obj.iTimeInterAlgorithm
        self.iTimeInter = param[8] if len(param) > 8 else obj.iTimeInter
        self.dGamma = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dGamma
        self.dAlpha = normalizeDoubleType(param[10]) if len(param) > 10 else obj.dAlpha
        self.dDelta = normalizeDoubleType(param[11]) if len(param) > 11 else obj.dDelta
        self.dAlphaF = normalizeDoubleType(param[12]) if len(param) > 12 else obj.dAlphaF
        self.dAlphaM = normalizeDoubleType(param[13]) if len(param) > 13 else obj.dAlphaM
        self.bTransientOutputTemperature = getBoolValue(param[14]) if len(param) > 14 else obj.bTransientOutputTemperature
        self.bTransientOutputHeatFlux = getBoolValue(param[15]) if len(param) > 15 else obj.bTransientOutputHeatFlux
        return self
    def __str__(self):
        obj = TRANSIENT()
        paramArgs = []
        if self.bTransientEffect != obj.bTransientEffect:
            paramArgs.append('bTransientEffect={0}'.format(getBoolStr(self.bTransientEffect)))
        if self.iLoadingType != obj.iLoadingType:
            paramArgs.append('iLoadingType={0}'.format(getValueStr(self.iLoadingType)))
        if self.dMassMatrixMultiplier != obj.dMassMatrixMultiplier:
            paramArgs.append('dMassMatrixMultiplier={0}'.format(getValueStr(self.dMassMatrixMultiplier)))
        if self.dStiffMatrixMultiplier != obj.dStiffMatrixMultiplier:
            paramArgs.append('dStiffMatrixMultiplier={0}'.format(getValueStr(self.dStiffMatrixMultiplier)))
        if self.bMidStep != obj.bMidStep:
            paramArgs.append('bMidStep={0}'.format(getBoolStr(self.bMidStep)))
        if self.dToleranceBisection != obj.dToleranceBisection:
            paramArgs.append('dToleranceBisection={0}'.format(getValueStr(self.dToleranceBisection)))
        if self.dToleranceTimeStep != obj.dToleranceTimeStep:
            paramArgs.append('dToleranceTimeStep={0}'.format(getValueStr(self.dToleranceTimeStep)))
        if self.iTimeInterAlgorithm != obj.iTimeInterAlgorithm:
            paramArgs.append('iTimeInterAlgorithm={0}'.format(getValueStr(self.iTimeInterAlgorithm)))
        if self.iTimeInter != obj.iTimeInter:
            paramArgs.append('iTimeInter={0}'.format(getValueStr(self.iTimeInter)))
        if self.dGamma != obj.dGamma:
            paramArgs.append('dGamma={0}'.format(getValueStr(self.dGamma)))
        if self.dAlpha != obj.dAlpha:
            paramArgs.append('dAlpha={0}'.format(getValueStr(self.dAlpha)))
        if self.dDelta != obj.dDelta:
            paramArgs.append('dDelta={0}'.format(getValueStr(self.dDelta)))
        if self.dAlphaF != obj.dAlphaF:
            paramArgs.append('dAlphaF={0}'.format(getValueStr(self.dAlphaF)))
        if self.dAlphaM != obj.dAlphaM:
            paramArgs.append('dAlphaM={0}'.format(getValueStr(self.dAlphaM)))
        if self.bTransientOutputTemperature != obj.bTransientOutputTemperature:
            paramArgs.append('bTransientOutputTemperature={0}'.format(getBoolStr(self.bTransientOutputTemperature)))
        if self.bTransientOutputHeatFlux != obj.bTransientOutputHeatFlux:
            paramArgs.append('bTransientOutputHeatFlux={0}'.format(getBoolStr(self.bTransientOutputHeatFlux)))
        return 'TRANSIENT({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}'.format(
            1 if self.bTransientEffect else 0,
            self.iLoadingType,
            self.dMassMatrixMultiplier,
            self.dStiffMatrixMultiplier,
            1 if self.bMidStep else 0,
            self.dToleranceBisection,
            self.dToleranceTimeStep,
            self.iTimeInterAlgorithm,
            self.iTimeInter,
            self.dGamma,
            self.dAlpha,
            self.dDelta,
            self.dAlphaF,
            self.dAlphaM,
            1 if self.bTransientOutputTemperature else 0,
            1 if self.bTransientOutputHeatFlux else 0) + rightBracket

class MODAL:
    def __init__(self,
        iModeMethod=0,
        iExtractNum=1,
        bExpandShape=True,
        iExpandNum=0,
        bUseApprox=False,
        bInclPrestressEffect=False,
        bModalMemorySave=False,
        bResidualVector=False,
        bModalOutputDisplacements=False,
        bModalOutputStrain=False,
        bModalOutputStress=False):
        self.iModeMethod = iModeMethod
        self.iExtractNum = iExtractNum
        self.bExpandShape = bExpandShape
        self.iExpandNum = iExpandNum
        self.bUseApprox = bUseApprox
        self.bInclPrestressEffect = bInclPrestressEffect
        self.bModalMemorySave = bModalMemorySave
        self.bResidualVector = bResidualVector
        self.bModalOutputDisplacements = bModalOutputDisplacements
        self.bModalOutputStrain = bModalOutputStrain
        self.bModalOutputStress = bModalOutputStress
    def isDefault(self):
        obj = MODAL()
        return self.iModeMethod == obj.iModeMethod and \
            self.iExtractNum == obj.iExtractNum and \
            self.bExpandShape == obj.bExpandShape and \
            self.iExpandNum == obj.iExpandNum and \
            self.bUseApprox == obj.bUseApprox and \
            self.bInclPrestressEffect == obj.bInclPrestressEffect and \
            self.bModalMemorySave == obj.bModalMemorySave and \
            self.bResidualVector == obj.bResidualVector and \
            self.bModalOutputDisplacements == obj.bModalOutputDisplacements and \
            self.bModalOutputStrain == obj.bModalOutputStrain and \
            self.bModalOutputStress == obj.bModalOutputStress
    def fromList(self, param):
        obj = MODAL()
        self.iModeMethod = param[0] if len(param) > 0 else obj.iModeMethod
        self.iExtractNum = param[1] if len(param) > 1 else obj.iExtractNum
        self.bExpandShape = getBoolValue(param[2]) if len(param) > 2 else obj.bExpandShape
        self.iExpandNum = param[3] if len(param) > 3 else obj.iExpandNum
        self.bUseApprox = getBoolValue(param[4]) if len(param) > 4 else obj.bUseApprox
        self.bInclPrestressEffect = getBoolValue(param[5]) if len(param) > 5 else obj.bInclPrestressEffect
        self.bModalMemorySave = getBoolValue(param[6]) if len(param) > 6 else obj.bModalMemorySave
        self.bResidualVector = getBoolValue(param[7]) if len(param) > 7 else obj.bResidualVector
        self.bModalOutputDisplacements = getBoolValue(param[8]) if len(param) > 8 else obj.bModalOutputDisplacements
        self.bModalOutputStrain = getBoolValue(param[9]) if len(param) > 9 else obj.bModalOutputStrain
        self.bModalOutputStress = getBoolValue(param[10]) if len(param) > 10 else obj.bModalOutputStress
        return self
    def __str__(self):
        obj = MODAL()
        paramArgs = []
        if self.iModeMethod != obj.iModeMethod:
            paramArgs.append('iModeMethod={0}'.format(getValueStr(self.iModeMethod)))
        if self.iExtractNum != obj.iExtractNum:
            paramArgs.append('iExtractNum={0}'.format(getValueStr(self.iExtractNum)))
        if self.bExpandShape != obj.bExpandShape:
            paramArgs.append('bExpandShape={0}'.format(getBoolStr(self.bExpandShape)))
        if self.iExpandNum != obj.iExpandNum:
            paramArgs.append('iExpandNum={0}'.format(getValueStr(self.iExpandNum)))
        if self.bUseApprox != obj.bUseApprox:
            paramArgs.append('bUseApprox={0}'.format(getBoolStr(self.bUseApprox)))
        if self.bInclPrestressEffect != obj.bInclPrestressEffect:
            paramArgs.append('bInclPrestressEffect={0}'.format(getBoolStr(self.bInclPrestressEffect)))
        if self.bModalMemorySave != obj.bModalMemorySave:
            paramArgs.append('bModalMemorySave={0}'.format(getBoolStr(self.bModalMemorySave)))
        if self.bResidualVector != obj.bResidualVector:
            paramArgs.append('bResidualVector={0}'.format(getBoolStr(self.bResidualVector)))
        if self.bModalOutputDisplacements != obj.bModalOutputDisplacements:
            paramArgs.append('bModalOutputDisplacements={0}'.format(getBoolStr(self.bModalOutputDisplacements)))
        if self.bModalOutputStrain != obj.bModalOutputStrain:
            paramArgs.append('bModalOutputStrain={0}'.format(getBoolStr(self.bModalOutputStrain)))
        if self.bModalOutputStress != obj.bModalOutputStress:
            paramArgs.append('bModalOutputStress={0}'.format(getBoolStr(self.bModalOutputStress)))
        return 'MODAL({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(
            self.iModeMethod,
            self.iExtractNum,
            1 if self.bExpandShape else 0,
            self.iExpandNum,
            1 if self.bUseApprox else 0,
            1 if self.bInclPrestressEffect else 0,
            1 if self.bModalMemorySave else 0,
            1 if self.bResidualVector else 0,
            1 if self.bModalOutputDisplacements else 0,
            1 if self.bModalOutputStrain else 0,
            1 if self.bModalOutputStress else 0) + rightBracket

class HARMONIC:
    def __init__(self,
        dHarmonicStartFreq=0.0,
        dHarmonicEndFreq=1.0,
        iSubSteps=0,
        dAlphaD=0.0,
        dBetaD=0.0,
        dDmprat=0.0,
        bHarmonicOutputDisplacements=False,
        bHarmonicOutputStress=False,
        bHarmonicOutputStrain=False):
        self.dHarmonicStartFreq = dHarmonicStartFreq
        self.dHarmonicEndFreq = dHarmonicEndFreq
        self.iSubSteps = iSubSteps
        self.dAlphaD = dAlphaD
        self.dBetaD = dBetaD
        self.dDmprat = dDmprat
        self.bHarmonicOutputDisplacements = bHarmonicOutputDisplacements
        self.bHarmonicOutputStress = bHarmonicOutputStress
        self.bHarmonicOutputStrain = bHarmonicOutputStrain
    def isDefault(self):
        obj = HARMONIC()
        return self.dHarmonicStartFreq == obj.dHarmonicStartFreq and \
            self.dHarmonicEndFreq == obj.dHarmonicEndFreq and \
            self.iSubSteps == obj.iSubSteps and \
            self.dAlphaD == obj.dAlphaD and \
            self.dBetaD == obj.dBetaD and \
            self.dDmprat == obj.dDmprat and \
            self.bHarmonicOutputDisplacements == obj.bHarmonicOutputDisplacements and \
            self.bHarmonicOutputStress == obj.bHarmonicOutputStress and \
            self.bHarmonicOutputStrain == obj.bHarmonicOutputStrain
    def fromList(self, param):
        obj = HARMONIC()
        self.dHarmonicStartFreq = normalizeDoubleType(param[0]) if len(param) > 0 else obj.dHarmonicStartFreq
        self.dHarmonicEndFreq = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dHarmonicEndFreq
        self.iSubSteps = param[2] if len(param) > 2 else obj.iSubSteps
        self.dAlphaD = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dAlphaD
        self.dBetaD = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dBetaD
        self.dDmprat = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dDmprat
        self.bHarmonicOutputDisplacements = getBoolValue(param[6]) if len(param) > 6 else obj.bHarmonicOutputDisplacements
        self.bHarmonicOutputStress = getBoolValue(param[7]) if len(param) > 7 else obj.bHarmonicOutputStress
        self.bHarmonicOutputStrain = getBoolValue(param[8]) if len(param) > 8 else obj.bHarmonicOutputStrain
        return self
    def __str__(self):
        obj = HARMONIC()
        paramArgs = []
        if self.dHarmonicStartFreq != obj.dHarmonicStartFreq:
            paramArgs.append('dHarmonicStartFreq={0}'.format(getValueStr(self.dHarmonicStartFreq)))
        if self.dHarmonicEndFreq != obj.dHarmonicEndFreq:
            paramArgs.append('dHarmonicEndFreq={0}'.format(getValueStr(self.dHarmonicEndFreq)))
        if self.iSubSteps != obj.iSubSteps:
            paramArgs.append('iSubSteps={0}'.format(getValueStr(self.iSubSteps)))
        if self.dAlphaD != obj.dAlphaD:
            paramArgs.append('dAlphaD={0}'.format(getValueStr(self.dAlphaD)))
        if self.dBetaD != obj.dBetaD:
            paramArgs.append('dBetaD={0}'.format(getValueStr(self.dBetaD)))
        if self.dDmprat != obj.dDmprat:
            paramArgs.append('dDmprat={0}'.format(getValueStr(self.dDmprat)))
        if self.bHarmonicOutputDisplacements != obj.bHarmonicOutputDisplacements:
            paramArgs.append('bHarmonicOutputDisplacements={0}'.format(getBoolStr(self.bHarmonicOutputDisplacements)))
        if self.bHarmonicOutputStress != obj.bHarmonicOutputStress:
            paramArgs.append('bHarmonicOutputStress={0}'.format(getBoolStr(self.bHarmonicOutputStress)))
        if self.bHarmonicOutputStrain != obj.bHarmonicOutputStrain:
            paramArgs.append('bHarmonicOutputStrain={0}'.format(getBoolStr(self.bHarmonicOutputStrain)))
        return 'HARMONIC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(
            self.dHarmonicStartFreq,
            self.dHarmonicEndFreq,
            self.iSubSteps,
            self.dAlphaD,
            self.dBetaD,
            self.dDmprat,
            1 if self.bHarmonicOutputDisplacements else 0,
            1 if self.bHarmonicOutputStress else 0,
            1 if self.bHarmonicOutputStrain else 0) + rightBracket

class SUBSPACE:
    def __init__(self,
        iRigidMode=0,
        iWorkSize=8,
        iNPADNum=4,
        iBlockNum=5,
        iMaxIteratorCnt=0,
        iMinNShift=0,
        iSeqCheck=0):
        self.iRigidMode = iRigidMode
        self.iWorkSize = iWorkSize
        self.iNPADNum = iNPADNum
        self.iBlockNum = iBlockNum
        self.iMaxIteratorCnt = iMaxIteratorCnt
        self.iMinNShift = iMinNShift
        self.iSeqCheck = iSeqCheck
    def isDefault(self):
        obj = SUBSPACE()
        return self.iRigidMode == obj.iRigidMode and \
            self.iWorkSize == obj.iWorkSize and \
            self.iNPADNum == obj.iNPADNum and \
            self.iBlockNum == obj.iBlockNum and \
            self.iMaxIteratorCnt == obj.iMaxIteratorCnt and \
            self.iMinNShift == obj.iMinNShift and \
            self.iSeqCheck == obj.iSeqCheck
    def fromList(self, param):
        obj = SUBSPACE()
        self.iRigidMode = param[0] if len(param) > 0 else obj.iRigidMode
        self.iWorkSize = param[1] if len(param) > 1 else obj.iWorkSize
        self.iNPADNum = param[2] if len(param) > 2 else obj.iNPADNum
        self.iBlockNum = param[3] if len(param) > 3 else obj.iBlockNum
        self.iMaxIteratorCnt = param[4] if len(param) > 4 else obj.iMaxIteratorCnt
        self.iMinNShift = param[5] if len(param) > 5 else obj.iMinNShift
        self.iSeqCheck = param[6] if len(param) > 6 else obj.iSeqCheck
        return self
    def __str__(self):
        obj = SUBSPACE()
        paramArgs = []
        if self.iRigidMode != obj.iRigidMode:
            paramArgs.append('iRigidMode={0}'.format(getValueStr(self.iRigidMode)))
        if self.iWorkSize != obj.iWorkSize:
            paramArgs.append('iWorkSize={0}'.format(getValueStr(self.iWorkSize)))
        if self.iNPADNum != obj.iNPADNum:
            paramArgs.append('iNPADNum={0}'.format(getValueStr(self.iNPADNum)))
        if self.iBlockNum != obj.iBlockNum:
            paramArgs.append('iBlockNum={0}'.format(getValueStr(self.iBlockNum)))
        if self.iMaxIteratorCnt != obj.iMaxIteratorCnt:
            paramArgs.append('iMaxIteratorCnt={0}'.format(getValueStr(self.iMaxIteratorCnt)))
        if self.iMinNShift != obj.iMinNShift:
            paramArgs.append('iMinNShift={0}'.format(getValueStr(self.iMinNShift)))
        if self.iSeqCheck != obj.iSeqCheck:
            paramArgs.append('iSeqCheck={0}'.format(getValueStr(self.iSeqCheck)))
        return 'SUBSPACE({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            self.iRigidMode,
            self.iWorkSize,
            self.iNPADNum,
            self.iBlockNum,
            self.iMaxIteratorCnt,
            self.iMinNShift,
            self.iSeqCheck) + rightBracket

class REDUCED:
    def __init__(self,
        iPrintNum=0):
        self.iPrintNum = iPrintNum
    def isDefault(self):
        obj = REDUCED()
        return self.iPrintNum == obj.iPrintNum
    def fromList(self, param):
        obj = REDUCED()
        self.iPrintNum = param[0] if len(param) > 0 else obj.iPrintNum
        return self
    def __str__(self):
        obj = REDUCED()
        paramArgs = []
        if self.iPrintNum != obj.iPrintNum:
            paramArgs.append('iPrintNum={0}'.format(getValueStr(self.iPrintNum)))
        return 'REDUCED({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}'.format(
            self.iPrintNum) + rightBracket

class STEADY_STATIC:
    def __init__(self,
        bSteadyStaticMemorySave=False,
        bSteadyStaticOutputHeatFlux=False,
        bSteadyStaticOutputTemperature=False,
        bPivotsCheck=True,
        bSteadyStaticSinglePrecision=False,
        dSteadyStaticMultiplier=0.0,
        dSteadyStaticTemperatureDifference=0.0,
        dSteadyStaticToleranceLevel=0.0,
        iAdaptiveDescent=0,
        iSteadyStaticEquationSolver=0,
        iNewtonRaphsonOption=0):
        self.bSteadyStaticMemorySave = bSteadyStaticMemorySave
        self.bSteadyStaticOutputHeatFlux = bSteadyStaticOutputHeatFlux
        self.bSteadyStaticOutputTemperature = bSteadyStaticOutputTemperature
        self.bPivotsCheck = bPivotsCheck
        self.bSteadyStaticSinglePrecision = bSteadyStaticSinglePrecision
        self.dSteadyStaticMultiplier = dSteadyStaticMultiplier
        self.dSteadyStaticTemperatureDifference = dSteadyStaticTemperatureDifference
        self.dSteadyStaticToleranceLevel = dSteadyStaticToleranceLevel
        self.iAdaptiveDescent = iAdaptiveDescent
        self.iSteadyStaticEquationSolver = iSteadyStaticEquationSolver
        self.iNewtonRaphsonOption = iNewtonRaphsonOption
    def isDefault(self):
        obj = STEADY_STATIC()
        return self.bSteadyStaticMemorySave == obj.bSteadyStaticMemorySave and \
            self.bSteadyStaticOutputHeatFlux == obj.bSteadyStaticOutputHeatFlux and \
            self.bSteadyStaticOutputTemperature == obj.bSteadyStaticOutputTemperature and \
            self.bPivotsCheck == obj.bPivotsCheck and \
            self.bSteadyStaticSinglePrecision == obj.bSteadyStaticSinglePrecision and \
            self.dSteadyStaticMultiplier == obj.dSteadyStaticMultiplier and \
            self.dSteadyStaticTemperatureDifference == obj.dSteadyStaticTemperatureDifference and \
            self.dSteadyStaticToleranceLevel == obj.dSteadyStaticToleranceLevel and \
            self.iAdaptiveDescent == obj.iAdaptiveDescent and \
            self.iSteadyStaticEquationSolver == obj.iSteadyStaticEquationSolver and \
            self.iNewtonRaphsonOption == obj.iNewtonRaphsonOption
    def fromList(self, param):
        obj = STEADY_STATIC()
        self.bSteadyStaticMemorySave = getBoolValue(param[0]) if len(param) > 0 else obj.bSteadyStaticMemorySave
        self.bSteadyStaticOutputHeatFlux = getBoolValue(param[1]) if len(param) > 1 else obj.bSteadyStaticOutputHeatFlux
        self.bSteadyStaticOutputTemperature = getBoolValue(param[2]) if len(param) > 2 else obj.bSteadyStaticOutputTemperature
        self.bPivotsCheck = getBoolValue(param[3]) if len(param) > 3 else obj.bPivotsCheck
        self.bSteadyStaticSinglePrecision = getBoolValue(param[4]) if len(param) > 4 else obj.bSteadyStaticSinglePrecision
        self.dSteadyStaticMultiplier = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dSteadyStaticMultiplier
        self.dSteadyStaticTemperatureDifference = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dSteadyStaticTemperatureDifference
        self.dSteadyStaticToleranceLevel = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dSteadyStaticToleranceLevel
        self.iAdaptiveDescent = param[8] if len(param) > 8 else obj.iAdaptiveDescent
        self.iSteadyStaticEquationSolver = param[9] if len(param) > 9 else obj.iSteadyStaticEquationSolver
        self.iNewtonRaphsonOption = param[10] if len(param) > 10 else obj.iNewtonRaphsonOption
        return self
    def __str__(self):
        obj = STEADY_STATIC()
        paramArgs = []
        if self.bSteadyStaticMemorySave != obj.bSteadyStaticMemorySave:
            paramArgs.append('bSteadyStaticMemorySave={0}'.format(getBoolStr(self.bSteadyStaticMemorySave)))
        if self.bSteadyStaticOutputHeatFlux != obj.bSteadyStaticOutputHeatFlux:
            paramArgs.append('bSteadyStaticOutputHeatFlux={0}'.format(getBoolStr(self.bSteadyStaticOutputHeatFlux)))
        if self.bSteadyStaticOutputTemperature != obj.bSteadyStaticOutputTemperature:
            paramArgs.append('bSteadyStaticOutputTemperature={0}'.format(getBoolStr(self.bSteadyStaticOutputTemperature)))
        if self.bPivotsCheck != obj.bPivotsCheck:
            paramArgs.append('bPivotsCheck={0}'.format(getBoolStr(self.bPivotsCheck)))
        if self.bSteadyStaticSinglePrecision != obj.bSteadyStaticSinglePrecision:
            paramArgs.append('bSteadyStaticSinglePrecision={0}'.format(getBoolStr(self.bSteadyStaticSinglePrecision)))
        if self.dSteadyStaticMultiplier != obj.dSteadyStaticMultiplier:
            paramArgs.append('dSteadyStaticMultiplier={0}'.format(getValueStr(self.dSteadyStaticMultiplier)))
        if self.dSteadyStaticTemperatureDifference != obj.dSteadyStaticTemperatureDifference:
            paramArgs.append('dSteadyStaticTemperatureDifference={0}'.format(getValueStr(self.dSteadyStaticTemperatureDifference)))
        if self.dSteadyStaticToleranceLevel != obj.dSteadyStaticToleranceLevel:
            paramArgs.append('dSteadyStaticToleranceLevel={0}'.format(getValueStr(self.dSteadyStaticToleranceLevel)))
        if self.iAdaptiveDescent != obj.iAdaptiveDescent:
            paramArgs.append('iAdaptiveDescent={0}'.format(getValueStr(self.iAdaptiveDescent)))
        if self.iSteadyStaticEquationSolver != obj.iSteadyStaticEquationSolver:
            paramArgs.append('iSteadyStaticEquationSolver={0}'.format(getValueStr(self.iSteadyStaticEquationSolver)))
        if self.iNewtonRaphsonOption != obj.iNewtonRaphsonOption:
            paramArgs.append('iNewtonRaphsonOption={0}'.format(getValueStr(self.iNewtonRaphsonOption)))
        return 'STEADY_STATIC({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(
            1 if self.bSteadyStaticMemorySave else 0,
            1 if self.bSteadyStaticOutputHeatFlux else 0,
            1 if self.bSteadyStaticOutputTemperature else 0,
            1 if self.bPivotsCheck else 0,
            1 if self.bSteadyStaticSinglePrecision else 0,
            self.dSteadyStaticMultiplier,
            self.dSteadyStaticTemperatureDifference,
            self.dSteadyStaticToleranceLevel,
            self.iAdaptiveDescent,
            self.iSteadyStaticEquationSolver,
            self.iNewtonRaphsonOption) + rightBracket

class FULLTRANS:
    def __init__(self,
        iSolutionOption=0,
        dPropertyChange=0.05,
        iPointNum=64,
        dMinTemp=0.0,
        dMaxTemp=0.0,
        iFullTransEquationSolver=0,
        dFullTransdToleranceLevel=0.0,
        dFullTransMultiplier=0.0,
        bFullTransSinglePrecision=False,
        bFullTransMemorySave=False,
        dFullTransTemperatureDifference=1.1):
        self.iSolutionOption = iSolutionOption
        self.dPropertyChange = dPropertyChange
        self.iPointNum = iPointNum
        self.dMinTemp = dMinTemp
        self.dMaxTemp = dMaxTemp
        self.iFullTransEquationSolver = iFullTransEquationSolver
        self.dFullTransdToleranceLevel = dFullTransdToleranceLevel
        self.dFullTransMultiplier = dFullTransMultiplier
        self.bFullTransSinglePrecision = bFullTransSinglePrecision
        self.bFullTransMemorySave = bFullTransMemorySave
        self.dFullTransTemperatureDifference = dFullTransTemperatureDifference
    def isDefault(self):
        obj = FULLTRANS()
        return self.iSolutionOption == obj.iSolutionOption and \
            self.dPropertyChange == obj.dPropertyChange and \
            self.iPointNum == obj.iPointNum and \
            self.dMinTemp == obj.dMinTemp and \
            self.dMaxTemp == obj.dMaxTemp and \
            self.iFullTransEquationSolver == obj.iFullTransEquationSolver and \
            self.dFullTransdToleranceLevel == obj.dFullTransdToleranceLevel and \
            self.dFullTransMultiplier == obj.dFullTransMultiplier and \
            self.bFullTransSinglePrecision == obj.bFullTransSinglePrecision and \
            self.bFullTransMemorySave == obj.bFullTransMemorySave and \
            self.dFullTransTemperatureDifference == obj.dFullTransTemperatureDifference
    def fromList(self, param):
        obj = FULLTRANS()
        self.iSolutionOption = param[0] if len(param) > 0 else obj.iSolutionOption
        self.dPropertyChange = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dPropertyChange
        self.iPointNum = param[2] if len(param) > 2 else obj.iPointNum
        self.dMinTemp = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dMinTemp
        self.dMaxTemp = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dMaxTemp
        self.iFullTransEquationSolver = param[5] if len(param) > 5 else obj.iFullTransEquationSolver
        self.dFullTransdToleranceLevel = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dFullTransdToleranceLevel
        self.dFullTransMultiplier = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dFullTransMultiplier
        self.bFullTransSinglePrecision = getBoolValue(param[8]) if len(param) > 8 else obj.bFullTransSinglePrecision
        self.bFullTransMemorySave = getBoolValue(param[9]) if len(param) > 9 else obj.bFullTransMemorySave
        self.dFullTransTemperatureDifference = normalizeDoubleType(param[10]) if len(param) > 10 else obj.dFullTransTemperatureDifference
        return self
    def __str__(self):
        obj = FULLTRANS()
        paramArgs = []
        if self.iSolutionOption != obj.iSolutionOption:
            paramArgs.append('iSolutionOption={0}'.format(getValueStr(self.iSolutionOption)))
        if self.dPropertyChange != obj.dPropertyChange:
            paramArgs.append('dPropertyChange={0}'.format(getValueStr(self.dPropertyChange)))
        if self.iPointNum != obj.iPointNum:
            paramArgs.append('iPointNum={0}'.format(getValueStr(self.iPointNum)))
        if self.dMinTemp != obj.dMinTemp:
            paramArgs.append('dMinTemp={0}'.format(getValueStr(self.dMinTemp)))
        if self.dMaxTemp != obj.dMaxTemp:
            paramArgs.append('dMaxTemp={0}'.format(getValueStr(self.dMaxTemp)))
        if self.iFullTransEquationSolver != obj.iFullTransEquationSolver:
            paramArgs.append('iFullTransEquationSolver={0}'.format(getValueStr(self.iFullTransEquationSolver)))
        if self.dFullTransdToleranceLevel != obj.dFullTransdToleranceLevel:
            paramArgs.append('dFullTransdToleranceLevel={0}'.format(getValueStr(self.dFullTransdToleranceLevel)))
        if self.dFullTransMultiplier != obj.dFullTransMultiplier:
            paramArgs.append('dFullTransMultiplier={0}'.format(getValueStr(self.dFullTransMultiplier)))
        if self.bFullTransSinglePrecision != obj.bFullTransSinglePrecision:
            paramArgs.append('bFullTransSinglePrecision={0}'.format(getBoolStr(self.bFullTransSinglePrecision)))
        if self.bFullTransMemorySave != obj.bFullTransMemorySave:
            paramArgs.append('bFullTransMemorySave={0}'.format(getBoolStr(self.bFullTransMemorySave)))
        if self.dFullTransTemperatureDifference != obj.dFullTransTemperatureDifference:
            paramArgs.append('dFullTransTemperatureDifference={0}'.format(getValueStr(self.dFullTransTemperatureDifference)))
        return 'FULLTRANS({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(
            self.iSolutionOption,
            self.dPropertyChange,
            self.iPointNum,
            self.dMinTemp,
            self.dMaxTemp,
            self.iFullTransEquationSolver,
            self.dFullTransdToleranceLevel,
            self.dFullTransMultiplier,
            1 if self.bFullTransSinglePrecision else 0,
            1 if self.bFullTransMemorySave else 0,
            self.dFullTransTemperatureDifference) + rightBracket

class ANSYS_SETTING:
    def __init__(self,
        iAnalysisType=0,
        iSolverType=0,
        strJobName="Job1",
        strJobDescription="",
        basicData=BASIC(),
        transientData=TRANSIENT(),
        dStartFreq=DFLT_DBL,
        dEndFreq=DFLT_DBL,
        iModeShape=0,
        modalData=MODAL(),
        subSpaceData=SUBSPACE(),
        reducedData=REDUCED(),
        sSData=STEADY_STATIC(),
        fullTransData=FULLTRANS(),
        harmonicData=HARMONIC(),
        iLoadCaseId=0,
        bWriteResultDB=False,
        bRunAPDL=False,
        bOutputSOLVE=False,
        strCommandLineOption="",
        strAnsysVersion=""):
        self.iAnalysisType = iAnalysisType
        self.iSolverType = iSolverType
        self.strJobName = strJobName
        self.strJobDescription = strJobDescription
        self.basicData = basicData
        self.transientData = transientData
        self.dStartFreq = dStartFreq
        self.dEndFreq = dEndFreq
        self.iModeShape = iModeShape
        self.modalData = modalData
        self.subSpaceData = subSpaceData
        self.reducedData = reducedData
        self.sSData = sSData
        self.fullTransData = fullTransData
        self.harmonicData = harmonicData
        self.iLoadCaseId = iLoadCaseId
        self.bWriteResultDB = bWriteResultDB
        self.bRunAPDL = bRunAPDL
        self.bOutputSOLVE = bOutputSOLVE
        self.strCommandLineOption = strCommandLineOption
        self.strAnsysVersion = strAnsysVersion
    def isDefault(self):
        obj = ANSYS_SETTING()
        return self.iAnalysisType == obj.iAnalysisType and \
            self.iSolverType == obj.iSolverType and \
            self.strJobName == obj.strJobName and \
            self.strJobDescription == obj.strJobDescription and \
            self.basicData == obj.basicData and \
            self.transientData == obj.transientData and \
            self.dStartFreq == obj.dStartFreq and \
            self.dEndFreq == obj.dEndFreq and \
            self.iModeShape == obj.iModeShape and \
            self.modalData == obj.modalData and \
            self.subSpaceData == obj.subSpaceData and \
            self.reducedData == obj.reducedData and \
            self.sSData == obj.sSData and \
            self.fullTransData == obj.fullTransData and \
            self.harmonicData == obj.harmonicData and \
            self.iLoadCaseId == obj.iLoadCaseId and \
            self.bWriteResultDB == obj.bWriteResultDB and \
            self.bRunAPDL == obj.bRunAPDL and \
            self.bOutputSOLVE == obj.bOutputSOLVE and \
            self.strCommandLineOption == obj.strCommandLineOption and \
            self.strAnsysVersion == obj.strAnsysVersion
    def fromList(self, param):
        obj = ANSYS_SETTING()
        self.iAnalysisType = param[0] if len(param) > 0 else obj.iAnalysisType
        self.iSolverType = param[1] if len(param) > 1 else obj.iSolverType
        self.strJobName = param[2] if len(param) > 2 else obj.strJobName
        self.strJobDescription = param[3] if len(param) > 3 else obj.strJobDescription
        self.basicData = BASIC().fromList(param[4]) if len(param) > 4 else obj.basicData
        self.transientData = TRANSIENT().fromList(param[5]) if len(param) > 5 else obj.transientData
        self.dStartFreq = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dStartFreq
        self.dEndFreq = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dEndFreq
        self.iModeShape = param[8] if len(param) > 8 else obj.iModeShape
        self.modalData = MODAL().fromList(param[9]) if len(param) > 9 else obj.modalData
        self.subSpaceData = SUBSPACE().fromList(param[10]) if len(param) > 10 else obj.subSpaceData
        self.reducedData = REDUCED().fromList(param[11]) if len(param) > 11 else obj.reducedData
        self.sSData = STEADY_STATIC().fromList(param[12]) if len(param) > 12 else obj.sSData
        self.fullTransData = FULLTRANS().fromList(param[13]) if len(param) > 13 else obj.fullTransData
        self.harmonicData = HARMONIC().fromList(param[14]) if len(param) > 14 else obj.harmonicData
        self.iLoadCaseId = param[15] if len(param) > 15 else obj.iLoadCaseId
        self.bWriteResultDB = getBoolValue(param[16]) if len(param) > 16 else obj.bWriteResultDB
        self.bRunAPDL = getBoolValue(param[17]) if len(param) > 17 else obj.bRunAPDL
        self.bOutputSOLVE = getBoolValue(param[18]) if len(param) > 18 else obj.bOutputSOLVE
        self.strCommandLineOption = param[19] if len(param) > 19 else obj.strCommandLineOption
        self.strAnsysVersion = param[20] if len(param) > 20 else obj.strAnsysVersion
        return self
    def __str__(self):
        obj = ANSYS_SETTING()
        paramArgs = []
        if self.iAnalysisType != obj.iAnalysisType:
            paramArgs.append('iAnalysisType={0}'.format(getValueStr(self.iAnalysisType)))
        if self.iSolverType != obj.iSolverType:
            paramArgs.append('iSolverType={0}'.format(getValueStr(self.iSolverType)))
        if self.strJobName != obj.strJobName:
            paramArgs.append('strJobName={0}'.format('"' + self.strJobName + '"'))
        if self.strJobDescription != obj.strJobDescription:
            paramArgs.append('strJobDescription={0}'.format('"' + self.strJobDescription + '"'))
        if self.basicData != obj.basicData:
            paramArgs.append('basicData={0}'.format(self.basicData))
        if self.transientData != obj.transientData:
            paramArgs.append('transientData={0}'.format(self.transientData))
        if self.dStartFreq != obj.dStartFreq:
            paramArgs.append('dStartFreq={0}'.format(getValueStr(self.dStartFreq)))
        if self.dEndFreq != obj.dEndFreq:
            paramArgs.append('dEndFreq={0}'.format(getValueStr(self.dEndFreq)))
        if self.iModeShape != obj.iModeShape:
            paramArgs.append('iModeShape={0}'.format(getValueStr(self.iModeShape)))
        if self.modalData != obj.modalData:
            paramArgs.append('modalData={0}'.format(self.modalData))
        if self.subSpaceData != obj.subSpaceData:
            paramArgs.append('subSpaceData={0}'.format(self.subSpaceData))
        if self.reducedData != obj.reducedData:
            paramArgs.append('reducedData={0}'.format(self.reducedData))
        if self.sSData != obj.sSData:
            paramArgs.append('sSData={0}'.format(self.sSData))
        if self.fullTransData != obj.fullTransData:
            paramArgs.append('fullTransData={0}'.format(self.fullTransData))
        if self.harmonicData != obj.harmonicData:
            paramArgs.append('harmonicData={0}'.format(self.harmonicData))
        if self.iLoadCaseId != obj.iLoadCaseId:
            paramArgs.append('iLoadCaseId={0}'.format(getValueStr(self.iLoadCaseId)))
        if self.bWriteResultDB != obj.bWriteResultDB:
            paramArgs.append('bWriteResultDB={0}'.format(getBoolStr(self.bWriteResultDB)))
        if self.bRunAPDL != obj.bRunAPDL:
            paramArgs.append('bRunAPDL={0}'.format(getBoolStr(self.bRunAPDL)))
        if self.bOutputSOLVE != obj.bOutputSOLVE:
            paramArgs.append('bOutputSOLVE={0}'.format(getBoolStr(self.bOutputSOLVE)))
        if self.strCommandLineOption != obj.strCommandLineOption:
            paramArgs.append('strCommandLineOption={0}'.format('"' + self.strCommandLineOption + '"'))
        if self.strAnsysVersion != obj.strAnsysVersion:
            paramArgs.append('strAnsysVersion={0}'.format('"' + self.strAnsysVersion + '"'))
        return 'ANSYS_SETTING({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}'.format(
            self.iAnalysisType,
            self.iSolverType,
            '"' + self.strJobName + '"',
            '"' + self.strJobDescription + '"',
            self.basicData.toNativeStr(isOneParam=True),
            self.transientData.toNativeStr(isOneParam=True),
            self.dStartFreq,
            self.dEndFreq,
            self.iModeShape,
            self.modalData.toNativeStr(isOneParam=True),
            self.subSpaceData.toNativeStr(isOneParam=True),
            self.reducedData.toNativeStr(isOneParam=True),
            self.sSData.toNativeStr(isOneParam=True),
            self.fullTransData.toNativeStr(isOneParam=True),
            self.harmonicData.toNativeStr(isOneParam=True),
            self.iLoadCaseId,
            1 if self.bWriteResultDB else 0,
            1 if self.bRunAPDL else 0,
            1 if self.bOutputSOLVE else 0,
            '"' + self.strCommandLineOption + '"',
            '"' + self.strAnsysVersion + '"') + rightBracket

class JOB_ABAQUS_DATA:
    def __init__(self,
        bRBE2toMPC=False,
        bRenameProcess=False,
        iCodeType=0,
        iSurfDefType=0,
        iUnit=0,
        iWriteType=0,
        strDescription="",
        strlUserText=[],
        bExportNodeElemGroup=False,
        bDeleteFloatingNodes=False,
        bExportFaceElemGroup=False,
        bLoadCase=False,
        bAutoAssignDummyProperty=True,
        crDummyMat=None,
        bOutputGeometryId=True):
        self.bRBE2toMPC = bRBE2toMPC
        self.bRenameProcess = bRenameProcess
        self.iCodeType = iCodeType
        self.iSurfDefType = iSurfDefType
        self.iUnit = iUnit
        self.iWriteType = iWriteType
        self.strDescription = strDescription
        self.strlUserText = strlUserText
        self.bExportNodeElemGroup = bExportNodeElemGroup
        self.bDeleteFloatingNodes = bDeleteFloatingNodes
        self.bExportFaceElemGroup = bExportFaceElemGroup
        self.bLoadCase = bLoadCase
        self.bAutoAssignDummyProperty = bAutoAssignDummyProperty
        self.crDummyMat = crDummyMat
        self.bOutputGeometryId = bOutputGeometryId
    def isDefault(self):
        obj = JOB_ABAQUS_DATA()
        return self.bRBE2toMPC == obj.bRBE2toMPC and \
            self.bRenameProcess == obj.bRenameProcess and \
            self.iCodeType == obj.iCodeType and \
            self.iSurfDefType == obj.iSurfDefType and \
            self.iUnit == obj.iUnit and \
            self.iWriteType == obj.iWriteType and \
            self.strDescription == obj.strDescription and \
            self.strlUserText == obj.strlUserText and \
            self.bExportNodeElemGroup == obj.bExportNodeElemGroup and \
            self.bDeleteFloatingNodes == obj.bDeleteFloatingNodes and \
            self.bExportFaceElemGroup == obj.bExportFaceElemGroup and \
            self.bLoadCase == obj.bLoadCase and \
            self.bAutoAssignDummyProperty == obj.bAutoAssignDummyProperty and \
            self.crDummyMat == obj.crDummyMat and \
            self.bOutputGeometryId == obj.bOutputGeometryId
    def fromList(self, param):
        obj = JOB_ABAQUS_DATA()
        self.bRBE2toMPC = getBoolValue(param[0]) if len(param) > 0 else obj.bRBE2toMPC
        self.bRenameProcess = getBoolValue(param[1]) if len(param) > 1 else obj.bRenameProcess
        self.iCodeType = param[2] if len(param) > 2 else obj.iCodeType
        self.iSurfDefType = param[3] if len(param) > 3 else obj.iSurfDefType
        self.iUnit = param[4] if len(param) > 4 else obj.iUnit
        self.iWriteType = param[5] if len(param) > 5 else obj.iWriteType
        self.strDescription = param[6] if len(param) > 6 else obj.strDescription
        self.strlUserText = param[7] if len(param) > 7 else obj.strlUserText
        self.bExportNodeElemGroup = getBoolValue(param[8]) if len(param) > 8 else obj.bExportNodeElemGroup
        self.bDeleteFloatingNodes = getBoolValue(param[9]) if len(param) > 9 else obj.bDeleteFloatingNodes
        self.bExportFaceElemGroup = getBoolValue(param[10]) if len(param) > 10 else obj.bExportFaceElemGroup
        self.bLoadCase = getBoolValue(param[11]) if len(param) > 11 else obj.bLoadCase
        self.bAutoAssignDummyProperty = getBoolValue(param[12]) if len(param) > 12 else obj.bAutoAssignDummyProperty
        self.crDummyMat = getCursorValue(param[13]) if len(param) > 13 else obj.crDummyMat
        self.bOutputGeometryId = getBoolValue(param[14]) if len(param) > 14 else obj.bOutputGeometryId
        return self
    def __str__(self):
        obj = JOB_ABAQUS_DATA()
        paramArgs = []
        if self.bRBE2toMPC != obj.bRBE2toMPC:
            paramArgs.append('bRBE2toMPC={0}'.format(getBoolStr(self.bRBE2toMPC)))
        if self.bRenameProcess != obj.bRenameProcess:
            paramArgs.append('bRenameProcess={0}'.format(getBoolStr(self.bRenameProcess)))
        if self.iCodeType != obj.iCodeType:
            paramArgs.append('iCodeType={0}'.format(getValueStr(self.iCodeType)))
        if self.iSurfDefType != obj.iSurfDefType:
            paramArgs.append('iSurfDefType={0}'.format(getValueStr(self.iSurfDefType)))
        if self.iUnit != obj.iUnit:
            paramArgs.append('iUnit={0}'.format(getValueStr(self.iUnit)))
        if self.iWriteType != obj.iWriteType:
            paramArgs.append('iWriteType={0}'.format(getValueStr(self.iWriteType)))
        if self.strDescription != obj.strDescription:
            paramArgs.append('strDescription={0}'.format('"' + self.strDescription + '"'))
        if self.strlUserText != obj.strlUserText:
            paramArgs.append('strlUserText={0}'.format(self.strlUserText))
        if self.bExportNodeElemGroup != obj.bExportNodeElemGroup:
            paramArgs.append('bExportNodeElemGroup={0}'.format(getBoolStr(self.bExportNodeElemGroup)))
        if self.bDeleteFloatingNodes != obj.bDeleteFloatingNodes:
            paramArgs.append('bDeleteFloatingNodes={0}'.format(getBoolStr(self.bDeleteFloatingNodes)))
        if self.bExportFaceElemGroup != obj.bExportFaceElemGroup:
            paramArgs.append('bExportFaceElemGroup={0}'.format(getBoolStr(self.bExportFaceElemGroup)))
        if self.bLoadCase != obj.bLoadCase:
            paramArgs.append('bLoadCase={0}'.format(getBoolStr(self.bLoadCase)))
        if self.bAutoAssignDummyProperty != obj.bAutoAssignDummyProperty:
            paramArgs.append('bAutoAssignDummyProperty={0}'.format(getBoolStr(self.bAutoAssignDummyProperty)))
        if self.crDummyMat != obj.crDummyMat:
            paramArgs.append('crDummyMat={0}'.format(getCursorValueStr(self.crDummyMat)))
        if self.bOutputGeometryId != obj.bOutputGeometryId:
            paramArgs.append('bOutputGeometryId={0}'.format(getBoolStr(self.bOutputGeometryId)))
        return 'JOB_ABAQUS_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}'.format(
            1 if self.bRBE2toMPC else 0,
            1 if self.bRenameProcess else 0,
            self.iCodeType,
            self.iSurfDefType,
            self.iUnit,
            self.iWriteType,
            '"' + self.strDescription + '"',
            '[' + ', '.join('"' + tok + '"' for tok in self.strlUserText) + ']',
            1 if self.bExportNodeElemGroup else 0,
            1 if self.bDeleteFloatingNodes else 0,
            1 if self.bExportFaceElemGroup else 0,
            1 if self.bLoadCase else 0,
            1 if self.bAutoAssignDummyProperty else 0,
            str(self.crDummyMat) if self.crDummyMat is not None else '0:0',
            1 if self.bOutputGeometryId else 0) + rightBracket

class ADVC_NORMAL_MODAL:
    def __init__(self,
        iNumberModes=2,
        iEigenNormalizationMethod=-1,
        dShift=DFLT_DBL,
        dCGCGPITolerance=DFLT_DBL,
        dCGCGPIEigenTolerance=DFLT_DBL,
        iCGCGPILoopMax=DFLT_INT,
        dCGCGPIInnerTolerance=DFLT_DBL,
        iCGCGPIBlockSize=DFLT_INT,
        iCGCGPIExtraMode=DFLT_INT,
        iEigenSolver=0,
        iIfFrequencyRange=0,
        dMaxFrequency=DFLT_DBL,
        dMinFrequency=DFLT_DBL,
        iMaxNumEigenValuesOnInterval=DFLT_INT,
        iOutputInit=-1,
        dOutputLowerLimitFrequency=DFLT_DBL,
        iOutputParticipationFactor=-1,
        strRotationCenterCoordinate="",
        dLanczosTol=DFLT_DBL,
        dImplicitRestartTol=DFLT_DBL,
        iImplicitRestartLoopMax=DFLT_INT):
        self.iNumberModes = iNumberModes
        self.iEigenNormalizationMethod = iEigenNormalizationMethod
        self.dShift = dShift
        self.dCGCGPITolerance = dCGCGPITolerance
        self.dCGCGPIEigenTolerance = dCGCGPIEigenTolerance
        self.iCGCGPILoopMax = iCGCGPILoopMax
        self.dCGCGPIInnerTolerance = dCGCGPIInnerTolerance
        self.iCGCGPIBlockSize = iCGCGPIBlockSize
        self.iCGCGPIExtraMode = iCGCGPIExtraMode
        self.iEigenSolver = iEigenSolver
        self.iIfFrequencyRange = iIfFrequencyRange
        self.dMaxFrequency = dMaxFrequency
        self.dMinFrequency = dMinFrequency
        self.iMaxNumEigenValuesOnInterval = iMaxNumEigenValuesOnInterval
        self.iOutputInit = iOutputInit
        self.dOutputLowerLimitFrequency = dOutputLowerLimitFrequency
        self.iOutputParticipationFactor = iOutputParticipationFactor
        self.strRotationCenterCoordinate = strRotationCenterCoordinate
        self.dLanczosTol = dLanczosTol
        self.dImplicitRestartTol = dImplicitRestartTol
        self.iImplicitRestartLoopMax = iImplicitRestartLoopMax
    def isDefault(self):
        obj = ADVC_NORMAL_MODAL()
        return self.iNumberModes == obj.iNumberModes and \
            self.iEigenNormalizationMethod == obj.iEigenNormalizationMethod and \
            self.dShift == obj.dShift and \
            self.dCGCGPITolerance == obj.dCGCGPITolerance and \
            self.dCGCGPIEigenTolerance == obj.dCGCGPIEigenTolerance and \
            self.iCGCGPILoopMax == obj.iCGCGPILoopMax and \
            self.dCGCGPIInnerTolerance == obj.dCGCGPIInnerTolerance and \
            self.iCGCGPIBlockSize == obj.iCGCGPIBlockSize and \
            self.iCGCGPIExtraMode == obj.iCGCGPIExtraMode and \
            self.iEigenSolver == obj.iEigenSolver and \
            self.iIfFrequencyRange == obj.iIfFrequencyRange and \
            self.dMaxFrequency == obj.dMaxFrequency and \
            self.dMinFrequency == obj.dMinFrequency and \
            self.iMaxNumEigenValuesOnInterval == obj.iMaxNumEigenValuesOnInterval and \
            self.iOutputInit == obj.iOutputInit and \
            self.dOutputLowerLimitFrequency == obj.dOutputLowerLimitFrequency and \
            self.iOutputParticipationFactor == obj.iOutputParticipationFactor and \
            self.strRotationCenterCoordinate == obj.strRotationCenterCoordinate and \
            self.dLanczosTol == obj.dLanczosTol and \
            self.dImplicitRestartTol == obj.dImplicitRestartTol and \
            self.iImplicitRestartLoopMax == obj.iImplicitRestartLoopMax
    def fromList(self, param):
        obj = ADVC_NORMAL_MODAL()
        self.iNumberModes = param[0] if len(param) > 0 else obj.iNumberModes
        self.iEigenNormalizationMethod = param[1] if len(param) > 1 else obj.iEigenNormalizationMethod
        self.dShift = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dShift
        self.dCGCGPITolerance = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dCGCGPITolerance
        self.dCGCGPIEigenTolerance = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dCGCGPIEigenTolerance
        self.iCGCGPILoopMax = param[5] if len(param) > 5 else obj.iCGCGPILoopMax
        self.dCGCGPIInnerTolerance = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dCGCGPIInnerTolerance
        self.iCGCGPIBlockSize = param[7] if len(param) > 7 else obj.iCGCGPIBlockSize
        self.iCGCGPIExtraMode = param[8] if len(param) > 8 else obj.iCGCGPIExtraMode
        self.iEigenSolver = param[9] if len(param) > 9 else obj.iEigenSolver
        self.iIfFrequencyRange = param[10] if len(param) > 10 else obj.iIfFrequencyRange
        self.dMaxFrequency = normalizeDoubleType(param[11]) if len(param) > 11 else obj.dMaxFrequency
        self.dMinFrequency = normalizeDoubleType(param[12]) if len(param) > 12 else obj.dMinFrequency
        self.iMaxNumEigenValuesOnInterval = param[13] if len(param) > 13 else obj.iMaxNumEigenValuesOnInterval
        self.iOutputInit = param[14] if len(param) > 14 else obj.iOutputInit
        self.dOutputLowerLimitFrequency = normalizeDoubleType(param[15]) if len(param) > 15 else obj.dOutputLowerLimitFrequency
        self.iOutputParticipationFactor = param[16] if len(param) > 16 else obj.iOutputParticipationFactor
        self.strRotationCenterCoordinate = param[17] if len(param) > 17 else obj.strRotationCenterCoordinate
        self.dLanczosTol = normalizeDoubleType(param[18]) if len(param) > 18 else obj.dLanczosTol
        self.dImplicitRestartTol = normalizeDoubleType(param[19]) if len(param) > 19 else obj.dImplicitRestartTol
        self.iImplicitRestartLoopMax = param[20] if len(param) > 20 else obj.iImplicitRestartLoopMax
        return self
    def __str__(self):
        obj = ADVC_NORMAL_MODAL()
        paramArgs = []
        if self.iNumberModes != obj.iNumberModes:
            paramArgs.append('iNumberModes={0}'.format(getValueStr(self.iNumberModes)))
        if self.iEigenNormalizationMethod != obj.iEigenNormalizationMethod:
            paramArgs.append('iEigenNormalizationMethod={0}'.format(getValueStr(self.iEigenNormalizationMethod)))
        if self.dShift != obj.dShift:
            paramArgs.append('dShift={0}'.format(getValueStr(self.dShift)))
        if self.dCGCGPITolerance != obj.dCGCGPITolerance:
            paramArgs.append('dCGCGPITolerance={0}'.format(getValueStr(self.dCGCGPITolerance)))
        if self.dCGCGPIEigenTolerance != obj.dCGCGPIEigenTolerance:
            paramArgs.append('dCGCGPIEigenTolerance={0}'.format(getValueStr(self.dCGCGPIEigenTolerance)))
        if self.iCGCGPILoopMax != obj.iCGCGPILoopMax:
            paramArgs.append('iCGCGPILoopMax={0}'.format(getValueStr(self.iCGCGPILoopMax)))
        if self.dCGCGPIInnerTolerance != obj.dCGCGPIInnerTolerance:
            paramArgs.append('dCGCGPIInnerTolerance={0}'.format(getValueStr(self.dCGCGPIInnerTolerance)))
        if self.iCGCGPIBlockSize != obj.iCGCGPIBlockSize:
            paramArgs.append('iCGCGPIBlockSize={0}'.format(getValueStr(self.iCGCGPIBlockSize)))
        if self.iCGCGPIExtraMode != obj.iCGCGPIExtraMode:
            paramArgs.append('iCGCGPIExtraMode={0}'.format(getValueStr(self.iCGCGPIExtraMode)))
        if self.iEigenSolver != obj.iEigenSolver:
            paramArgs.append('iEigenSolver={0}'.format(getValueStr(self.iEigenSolver)))
        if self.iIfFrequencyRange != obj.iIfFrequencyRange:
            paramArgs.append('iIfFrequencyRange={0}'.format(getValueStr(self.iIfFrequencyRange)))
        if self.dMaxFrequency != obj.dMaxFrequency:
            paramArgs.append('dMaxFrequency={0}'.format(getValueStr(self.dMaxFrequency)))
        if self.dMinFrequency != obj.dMinFrequency:
            paramArgs.append('dMinFrequency={0}'.format(getValueStr(self.dMinFrequency)))
        if self.iMaxNumEigenValuesOnInterval != obj.iMaxNumEigenValuesOnInterval:
            paramArgs.append('iMaxNumEigenValuesOnInterval={0}'.format(getValueStr(self.iMaxNumEigenValuesOnInterval)))
        if self.iOutputInit != obj.iOutputInit:
            paramArgs.append('iOutputInit={0}'.format(getValueStr(self.iOutputInit)))
        if self.dOutputLowerLimitFrequency != obj.dOutputLowerLimitFrequency:
            paramArgs.append('dOutputLowerLimitFrequency={0}'.format(getValueStr(self.dOutputLowerLimitFrequency)))
        if self.iOutputParticipationFactor != obj.iOutputParticipationFactor:
            paramArgs.append('iOutputParticipationFactor={0}'.format(getValueStr(self.iOutputParticipationFactor)))
        if self.strRotationCenterCoordinate != obj.strRotationCenterCoordinate:
            paramArgs.append('strRotationCenterCoordinate={0}'.format('"' + self.strRotationCenterCoordinate + '"'))
        if self.dLanczosTol != obj.dLanczosTol:
            paramArgs.append('dLanczosTol={0}'.format(getValueStr(self.dLanczosTol)))
        if self.dImplicitRestartTol != obj.dImplicitRestartTol:
            paramArgs.append('dImplicitRestartTol={0}'.format(getValueStr(self.dImplicitRestartTol)))
        if self.iImplicitRestartLoopMax != obj.iImplicitRestartLoopMax:
            paramArgs.append('iImplicitRestartLoopMax={0}'.format(getValueStr(self.iImplicitRestartLoopMax)))
        return 'ADVC_NORMAL_MODAL({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}'.format(
            self.iNumberModes,
            self.iEigenNormalizationMethod,
            self.dShift,
            self.dCGCGPITolerance,
            self.dCGCGPIEigenTolerance,
            self.iCGCGPILoopMax,
            self.dCGCGPIInnerTolerance,
            self.iCGCGPIBlockSize,
            self.iCGCGPIExtraMode,
            self.iEigenSolver,
            self.iIfFrequencyRange,
            self.dMaxFrequency,
            self.dMinFrequency,
            self.iMaxNumEigenValuesOnInterval,
            self.iOutputInit,
            self.dOutputLowerLimitFrequency,
            self.iOutputParticipationFactor,
            '"' + self.strRotationCenterCoordinate + '"',
            self.dLanczosTol,
            self.dImplicitRestartTol,
            self.iImplicitRestartLoopMax) + rightBracket

class ADVC_HEAT_TIME_STEP:
    def __init__(self,
        iEndType=1,
        dMaxTime=1,
        iFixedAuto=0,
        dMaxChange=DFLT_DBL,
        dInitdt=DFLT_DBL,
        iDefineMaxdt=0,
        dMaxdt=DFLT_DBL,
        iDefineMindt=0,
        dMindt=DFLT_DBL,
        dFixeddt=DFLT_DBL,
        iOutputLast=-1,
        iOutputInterval=DFLT_INT,
        iRestartLast=-1,
        iRestartInterval=DFLT_INT,
        dOutputTimeInterval=DFLT_DBL,
        dRestartTimeInterval=DFLT_DBL,
        iOutputInit=-1,
        iListOutputInterval=DFLT_INT):
        self.iEndType = iEndType
        self.dMaxTime = dMaxTime
        self.iFixedAuto = iFixedAuto
        self.dMaxChange = dMaxChange
        self.dInitdt = dInitdt
        self.iDefineMaxdt = iDefineMaxdt
        self.dMaxdt = dMaxdt
        self.iDefineMindt = iDefineMindt
        self.dMindt = dMindt
        self.dFixeddt = dFixeddt
        self.iOutputLast = iOutputLast
        self.iOutputInterval = iOutputInterval
        self.iRestartLast = iRestartLast
        self.iRestartInterval = iRestartInterval
        self.dOutputTimeInterval = dOutputTimeInterval
        self.dRestartTimeInterval = dRestartTimeInterval
        self.iOutputInit = iOutputInit
        self.iListOutputInterval = iListOutputInterval
    def isDefault(self):
        obj = ADVC_HEAT_TIME_STEP()
        return self.iEndType == obj.iEndType and \
            self.dMaxTime == obj.dMaxTime and \
            self.iFixedAuto == obj.iFixedAuto and \
            self.dMaxChange == obj.dMaxChange and \
            self.dInitdt == obj.dInitdt and \
            self.iDefineMaxdt == obj.iDefineMaxdt and \
            self.dMaxdt == obj.dMaxdt and \
            self.iDefineMindt == obj.iDefineMindt and \
            self.dMindt == obj.dMindt and \
            self.dFixeddt == obj.dFixeddt and \
            self.iOutputLast == obj.iOutputLast and \
            self.iOutputInterval == obj.iOutputInterval and \
            self.iRestartLast == obj.iRestartLast and \
            self.iRestartInterval == obj.iRestartInterval and \
            self.dOutputTimeInterval == obj.dOutputTimeInterval and \
            self.dRestartTimeInterval == obj.dRestartTimeInterval and \
            self.iOutputInit == obj.iOutputInit and \
            self.iListOutputInterval == obj.iListOutputInterval
    def fromList(self, param):
        obj = ADVC_HEAT_TIME_STEP()
        self.iEndType = param[0] if len(param) > 0 else obj.iEndType
        self.dMaxTime = normalizeDoubleType(param[1]) if len(param) > 1 else obj.dMaxTime
        self.iFixedAuto = param[2] if len(param) > 2 else obj.iFixedAuto
        self.dMaxChange = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dMaxChange
        self.dInitdt = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dInitdt
        self.iDefineMaxdt = param[5] if len(param) > 5 else obj.iDefineMaxdt
        self.dMaxdt = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dMaxdt
        self.iDefineMindt = param[7] if len(param) > 7 else obj.iDefineMindt
        self.dMindt = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dMindt
        self.dFixeddt = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dFixeddt
        self.iOutputLast = param[10] if len(param) > 10 else obj.iOutputLast
        self.iOutputInterval = param[11] if len(param) > 11 else obj.iOutputInterval
        self.iRestartLast = param[12] if len(param) > 12 else obj.iRestartLast
        self.iRestartInterval = param[13] if len(param) > 13 else obj.iRestartInterval
        self.dOutputTimeInterval = normalizeDoubleType(param[14]) if len(param) > 14 else obj.dOutputTimeInterval
        self.dRestartTimeInterval = normalizeDoubleType(param[15]) if len(param) > 15 else obj.dRestartTimeInterval
        self.iOutputInit = param[16] if len(param) > 16 else obj.iOutputInit
        self.iListOutputInterval = param[17] if len(param) > 17 else obj.iListOutputInterval
        return self
    def __str__(self):
        obj = ADVC_HEAT_TIME_STEP()
        paramArgs = []
        if self.iEndType != obj.iEndType:
            paramArgs.append('iEndType={0}'.format(getValueStr(self.iEndType)))
        if self.dMaxTime != obj.dMaxTime:
            paramArgs.append('dMaxTime={0}'.format(getValueStr(self.dMaxTime)))
        if self.iFixedAuto != obj.iFixedAuto:
            paramArgs.append('iFixedAuto={0}'.format(getValueStr(self.iFixedAuto)))
        if self.dMaxChange != obj.dMaxChange:
            paramArgs.append('dMaxChange={0}'.format(getValueStr(self.dMaxChange)))
        if self.dInitdt != obj.dInitdt:
            paramArgs.append('dInitdt={0}'.format(getValueStr(self.dInitdt)))
        if self.iDefineMaxdt != obj.iDefineMaxdt:
            paramArgs.append('iDefineMaxdt={0}'.format(getValueStr(self.iDefineMaxdt)))
        if self.dMaxdt != obj.dMaxdt:
            paramArgs.append('dMaxdt={0}'.format(getValueStr(self.dMaxdt)))
        if self.iDefineMindt != obj.iDefineMindt:
            paramArgs.append('iDefineMindt={0}'.format(getValueStr(self.iDefineMindt)))
        if self.dMindt != obj.dMindt:
            paramArgs.append('dMindt={0}'.format(getValueStr(self.dMindt)))
        if self.dFixeddt != obj.dFixeddt:
            paramArgs.append('dFixeddt={0}'.format(getValueStr(self.dFixeddt)))
        if self.iOutputLast != obj.iOutputLast:
            paramArgs.append('iOutputLast={0}'.format(getValueStr(self.iOutputLast)))
        if self.iOutputInterval != obj.iOutputInterval:
            paramArgs.append('iOutputInterval={0}'.format(getValueStr(self.iOutputInterval)))
        if self.iRestartLast != obj.iRestartLast:
            paramArgs.append('iRestartLast={0}'.format(getValueStr(self.iRestartLast)))
        if self.iRestartInterval != obj.iRestartInterval:
            paramArgs.append('iRestartInterval={0}'.format(getValueStr(self.iRestartInterval)))
        if self.dOutputTimeInterval != obj.dOutputTimeInterval:
            paramArgs.append('dOutputTimeInterval={0}'.format(getValueStr(self.dOutputTimeInterval)))
        if self.dRestartTimeInterval != obj.dRestartTimeInterval:
            paramArgs.append('dRestartTimeInterval={0}'.format(getValueStr(self.dRestartTimeInterval)))
        if self.iOutputInit != obj.iOutputInit:
            paramArgs.append('iOutputInit={0}'.format(getValueStr(self.iOutputInit)))
        if self.iListOutputInterval != obj.iListOutputInterval:
            paramArgs.append('iListOutputInterval={0}'.format(getValueStr(self.iListOutputInterval)))
        return 'ADVC_HEAT_TIME_STEP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}'.format(
            self.iEndType,
            self.dMaxTime,
            self.iFixedAuto,
            self.dMaxChange,
            self.dInitdt,
            self.iDefineMaxdt,
            self.dMaxdt,
            self.iDefineMindt,
            self.dMindt,
            self.dFixeddt,
            self.iOutputLast,
            self.iOutputInterval,
            self.iRestartLast,
            self.iRestartInterval,
            self.dOutputTimeInterval,
            self.dRestartTimeInterval,
            self.iOutputInit,
            self.iListOutputInterval) + rightBracket

class NASTRAN_FMBD_SETTING:
    def __init__(self,
        iMDBSolverType=0,
        iMassUnitType=0,
        iForceUnitType=0,
        iLengthUnitType=0,
        iTimeUnitType=0,
        bFlexBody=False,
        bFlexOnly=False,
        bOUTGSTRS=False,
        bOUTGSTRN=False,
        iMiniVarType=0,
        iSHELSTRS=0,
        iSHELSTRN=0,
        bCHECKRFI=False,
        bRMIDNODE=False,
        iRMSHAPE=0):
        self.iMDBSolverType = iMDBSolverType
        self.iMassUnitType = iMassUnitType
        self.iForceUnitType = iForceUnitType
        self.iLengthUnitType = iLengthUnitType
        self.iTimeUnitType = iTimeUnitType
        self.bFlexBody = bFlexBody
        self.bFlexOnly = bFlexOnly
        self.bOUTGSTRS = bOUTGSTRS
        self.bOUTGSTRN = bOUTGSTRN
        self.iMiniVarType = iMiniVarType
        self.iSHELSTRS = iSHELSTRS
        self.iSHELSTRN = iSHELSTRN
        self.bCHECKRFI = bCHECKRFI
        self.bRMIDNODE = bRMIDNODE
        self.iRMSHAPE = iRMSHAPE
    def isDefault(self):
        obj = NASTRAN_FMBD_SETTING()
        return self.iMDBSolverType == obj.iMDBSolverType and \
            self.iMassUnitType == obj.iMassUnitType and \
            self.iForceUnitType == obj.iForceUnitType and \
            self.iLengthUnitType == obj.iLengthUnitType and \
            self.iTimeUnitType == obj.iTimeUnitType and \
            self.bFlexBody == obj.bFlexBody and \
            self.bFlexOnly == obj.bFlexOnly and \
            self.bOUTGSTRS == obj.bOUTGSTRS and \
            self.bOUTGSTRN == obj.bOUTGSTRN and \
            self.iMiniVarType == obj.iMiniVarType and \
            self.iSHELSTRS == obj.iSHELSTRS and \
            self.iSHELSTRN == obj.iSHELSTRN and \
            self.bCHECKRFI == obj.bCHECKRFI and \
            self.bRMIDNODE == obj.bRMIDNODE and \
            self.iRMSHAPE == obj.iRMSHAPE
    def fromList(self, param):
        obj = NASTRAN_FMBD_SETTING()
        self.iMDBSolverType = param[0] if len(param) > 0 else obj.iMDBSolverType
        self.iMassUnitType = param[1] if len(param) > 1 else obj.iMassUnitType
        self.iForceUnitType = param[2] if len(param) > 2 else obj.iForceUnitType
        self.iLengthUnitType = param[3] if len(param) > 3 else obj.iLengthUnitType
        self.iTimeUnitType = param[4] if len(param) > 4 else obj.iTimeUnitType
        self.bFlexBody = getBoolValue(param[5]) if len(param) > 5 else obj.bFlexBody
        self.bFlexOnly = getBoolValue(param[6]) if len(param) > 6 else obj.bFlexOnly
        self.bOUTGSTRS = getBoolValue(param[7]) if len(param) > 7 else obj.bOUTGSTRS
        self.bOUTGSTRN = getBoolValue(param[8]) if len(param) > 8 else obj.bOUTGSTRN
        self.iMiniVarType = param[9] if len(param) > 9 else obj.iMiniVarType
        self.iSHELSTRS = param[10] if len(param) > 10 else obj.iSHELSTRS
        self.iSHELSTRN = param[11] if len(param) > 11 else obj.iSHELSTRN
        self.bCHECKRFI = getBoolValue(param[12]) if len(param) > 12 else obj.bCHECKRFI
        self.bRMIDNODE = getBoolValue(param[13]) if len(param) > 13 else obj.bRMIDNODE
        self.iRMSHAPE = param[14] if len(param) > 14 else obj.iRMSHAPE
        return self
    def __str__(self):
        obj = NASTRAN_FMBD_SETTING()
        paramArgs = []
        if self.iMDBSolverType != obj.iMDBSolverType:
            paramArgs.append('iMDBSolverType={0}'.format(getValueStr(self.iMDBSolverType)))
        if self.iMassUnitType != obj.iMassUnitType:
            paramArgs.append('iMassUnitType={0}'.format(getValueStr(self.iMassUnitType)))
        if self.iForceUnitType != obj.iForceUnitType:
            paramArgs.append('iForceUnitType={0}'.format(getValueStr(self.iForceUnitType)))
        if self.iLengthUnitType != obj.iLengthUnitType:
            paramArgs.append('iLengthUnitType={0}'.format(getValueStr(self.iLengthUnitType)))
        if self.iTimeUnitType != obj.iTimeUnitType:
            paramArgs.append('iTimeUnitType={0}'.format(getValueStr(self.iTimeUnitType)))
        if self.bFlexBody != obj.bFlexBody:
            paramArgs.append('bFlexBody={0}'.format(getBoolStr(self.bFlexBody)))
        if self.bFlexOnly != obj.bFlexOnly:
            paramArgs.append('bFlexOnly={0}'.format(getBoolStr(self.bFlexOnly)))
        if self.bOUTGSTRS != obj.bOUTGSTRS:
            paramArgs.append('bOUTGSTRS={0}'.format(getBoolStr(self.bOUTGSTRS)))
        if self.bOUTGSTRN != obj.bOUTGSTRN:
            paramArgs.append('bOUTGSTRN={0}'.format(getBoolStr(self.bOUTGSTRN)))
        if self.iMiniVarType != obj.iMiniVarType:
            paramArgs.append('iMiniVarType={0}'.format(getValueStr(self.iMiniVarType)))
        if self.iSHELSTRS != obj.iSHELSTRS:
            paramArgs.append('iSHELSTRS={0}'.format(getValueStr(self.iSHELSTRS)))
        if self.iSHELSTRN != obj.iSHELSTRN:
            paramArgs.append('iSHELSTRN={0}'.format(getValueStr(self.iSHELSTRN)))
        if self.bCHECKRFI != obj.bCHECKRFI:
            paramArgs.append('bCHECKRFI={0}'.format(getBoolStr(self.bCHECKRFI)))
        if self.bRMIDNODE != obj.bRMIDNODE:
            paramArgs.append('bRMIDNODE={0}'.format(getBoolStr(self.bRMIDNODE)))
        if self.iRMSHAPE != obj.iRMSHAPE:
            paramArgs.append('iRMSHAPE={0}'.format(getValueStr(self.iRMSHAPE)))
        return 'NASTRAN_FMBD_SETTING({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}'.format(
            self.iMDBSolverType,
            self.iMassUnitType,
            self.iForceUnitType,
            self.iLengthUnitType,
            self.iTimeUnitType,
            1 if self.bFlexBody else 0,
            1 if self.bFlexOnly else 0,
            1 if self.bOUTGSTRS else 0,
            1 if self.bOUTGSTRN else 0,
            self.iMiniVarType,
            self.iSHELSTRS,
            self.iSHELSTRN,
            1 if self.bCHECKRFI else 0,
            1 if self.bRMIDNODE else 0,
            self.iRMSHAPE) + rightBracket

class CONTACT_TABLE_TARGET:
    def __init__(self,
        crMasterGroup=None,
        crSlaveGroup=None,
        strMaster="",
        strSlave="",
        taFacesMaster=[],
        taFacesSlave=[]):
        self.crMasterGroup = crMasterGroup
        self.crSlaveGroup = crSlaveGroup
        self.strMaster = strMaster
        self.strSlave = strSlave
        self.taFacesMaster = taFacesMaster
        self.taFacesSlave = taFacesSlave
    def isDefault(self):
        obj = CONTACT_TABLE_TARGET()
        return self.crMasterGroup == obj.crMasterGroup and \
            self.crSlaveGroup == obj.crSlaveGroup and \
            self.strMaster == obj.strMaster and \
            self.strSlave == obj.strSlave and \
            self.taFacesMaster == obj.taFacesMaster and \
            self.taFacesSlave == obj.taFacesSlave
    def fromList(self, param):
        obj = CONTACT_TABLE_TARGET()
        self.crMasterGroup = getCursorValue(param[0]) if len(param) > 0 else obj.crMasterGroup
        self.crSlaveGroup = getCursorValue(param[1]) if len(param) > 1 else obj.crSlaveGroup
        self.strMaster = param[2] if len(param) > 2 else obj.strMaster
        self.strSlave = param[3] if len(param) > 3 else obj.strSlave
        self.taFacesMaster = getCursorListValue(param[4]) if len(param) > 4 else obj.taFacesMaster
        self.taFacesSlave = getCursorListValue(param[5]) if len(param) > 5 else obj.taFacesSlave
        return self
    def __str__(self):
        obj = CONTACT_TABLE_TARGET()
        paramArgs = []
        if self.crMasterGroup != obj.crMasterGroup:
            paramArgs.append('crMasterGroup={0}'.format(getCursorValueStr(self.crMasterGroup)))
        if self.crSlaveGroup != obj.crSlaveGroup:
            paramArgs.append('crSlaveGroup={0}'.format(getCursorValueStr(self.crSlaveGroup)))
        if self.strMaster != obj.strMaster:
            paramArgs.append('strMaster={0}'.format('"' + self.strMaster + '"'))
        if self.strSlave != obj.strSlave:
            paramArgs.append('strSlave={0}'.format('"' + self.strSlave + '"'))
        if self.taFacesMaster != obj.taFacesMaster:
            paramArgs.append('taFacesMaster={0}'.format(getCursorListValueStr(self.taFacesMaster)))
        if self.taFacesSlave != obj.taFacesSlave:
            paramArgs.append('taFacesSlave={0}'.format(getCursorListValueStr(self.taFacesSlave)))
        return 'CONTACT_TABLE_TARGET({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            str(self.crMasterGroup) if self.crMasterGroup is not None else '0:0',
            str(self.crSlaveGroup) if self.crSlaveGroup is not None else '0:0',
            '"' + self.strMaster + '"',
            '"' + self.strSlave + '"',
            str(self.taFacesMaster) if self.taFacesMaster != [None] else '[0:0]',
            str(self.taFacesSlave) if self.taFacesSlave != [None] else '[0:0]') + rightBracket

class CONTACT_DATA_TSSS:
    def __init__(self,
        strName="",
        crContact=None,
        stNastranParam=SUNSHINE_CONTACT(),
        Color=0,
        bDuplicated=False):
        self.strName = strName
        self.crContact = crContact
        self.stNastranParam = stNastranParam
        self.Color = Color
        self.bDuplicated = bDuplicated
    def isDefault(self):
        obj = CONTACT_DATA_TSSS()
        return self.strName == obj.strName and \
            self.crContact == obj.crContact and \
            self.stNastranParam == obj.stNastranParam and \
            self.Color == obj.Color and \
            self.bDuplicated == obj.bDuplicated
    def fromList(self, param):
        obj = CONTACT_DATA_TSSS()
        self.strName = param[0] if len(param) > 0 else obj.strName
        self.crContact = getCursorValue(param[1]) if len(param) > 1 else obj.crContact
        self.stNastranParam = SUNSHINE_CONTACT().fromList(param[2]) if len(param) > 2 else obj.stNastranParam
        self.Color = param[3] if len(param) > 3 else obj.Color
        self.bDuplicated = getBoolValue(param[4]) if len(param) > 4 else obj.bDuplicated
        return self
    def __str__(self):
        obj = CONTACT_DATA_TSSS()
        paramArgs = []
        if self.strName != obj.strName:
            paramArgs.append('strName={0}'.format('"' + self.strName + '"'))
        if self.crContact != obj.crContact:
            paramArgs.append('crContact={0}'.format(getCursorValueStr(self.crContact)))
        if self.stNastranParam != obj.stNastranParam:
            paramArgs.append('stNastranParam={0}'.format(self.stNastranParam))
        if self.Color != obj.Color:
            paramArgs.append('Color={0}'.format(getValueStr(self.Color)))
        if self.bDuplicated != obj.bDuplicated:
            paramArgs.append('bDuplicated={0}'.format(getBoolStr(self.bDuplicated)))
        return 'CONTACT_DATA_TSSS({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            '"' + self.strName + '"',
            str(self.crContact) if self.crContact is not None else '0:0',
            self.stNastranParam.toNativeStr(isOneParam=True),
            self.Color,
            1 if self.bDuplicated else 0) + rightBracket

class Optimization_ObjectiveConstraint_Parameter:
    def __init__(self,
        iEnFunctionType=-1,
        strFunctionName="",
        iDisplacementRelation=-1,
        strDegreeOfFreedomNum="",
        dDisplacementCoefficient=DFLT_DBL,
        vecProcess=[],
        iConstraint=-1,
        dConstraintTol=DFLT_DBL,
        iTargetType=-1,
        dRatioOrValue=DFLT_DBL,
        dCoefficient=DFLT_DBL,
        crNodeSet=None,
        crPropOrElemSet=None,
        crSurfaceSet=None,
        iKSKernel=-1,
        dRHO=DFLT_DBL,
        dExponent=DFLT_DBL,
        iEigenNumber=DFLT_INT):
        self.iEnFunctionType = iEnFunctionType
        self.strFunctionName = strFunctionName
        self.iDisplacementRelation = iDisplacementRelation
        self.strDegreeOfFreedomNum = strDegreeOfFreedomNum
        self.dDisplacementCoefficient = dDisplacementCoefficient
        self.vecProcess = vecProcess
        self.iConstraint = iConstraint
        self.dConstraintTol = dConstraintTol
        self.iTargetType = iTargetType
        self.dRatioOrValue = dRatioOrValue
        self.dCoefficient = dCoefficient
        self.crNodeSet = crNodeSet
        self.crPropOrElemSet = crPropOrElemSet
        self.crSurfaceSet = crSurfaceSet
        self.iKSKernel = iKSKernel
        self.dRHO = dRHO
        self.dExponent = dExponent
        self.iEigenNumber = iEigenNumber
    def isDefault(self):
        obj = Optimization_ObjectiveConstraint_Parameter()
        return self.iEnFunctionType == obj.iEnFunctionType and \
            self.strFunctionName == obj.strFunctionName and \
            self.iDisplacementRelation == obj.iDisplacementRelation and \
            self.strDegreeOfFreedomNum == obj.strDegreeOfFreedomNum and \
            self.dDisplacementCoefficient == obj.dDisplacementCoefficient and \
            self.vecProcess == obj.vecProcess and \
            self.iConstraint == obj.iConstraint and \
            self.dConstraintTol == obj.dConstraintTol and \
            self.iTargetType == obj.iTargetType and \
            self.dRatioOrValue == obj.dRatioOrValue and \
            self.dCoefficient == obj.dCoefficient and \
            self.crNodeSet == obj.crNodeSet and \
            self.crPropOrElemSet == obj.crPropOrElemSet and \
            self.crSurfaceSet == obj.crSurfaceSet and \
            self.iKSKernel == obj.iKSKernel and \
            self.dRHO == obj.dRHO and \
            self.dExponent == obj.dExponent and \
            self.iEigenNumber == obj.iEigenNumber
    def fromList(self, param):
        obj = Optimization_ObjectiveConstraint_Parameter()
        self.iEnFunctionType = param[0] if len(param) > 0 else obj.iEnFunctionType
        self.strFunctionName = param[1] if len(param) > 1 else obj.strFunctionName
        self.iDisplacementRelation = param[2] if len(param) > 2 else obj.iDisplacementRelation
        self.strDegreeOfFreedomNum = param[3] if len(param) > 3 else obj.strDegreeOfFreedomNum
        self.dDisplacementCoefficient = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dDisplacementCoefficient
        self.vecProcess = getCursorListValue(param[5]) if len(param) > 5 else obj.vecProcess
        self.iConstraint = param[6] if len(param) > 6 else obj.iConstraint
        self.dConstraintTol = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dConstraintTol
        self.iTargetType = param[8] if len(param) > 8 else obj.iTargetType
        self.dRatioOrValue = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dRatioOrValue
        self.dCoefficient = normalizeDoubleType(param[10]) if len(param) > 10 else obj.dCoefficient
        self.crNodeSet = getCursorValue(param[11]) if len(param) > 11 else obj.crNodeSet
        self.crPropOrElemSet = getCursorValue(param[12]) if len(param) > 12 else obj.crPropOrElemSet
        self.crSurfaceSet = getCursorValue(param[13]) if len(param) > 13 else obj.crSurfaceSet
        self.iKSKernel = param[14] if len(param) > 14 else obj.iKSKernel
        self.dRHO = normalizeDoubleType(param[15]) if len(param) > 15 else obj.dRHO
        self.dExponent = normalizeDoubleType(param[16]) if len(param) > 16 else obj.dExponent
        self.iEigenNumber = param[17] if len(param) > 17 else obj.iEigenNumber
        return self
    def __str__(self):
        obj = Optimization_ObjectiveConstraint_Parameter()
        paramArgs = []
        if self.iEnFunctionType != obj.iEnFunctionType:
            paramArgs.append('iEnFunctionType={0}'.format(getValueStr(self.iEnFunctionType)))
        if self.strFunctionName != obj.strFunctionName:
            paramArgs.append('strFunctionName={0}'.format('"' + self.strFunctionName + '"'))
        if self.iDisplacementRelation != obj.iDisplacementRelation:
            paramArgs.append('iDisplacementRelation={0}'.format(getValueStr(self.iDisplacementRelation)))
        if self.strDegreeOfFreedomNum != obj.strDegreeOfFreedomNum:
            paramArgs.append('strDegreeOfFreedomNum={0}'.format('"' + self.strDegreeOfFreedomNum + '"'))
        if self.dDisplacementCoefficient != obj.dDisplacementCoefficient:
            paramArgs.append('dDisplacementCoefficient={0}'.format(getValueStr(self.dDisplacementCoefficient)))
        if self.vecProcess != obj.vecProcess:
            paramArgs.append('vecProcess={0}'.format(getCursorListValueStr(self.vecProcess)))
        if self.iConstraint != obj.iConstraint:
            paramArgs.append('iConstraint={0}'.format(getValueStr(self.iConstraint)))
        if self.dConstraintTol != obj.dConstraintTol:
            paramArgs.append('dConstraintTol={0}'.format(getValueStr(self.dConstraintTol)))
        if self.iTargetType != obj.iTargetType:
            paramArgs.append('iTargetType={0}'.format(getValueStr(self.iTargetType)))
        if self.dRatioOrValue != obj.dRatioOrValue:
            paramArgs.append('dRatioOrValue={0}'.format(getValueStr(self.dRatioOrValue)))
        if self.dCoefficient != obj.dCoefficient:
            paramArgs.append('dCoefficient={0}'.format(getValueStr(self.dCoefficient)))
        if self.crNodeSet != obj.crNodeSet:
            paramArgs.append('crNodeSet={0}'.format(getCursorValueStr(self.crNodeSet)))
        if self.crPropOrElemSet != obj.crPropOrElemSet:
            paramArgs.append('crPropOrElemSet={0}'.format(getCursorValueStr(self.crPropOrElemSet)))
        if self.crSurfaceSet != obj.crSurfaceSet:
            paramArgs.append('crSurfaceSet={0}'.format(getCursorValueStr(self.crSurfaceSet)))
        if self.iKSKernel != obj.iKSKernel:
            paramArgs.append('iKSKernel={0}'.format(getValueStr(self.iKSKernel)))
        if self.dRHO != obj.dRHO:
            paramArgs.append('dRHO={0}'.format(getValueStr(self.dRHO)))
        if self.dExponent != obj.dExponent:
            paramArgs.append('dExponent={0}'.format(getValueStr(self.dExponent)))
        if self.iEigenNumber != obj.iEigenNumber:
            paramArgs.append('iEigenNumber={0}'.format(getValueStr(self.iEigenNumber)))
        return 'Optimization_ObjectiveConstraint_Parameter({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}'.format(
            self.iEnFunctionType,
            '"' + self.strFunctionName + '"',
            self.iDisplacementRelation,
            '"' + self.strDegreeOfFreedomNum + '"',
            self.dDisplacementCoefficient,
            self.vecProcess,
            self.iConstraint,
            self.dConstraintTol,
            self.iTargetType,
            self.dRatioOrValue,
            self.dCoefficient,
            str(self.crNodeSet) if self.crNodeSet is not None else '0:0',
            str(self.crPropOrElemSet) if self.crPropOrElemSet is not None else '0:0',
            str(self.crSurfaceSet) if self.crSurfaceSet is not None else '0:0',
            self.iKSKernel,
            self.dRHO,
            self.dExponent,
            self.iEigenNumber) + rightBracket

class Optimization_NonDesignableArea_Parameter:
    def __init__(self,
        iEnFunctionType=-1,
        strFunctionName="",
        iOptimization=-1,
        strDegreeOfFreedomNum="",
        crNodeSet=None,
        crPropOrElemSet=None):
        self.iEnFunctionType = iEnFunctionType
        self.strFunctionName = strFunctionName
        self.iOptimization = iOptimization
        self.strDegreeOfFreedomNum = strDegreeOfFreedomNum
        self.crNodeSet = crNodeSet
        self.crPropOrElemSet = crPropOrElemSet
    def isDefault(self):
        obj = Optimization_NonDesignableArea_Parameter()
        return self.iEnFunctionType == obj.iEnFunctionType and \
            self.strFunctionName == obj.strFunctionName and \
            self.iOptimization == obj.iOptimization and \
            self.strDegreeOfFreedomNum == obj.strDegreeOfFreedomNum and \
            self.crNodeSet == obj.crNodeSet and \
            self.crPropOrElemSet == obj.crPropOrElemSet
    def fromList(self, param):
        obj = Optimization_NonDesignableArea_Parameter()
        self.iEnFunctionType = param[0] if len(param) > 0 else obj.iEnFunctionType
        self.strFunctionName = param[1] if len(param) > 1 else obj.strFunctionName
        self.iOptimization = param[2] if len(param) > 2 else obj.iOptimization
        self.strDegreeOfFreedomNum = param[3] if len(param) > 3 else obj.strDegreeOfFreedomNum
        self.crNodeSet = getCursorValue(param[4]) if len(param) > 4 else obj.crNodeSet
        self.crPropOrElemSet = getCursorValue(param[5]) if len(param) > 5 else obj.crPropOrElemSet
        return self
    def __str__(self):
        obj = Optimization_NonDesignableArea_Parameter()
        paramArgs = []
        if self.iEnFunctionType != obj.iEnFunctionType:
            paramArgs.append('iEnFunctionType={0}'.format(getValueStr(self.iEnFunctionType)))
        if self.strFunctionName != obj.strFunctionName:
            paramArgs.append('strFunctionName={0}'.format('"' + self.strFunctionName + '"'))
        if self.iOptimization != obj.iOptimization:
            paramArgs.append('iOptimization={0}'.format(getValueStr(self.iOptimization)))
        if self.strDegreeOfFreedomNum != obj.strDegreeOfFreedomNum:
            paramArgs.append('strDegreeOfFreedomNum={0}'.format('"' + self.strDegreeOfFreedomNum + '"'))
        if self.crNodeSet != obj.crNodeSet:
            paramArgs.append('crNodeSet={0}'.format(getCursorValueStr(self.crNodeSet)))
        if self.crPropOrElemSet != obj.crPropOrElemSet:
            paramArgs.append('crPropOrElemSet={0}'.format(getCursorValueStr(self.crPropOrElemSet)))
        return 'Optimization_NonDesignableArea_Parameter({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}'.format(
            self.iEnFunctionType,
            '"' + self.strFunctionName + '"',
            self.iOptimization,
            '"' + self.strDegreeOfFreedomNum + '"',
            str(self.crNodeSet) if self.crNodeSet is not None else '0:0',
            str(self.crPropOrElemSet) if self.crPropOrElemSet is not None else '0:0') + rightBracket

class Optimization_ShapeTopology_Parameter:
    def __init__(self,
        iEnFunctionType=-1,
        strFunctionName="",
        dInitialDensity=DFLT_DBL,
        dDensityRandom=DFLT_DBL,
        dAlpha=DFLT_DBL,
        dDraftAngle=DFLT_DBL,
        dGap=DFLT_DBL,
        dDepth=DFLT_DBL,
        dAngle=DFLT_DBL,
        dClearance=DFLT_DBL,
        dThicknessDepth=DFLT_DBL,
        dMaxThickness=DFLT_DBL,
        dMinThickness=DFLT_DBL,
        iMaxIteration=DFLT_INT,
        dMaxStrain=DFLT_DBL,
        dMaxTheta=DFLT_DBL,
        dH1Tolerance=DFLT_DBL,
        iOutputLast=-1,
        iOutputInterval=DFLT_INT,
        iResoutLast=-1,
        iResoutInterval=DFLT_INT,
        iArmijoCheck=-1,
        dArmijoParam=DFLT_DBL,
        strDirection="",
        iPunchingOneSide=-1,
        iAutoIncrement=-1,
        dStabilizationFactor=DFLT_DBL,
        dPoissonRatio=DFLT_DBL,
        iAutoFrozen=-1,
        iKeyCoordinate=-1,
        crNodeSet=None,
        crPropOrElemSet=None,
        crSurfaceSetNonInterferingArea=None,
        crSurfaceSetOptimizedArea=None,
        vecSurfaceSetPair=[],
        iWolfeCheck=-1,
        dWolfeParam=DFLT_DBL,
        iMatrix=-1,
        iElementDStiffness=-1,
        iConstraintMethod=-1,
        dGrayScaleRatio=DFLT_DBL,
        iOutputGrayScaleRatio=-1):
        self.iEnFunctionType = iEnFunctionType
        self.strFunctionName = strFunctionName
        self.dInitialDensity = dInitialDensity
        self.dDensityRandom = dDensityRandom
        self.dAlpha = dAlpha
        self.dDraftAngle = dDraftAngle
        self.dGap = dGap
        self.dDepth = dDepth
        self.dAngle = dAngle
        self.dClearance = dClearance
        self.dThicknessDepth = dThicknessDepth
        self.dMaxThickness = dMaxThickness
        self.dMinThickness = dMinThickness
        self.iMaxIteration = iMaxIteration
        self.dMaxStrain = dMaxStrain
        self.dMaxTheta = dMaxTheta
        self.dH1Tolerance = dH1Tolerance
        self.iOutputLast = iOutputLast
        self.iOutputInterval = iOutputInterval
        self.iResoutLast = iResoutLast
        self.iResoutInterval = iResoutInterval
        self.iArmijoCheck = iArmijoCheck
        self.dArmijoParam = dArmijoParam
        self.strDirection = strDirection
        self.iPunchingOneSide = iPunchingOneSide
        self.iAutoIncrement = iAutoIncrement
        self.dStabilizationFactor = dStabilizationFactor
        self.dPoissonRatio = dPoissonRatio
        self.iAutoFrozen = iAutoFrozen
        self.iKeyCoordinate = iKeyCoordinate
        self.crNodeSet = crNodeSet
        self.crPropOrElemSet = crPropOrElemSet
        self.crSurfaceSetNonInterferingArea = crSurfaceSetNonInterferingArea
        self.crSurfaceSetOptimizedArea = crSurfaceSetOptimizedArea
        self.vecSurfaceSetPair = vecSurfaceSetPair
        self.iWolfeCheck = iWolfeCheck
        self.dWolfeParam = dWolfeParam
        self.iMatrix = iMatrix
        self.iElementDStiffness = iElementDStiffness
        self.iConstraintMethod = iConstraintMethod
        self.dGrayScaleRatio = dGrayScaleRatio
        self.iOutputGrayScaleRatio = iOutputGrayScaleRatio
    def isDefault(self):
        obj = Optimization_ShapeTopology_Parameter()
        return self.iEnFunctionType == obj.iEnFunctionType and \
            self.strFunctionName == obj.strFunctionName and \
            self.dInitialDensity == obj.dInitialDensity and \
            self.dDensityRandom == obj.dDensityRandom and \
            self.dAlpha == obj.dAlpha and \
            self.dDraftAngle == obj.dDraftAngle and \
            self.dGap == obj.dGap and \
            self.dDepth == obj.dDepth and \
            self.dAngle == obj.dAngle and \
            self.dClearance == obj.dClearance and \
            self.dThicknessDepth == obj.dThicknessDepth and \
            self.dMaxThickness == obj.dMaxThickness and \
            self.dMinThickness == obj.dMinThickness and \
            self.iMaxIteration == obj.iMaxIteration and \
            self.dMaxStrain == obj.dMaxStrain and \
            self.dMaxTheta == obj.dMaxTheta and \
            self.dH1Tolerance == obj.dH1Tolerance and \
            self.iOutputLast == obj.iOutputLast and \
            self.iOutputInterval == obj.iOutputInterval and \
            self.iResoutLast == obj.iResoutLast and \
            self.iResoutInterval == obj.iResoutInterval and \
            self.iArmijoCheck == obj.iArmijoCheck and \
            self.dArmijoParam == obj.dArmijoParam and \
            self.strDirection == obj.strDirection and \
            self.iPunchingOneSide == obj.iPunchingOneSide and \
            self.iAutoIncrement == obj.iAutoIncrement and \
            self.dStabilizationFactor == obj.dStabilizationFactor and \
            self.dPoissonRatio == obj.dPoissonRatio and \
            self.iAutoFrozen == obj.iAutoFrozen and \
            self.iKeyCoordinate == obj.iKeyCoordinate and \
            self.crNodeSet == obj.crNodeSet and \
            self.crPropOrElemSet == obj.crPropOrElemSet and \
            self.crSurfaceSetNonInterferingArea == obj.crSurfaceSetNonInterferingArea and \
            self.crSurfaceSetOptimizedArea == obj.crSurfaceSetOptimizedArea and \
            self.vecSurfaceSetPair == obj.vecSurfaceSetPair and \
            self.iWolfeCheck == obj.iWolfeCheck and \
            self.dWolfeParam == obj.dWolfeParam and \
            self.iMatrix == obj.iMatrix and \
            self.iElementDStiffness == obj.iElementDStiffness and \
            self.iConstraintMethod == obj.iConstraintMethod and \
            self.dGrayScaleRatio == obj.dGrayScaleRatio and \
            self.iOutputGrayScaleRatio == obj.iOutputGrayScaleRatio
    def fromList(self, param):
        obj = Optimization_ShapeTopology_Parameter()
        self.iEnFunctionType = param[0] if len(param) > 0 else obj.iEnFunctionType
        self.strFunctionName = param[1] if len(param) > 1 else obj.strFunctionName
        self.dInitialDensity = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dInitialDensity
        self.dDensityRandom = normalizeDoubleType(param[3]) if len(param) > 3 else obj.dDensityRandom
        self.dAlpha = normalizeDoubleType(param[4]) if len(param) > 4 else obj.dAlpha
        self.dDraftAngle = normalizeDoubleType(param[5]) if len(param) > 5 else obj.dDraftAngle
        self.dGap = normalizeDoubleType(param[6]) if len(param) > 6 else obj.dGap
        self.dDepth = normalizeDoubleType(param[7]) if len(param) > 7 else obj.dDepth
        self.dAngle = normalizeDoubleType(param[8]) if len(param) > 8 else obj.dAngle
        self.dClearance = normalizeDoubleType(param[9]) if len(param) > 9 else obj.dClearance
        self.dThicknessDepth = normalizeDoubleType(param[10]) if len(param) > 10 else obj.dThicknessDepth
        self.dMaxThickness = normalizeDoubleType(param[11]) if len(param) > 11 else obj.dMaxThickness
        self.dMinThickness = normalizeDoubleType(param[12]) if len(param) > 12 else obj.dMinThickness
        self.iMaxIteration = param[13] if len(param) > 13 else obj.iMaxIteration
        self.dMaxStrain = normalizeDoubleType(param[14]) if len(param) > 14 else obj.dMaxStrain
        self.dMaxTheta = normalizeDoubleType(param[15]) if len(param) > 15 else obj.dMaxTheta
        self.dH1Tolerance = normalizeDoubleType(param[16]) if len(param) > 16 else obj.dH1Tolerance
        self.iOutputLast = param[17] if len(param) > 17 else obj.iOutputLast
        self.iOutputInterval = param[18] if len(param) > 18 else obj.iOutputInterval
        self.iResoutLast = param[19] if len(param) > 19 else obj.iResoutLast
        self.iResoutInterval = param[20] if len(param) > 20 else obj.iResoutInterval
        self.iArmijoCheck = param[21] if len(param) > 21 else obj.iArmijoCheck
        self.dArmijoParam = normalizeDoubleType(param[22]) if len(param) > 22 else obj.dArmijoParam
        self.strDirection = param[23] if len(param) > 23 else obj.strDirection
        self.iPunchingOneSide = param[24] if len(param) > 24 else obj.iPunchingOneSide
        self.iAutoIncrement = param[25] if len(param) > 25 else obj.iAutoIncrement
        self.dStabilizationFactor = normalizeDoubleType(param[26]) if len(param) > 26 else obj.dStabilizationFactor
        self.dPoissonRatio = normalizeDoubleType(param[27]) if len(param) > 27 else obj.dPoissonRatio
        self.iAutoFrozen = param[28] if len(param) > 28 else obj.iAutoFrozen
        self.iKeyCoordinate = param[29] if len(param) > 29 else obj.iKeyCoordinate
        self.crNodeSet = getCursorValue(param[30]) if len(param) > 30 else obj.crNodeSet
        self.crPropOrElemSet = getCursorValue(param[31]) if len(param) > 31 else obj.crPropOrElemSet
        self.crSurfaceSetNonInterferingArea = getCursorValue(param[32]) if len(param) > 32 else obj.crSurfaceSetNonInterferingArea
        self.crSurfaceSetOptimizedArea = getCursorValue(param[33]) if len(param) > 33 else obj.crSurfaceSetOptimizedArea
        self.vecSurfaceSetPair = [normalizeDoubleType(tok) for tok in param[34]] if len(param) > 34 else obj.vecSurfaceSetPair
        self.iWolfeCheck = param[35] if len(param) > 35 else obj.iWolfeCheck
        self.dWolfeParam = normalizeDoubleType(param[36]) if len(param) > 36 else obj.dWolfeParam
        self.iMatrix = param[37] if len(param) > 37 else obj.iMatrix
        self.iElementDStiffness = param[38] if len(param) > 38 else obj.iElementDStiffness
        self.iConstraintMethod = param[39] if len(param) > 39 else obj.iConstraintMethod
        self.dGrayScaleRatio = normalizeDoubleType(param[40]) if len(param) > 40 else obj.dGrayScaleRatio
        self.iOutputGrayScaleRatio = param[41] if len(param) > 41 else obj.iOutputGrayScaleRatio
        return self
    def __str__(self):
        obj = Optimization_ShapeTopology_Parameter()
        paramArgs = []
        if self.iEnFunctionType != obj.iEnFunctionType:
            paramArgs.append('iEnFunctionType={0}'.format(getValueStr(self.iEnFunctionType)))
        if self.strFunctionName != obj.strFunctionName:
            paramArgs.append('strFunctionName={0}'.format('"' + self.strFunctionName + '"'))
        if self.dInitialDensity != obj.dInitialDensity:
            paramArgs.append('dInitialDensity={0}'.format(getValueStr(self.dInitialDensity)))
        if self.dDensityRandom != obj.dDensityRandom:
            paramArgs.append('dDensityRandom={0}'.format(getValueStr(self.dDensityRandom)))
        if self.dAlpha != obj.dAlpha:
            paramArgs.append('dAlpha={0}'.format(getValueStr(self.dAlpha)))
        if self.dDraftAngle != obj.dDraftAngle:
            paramArgs.append('dDraftAngle={0}'.format(getValueStr(self.dDraftAngle)))
        if self.dGap != obj.dGap:
            paramArgs.append('dGap={0}'.format(getValueStr(self.dGap)))
        if self.dDepth != obj.dDepth:
            paramArgs.append('dDepth={0}'.format(getValueStr(self.dDepth)))
        if self.dAngle != obj.dAngle:
            paramArgs.append('dAngle={0}'.format(getValueStr(self.dAngle)))
        if self.dClearance != obj.dClearance:
            paramArgs.append('dClearance={0}'.format(getValueStr(self.dClearance)))
        if self.dThicknessDepth != obj.dThicknessDepth:
            paramArgs.append('dThicknessDepth={0}'.format(getValueStr(self.dThicknessDepth)))
        if self.dMaxThickness != obj.dMaxThickness:
            paramArgs.append('dMaxThickness={0}'.format(getValueStr(self.dMaxThickness)))
        if self.dMinThickness != obj.dMinThickness:
            paramArgs.append('dMinThickness={0}'.format(getValueStr(self.dMinThickness)))
        if self.iMaxIteration != obj.iMaxIteration:
            paramArgs.append('iMaxIteration={0}'.format(getValueStr(self.iMaxIteration)))
        if self.dMaxStrain != obj.dMaxStrain:
            paramArgs.append('dMaxStrain={0}'.format(getValueStr(self.dMaxStrain)))
        if self.dMaxTheta != obj.dMaxTheta:
            paramArgs.append('dMaxTheta={0}'.format(getValueStr(self.dMaxTheta)))
        if self.dH1Tolerance != obj.dH1Tolerance:
            paramArgs.append('dH1Tolerance={0}'.format(getValueStr(self.dH1Tolerance)))
        if self.iOutputLast != obj.iOutputLast:
            paramArgs.append('iOutputLast={0}'.format(getValueStr(self.iOutputLast)))
        if self.iOutputInterval != obj.iOutputInterval:
            paramArgs.append('iOutputInterval={0}'.format(getValueStr(self.iOutputInterval)))
        if self.iResoutLast != obj.iResoutLast:
            paramArgs.append('iResoutLast={0}'.format(getValueStr(self.iResoutLast)))
        if self.iResoutInterval != obj.iResoutInterval:
            paramArgs.append('iResoutInterval={0}'.format(getValueStr(self.iResoutInterval)))
        if self.iArmijoCheck != obj.iArmijoCheck:
            paramArgs.append('iArmijoCheck={0}'.format(getValueStr(self.iArmijoCheck)))
        if self.dArmijoParam != obj.dArmijoParam:
            paramArgs.append('dArmijoParam={0}'.format(getValueStr(self.dArmijoParam)))
        if self.strDirection != obj.strDirection:
            paramArgs.append('strDirection={0}'.format('"' + self.strDirection + '"'))
        if self.iPunchingOneSide != obj.iPunchingOneSide:
            paramArgs.append('iPunchingOneSide={0}'.format(getValueStr(self.iPunchingOneSide)))
        if self.iAutoIncrement != obj.iAutoIncrement:
            paramArgs.append('iAutoIncrement={0}'.format(getValueStr(self.iAutoIncrement)))
        if self.dStabilizationFactor != obj.dStabilizationFactor:
            paramArgs.append('dStabilizationFactor={0}'.format(getValueStr(self.dStabilizationFactor)))
        if self.dPoissonRatio != obj.dPoissonRatio:
            paramArgs.append('dPoissonRatio={0}'.format(getValueStr(self.dPoissonRatio)))
        if self.iAutoFrozen != obj.iAutoFrozen:
            paramArgs.append('iAutoFrozen={0}'.format(getValueStr(self.iAutoFrozen)))
        if self.iKeyCoordinate != obj.iKeyCoordinate:
            paramArgs.append('iKeyCoordinate={0}'.format(getValueStr(self.iKeyCoordinate)))
        if self.crNodeSet != obj.crNodeSet:
            paramArgs.append('crNodeSet={0}'.format(getCursorValueStr(self.crNodeSet)))
        if self.crPropOrElemSet != obj.crPropOrElemSet:
            paramArgs.append('crPropOrElemSet={0}'.format(getCursorValueStr(self.crPropOrElemSet)))
        if self.crSurfaceSetNonInterferingArea != obj.crSurfaceSetNonInterferingArea:
            paramArgs.append('crSurfaceSetNonInterferingArea={0}'.format(getCursorValueStr(self.crSurfaceSetNonInterferingArea)))
        if self.crSurfaceSetOptimizedArea != obj.crSurfaceSetOptimizedArea:
            paramArgs.append('crSurfaceSetOptimizedArea={0}'.format(getCursorValueStr(self.crSurfaceSetOptimizedArea)))
        if self.vecSurfaceSetPair != obj.vecSurfaceSetPair:
            paramArgs.append('vecSurfaceSetPair={0}'.format(getValueStr(self.vecSurfaceSetPair)))
        if self.iWolfeCheck != obj.iWolfeCheck:
            paramArgs.append('iWolfeCheck={0}'.format(getValueStr(self.iWolfeCheck)))
        if self.dWolfeParam != obj.dWolfeParam:
            paramArgs.append('dWolfeParam={0}'.format(getValueStr(self.dWolfeParam)))
        if self.iMatrix != obj.iMatrix:
            paramArgs.append('iMatrix={0}'.format(getValueStr(self.iMatrix)))
        if self.iElementDStiffness != obj.iElementDStiffness:
            paramArgs.append('iElementDStiffness={0}'.format(getValueStr(self.iElementDStiffness)))
        if self.iConstraintMethod != obj.iConstraintMethod:
            paramArgs.append('iConstraintMethod={0}'.format(getValueStr(self.iConstraintMethod)))
        if self.dGrayScaleRatio != obj.dGrayScaleRatio:
            paramArgs.append('dGrayScaleRatio={0}'.format(getValueStr(self.dGrayScaleRatio)))
        if self.iOutputGrayScaleRatio != obj.iOutputGrayScaleRatio:
            paramArgs.append('iOutputGrayScaleRatio={0}'.format(getValueStr(self.iOutputGrayScaleRatio)))
        return 'Optimization_ShapeTopology_Parameter({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}'.format(
            self.iEnFunctionType,
            '"' + self.strFunctionName + '"',
            self.dInitialDensity,
            self.dDensityRandom,
            self.dAlpha,
            self.dDraftAngle,
            self.dGap,
            self.dDepth,
            self.dAngle,
            self.dClearance,
            self.dThicknessDepth,
            self.dMaxThickness,
            self.dMinThickness,
            self.iMaxIteration,
            self.dMaxStrain,
            self.dMaxTheta,
            self.dH1Tolerance,
            self.iOutputLast,
            self.iOutputInterval,
            self.iResoutLast,
            self.iResoutInterval,
            self.iArmijoCheck,
            self.dArmijoParam,
            '"' + self.strDirection + '"',
            self.iPunchingOneSide,
            self.iAutoIncrement,
            self.dStabilizationFactor,
            self.dPoissonRatio,
            self.iAutoFrozen,
            self.iKeyCoordinate,
            str(self.crNodeSet) if self.crNodeSet is not None else '0:0',
            str(self.crPropOrElemSet) if self.crPropOrElemSet is not None else '0:0',
            str(self.crSurfaceSetNonInterferingArea) if self.crSurfaceSetNonInterferingArea is not None else '0:0',
            str(self.crSurfaceSetOptimizedArea) if self.crSurfaceSetOptimizedArea is not None else '0:0',
            self.vecSurfaceSetPair,
            self.iWolfeCheck,
            self.dWolfeParam,
            self.iMatrix,
            self.iElementDStiffness,
            self.iConstraintMethod,
            self.dGrayScaleRatio,
            self.iOutputGrayScaleRatio) + rightBracket

class Optimization_Output_Parameter:
    def __init__(self,
        bNodalShapeVariation=False,
        bShapeVariation=False,
        bNodalDensityRation=False,
        bDensityRation=False,
        bSensitivity=False,
        bSensitivity_Of_Objective=False,
        bSensitivity_Of_Constraint=False,
        bSensitivities=False):
        self.bNodalShapeVariation = bNodalShapeVariation
        self.bShapeVariation = bShapeVariation
        self.bNodalDensityRation = bNodalDensityRation
        self.bDensityRation = bDensityRation
        self.bSensitivity = bSensitivity
        self.bSensitivity_Of_Objective = bSensitivity_Of_Objective
        self.bSensitivity_Of_Constraint = bSensitivity_Of_Constraint
        self.bSensitivities = bSensitivities
    def isDefault(self):
        obj = Optimization_Output_Parameter()
        return self.bNodalShapeVariation == obj.bNodalShapeVariation and \
            self.bShapeVariation == obj.bShapeVariation and \
            self.bNodalDensityRation == obj.bNodalDensityRation and \
            self.bDensityRation == obj.bDensityRation and \
            self.bSensitivity == obj.bSensitivity and \
            self.bSensitivity_Of_Objective == obj.bSensitivity_Of_Objective and \
            self.bSensitivity_Of_Constraint == obj.bSensitivity_Of_Constraint and \
            self.bSensitivities == obj.bSensitivities
    def fromList(self, param):
        obj = Optimization_Output_Parameter()
        self.bNodalShapeVariation = getBoolValue(param[0]) if len(param) > 0 else obj.bNodalShapeVariation
        self.bShapeVariation = getBoolValue(param[1]) if len(param) > 1 else obj.bShapeVariation
        self.bNodalDensityRation = getBoolValue(param[2]) if len(param) > 2 else obj.bNodalDensityRation
        self.bDensityRation = getBoolValue(param[3]) if len(param) > 3 else obj.bDensityRation
        self.bSensitivity = getBoolValue(param[4]) if len(param) > 4 else obj.bSensitivity
        self.bSensitivity_Of_Objective = getBoolValue(param[5]) if len(param) > 5 else obj.bSensitivity_Of_Objective
        self.bSensitivity_Of_Constraint = getBoolValue(param[6]) if len(param) > 6 else obj.bSensitivity_Of_Constraint
        self.bSensitivities = getBoolValue(param[7]) if len(param) > 7 else obj.bSensitivities
        return self
    def __str__(self):
        obj = Optimization_Output_Parameter()
        paramArgs = []
        if self.bNodalShapeVariation != obj.bNodalShapeVariation:
            paramArgs.append('bNodalShapeVariation={0}'.format(getBoolStr(self.bNodalShapeVariation)))
        if self.bShapeVariation != obj.bShapeVariation:
            paramArgs.append('bShapeVariation={0}'.format(getBoolStr(self.bShapeVariation)))
        if self.bNodalDensityRation != obj.bNodalDensityRation:
            paramArgs.append('bNodalDensityRation={0}'.format(getBoolStr(self.bNodalDensityRation)))
        if self.bDensityRation != obj.bDensityRation:
            paramArgs.append('bDensityRation={0}'.format(getBoolStr(self.bDensityRation)))
        if self.bSensitivity != obj.bSensitivity:
            paramArgs.append('bSensitivity={0}'.format(getBoolStr(self.bSensitivity)))
        if self.bSensitivity_Of_Objective != obj.bSensitivity_Of_Objective:
            paramArgs.append('bSensitivity_Of_Objective={0}'.format(getBoolStr(self.bSensitivity_Of_Objective)))
        if self.bSensitivity_Of_Constraint != obj.bSensitivity_Of_Constraint:
            paramArgs.append('bSensitivity_Of_Constraint={0}'.format(getBoolStr(self.bSensitivity_Of_Constraint)))
        if self.bSensitivities != obj.bSensitivities:
            paramArgs.append('bSensitivities={0}'.format(getBoolStr(self.bSensitivities)))
        return 'Optimization_Output_Parameter({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(
            1 if self.bNodalShapeVariation else 0,
            1 if self.bShapeVariation else 0,
            1 if self.bNodalDensityRation else 0,
            1 if self.bDensityRation else 0,
            1 if self.bSensitivity else 0,
            1 if self.bSensitivity_Of_Objective else 0,
            1 if self.bSensitivity_Of_Constraint else 0,
            1 if self.bSensitivities else 0) + rightBracket

class Post_Tree_Item_Target:
    def __init__(self,
        iAnalysisType=0,
        iResultSet=0,
        iTimeStep=0,
        iTreeIndex=0):
        self.iAnalysisType = iAnalysisType
        self.iResultSet = iResultSet
        self.iTimeStep = iTimeStep
        self.iTreeIndex = iTreeIndex
                                    
                                                  
    def isDefault(self):
        obj = Post_Tree_Item_Target()
        return self.iAnalysisType == obj.iAnalysisType and \
            self.iResultSet == obj.iResultSet and \
            self.iTimeStep == obj.iTimeStep and \
            self.iTreeIndex == obj.iTreeIndex
                                                           
    def fromList(self, param):
        obj = Post_Tree_Item_Target()
        self.iAnalysisType = param[0] if len(param) > 0 else obj.iAnalysisType
        self.iResultSet = param[1] if len(param) > 0 else obj.iResultSet
        self.iTimeStep = param[2] if len(param) > 0 else obj.iTimeStep
        self.iTreeIndex = param[3] if len(param) > 0 else obj.iTreeIndex
                                                                                                      
        return self
    def __str__(self):
        obj = Post_Tree_Item_Target()
        paramArgs = []
        if self.iAnalysisType != obj.iAnalysisType:
            paramArgs.append('iAnalysisType={0}'.format(getValueStr(self.iAnalysisType)))
        if self.iResultSet != obj.iResultSet:
            paramArgs.append('iResultSet={0}'.format(getValueStr(self.iResultSet)))
        if self.iTimeStep != obj.iTimeStep:
            paramArgs.append('iTimeStep={0}'.format(getValueStr(self.iTimeStep)))
        if self.iTreeIndex != obj.iTreeIndex:
            paramArgs.append('iTreeIndex={0}'.format(getValueStr(self.iTreeIndex)))
                                                           
                                                                                                       
        return 'Post_Tree_Item_Target({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.iAnalysisType,
            self.iResultSet,
                                      
            self.iTimeStep,
            self.iTreeIndex) + rightBracket

class PostResultKey:
    def __init__(
        self,
        iAnalysisType=0,
        iAnalysisID=0,
        iResultSet=0,
        iTimeStep=0,
        iResultType=0,
        strResultName="",
        strResultCompName="",
        iResultPos=0,
    ):
        self.iAnalysisType = iAnalysisType
        self.iAnalysisID = iAnalysisID
        self.iResultSet = iResultSet
        self.iTimeStep = iTimeStep
        self.iResultType = iResultType
        self.strResultName = strResultName
        self.strResultCompName = strResultCompName
        self.iResultPos = iResultPos

    def isDefault(self):
        obj = PostResultKey()
        return (
            self.iAnalysisType == obj.iAnalysisType
            and self.iAnalysisID == obj.iAnalysisID
            and self.iResultSet == obj.iResultSet
            and self.iTimeStep == obj.iTimeStep
            and self.iResultType == obj.iResultType
            and self.strResultName == obj.strResultName
            and self.strResultCompName == obj.strResultCompName
            and self.iResultPos == obj.iResultPos
        )

    def fromList(self, param):
        obj = PostResultKey()
        self.iAnalysisType = param[0] if len(param) > 0 else obj.iAnalysisType
        self.iAnalysisID = param[1] if len(param) > 1 else obj.iAnalysisID
        self.iResultSet = param[2] if len(param) > 2 else obj.iResultSet
        self.iTimeStep = param[3] if len(param) > 3 else obj.iTimeStep
        self.iResultType = param[4] if len(param) > 4 else obj.iResultType
        self.strResultName = str(param[5]) if len(param) > 5 else obj.strResultName
        self.strResultCompName = (
            str(param[6]) if len(param) > 6 else obj.strResultCompName
        )
        self.iResultPos = param[7] if len(param) > 7 else obj.iResultPos
        return self

    def __str__(self):
        obj = PostResultKey()
        paramArgs = []
        if self.iAnalysisType != obj.iAnalysisType:
            paramArgs.append(
                "iAnalysisType={0}".format(getValueStr(self.iAnalysisType))
            )
        if self.iAnalysisID != obj.iAnalysisID:
            paramArgs.append("iAnalysisID={0}".format(getValueStr(self.iAnalysisID)))
        if self.iResultSet != obj.iResultSet:
            paramArgs.append("iResultSet={0}".format(getValueStr(self.iResultSet)))
        if self.iTimeStep != obj.iTimeStep:
            paramArgs.append("iTimeStep={0}".format(getValueStr(self.iTimeStep)))
        if self.iResultType != obj.iResultType:
            paramArgs.append("iResultType={0}".format(getValueStr(self.iResultType)))
        if self.strResultName != obj.strResultName:
            paramArgs.append("strResultName={0}".format('"' + self.strResultName + '"'))
        if self.strResultCompName != obj.strResultCompName:
            paramArgs.append(
                "strResultCompName={0}".format('"' + self.strResultCompName + '"')
            )
        if self.iResultPos != obj.iResultPos:
            paramArgs.append("iResultPos={0}".format(getValueStr(self.iResultPos)))
        return "PostResultKey({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(
                self.iAnalysisType,
                self.iAnalysisID,
                self.iResultSet,
                self.iTimeStep,
                self.iResultType,
                '"' + self.strResultName + '"',
                '"' + self.strResultCompName + '"',
                self.iResultPos,
            )
            + rightBracket
        )
    
    def toNativeStr2(self, isOneParam=True):
        leftBracket = "{" if isOneParam else ""
        rightBracket = "}" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}".format(
                self.iAnalysisType,
                self.iResultSet,
                self.iTimeStep,
                self.iResultType,
                self.iResultPos,
            )
            + rightBracket
        )

class PostDataOp:
    def __init__(
        self,
        iResultLocation=0,
        iOptionCoord=0,
        iOptionLoad1D=0,
        iOptionLoad2D=0,
        iOptionConversion=0,
        iOptionContinuous=0,
        iOptionComplex=0,
        iOptionAmount=0,
        dOptionPhaseAngle=0.0,
        iUserCoordSysId=0,
    ):
        self.iResultLocation = iResultLocation
        self.iOptionCoord = iOptionCoord
        self.iOptionLoad1D = iOptionLoad1D
        self.iOptionLoad2D = iOptionLoad2D
        self.iOptionConversion = iOptionConversion
        self.iOptionContinuous = iOptionContinuous
        self.iOptionComplex = iOptionComplex
        self.iOptionAmount = iOptionAmount
        self.dOptionPhaseAngle = dOptionPhaseAngle
        self.iUserCoordSysId = iUserCoordSysId

    def isDefault(self):
        obj = PostDataOp()
        return (
            self.iResultLocation == obj.iResultLocation
            and self.iOptionCoord == obj.iOptionCoord
            and self.iOptionLoad1D == obj.iOptionLoad1D
            and self.iOptionLoad2D == obj.iOptionLoad2D
            and self.iOptionConversion == obj.iOptionConversion
            and self.iOptionContinuous == obj.iOptionContinuous
            and self.iOptionComplex == obj.iOptionComplex
            and self.iOptionAmount == obj.iOptionAmount
            and self.dOptionPhaseAngle == obj.dOptionPhaseAngle
            and self.iUserCoordSysId == obj.iUserCoordSysId
        )

    def fromList(self, param):
        obj = PostDataOp()
        self.iResultLocation = param[0] if len(param) > 0 else obj.iResultLocation
        self.iOptionCoord = param[1] if len(param) > 1 else obj.iOptionCoord
        self.iOptionLoad1D = param[2] if len(param) > 2 else obj.iOptionLoad1D
        self.iOptionLoad2D = param[3] if len(param) > 3 else obj.iOptionLoad2D
        self.iOptionConversion = param[4] if len(param) > 4 else obj.iOptionConversion
        self.iOptionContinuous = param[5] if len(param) > 5 else obj.iOptionContinuous
        self.iOptionComplex = param[6] if len(param) > 6 else obj.iOptionComplex
        self.iOptionAmount = param[7] if len(param) > 7 else obj.iOptionAmount
        self.dOptionPhaseAngle = (
            normalizeDoubleType(param[8]) if len(param) > 8 else obj.dOptionPhaseAngle
        )
        self.iUserCoordSysId = param[9] if len(param) > 9 else obj.iUserCoordSysId
        return self

    def __str__(self):
        obj = PostDataOp()
        paramArgs = []
        if self.iResultLocation != obj.iResultLocation:
            paramArgs.append(
                "iResultLocation={0}".format(getValueStr(self.iResultLocation))
            )
        if self.iOptionCoord != obj.iOptionCoord:
            paramArgs.append("iOptionCoord={0}".format(getValueStr(self.iOptionCoord)))
        if self.iOptionLoad1D != obj.iOptionLoad1D:
            paramArgs.append(
                "iOptionLoad1D={0}".format(getValueStr(self.iOptionLoad1D))
            )
        if self.iOptionLoad2D != obj.iOptionLoad2D:
            paramArgs.append(
                "iOptionLoad2D={0}".format(getValueStr(self.iOptionLoad2D))
            )
        if self.iOptionConversion != obj.iOptionConversion:
            paramArgs.append(
                "iOptionConversion={0}".format(getValueStr(self.iOptionConversion))
            )
        if self.iOptionContinuous != obj.iOptionContinuous:
            paramArgs.append(
                "iOptionContinuous={0}".format(getValueStr(self.iOptionContinuous))
            )
        if self.iOptionComplex != obj.iOptionComplex:
            paramArgs.append(
                "iOptionComplex={0}".format(getValueStr(self.iOptionComplex))
            )
        if self.iOptionAmount != obj.iOptionAmount:
            paramArgs.append(
                "iOptionAmount={0}".format(getValueStr(self.iOptionAmount))
            )
        if self.dOptionPhaseAngle != obj.dOptionPhaseAngle:
            paramArgs.append(
                "dOptionPhaseAngle={0}".format(getValueStr(self.dOptionPhaseAngle))
            )
        if self.iUserCoordSysId != obj.iUserCoordSysId:
            paramArgs.append(
                "iUserCoordSysId={0}".format(getValueStr(self.iUserCoordSysId))
            )
        return "PostDataOp({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}".format(
                self.iResultLocation,
                self.iOptionCoord,
                self.iOptionLoad1D,
                self.iOptionLoad2D,
                self.iOptionConversion,
                self.iOptionContinuous,
                self.iOptionComplex,
                self.iOptionAmount,
                self.dOptionPhaseAngle,
                self.iUserCoordSysId,
            )
            + rightBracket
        )

class PostContourSetting:
    def __init__(self, postResultKey, postDataOp, bMultiResult=False):
        self.postResultKey = postResultKey
        self.postDataOp = postDataOp
        self.bMultiResult = bMultiResult

    def isDefault(self):
        obj = PostContourSetting(PostResultKey(), PostDataOp())
        return (
            self.postResultKey == obj.postResultKey
            and self.postDataOp == obj.postDataOp
            and self.bMultiResult == obj.bMultiResult
        )

    def fromList(self, param):
        obj = PostContourSetting(PostResultKey(), PostDataOp())
        self.postResultKey.fromList(
            [
                param[0],
                param[1],
                param[2],
                param[3],
                param[4],
                param[5],
                param[6],
                param[7],
            ]
        )
        self.postDataOp.fromList(
            [
                param[8],
                param[9],
                param[10],
                param[11],
                param[12],
                param[13],
                param[14],
                param[15],
                param[16],
                param[17],
            ]
        )
        self.bMultiResult = param[18] if len(param) > 18 else obj.bMultiResult
        return self

    def __str__(self):
        obj = PostContourSetting(PostResultKey(), PostDataOp())
        paramArgs = []
        if self.postResultKey != obj.postResultKey:
            paramArgs.append(
                "postResultKey={0}".format(getValueStr(self.postResultKey))
            )
        if self.postDataOp != obj.postDataOp:
            paramArgs.append("postDataOp={0}".format(getValueStr(self.postDataOp)))
        if self.bMultiResult != obj.bMultiResult:
            paramArgs.append("bMultiResult={0}".format(getValueStr(self.bMultiResult)))
        return "PostContourSetting({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self):
        return "{0}, {1}, {2}".format(
            self.postResultKey.toNativeStr(),
            self.postDataOp.toNativeStr(),
            self.bMultiResult,
        )

    def toNativePostResultKeyStr(self):
        return "{0}".format(self.postResultKey.toNativeStr())

    def toNativePostDataOpStr(self):
        return "{0}".format(self.postDataOp.toNativeStr())

class PostDataOptionDeform:
    def __init__(
        self,
        iScaleMethod=0,
        dDeformRatio=0.07,
        bEachDirectionComp=False,
        dlDirectionRatio=[0.07, 0.07, 0.07],
        bShowOriginalShade=False,
        bShowOriginalMesh=True,
        bShowOriginalEdge=True,
        iColorShade=13158600,
        iColorMesh=11184810,
        iColorEdge=11184810,
        dOriginalShadeTrans=0.8,
    ):
        self.iScaleMethod = iScaleMethod
        self.dDeformRatio = dDeformRatio
        self.bEachDirectionComp = bEachDirectionComp
        self.dlDirectionRatio = dlDirectionRatio
        self.bShowOriginalShade = bShowOriginalShade
        self.bShowOriginalMesh = bShowOriginalMesh
        self.bShowOriginalEdge = bShowOriginalEdge
        self.iColorShade = iColorShade
        self.iColorMesh = iColorMesh
        self.iColorEdge = iColorEdge
        self.dOriginalShadeTrans = dOriginalShadeTrans

    def isDefault(self):
        obj = PostDataOptionDeform()
        return (
            self.iScaleMethod == obj.iScaleMethod
            and self.dDeformRatio == obj.dDeformRatio
            and self.bEachDirectionComp == obj.bEachDirectionComp
            and self.dlDirectionRatio == obj.dlDirectionRatio
            and self.bShowOriginalShade == obj.bShowOriginalShade
            and self.bShowOriginalMesh == obj.bShowOriginalMesh
            and self.bShowOriginalEdge == obj.bShowOriginalEdge
            and self.iColorShade == obj.iColorShade
            and self.iColorMesh == obj.iColorMesh
            and self.iColorEdge == obj.iColorEdge
            and self.dOriginalShadeTrans == obj.dOriginalShadeTrans
        )

    def fromList(self, param):
        obj = PostDataOptionDeform()
        self.iScaleMethod = param[0] if len(param) > 0 else obj.iScaleMethod
        self.dDeformRatio = (
            normalizeDoubleType(param[1]) if len(param) > 1 else obj.dDeformRatio
        )
        self.bEachDirectionComp = (
            getBoolValue(param[2]) if len(param) > 2 else obj.bEachDirectionComp
        )
        self.dlDirectionRatio = (
            [normalizeDoubleType(tok) for tok in param[3]]
            if len(param) > 3
            else obj.dlDirectionRatio
        )
        self.bShowOriginalShade = (
            getBoolValue(param[4]) if len(param) > 4 else obj.bShowOriginalShade
        )
        self.bShowOriginalMesh = (
            getBoolValue(param[5]) if len(param) > 5 else obj.bShowOriginalMesh
        )
        self.bShowOriginalEdge = (
            getBoolValue(param[6]) if len(param) > 6 else obj.bShowOriginalEdge
        )
        self.iColorShade = param[7] if len(param) > 7 else obj.iColorShade
        self.iColorMesh = param[8] if len(param) > 8 else obj.iColorMesh
        self.iColorEdge = param[9] if len(param) > 9 else obj.iColorEdge
        self.dOriginalShadeTrans = (
            normalizeDoubleType(param[10])
            if len(param) > 10
            else obj.dOriginalShadeTrans
        )
        return self

    def __str__(self):
        obj = PostDataOptionDeform()
        paramArgs = []
        if self.iScaleMethod != obj.iScaleMethod:
            paramArgs.append("iScaleMethod={0}".format(getValueStr(self.iScaleMethod)))
        if self.dDeformRatio != obj.dDeformRatio:
            paramArgs.append("dDeformRatio={0}".format(getValueStr(self.dDeformRatio)))
        if self.bEachDirectionComp != obj.bEachDirectionComp:
            paramArgs.append(
                "bEachDirectionComp={0}".format(getValueStr(self.bEachDirectionComp))
            )
        if self.dlDirectionRatio != obj.dlDirectionRatio:
            paramArgs.append(
                "dlDirectionRatio={0}".format(getValueStr(self.dlDirectionRatio))
            )
        if self.bShowOriginalShade != obj.bShowOriginalShade:
            paramArgs.append(
                "bShowOriginalShade={0}".format(getValueStr(self.bShowOriginalShade))
            )
        if self.bShowOriginalMesh != obj.bShowOriginalMesh:
            paramArgs.append(
                "bShowOriginalMesh={0}".format(getValueStr(self.bShowOriginalMesh))
            )
        if self.bShowOriginalEdge != obj.bShowOriginalEdge:
            paramArgs.append(
                "bShowOriginalEdge={0}".format(getValueStr(self.bShowOriginalEdge))
            )
        if self.iColorShade != obj.iColorShade:
            paramArgs.append("iColorShade={0}".format(getValueStr(self.iColorShade)))
        if self.iColorMesh != obj.iColorMesh:
            paramArgs.append("iColorMesh={0}".format(getValueStr(self.iColorMesh)))
        if self.iColorEdge != obj.iColorEdge:
            paramArgs.append("iColorEdge={0}".format(getValueStr(self.iColorEdge)))
        if self.dOriginalShadeTrans != obj.dOriginalShadeTrans:
            paramArgs.append(
                "dOriginalShadeTrans={0}".format(getValueStr(self.dOriginalShadeTrans))
            )
        return "PostDataOptionDeform({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}".format(
                self.iScaleMethod,
                self.dDeformRatio,
                self.bEachDirectionComp,
                self.dlDirectionRatio,
                self.bShowOriginalShade,
                self.bShowOriginalMesh,
                self.bShowOriginalEdge,
                self.iColorShade,
                self.iColorMesh,
                self.iColorEdge,
                self.dOriginalShadeTrans,
            )
            + rightBracket
        )

class ACCELERATION_LOAD_ACCEL_DATA:
    def __init__(self,
        iAccelerationDirection=0,
        crCoord=None,
        vecAccelerationValue=[DFLT_DBL, DFLT_DBL, DFLT_DBL],
        iInputUnit=0,
        crLOCi_VALi_Table=None):
        self.iAccelerationDirection = iAccelerationDirection
        self.crCoord = crCoord
        self.vecAccelerationValue = vecAccelerationValue
        self.iInputUnit = iInputUnit
        self.crLOCi_VALi_Table = crLOCi_VALi_Table
    def isDefault(self):
        obj = ACCELERATION_LOAD_ACCEL_DATA()
        return self.iAccelerationDirection == obj.iAccelerationDirection and \
            self.crCoord == obj.crCoord and \
            self.vecAccelerationValue == obj.vecAccelerationValue and \
            self.iInputUnit == obj.iInputUnit and \
            self.crLOCi_VALi_Table == obj.crLOCi_VALi_Table
    def fromList(self, param):
        obj = ACCELERATION_LOAD_ACCEL_DATA()
        self.iAccelerationDirection = param[0] if len(param) > 0 else obj.iAccelerationDirection
        self.crCoord = getCursorValue(param[1]) if len(param) > 1 else obj.crCoord
        self.vecAccelerationValue = [normalizeDoubleType(tok) for tok in param[2]] if len(param) > 2 else obj.vecAccelerationValue
        self.iInputUnit = param[3] if len(param) > 3 else obj.iInputUnit
        self.crLOCi_VALi_Table = getCursorValue(param[4]) if len(param) > 4 else obj.crLOCi_VALi_Table
        return self
    def __str__(self):
        obj = ACCELERATION_LOAD_ACCEL_DATA()
        paramArgs = []
        if self.iAccelerationDirection != obj.iAccelerationDirection:
            paramArgs.append('iAccelerationDirection={0}'.format(getValueStr(self.iAccelerationDirection)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        if self.vecAccelerationValue != obj.vecAccelerationValue:
            paramArgs.append('vecAccelerationValue={0}'.format(getValueStr(self.vecAccelerationValue)))
        if self.iInputUnit != obj.iInputUnit:
            paramArgs.append('iInputUnit={0}'.format(getValueStr(self.iInputUnit)))
        if self.crLOCi_VALi_Table != obj.crLOCi_VALi_Table:
            paramArgs.append('crLOCi_VALi_Table={0}'.format(getCursorValueStr(self.crLOCi_VALi_Table)))
        return 'ACCELERATION_LOAD_ACCEL_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}'.format(
            self.iAccelerationDirection,
            str(self.crCoord) if self.crCoord is not None else '0:0',
            self.vecAccelerationValue,
            self.iInputUnit,
            str(self.crLOCi_VALi_Table) if self.crLOCi_VALi_Table is not None else '0:0') + rightBracket

class ACCELERATION_LOAD_ACCEL1_DATA:
    def __init__(self,
        vecAccelerationValue=[DFLT_DBL, DFLT_DBL, DFLT_DBL],
        iInputUnit=0,
        dScaleFactor=1,
        crCoord=None):
        self.vecAccelerationValue = vecAccelerationValue
        self.iInputUnit = iInputUnit
        self.dScaleFactor = dScaleFactor
        self.crCoord = crCoord
    def isDefault(self):
        obj = ACCELERATION_LOAD_ACCEL1_DATA()
        return self.vecAccelerationValue == obj.vecAccelerationValue and \
            self.iInputUnit == obj.iInputUnit and \
            self.dScaleFactor == obj.dScaleFactor and \
            self.crCoord == obj.crCoord
    def fromList(self, param):
        obj = ACCELERATION_LOAD_ACCEL1_DATA()
        self.vecAccelerationValue = [normalizeDoubleType(tok) for tok in param[0]] if len(param) > 0 else obj.vecAccelerationValue
        self.iInputUnit = param[1] if len(param) > 1 else obj.iInputUnit
        self.dScaleFactor = normalizeDoubleType(param[2]) if len(param) > 2 else obj.dScaleFactor
        self.crCoord = getCursorValue(param[3]) if len(param) > 3 else obj.crCoord
        return self
    def __str__(self):
        obj = ACCELERATION_LOAD_ACCEL1_DATA()
        paramArgs = []
        if self.vecAccelerationValue != obj.vecAccelerationValue:
            paramArgs.append('vecAccelerationValue={0}'.format(getValueStr(self.vecAccelerationValue)))
        if self.iInputUnit != obj.iInputUnit:
            paramArgs.append('iInputUnit={0}'.format(getValueStr(self.iInputUnit)))
        if self.dScaleFactor != obj.dScaleFactor:
            paramArgs.append('dScaleFactor={0}'.format(getValueStr(self.dScaleFactor)))
        if self.crCoord != obj.crCoord:
            paramArgs.append('crCoord={0}'.format(getCursorValueStr(self.crCoord)))
        return 'ACCELERATION_LOAD_ACCEL1_DATA({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.vecAccelerationValue,
            self.iInputUnit,
            self.dScaleFactor,
            str(self.crCoord) if self.crCoord is not None else '0:0') + rightBracket

class ResultVariable:
    def __init__(self,
        crReferencePostJob=None,
        strName="",
        iAnalysisType=0,
        iResultSet=0,
        iTimeStep=0,
        iResultType=0,
        iResultPos=0):
        self.crReferencePostJob = crReferencePostJob
        self.strName = strName
        self.iAnalysisType = iAnalysisType
        self.iResultSet = iResultSet
        self.iTimeStep = iTimeStep
        self.iResultType = iResultType
        self.iResultPos = iResultPos
    def isDefault(self):
        obj = ResultVariable()
        return self.crReferencePostJob == obj.crReferencePostJob and \
            self.strName == obj.strName and \
            self.iAnalysisType == obj.iAnalysisType and \
            self.iResultSet == obj.iResultSet and \
            self.iTimeStep == obj.iTimeStep and \
            self.iResultType == obj.iResultType and \
            self.iResultPos == obj.iResultPos
    def fromList(self, param):
        obj = ResultVariable()
        self.crReferencePostJob = getCursorValue(param[0]) if len(param) > 0 else obj.crReferencePostJob
        self.strName = param[1] if len(param) > 1 else obj.strName
        self.iAnalysisType = param[2] if len(param) > 2 else obj.iAnalysisType
        self.iResultSet = param[3] if len(param) > 3 else obj.iResultSet
        self.iTimeStep = param[4] if len(param) > 4 else obj.iTimeStep
        self.iResultType = param[5] if len(param) > 5 else obj.iResultType
        self.iResultPos = param[6] if len(param) > 6 else obj.iResultPos
        return self
    def __str__(self):
        obj = ResultVariable()
        paramArgs = []
        if self.crReferencePostJob != obj.crReferencePostJob:
            paramArgs.append('crReferencePostJob={0}'.format(getCursorValueStr(self.crReferencePostJob)))
        if self.strName != obj.strName:
            paramArgs.append('strName={0}'.format('"' + self.strName + '"'))
        if self.iAnalysisType != obj.iAnalysisType:
            paramArgs.append('iAnalysisType={0}'.format(getValueStr(self.iAnalysisType)))
        if self.iResultSet != obj.iResultSet:
            paramArgs.append('iResultSet={0}'.format(getValueStr(self.iResultSet)))
        if self.iTimeStep != obj.iTimeStep:
            paramArgs.append('iTimeStep={0}'.format(getValueStr(self.iTimeStep)))
        if self.iResultType != obj.iResultType:
            paramArgs.append('iResultType={0}'.format(getValueStr(self.iResultType)))
        if self.iResultPos != obj.iResultPos:
            paramArgs.append('iResultPos={0}'.format(getValueStr(self.iResultPos)))
        return 'ResultVariable({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            str(self.crReferencePostJob) if self.crReferencePostJob is not None else '0:0',
            '"' + self.strName + '"',
            self.iAnalysisType,
            self.iResultSet,
            self.iTimeStep,
            self.iResultType,
            self.iResultPos) + rightBracket

class PostTimeStepInfo:
    def __init__(
        self,
        iMode=DFLT_INT,
        dTime=FLT_MAX,
        dFrequency=FLT_MAX,
        iBaseAnalysisType=0,
        strResultSetName="",
    ):
        self.iMode = iMode
        self.dTime = dTime
        self.dFrequency = dFrequency
        self.iBaseAnalysisType = iBaseAnalysisType
        self.strResultSetName = strResultSetName

    def isDefault(self):
        obj = PostTimeStepInfo()
        return (
            self.iMode == obj.iMode
            and self.dTime == obj.dTime
            and self.dFrequency == obj.dFrequency
            and self.iBaseAnalysisType == obj.iBaseAnalysisType
            and self.strResultSetName == obj.strResultSetName
        )

    def fromList(self, param):
        obj = PostTimeStepInfo()
        self.iMode = param[0] if len(param) > 0 else obj.iMode
        self.dTime = param[1] if len(param) > 1 else obj.dTime
        self.dFrequency = param[2] if len(param) > 2 else obj.dFrequency
        self.iBaseAnalysisType = param[3] if len(param) > 3 else obj.iBaseAnalysisType
        self.strResultSetName = param[4] if len(param) > 4 else obj.strResultSetName
        return self        

    def __str__(self):
        obj = PostTimeStepInfo()
        paramArgs = []
        if self.iMode != obj.iMode:
            paramArgs.append("iMode={0}".format(getValueStr(self.iMode)))
        if self.dTime != obj.dTime:
            paramArgs.append("dTime={0}".format(getValueStr(self.dTime)))
        if self.dFrequency != obj.dFrequency:
            paramArgs.append("dFrequency={0}".format(getValueStr(self.dFrequency)))
        if self.iBaseAnalysisType != obj.iBaseAnalysisType:
            paramArgs.append(
                "iBaseAnalysisType={0}".format(getValueStr(self.iBaseAnalysisType))
            )
        if self.strResultSetName != obj.strResultSetName:
            paramArgs.append("strResultSetName={0}".format(self.strResultSetName))
        return "PostTimeStepInfo({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}".format(
                self.iMode,
                self.dTime,
                self.dFrequency,
                self.iBaseAnalysisType,
                self.strResultSetName,
            )
            + rightBracket
        )

class PostStepItem:
    def __init__(
        self,
        postTimeStepInfo=PostTimeStepInfo(),
        crPostJob=None,
        iAnalysisType=0,
        iResultSet=0,
        iTimeStep=0,
    ):
        self.postTimeStepInfo = postTimeStepInfo
        self.crPostJob = crPostJob
        self.iAnalysisType = iAnalysisType
        self.iResultSet = iResultSet
        self.iTimeStep = iTimeStep

    def isDefault(self):
        obj = PostStepItem()
        return (
            self.postTimeStepInfo == obj.postTimeStepInfo
            and self.crPostJob == obj.crPostJob
            and self.iAnalysisType == obj.iAnalysisType
            and self.iResultSet == obj.iResultSet
            and self.iTimeStep == obj.iTimeStep
        )

    def fromList(self, param):
        obj = PostStepItem()
        self.postTimeStepInfo.fromList(param[0]) if len(
            param
        ) > 0 else obj.postTimeStepInfo
        self.crPostJob = getCursorValue(param[1]) if len(param) > 1 else obj.crPostJob
        self.iAnalysisType = param[2] if len(param) > 2 else obj.iAnalysisType
        self.iResultSet = param[3] if len(param) > 3 else obj.iResultSet
        self.iTimeStep = param[4] if len(param) > 4 else obj.iTimeStep
        return self

    def __str__(self):
        obj = PostStepItem()
        paramArgs = []
        if self.postTimeStepInfo != obj.postTimeStepInfo:
            paramArgs.append(
                "postTimeStepInfo={0}".format(getValueStr(self.postTimeStepInfo))
            )
        if self.crPostJob != obj.crPostJob:
            paramArgs.append("crPostJob={0}".format(getCursorValueStr(self.crPostJob)))
        if self.iAnalysisType != obj.iAnalysisType:
            paramArgs.append(
                "iAnalysisType={0}".format(getValueStr(self.iAnalysisType))
            )
        if self.iResultSet != obj.iResultSet:
            paramArgs.append("iResultSet={0}".format(getValueStr(self.iResultSet)))
        if self.iTimeStep != obj.iTimeStep:
            paramArgs.append("iTimeStep={0}".format(getValueStr(self.iTimeStep)))
        return "PostStepItem({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}".format(
                self.postTimeStepInfo.toNativeStr(),
                str(self.crPostJob) if self.crPostJob is not None else "0:0",
                self.iAnalysisType,
                self.iResultSet,
                self.iTimeStep,
            )
            + rightBracket
        )

class SubcaseItem:
    def __init__(self,
        iSID=1,
        strName="",
        dCoefficient=1.0,
        bStatus=True):
        self.iSID = iSID
        self.strName = strName
        self.dCoefficient = dCoefficient
        self.bStatus = bStatus
    def isDefault(self):
        obj = SubcaseItem()
        return self.iSID == obj.iSID and \
            self.strName == obj.strName and \
            self.dCoefficient == obj.dCoefficient and \
            self.bStatus == obj.bStatus
    def fromList(self, param):
        obj = SubcaseItem()
        self.iSID = param[0] if len(param) > 0 else obj.iSID
        self.strName = param[1] if len(param) > 1 else obj.strName
        self.dCoefficient = param[2] if len(param) > 2 else obj.dCoefficient
        self.bStatus = param[3] if len(param) > 3 else obj.bStatus
        return self
    def __str__(self):
        obj = SubcaseItem()
        paramArgs = []
        if self.iSID != obj.iSID:
            paramArgs.append('iSID={0}'.format(getValueStr(self.iSID)))
        if self.strName != obj.strName:
            paramArgs.append('strName={0}'.format('"' + self.strName + '"'))
        if self.dCoefficient != obj.dCoefficient:
            paramArgs.append('dCoefficient={0}'.format(getValueStr(self.dCoefficient)))
        if self.bStatus != obj.bStatus:
            paramArgs.append('bStatus={0}'.format(getBoolStr(self.bStatus)))
        return 'SubcaseItem({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.iSID,
            '"' + self.strName + '"',
            self.dCoefficient,
            1 if self.bStatus else 0) + rightBracket

class SafetyItem:
    def __init__(self,
        crPart=None,
        dThreshold=0.0):
        self.crPart = crPart
        self.dThreshold = dThreshold
    def isDefault(self):
        obj = SafetyItem()
        return self.crPart == obj.crPart and \
            self.dThreshold == obj.dThreshold
    def fromList(self, param):
        obj = SafetyItem()
        self.crPart = getCursorValue(param[0]) if len(param) > 0 else obj.crPart
        self.dThreshold = param[1] if len(param) > 1 else obj.dThreshold
        return self
    def __str__(self):
        obj = SafetyItem()
        paramArgs = []
        if self.crPart != obj.crPart:
            paramArgs.append('crPart={0}'.format(getCursorValueStr(self.crPart)))
        if self.dThreshold != obj.dThreshold:
            paramArgs.append('dThreshold={0}'.format(getValueStr(self.dThreshold)))
        return 'SafetyItem({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            str(self.crPart) if self.crPart is not None else '0:0',
            self.dThreshold) + rightBracket

class PEAKHOLD_SUBCASE_MAP:
    def __init__(self,
        iResultSet=1,
        listSubCaseItems=[]):
        self.iResultSet = iResultSet
        self.listSubCaseItems = listSubCaseItems
    def isDefault(self):
        obj = PEAKHOLD_SUBCASE_MAP()
        return self.iResultSet == obj.iResultSet and \
            self.listSubCaseItems == obj.listSubCaseItems
    def fromList(self, param):
        obj = PEAKHOLD_SUBCASE_MAP()
        self.iResultSet = param[0] if len(param) > 1 else obj.iResultSet
        self.listSubCaseItems = param[1] if len(param) > 1 else obj.listSubCaseItems
        return self
    def __str__(self):
        obj = PEAKHOLD_SUBCASE_MAP()
        paramArgs = []
        if self.iResultSet != obj.iResultSet:
            paramArgs.append('iResultSet={0}'.format(getValueStr(self.iResultSet)))
        if self.listSubCaseItems != obj.listSubCaseItems:
            listSubCaseItems = [SubcaseItem().fromList(tok) for tok in self.listSubCaseItems]
            paramArgs.append('listSubCaseItems=[' + ', '.join(str(tok) for tok in listSubCaseItems) + ']')
        return 'PEAKHOLD_SUBCASE_MAP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            self.iResultSet,
            '[' + ', '.join([tok.toNativeStr(isOneParam=True) for tok in self.listSubCaseItems]) + ']') + rightBracket
    
class General_Report_LinearStatic_Data:
    def __init__(self,
        strPartName="",
        strPropName="",
        strMatName="",
        dValue=0.0):
        self.strPartName = strPartName
        self.strPropName = strPropName
        self.strMatName = strMatName
        self.dValue = dValue
                                    
                                                  
    def isDefault(self):
        obj = General_Report_LinearStatic_Data()
        return self.strPartName == obj.strPartName and \
            self.strPropName == obj.strPropName and \
            self.strMatName == obj.strMatName and \
            self.dValue == obj.dValue
                                                           
    def fromList(self, param):
        obj = General_Report_LinearStatic_Data()
        self.strPartName = param[0] if len(param) > 0 else obj.strPartName
        self.strPropName = param[1] if len(param) > 0 else obj.strPropName
        self.strMatName = param[2] if len(param) > 0 else obj.strMatName
        self.dValue = param[3] if len(param) > 0 else obj.dValue
                                                                                                      
        return self
    def __str__(self):
        obj = General_Report_LinearStatic_Data()
        paramArgs = []
        if self.strPartName != obj.strPartName:
            paramArgs.append('strPartName="{0}"'.format(getValueStr(self.strPartName)))
        if self.strPropName != obj.strPropName:
            paramArgs.append('strPropName="{0}"'.format(getValueStr(self.strPropName)))
        if self.strMatName != obj.strMatName:
            paramArgs.append('strMatName="{0}"'.format(getValueStr(self.strMatName)))
        if self.dValue != obj.dValue:
            paramArgs.append('dValue={0}'.format(getValueStr(self.dValue)))
                                                           
                                                                                                       
        return 'General_Report_LinearStatic_Data({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}, {2}, {3}'.format(
            self.strPartName,
            self.strPropName,                                      
            self.strMatName,
            self.dValue) + rightBracket

class FATIGUE_SUBCASE_MAP:
    def __init__(self,
        iResultSet=1,
        listSubCaseItems=[]):
        self.iResultSet = iResultSet
        self.listSubCaseItems = listSubCaseItems
    def isDefault(self):
        obj = FATIGUE_SUBCASE_MAP()
        return self.iResultSet == obj.iResultSet and \
            self.listSubCaseItems == obj.listSubCaseItems
    def fromList(self, param):
        obj = FATIGUE_SUBCASE_MAP()
        self.iResultSet = param[0] if len(param) > 1 else obj.iResultSet
        self.listSubCaseItems = param[1] if len(param) > 1 else obj.listSubCaseItems
        return self
    def __str__(self):
        obj = FATIGUE_SUBCASE_MAP()
        paramArgs = []
        if self.iResultSet != obj.iResultSet:
            paramArgs.append('iResultSet={0}'.format(getValueStr(self.iResultSet)))
        if self.listSubCaseItems != obj.listSubCaseItems:
            listSubCaseItems = [SubcaseItem().fromList(tok) for tok in self.listSubCaseItems]
            paramArgs.append('listSubCaseItems=[' + ', '.join(str(tok) for tok in listSubCaseItems) + ']')
        return 'FATIGUE_SUBCASE_MAP({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '(' if isOneParam else ''
        rightBracket = ')' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            self.iResultSet,
            '[' + ', '.join([tok.toNativeStr(isOneParam=True) for tok in self.listSubCaseItems]) + ']') + rightBracket

class PostDataVizOptAnimation:
    def __init__(
        self,
        iMode=0,  # Single
        iFPS=8,  # 4 FPS
        iDivideNum=8,  # 8 Frames divide
        iDivideType=1,  # Linear
        iLoopType=1,  # One way
        iAnimationResType=0,
        bApplyDeform=True,  # Apply Deform
        bLocus=False,  # No Tracing
        bPhaseAngleAni=False,  # Phase angle animation type setting
        bAcousticCombineAni=False,  # Acoustic combine animation setting
        listSubcaseIds=[],  # Selected Subcases
        bMultiAnalysis=False,
        bMemCache=True,
        bFixContour=False,
        bSectionMode=0,
        bSetTime=False,
        dStartTime=0.0,
        dEndTime=0.0,
    ):
        self.iMode = iMode
        self.iFPS = iFPS
        self.iDivideNum = iDivideNum
        self.iDivideType = iDivideType
        self.iLoopType = iLoopType
        self.iAnimationResType = iAnimationResType
        self.bApplyDeform = bApplyDeform
        self.bLocus = bLocus
        self.bPhaseAngleAni = bPhaseAngleAni
        self.bAcousticCombineAni = bAcousticCombineAni
        self.listSubcaseIds = listSubcaseIds
        self.bMultiAnalysis = bMultiAnalysis
        self.bMemCache = bMemCache
        self.bFixContour = bFixContour
        self.bSectionMode = bSectionMode
        self.bSetTime = bSetTime
        self.dStartTime = dStartTime
        self.dEndTime = dEndTime
        ...

    def isDefault(self):
        obj = PostDataVizOptAnimation()
        return (
            self.iMode == obj.iMode
            and self.iFPS == obj.iFPS
            and self.iDivideNum == obj.iDivideNum
            and self.iDivideType == obj.iDivideType
            and self.iLoopType == obj.iLoopType
            and self.iAnimationResType == obj.iAnimationResType
            and self.bApplyDeform == obj.bApplyDeform
            and self.bLocus == obj.bLocus
            and self.bPhaseAngleAni == obj.bPhaseAngleAni
            and self.bAcousticCombineAni == obj.bAcousticCombineAni
            and self.listSubcaseIds == obj.listSubcaseIds
            and self.bMultiAnalysis == obj.bMultiAnalysis
            and self.bMemCache == obj.bMemCache
            and self.bFixContour == obj.bFixContour
            and self.bSectionMode == obj.bSectionMode
            and self.bSetTime == obj.bSetTime
            and self.dStartTime == obj.dStartTime
            and self.dEndTime == obj.dEndTime
        )

    def fromList(self, param):
        obj = PostDataVizOptAnimation()
        self.iMode = param[0] if len(param) > 0 else obj.iMode
        self.iFPS = param[1] if len(param) > 1 else obj.iFPS
        self.iDivideNum = param[2] if len(param) > 2 else obj.iDivideNum
        self.iDivideType = param[3] if len(param) > 3 else obj.iDivideType
        self.iLoopType = param[4] if len(param) > 4 else obj.iLoopType
        self.iAnimationResType = param[5] if len(param) > 5 else obj.iAnimationResType
        self.bApplyDeform = param[6] if len(param) > 6 else obj.bApplyDeform
        self.bLocus = param[7] if len(param) > 7 else obj.bLocus
        self.bPhaseAngleAni = param[8] if len(param) > 8 else obj.bPhaseAngleAni
        self.bAcousticCombineAni = (
            param[9] if len(param) > 9 else obj.bAcousticCombineAni
        )
        self.listSubcaseIds = param[10] if len(param) > 10 else obj.listSubcaseIds
        self.bMultiAnalysis = param[11] if len(param) > 11 else obj.bMultiAnalysis
        self.bMemCache = param[12] if len(param) > 12 else obj.bMemCache
        self.bFixContour = param[13] if len(param) > 13 else obj.bFixContour
        self.bSectionMode = param[14] if len(param) > 14 else obj.bSectionMode
        self.bSetTime = param[15] if len(param) > 15 else obj.bSetTime
        self.dStartTime = param[16] if len(param) > 16 else obj.dStartTime
        self.dEndTime = param[17] if len(param) > 17 else obj.dEndTime
        return self

    def __str__(self):
        obj = PostDataVizOptAnimation()
        paramArgs = []
        if self.iMode != obj.iMode:
            paramArgs.append("iMode={0}".format(getValueStr(self.iMode)))
        if self.iFPS != obj.iFPS:
            paramArgs.append("iFPS={0}".format(getValueStr(self.iFPS)))
        if self.iDivideNum != obj.iDivideNum:
            paramArgs.append("iDivideNum={0}".format(getValueStr(self.iDivideNum)))
        if self.iDivideType != obj.iDivideType:
            paramArgs.append("iDivideType={0}".format(getValueStr(self.iDivideType)))
        if self.iLoopType != obj.iLoopType:
            paramArgs.append("iLoopType={0}".format(getValueStr(self.iLoopType)))
        if self.iAnimationResType != obj.iAnimationResType:
            paramArgs.append(
                "iAnimationResType={0}".format(getValueStr(self.iAnimationResType))
            )
        if self.bApplyDeform != obj.bApplyDeform:
            paramArgs.append("bApplyDeform={0}".format(getBoolStr(self.bApplyDeform)))
        if self.bLocus != obj.bLocus:
            paramArgs.append("bLocus={0}".format(getBoolStr(self.bLocus)))
        if self.bPhaseAngleAni != obj.bPhaseAngleAni:
            paramArgs.append(
                "bPhaseAngleAni={0}".format(getBoolStr(self.bPhaseAngleAni))
            )
        if self.bAcousticCombineAni != obj.bAcousticCombineAni:
            paramArgs.append(
                "bAcousticCombineAni={0}".format(getBoolStr(self.bAcousticCombineAni))
            )
        if self.listSubcaseIds != obj.listSubcaseIds:
            paramArgs.append(
                "listSubcaseIds={0}".format(getValueStr(self.listSubcaseIds))
            )
        if self.bMultiAnalysis != obj.bMultiAnalysis:
            paramArgs.append(
                "bMultiAnalysis={0}".format(getBoolStr(self.bMultiAnalysis))
            )
        if self.bMemCache != obj.bMemCache:
            paramArgs.append("bMemCache={0}".format(getBoolStr(self.bMemCache)))
        if self.bFixContour != obj.bFixContour:
            paramArgs.append("bFixContour={0}".format(getBoolStr(self.bFixContour)))
        if self.bSectionMode != obj.bSectionMode:
            paramArgs.append("bSectionMode={0}".format(getBoolStr(self.bSectionMode)))
        if self.bSetTime != obj.bSetTime:
            paramArgs.append("bSetTime={0}".format(getBoolStr(self.bSetTime)))
        if self.dStartTime != obj.dStartTime:
            paramArgs.append("dStartTime={0}".format(getValueStr(self.dStartTime)))
        if self.dEndTime != obj.dEndTime:
            paramArgs.append("dEndTime={0}".format(getValueStr(self.dEndTime)))
        return "PostDataVizOptAnimation({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}".format(
                self.iMode,
                self.iFPS,
                self.iDivideNum,
                self.iDivideType,
                self.iLoopType,
                self.iAnimationResType,
                1 if self.bApplyDeform else 0,
                1 if self.bLocus else 0,
                1 if self.bPhaseAngleAni else 0,
                1 if self.bAcousticCombineAni else 0,
                self.listSubcaseIds,
                1 if self.bMultiAnalysis else 0,
                1 if self.bMemCache else 0,
                1 if self.bFixContour else 0,
                1 if self.bSectionMode else 0,
                1 if self.bSetTime else 0,
                self.dStartTime,
                self.dEndTime,
            )
            + rightBracket
        )

class PostDataVizOptCircle:
    def __init__(
        self,
        iScaleMethod=0,
        dRatioModel=0.03,  # relative to model size
        dRatioScreen=0.03,  # relative to screen
        dRatioValue=1.0,  # relative to real value (length of vector)
        # bUseArrow = True, # Has Arrow or not
        iColorHighlight=255,  # RGB(255, 0 , 0)
        iColorPositive=16777215,  # RGB(255, 255 , 255)
        iColorNegative=51400,  # RGB(200, 200, 0)
        bUseContour=False,
        iHighlightTarget=0,
        dHighlightValue1=0.0,
        dHighlightValue2=1.0,
        iDisplayTarget=0,  # Edge / Surface + Section / All (for solid)
        bReverse=False,
        # bAllModelVector = False,
        iThresholdOpt=0,
        dThresholdValue=0.0,
        dThresholdValueMax=100,
        iComparisonOpt=0,  # 0: < Greater , 1: <= Greater and Equal, 2: > Less, 3: >= Less and Equal
        iComparisonMinRangeOpt=0,  # 0: < Greater , 1: <= Greater and Equal
        iComparisonMaxRangeOpt=0,  # 0: < Greater , 1: <= Greater and Equal
    ):
        self.iScaleMethod = iScaleMethod
        self.dRatioModel = dRatioModel
        self.dRatioScreen = dRatioScreen
        self.dRatioValue = dRatioValue
        # self.bUseArrow = bUseArrow
        self.iColorHighlight = iColorHighlight
        self.iColorPositive = iColorPositive
        self.iColorNegative = iColorNegative
        self.bUseContour = bUseContour
        self.iHighlightTarget = iHighlightTarget
        self.dHighlightValue1 = dHighlightValue1
        self.dHighlightValue2 = dHighlightValue2
        self.iDisplayTarget = iDisplayTarget
        self.bReverse = bReverse
        # self.bAllModelVector = bAllModelVector
        self.iThresholdOpt = iThresholdOpt
        self.dThresholdValue = dThresholdValue
        self.dThresholdValueMax = dThresholdValueMax
        self.iComparisonOpt = iComparisonOpt
        self.iComparisonMinRangeOpt = iComparisonMinRangeOpt
        self.iComparisonMaxRangeOpt = iComparisonMaxRangeOpt
        ...

    def isDefault(self):
        obj = PostDataVizOptCircle()
        return (
            self.iScaleMethod == obj.iScaleMethod
            and self.dRatioModel == obj.dRatioModel
            and self.dRatioScreen == obj.dRatioScreen
            and self.dRatioValue == obj.dRatioValue
            # and self.bUseArrow == obj.bUseArrow
            and self.iColorHighlight == obj.iColorHighlight
            and self.iColorPositive == obj.iColorPositive
            and self.iColorNegative == obj.iColorNegative
            and self.bUseContour == obj.bUseContour
            and self.iHighlightTarget == obj.iHighlightTarget
            and self.dHighlightValue1 == obj.dHighlightValue1
            and self.dHighlightValue2 == obj.dHighlightValue2
            and self.iDisplayTarget == obj.iDisplayTarget
            and self.bReverse == obj.bReverse
            # and self.bAllModelVector == obj.bAllModelVector
            and self.iThresholdOpt == obj.iThresholdOpt
            and self.dThresholdValue == obj.dThresholdValue
            and self.dThresholdValueMax == obj.dThresholdValueMax
            and self.iComparisonOpt == obj.iComparisonOpt
            and self.iComparisonMinRangeOpt == obj.iComparisonMinRangeOpt
            and self.iComparisonMaxRangeOpt == obj.iComparisonMaxRangeOpt
        )

    def fromList(self, param):
        obj = PostDataVizOptCircle()
        self.iScaleMethod = param[0] if len(param) > 0 else obj.iScaleMethod
        self.dRatioModel = param[1] if len(param) > 1 else obj.dRatioModel
        self.dRatioScreen = param[2] if len(param) > 2 else obj.dRatioScreen
        self.dRatioValue = param[3] if len(param) > 3 else obj.dRatioValue
        # self.bUseArrow  = param[] if len(param) > else obj.bUseArrow
        self.iColorHighlight = param[4] if len(param) > 4 else obj.iColorHighlight
        self.iColorPositive = param[5] if len(param) > 5 else obj.iColorPositive
        self.iColorNegative = param[6] if len(param) > 6 else obj.iColorNegative
        self.bUseContour = param[7] if len(param) > 7 else obj.bUseContour
        self.iHighlightTarget = param[8] if len(param) > 8 else obj.iHighlightTarget
        self.dHighlightValue1 = param[9] if len(param) > 9 else obj.dHighlightValue1
        self.dHighlightValue2 = param[10] if len(param) > 10 else obj.dHighlightValue2
        self.iDisplayTarget = param[11] if len(param) > 11 else obj.iDisplayTarget
        self.bReverse = param[12] if len(param) > 12 else obj.bReverse
        # self.bAllModelVector  = param[] if len(param) > else obj.bAllModelVector
        self.iThresholdOpt = param[13] if len(param) > 13 else obj.iThresholdOpt
        self.dThresholdValue = param[14] if len(param) > 14 else obj.dThresholdValue
        self.dThresholdValueMax = (
            param[15] if len(param) > 15 else obj.dThresholdValueMax
        )
        self.iComparisonOpt = param[16] if len(param) > 16 else obj.iComparisonOpt
        self.iComparisonMinRangeOpt = (
            param[17] if len(param) > 17 else obj.iComparisonMinRangeOpt
        )
        self.iComparisonMaxRangeOpt = (
            param[18] if len(param) > 18 else obj.iComparisonMaxRangeOpt
        )
        return self

    def __str__(self):
        obj = PostDataVizOptCircle()
        paramArgs = []
        if self.iScaleMethod != obj.iScaleMethod:
            paramArgs.append("iScaleMethod={0}".format(getValueStr(self.iScaleMethod)))
        if self.dRatioModel != obj.dRatioModel:
            paramArgs.append("dRatioModel={0}".format(getValueStr(self.dRatioModel)))
        if self.dRatioScreen != obj.dRatioScreen:
            paramArgs.append("dRatioScreen={0}".format(getValueStr(self.dRatioScreen)))
        if self.dRatioValue != obj.dRatioValue:
            paramArgs.append("dRatioValue={0}".format(getValueStr(self.dRatioValue)))
        # if self.bUseArrow != obj.bUseArrow:
        #     paramArgs.append("bUseArrow ={0}".format(getBoolStr(self.bUseArrow)))
        if self.iColorHighlight != obj.iColorHighlight:
            paramArgs.append(
                "iColorHighlight={0}".format(getValueStr(self.iColorHighlight))
            )
        if self.iColorPositive != obj.iColorPositive:
            paramArgs.append(
                "iColorPositive={0}".format(getValueStr(self.iColorPositive))
            )
        if self.iColorNegative != obj.iColorNegative:
            paramArgs.append(
                "iColorNegative={0}".format(getValueStr(self.iColorNegative))
            )
        if self.bUseContour != obj.bUseContour:
            paramArgs.append("bUseContour={0}".format(getBoolStr(self.bUseContour)))
        if self.iHighlightTarget != obj.iHighlightTarget:
            paramArgs.append(
                "iHighlightTarget={0}".format(getValueStr(self.iHighlightTarget))
            )
        if self.dHighlightValue1 != obj.dHighlightValue1:
            paramArgs.append(
                "dHighligValue1={0}".format(getValueStr(self.dHighligValue1))
            )
        if self.dHighlightValue2 != obj.dHighlightValue2:
            paramArgs.append(
                "dHighligValue2={0}".format(getValueStr(self.dHighligValue2))
            )
        if self.iDisplayTarget != obj.iDisplayTarget:
            paramArgs.append(
                "iDisplayTarget={0}".format(getValueStr(self.iDisplayTarget))
            )
        if self.bReverse != obj.bReverse:
            paramArgs.append("bReverse={0}".format(getBoolStr(self.bReverse)))
        # if self.bAllModelVector != obj.bAllModelVector:
        #     paramArgs.append(
        #         "bAllModelVector ={0}".format(getValueStr(self.bAllModelVector))
        #     )
        if self.iThresholdOpt != obj.iThresholdOpt:
            paramArgs.append(
                "iThresholdOpt={0}".format(getValueStr(self.iThresholdOpt))
            )
        if self.dThresholdValue != obj.dThresholdValue:
            paramArgs.append(
                "dThresholdValue={0}".format(getValueStr(self.dThresholdValue))
            )
        if self.dThresholdValueMax != obj.dThresholdValueMax:
            paramArgs.append(
                "dThresholdValueMax={0}".format(getValueStr(self.dThresholdValueMax))
            )
        if self.iComparisonOpt != obj.iComparisonOpt:
            paramArgs.append(
                "iComparisonOpt={0}".format(getValueStr(self.iComparisonOpt))
            )
        if self.iComparisonMinRangeOpt != obj.iComparisonMinRangeOpt:
            paramArgs.append(
                "iComparisonMinRangeOpt={0}".format(
                    getValueStr(self.iComparisonMinRangeOpt)
                )
            )
        if self.iComparisonMaxRangeOpt != obj.iComparisonMaxRangeOpt:
            paramArgs.append(
                "iComparisonMaxRangeOpt={0}".format(
                    getValueStr(self.iComparisonMaxRangeOpt)
                )
            )

        return "PostDataVizOptCircle({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}".format(
                self.iScaleMethod,
                self.dRatioModel,
                self.dRatioScreen,
                self.dRatioValue,
                # 1 if self.bUseArrow else 0,
                self.iColorHighlight,
                self.iColorPositive,
                self.iColorNegative,
                1 if self.bUseContour else 0,
                self.iHighlightTarget,
                self.dHighlightValue1,
                self.dHighlightValue2,
                self.iDisplayTarget,
                1 if self.bReverse else 0,
                # 1 if self.bAllModelVector else 0,
                self.iThresholdOpt,
                self.dThresholdValue,
                self.dThresholdValueMax,
                self.iComparisonOpt,
                self.iComparisonMinRangeOpt,
                self.iComparisonMaxRangeOpt,
            )
            + rightBracket
        )

class PostDataVizOptContour:
    def __init__(
        self,
        iContour=10,
        iContourType=1,  # 0: POST_SLT_CONTINEOUS, 1: POST_SLT_STEP, 2: POST_SLT_ISOSURFACE, 3: POST_SLT_MANUAL, 4: POST_SLT_ISOVOLUME
        iMaxMinType=0,  # 0: POST_EMT_VISIBLE, 1: POST_EMT_TOTAL, 2: POST_EMT_USER, 3: POST_EMT_TOTAL_MULTI, 4: POST_EMT_VISIBLE_MULTI
        dMaxUser=1.0,
        dMinUser=0.0,
        dMaxTotal=1.0,
        dMinTotal=0.0,
        dIsoVolumeScalar=0.0,
        iSpectrumType=2,  # 0: POST_SCT_BRW, 1: POST_SCT_V_BRW, 2: POST_SCT_BGR, POST_SCT_STD_BGR, POST_SCT_AVE_BGR, POST_SCT_GRAY, POST_SCT_V_GRAY, POST_SCT_SAFETY, POST_SCT_AWE, POST_SCT_AWE2, POST_SCT_ADVC_AWE, POST_SCT_ADVC_AWE2, POST_SCT_BWR, POST_SCT_CUSTOM, POST_SCT_CIRCULAR, 								 POST_SCT_NMRI, POST_SCT_BGR_SYM, POST_SCT_BGR2_SYM, POST_SCT_STD_BGR_SYM, POST_SCT_STD_BGR2_SYM
        iUpperColor=255,  # RGB(255, 0, 0)
        iLowerColor=16711680,  # RGB(0, 0, 255)
        iFrameColor=65535,  # RGB(255, 255, 0)
        listCustomColors=[],
        listCustomValues=[
            100.0000000000,
            90.0000000000,
            80.0000000000,
            70.0000000000,
            60.0000000000,
            50.0000000000,
            40.0000000000,
            30.0000000000,
            20.0000000000,
            10.0000000000,
            0.0000000000,
        ],  # custom range values
        iLog=0,
        bShowBlankValueAs0=False,
        bOptimizedShape=False,
        bGururiContour=False,
        bAutoSetAmplitudeValue=True,
        iBlankColor=8421504, # RGB(128, 128, 128)
    ):
        self.iContour = iContour
        self.iContourType = iContourType
        self.iMaxMinType = iMaxMinType
        self.dMaxUser = dMaxUser
        self.dMinUser = dMinUser
        self.dMaxTotal = dMaxTotal
        self.dMinTotal = dMinTotal
        self.dIsoVolumeScalar = dIsoVolumeScalar
        self.iSpectrumType = iSpectrumType
        self.iUpperColor = iUpperColor
        self.iLowerColor = iLowerColor
        self.iFrameColor = iFrameColor
        self.listCustomColors = listCustomColors
        self.listCustomValues = listCustomValues
        self.iLog = iLog
        self.bShowBlankValueAs0 = bShowBlankValueAs0
        self.bOptimizedShape = bOptimizedShape
        self.bGururiContour = bGururiContour
        self.bAutoSetAmplitudeValue = bAutoSetAmplitudeValue
        self.iBlankColor = iBlankColor
        ...

    def isDefault(self):
        obj = PostDataVizOptContour()
        return (
            self.iContour == obj.iContour
            and self.iContourType == obj.iContourType
            and self.iMaxMinType == obj.iMaxMinType
            and self.dMaxUser == obj.dMaxUser
            and self.dMinUser == obj.dMinUser
            and self.dMaxTotal == obj.dMaxTotal
            and self.dMinTotal == obj.dMinTotal
            and self.dIsoVolumeScalar == obj.dIsoVolumeScalar
            and self.iSpectrumType == obj.iSpectrumType
            and self.iUpperColor == obj.iUpperColor
            and self.iLowerColor == obj.iLowerColor
            and self.iFrameColor == obj.iFrameColor
            and self.listCustomColors == obj.listCustomColors
            and self.listCustomValues == obj.listCustomValues
            and self.iLog == obj.iLog
            and self.bShowBlankValueAs0 == obj.bShowBlankValueAs0
            and self.bOptimizedShape == obj.bOptimizedShape
            and self.bGururiContour == obj.bGururiContour
            and self.bAutoSetAmplitudeValue == obj.bAutoSetAmplitudeValue
            and self.iBlankColor == obj.iBlankColor
        )

    def fromList(self, param):
        obj = PostDataVizOptContour()
        self.iContour = param[0] if len(param) > 0 else obj.iContour
        self.iContourType = param[1] if len(param) > 1 else obj.iContourType
        self.iMaxMinType = param[2] if len(param) > 2 else obj.iMaxMinType
        self.dMaxUser = param[3] if len(param) > 3 else obj.dMaxUser
        self.dMinUser = param[4] if len(param) > 4 else obj.dMinUser
        self.dMaxTotal = param[5] if len(param) > 5 else obj.dMaxTotal
        self.dMinTotal = param[6] if len(param) > 6 else obj.dMinTotal
        self.dIsoVolumeScalar = param[7] if len(param) > 7 else obj.dIsoVolumeScalar
        self.iSpectrumType = param[8] if len(param) > 8 else obj.iSpectrumType
        self.iUpperColor = param[9] if len(param) > 9 else obj.iUpperColor
        self.iLowerColor = param[10] if len(param) > 10 else obj.iLowerColor
        self.iFrameColor = param[11] if len(param) > 11 else obj.iFrameColor
        self.listCustomColors = param[12] if len(param) > 12 else obj.listCustomColors
        self.listCustomValues = param[13] if len(param) > 13 else obj.listCustomValues
        self.iLog = param[14] if len(param) > 14 else obj.iLog
        self.bShowBlankValueAs0 = (
            param[15] if len(param) > 15 else obj.bShowBlankValueAs0
        )
        self.bOptimizedShape = param[16] if len(param) > 16 else obj.bOptimizedShape
        self.bGururiContour = param[17] if len(param) > 17 else obj.bGururiContour
        self.bAutoSetAmplitudeValue = (
            param[18] if len(param) > 18 else obj.bAutoSetAmplitudeValue
        )
        self.iBlankColor = param[19] if len(param) > 19 else obj.iBlankColor
        return self

    def __str__(self):
        obj = PostDataVizOptContour()
        paramArgs = []
        if self.iContour != obj.iContour:
            paramArgs.append("iContour={0}".format(getValueStr(self.iContour)))
        if self.iContourType != obj.iContourType:
            paramArgs.append("iContourType={0}".format(getValueStr(self.iContourType)))
        if self.iMaxMinType != obj.iMaxMinType:
            paramArgs.append("iMaxMinType={0}".format(getValueStr(self.iMaxMinType)))
        if self.dMaxUser != obj.dMaxUser:
            paramArgs.append("dMaxUser={0}".format(getValueStr(self.dMaxUser)))
        if self.dMinUser != obj.dMinUser:
            paramArgs.append("dMinUser={0}".format(getValueStr(self.dMinUser)))
        if self.dMaxTotal != obj.dMaxTotal:
            paramArgs.append("dMaxTotal={0}".format(getValueStr(self.dMaxTotal)))
        if self.dMinTotal != obj.dMinTotal:
            paramArgs.append("dMinTotal={0}".format(getValueStr(self.dMinTotal)))
        if self.dIsoVolumeScalar != obj.dIsoVolumeScalar:
            paramArgs.append(
                "dIsoVolumeScalar={0}".format(getValueStr(self.dIsoVolumeScalar))
            )
        if self.iSpectrumType != obj.iSpectrumType:
            paramArgs.append(
                "iSpectrumType={0}".format(getValueStr(self.iSpectrumType))
            )
        if self.iUpperColor != obj.iUpperColor:
            paramArgs.append("iUpperColor={0}".format(getValueStr(self.iUpperColor)))
        if self.iLowerColor != obj.iLowerColor:
            paramArgs.append("iLowerColor={0}".format(getValueStr(self.iLowerColor)))
        if self.iFrameColor != obj.iFrameColor:
            paramArgs.append("iFrameColor={0}".format(getValueStr(self.iFrameColor)))
        if self.listCustomColors != obj.listCustomColors:
            paramArgs.append(
                "listCustomColors={0}".format(getValueStr(self.listCustomColors))
            )
        if self.listCustomValues != obj.listCustomValues:
            paramArgs.append(
                "listCustomValues={0}".format(getValueStr(self.listCustomValues))
            )
        if self.iLog != obj.iLog:
            paramArgs.append("iLog={0}".format(getValueStr(self.iLog)))
        if self.bShowBlankValueAs0 != obj.bShowBlankValueAs0:
            paramArgs.append(
                "bShowBlankValueAs0={0}".format(getBoolStr(self.bShowBlankValueAs0))
            )
        if self.bOptimizedShape != obj.bOptimizedShape:
            paramArgs.append(
                "bOptimizedShape={0}".format(getBoolStr(self.bOptimizedShape))
            )
        if self.bGururiContour != obj.bGururiContour:
            paramArgs.append(
                "bGururiContour={0}".format(getBoolStr(self.bGururiContour))
            )
        if self.bAutoSetAmplitudeValue != obj.bAutoSetAmplitudeValue:
            paramArgs.append(
                "bAutoSetAmplitudeValue={0}".format(
                    getBoolStr(self.bAutoSetAmplitudeValue)
                )
            )
        if self.iBlankColor != obj.iBlankColor:
            paramArgs.append("iBlankColor={0}".format(getValueStr(self.iBlankColor)))

        return "PostDataVizOptContour({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}".format(
                self.iContour,
                self.iContourType,
                self.iMaxMinType,
                self.dMaxUser,
                self.dMinUser,
                self.dMaxTotal,
                self.dMinTotal,
                self.dIsoVolumeScalar,
                self.iSpectrumType,
                self.iUpperColor,
                self.iLowerColor,
                self.iFrameColor,
                self.listCustomColors,
                self.listCustomValues,
                self.iLog,
                1 if self.bShowBlankValueAs0 else 0,
                1 if self.bOptimizedShape else 0,
                1 if self.bGururiContour else 0,
                1 if self.bAutoSetAmplitudeValue else 0,
                self.iBlankColor,
            )
            + rightBracket
        )

class PostDataVizOptDeform:
    def __init__(
        self,
        listDispRatioEach=[0.07, 0.07, 0.07],
        dDispRatio=0.07,
        iScaleMethod=0,
        bEachDispComp=False,
        bShowOriginalShade=False,
        bShowOriginalMesh=True,
        bShowOriginalEdge=True,
        iOriginalShade=13158600,  # RGB(200, 200, 200)
        iOriginalMesh=11184810,  # RGB(170, 170, 170)
        iOriginalEdge=11184810,  # RGB(170, 170, 170)
        dOriginalShadeTrans=0.8,
    ):
        self.listDispRatioEach = listDispRatioEach
        self.dDispRatio = dDispRatio
        self.iScaleMethod = iScaleMethod
        self.bEachDispComp = bEachDispComp
        self.bShowOriginalShade = bShowOriginalShade
        self.bShowOriginalMesh = bShowOriginalMesh
        self.bShowOriginalEdge = bShowOriginalEdge
        self.iOriginalShade = iOriginalShade
        self.iOriginalMesh = iOriginalMesh
        self.iOriginalEdge = iOriginalEdge
        self.dOriginalShadeTrans = dOriginalShadeTrans
        ...

    def isDefault(self):
        obj = PostDataVizOptDeform()
        return (
            self.listDispRatioEach == obj.listDispRatioEach
            and self.dDispRatio == obj.dDispRatio
            and self.iScaleMethod == obj.iScaleMethod
            and self.bEachDispComp == obj.bEachDispComp
            and self.bShowOriginalShade == obj.bShowOriginalShade
            and self.bShowOriginalMesh == obj.bShowOriginalMesh
            and self.bShowOriginalEdge == obj.bShowOriginalEdge
            and self.iOriginalShade == obj.iOriginalShade
            and self.iOriginalMesh == obj.iOriginalMesh
            and self.iOriginalEdge == obj.iOriginalEdge
            and self.dOriginalShadeTrans == obj.dOriginalShadeTrans
        )

    def fromList(self, param):
        obj = PostDataVizOptDeform()
        self.listDispRatioEach = param[0] if len(param) > 0 else obj.listDispRatioEach
        self.dDispRatio = param[1] if len(param) > 1 else obj.dDispRatio
        self.iScaleMethod = param[2] if len(param) > 2 else obj.iScaleMethod
        self.bEachDispComp = param[3] if len(param) > 3 else obj.bEachDispComp
        self.bShowOriginalShade = param[4] if len(param) > 4 else obj.bShowOriginalShade
        self.bShowOriginalMesh = param[5] if len(param) > 5 else obj.bShowOriginalMesh
        self.bShowOriginalEdge = param[6] if len(param) > 6 else obj.bShowOriginalEdge
        self.iOriginalShade = param[7] if len(param) > 7 else obj.iOriginalShade
        self.iOriginalMesh = param[8] if len(param) > 8 else obj.iOriginalMesh
        self.iOriginalEdge = param[9] if len(param) > 9 else obj.iOriginalEdge
        self.dOriginalShadeTrans = (
            param[10] if len(param) > 10 else obj.dOriginalShadeTrans
        )
        return self

    def __str__(self):
        obj = PostDataVizOptDeform()
        paramArgs = []
        if self.listDispRatioEach != obj.listDispRatioEach:
            paramArgs.append(
                "listDispRatioEach={0}".format(getValueStr(self.listDispRatioEach))
            )
        if self.dDispRatio != obj.dDispRatio:
            paramArgs.append("dDispRatio={0}".format(getValueStr(self.dDispRatio)))
        if self.iScaleMethod != obj.iScaleMethod:
            paramArgs.append("iScaleMethod={0}".format(getValueStr(self.iScaleMethod)))
        if self.bEachDispComp != obj.bEachDispComp:
            paramArgs.append("bEachDispComp={0}".format(getBoolStr(self.bEachDispComp)))
        if self.bShowOriginalShade != obj.bShowOriginalShade:
            paramArgs.append(
                "bShowOriginalShade={0}".format(getBoolStr(self.bShowOriginalShade))
            )
        if self.bShowOriginalMesh != obj.bShowOriginalMesh:
            paramArgs.append(
                "bShowOriginalMesh={0}".format(getBoolStr(self.bShowOriginalMesh))
            )
        if self.bShowOriginalEdge != obj.bShowOriginalEdge:
            paramArgs.append(
                "bShowOriginalEdge={0}".format(getBoolStr(self.bShowOriginalEdge))
            )
        if self.iOriginalShade != obj.iOriginalShade:
            paramArgs.append(
                "iOriginalShade={0}".format(getValueStr(self.iOriginalShade))
            )
        if self.iOriginalMesh != obj.iOriginalMesh:
            paramArgs.append(
                "iOriginalMesh={0}".format(getValueStr(self.iOriginalMesh))
            )
        if self.iOriginalEdge != obj.iOriginalEdge:
            paramArgs.append(
                "iOriginalEdge={0}".format(getValueStr(self.iOriginalEdge))
            )
        if self.dOriginalShadeTrans != obj.dOriginalShadeTrans:
            paramArgs.append(
                "dOriginalShadeTrans={0}".format(getValueStr(self.dOriginalShadeTrans))
            )
        return "PostDataVizOptDeform({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}".format(
                self.listDispRatioEach,
                self.dDispRatio,
                self.iScaleMethod,
                self.bEachDispComp,
                1 if self.bShowOriginalShade else 0,
                1 if self.bShowOriginalMesh else 0,
                1 if self.bShowOriginalEdge else 0,
                self.iOriginalShade,
                self.iOriginalMesh,
                self.iOriginalEdge,
                self.dOriginalShadeTrans,
            )
            + rightBracket
        )

class PostDataVizOptDiagram:
    def __init__(
        self,
        iScaleMethod=0,
        dRatioModel=0.03,
        dRatioScreen=0.03,
        iColorHighlight=255,  #  RGB(255, 0, 0)
        iColorPositive=16777215,  # RGB(255, 255, 255)
        iColorNegative=51400,  # RGB(200, 200, 0)
        bUseContour=False,
        bTwoSides=True,
        iHighlightTarget=0,
        dHighlightValue1=0.0,
        dHighlightValue2=1.0,
        iDisplayTarget=0,
        iThresholdOpt=0,
        dThresholdValue=0.0,
        dThresholdValueMax=100.0,
        iComparisonOpt=0,  # 0: < Greater , 1: <= Greater and Equal, 2: > Less, 3: >= Less and Equal
        iComparisonMinRangeOpt=0,
        iComparisonMaxRangeOpt=0,
    ):
        self.iScaleMethod = iScaleMethod
        self.dRatioModel = dRatioModel
        self.dRatioScreen = dRatioScreen
        self.iColorHighlight = iColorHighlight
        self.iColorPositive = iColorPositive
        self.iColorNegative = iColorNegative
        self.bUseContour = bUseContour
        self.bTwoSides = bTwoSides
        self.iHighlightTarget = iHighlightTarget
        self.dHighlightValue1 = dHighlightValue1
        self.dHighlightValue2 = dHighlightValue2
        self.iDisplayTarget = iDisplayTarget
        self.iThresholdOpt = iThresholdOpt
        self.dThresholdValue = dThresholdValue
        self.dThresholdValueMax = dThresholdValueMax
        self.iComparisonOpt = iComparisonOpt
        self.iComparisonMinRangeOpt = iComparisonMinRangeOpt
        self.iComparisonMaxRangeOpt = iComparisonMaxRangeOpt
        ...

    def isDefault(self):
        obj = PostDataVizOptDiagram()
        return (
            self.iScaleMethod == obj.iScaleMethod
            and self.dRatioModel == obj.dRatioModel
            and self.dRatioScreen == obj.dRatioScreen
            and self.iColorHighlight == obj.iColorHighlight
            and self.iColorPositive == obj.iColorPositive
            and self.iColorNegative == obj.iColorNegative
            and self.bUseContour == obj.bUseContour
            and self.bTwoSides == obj.bTwoSides
            and self.iHighlightTarget == obj.iHighlightTarget
            and self.dHighlightValue1 == obj.dHighlightValue1
            and self.dHighlightValue2 == obj.dHighlightValue2
            and self.iDisplayTarget == obj.iDisplayTarget
            and self.iThresholdOpt == obj.iThresholdOpt
            and self.dThresholdValue == obj.dThresholdValue
            and self.dThresholdValueMax == obj.dThresholdValueMax
            and self.iComparisonOpt == obj.iComparisonOpt
            and self.iComparisonMinRangeOpt == obj.iComparisonMinRangeOpt
            and self.iComparisonMaxRangeOpt == obj.iComparisonMaxRangeOpt
        )

    def fromList(self, param):
        obj = PostDataVizOptDiagram()
        self.iScaleMethod = param[0] if len(param) > 0 else obj.iScaleMethod
        self.dRatioModel = param[1] if len(param) > 1 else obj.dRatioModel
        self.dRatioScreen = param[2] if len(param) > 2 else obj.dRatioScreen
        self.iColorHighlight = param[3] if len(param) > 3 else obj.iColorHighlight
        self.iColorPositive = param[4] if len(param) > 4 else obj.iColorPositive
        self.iColorNegative = param[5] if len(param) > 5 else obj.iColorNegative
        self.bUseContour = param[6] if len(param) > 6 else obj.bUseContour
        self.bTwoSides = param[7] if len(param) > 7 else obj.bTwoSides
        self.iHighlightTarget = param[8] if len(param) > 8 else obj.iHighlightTarget
        self.dHighlightValue1 = param[9] if len(param) > 9 else obj.dHighlightValue1
        self.dHighlightValue2 = param[10] if len(param) > 10 else obj.dHighlightValue2
        self.iDisplayTarget = param[11] if len(param) > 11 else obj.iDisplayTarget
        self.iThresholdOpt = param[12] if len(param) > 12 else obj.iThresholdOpt
        self.dThresholdValue = param[13] if len(param) > 13 else obj.dThresholdValue
        self.dThresholdValueMax = (
            param[14] if len(param) > 14 else obj.dThresholdValueMax
        )
        self.iComparisonOpt = param[15] if len(param) > 15 else obj.iComparisonOpt
        self.iComparisonMinRangeOpt = (
            param[16] if len(param) > 16 else obj.iComparisonMinRangeOpt
        )
        self.iComparisonMaxRangeOpt = (
            param[17] if len(param) > 17 else obj.iComparisonMaxRangeOpt
        )
        return self

    def __str__(self):
        obj = PostDataVizOptDiagram()
        paramArgs = []
        if self.iScaleMethod != obj.iScaleMethod:
            paramArgs.append("iScaleMethod={0}".format(getValueStr(self.iScaleMethod)))
        if self.dRatioModel != obj.dRatioModel:
            paramArgs.append("dRatioModel={0}".format(getValueStr(self.dRatioModel)))
        if self.dRatioScreen != obj.dRatioScreen:
            paramArgs.append("dRatioScreen={0}".format(getValueStr(self.dRatioScreen)))
        if self.iColorHighlight != obj.iColorHighlight:
            paramArgs.append(
                "iColorHighlight={0}".format(getValueStr(self.iColorHighlight))
            )
        if self.iColorPositive != obj.iColorPositive:
            paramArgs.append(
                "iColorPositive={0}".format(getValueStr(self.iColorPositive))
            )
        if self.iColorNegative != obj.iColorNegative:
            paramArgs.append(
                "iColorNegative={0}".format(getValueStr(self.iColorNegative))
            )
        if self.bUseContour != obj.bUseContour:
            paramArgs.append("bUseContour={0}".format(getBoolStr(self.bUseContour)))
        if self.bTwoSides != obj.bTwoSides:
            paramArgs.append("bTwoSides={0}".format(getBoolStr(self.bTwoSides)))
        if self.iHighlightTarget != obj.iHighlightTarget:
            paramArgs.append(
                "iHighlightTarget={0}".format(getValueStr(self.iHighlightTarget))
            )
        if self.dHighlightValue1 != obj.dHighlightValue1:
            paramArgs.append(
                "dHighlightValue1={0}".format(getValueStr(self.dHighlightValue1))
            )
        if self.dHighlightValue2 != obj.dHighlightValue2:
            paramArgs.append(
                "dHighlightValue2={0}".format(getValueStr(self.dHighlightValue2))
            )
        if self.iDisplayTarget != obj.iDisplayTarget:
            paramArgs.append(
                "iDisplayTarget={0}".format(getValueStr(self.iDisplayTarget))
            )
        if self.iThresholdOpt != obj.iThresholdOpt:
            paramArgs.append(
                "iThresholdOpt={0}".format(getValueStr(self.iThresholdOpt))
            )
        if self.dThresholdValue != obj.dThresholdValue:
            paramArgs.append(
                "dThresholdValue={0}".format(getValueStr(self.dThresholdValue))
            )
        if self.dThresholdValueMax != obj.dThresholdValueMax:
            paramArgs.append(
                "dThresholdValueMax={0}".format(getValueStr(self.dThresholdValueMax))
            )
        if self.iComparisonOpt != obj.iComparisonOpt:
            paramArgs.append(
                "iComparisonOpt={0}".format(getValueStr(self.iComparisonOpt))
            )
        if self.iComparisonMinRangeOpt != obj.iComparisonMinRangeOpt:
            paramArgs.append(
                "iComparisonMinRangeOpt={0}".format(
                    getValueStr(self.iComparisonMinRangeOpt)
                )
            )
        if self.iComparisonMaxRangeOpt != obj.iComparisonMaxRangeOpt:
            paramArgs.append(
                "iComparisonMaxRangeOpt={0}".format(
                    getValueStr(self.iComparisonMaxRangeOpt)
                )
            )
        return "PostDataVizOptDiagram({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}".format(
                self.iScaleMethod,
                self.dRatioModel,
                self.dRatioScreen,
                self.iColorHighlight,
                self.iColorPositive,
                self.iColorNegative,
                self.bUseContour,
                self.bTwoSides,
                self.iHighlightTarget,
                self.dHighlightValue1,
                self.dHighlightValue2,
                self.iDisplayTarget,
                self.iThresholdOpt,
                self.dThresholdValue,
                self.dThresholdValueMax,
                self.iComparisonOpt,
                self.iComparisonMinRangeOpt,
                self.iComparisonMaxRangeOpt,
            )
            + rightBracket
        )

class PostDataVizOptMaxMin:
    def __init__(
        self,
        iGroupMethod=0,  # 0-All, 1-Each
        iColorMax=255,  # RGB(255, 0, 0),
        iColorMin=16711680,  # RGB(0, 0, 255),
        iColorText=65535,  # RGB(255, 255, 0),
    ):
        self.iGroupMethod = iGroupMethod
        self.iColorMax = iColorMax
        self.iColorMin = iColorMin
        self.iColorText = iColorText
        ...

    def isDefault(self):
        obj = PostDataVizOptMaxMin()
        return (
            self.iGroupMethod == obj.iGroupMethod
            and self.iColorMax == obj.iColorMax
            and self.iColorMin == obj.iColorMin
            and self.iColorText == obj.iColorText
        )

    def fromList(self, param):
        obj = PostDataVizOptMaxMin()
        self.iGroupMethod = param[0] if len(param) > 0 else obj.iGroupMethod
        self.iColorMax = param[1] if len(param) > 1 else obj.iColorMax
        self.iColorMin = param[2] if len(param) > 2 else obj.iColorMin
        self.iColorText = param[3] if len(param) > 3 else obj.iColorText
        return self

    def __str__(self):
        obj = PostDataVizOptMaxMin()
        paramArgs = []
        if self.iGroupMethod != obj.iGroupMethod:
            paramArgs.append("iGroupMethod={0}".format(getValueStr(self.iGroupMethod)))
        if self.iColorMax != obj.iColorMax:
            paramArgs.append("iColorMax={0}".format(getValueStr(self.iColorMax)))
        if self.iColorMin != obj.iColorMin:
            paramArgs.append("iColorMin={0}".format(getValueStr(self.iColorMin)))
        if self.iColorText != obj.iColorText:
            paramArgs.append("iColorText={0}".format(getValueStr(self.iColorText)))
        return "PostDataVizOptMaxMin({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}".format(
                self.iGroupMethod, self.iColorMax, self.iColorMin, self.iColorText
            )
            + rightBracket
        )

class PostDataVizOptTransparency:
    def __init__(self, dPercentage=0.0):
        self.dPercentage = dPercentage
        ...

    def isDefault(self):
        obj = PostDataVizOptTransparency()
        return self.dPercentage == obj.dPercentage

    def fromList(self, param):
        obj = PostDataVizOptTransparency()
        self.dPercentage = param[0] if len(param) > 0 else obj.dPercentage
        return self

    def __str__(self):
        obj = PostDataVizOptTransparency()
        paramArgs = []
        if self.dPercentage != obj.dPercentage:
            paramArgs.append("dPercentage={0}".format(getValueStr(self.dPercentage)))
        return "PostDataVizOptTransparency({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return leftBracket + "{0}".format(self.dPercentage) + rightBracket

class PostDataVizOptTitle:
    def __init__(
        self,
        bResultName=True,
        bConvection=True,
        bUnit=True,
        bCoordinate=True,
        bTotalMaxMin=True,
        bFileName=True,
        bLocation=True,
        bVisibleMaxMin=True,
        bAnimation=True,
        bDeformRatio=True,
        bDetail=True,
        iSizeTitleTarget=6,
        iSizeDesTarget=5,
        iResultTitle=6,
        iColorResultTitle=16777215,  # RGB(255, 255, 255),
        bResultTitle=True,
        iResultDescription=5,
        iColorResultDescription=16777215,  # RGB(255, 255, 255),
        bResultDescription=False,
        bUseBackground=False,
        iColorFillBackground=16777215,  # RGB(255, 255, 255),
        iColorBorderBackground=16777215,  # RGB(255, 255, 255),
        dPercentage=0.5,
        bAdjustTitlePos=True,
    ):
        self.bResultName = bResultName
        self.bConvection = bConvection
        self.bUnit = bUnit
        self.bCoordinate = bCoordinate
        self.bTotalMaxMin = bTotalMaxMin
        self.bFileName = bFileName
        self.bLocation = bLocation
        self.bVisibleMaxMin = bVisibleMaxMin
        self.bAnimation = bAnimation
        self.bDeformRatio = bDeformRatio
        self.bDetail = bDetail
        self.iSizeTitleTarget = iSizeTitleTarget
        self.iSizeDesTarget = iSizeDesTarget
        self.iResultTitle = iResultTitle
        self.iColorResultTitle = iColorResultTitle
        self.bResultTitle = bResultTitle
        self.iResultDescription = iResultDescription
        self.iColorResultDescription = iColorResultDescription
        self.bResultDescription = bResultDescription
        self.bUseBackground = bUseBackground
        self.iColorFillBackground = iColorFillBackground
        self.iColorBorderBackground = iColorBorderBackground
        self.dPercentage = dPercentage
        self.bAdjustTitlePos = bAdjustTitlePos
        ...

    def isDefault(self):
        obj = PostDataVizOptTitle()
        return (
            self.bResultName == obj.bResultName
            and self.bConvection == obj.bConvection
            and self.bUnit == obj.bUnit
            and self.bCoordinate == obj.bCoordinate
            and self.bTotalMaxMin == obj.bTotalMaxMin
            and self.bFileName == obj.bFileName
            and self.bLocation == obj.bLocation
            and self.bVisibleMaxMin == obj.bVisibleMaxMin
            and self.bAnimation == obj.bAnimation
            and self.bDeformRatio == obj.bDeformRatio
            and self.bDetail == obj.bDetail
            and self.iSizeTitleTarget == obj.iSizeTitleTarget
            and self.iSizeDesTarget == obj.iSizeDesTarget
            and self.iResultTitle == obj.iResultTitle
            and self.iColorResultTitle == obj.iColorResultTitle
            and self.bResultTitle == obj.bResultTitle
            and self.iResultDescription == obj.iResultDescription
            and self.iColorResultDescription == obj.iColorResultDescription
            and self.bResultDescription == obj.bResultDescription
            and self.bUseBackground == obj.bUseBackground
            and self.iColorFillBackground == obj.iColorFillBackground
            and self.iColorBorderBackground == obj.iColorBorderBackground
            and self.dPercentage == obj.dPercentage
            and self.bAdjustTitlePos == obj.bAdjustTitlePos
        )

    def fromList(self, param):
        obj = PostDataVizOptTitle()
        self.bResultName = param[0] if len(param) > 0 else obj.bResultName
        self.bConvection = param[1] if len(param) > 1 else obj.bConvection
        self.bUnit = param[2] if len(param) > 2 else obj.bUnit
        self.bCoordinate = param[3] if len(param) > 3 else obj.bCoordinate
        self.bTotalMaxMin = param[4] if len(param) > 4 else obj.bTotalMaxMin
        self.bFileName = param[5] if len(param) > 5 else obj.bFileName
        self.bLocation = param[6] if len(param) > 6 else obj.bLocation
        self.bVisibleMaxMin = param[7] if len(param) > 7 else obj.bVisibleMaxMin
        self.bAnimation = param[8] if len(param) > 8 else obj.bAnimation
        self.bDeformRatio = param[9] if len(param) > 9 else obj.bDeformRatio
        self.bDetail = param[10] if len(param) > 10 else obj.bDetail
        self.iSizeTitleTarget = param[11] if len(param) > 11 else obj.iSizeTitleTarget
        self.iSizeDesTarget = param[12] if len(param) > 12 else obj.iSizeDesTarget
        self.iResultTitle = param[13] if len(param) > 13 else obj.iResultTitle
        self.iColorResultTitle = param[14] if len(param) > 14 else obj.iColorResultTitle
        self.bResultTitle = param[15] if len(param) > 15 else obj.bResultTitle
        self.iResultDescription = (
            param[16] if len(param) > 16 else obj.iResultDescription
        )
        self.iColorResultDescription = (
            param[17] if len(param) > 17 else obj.iColorResultDescription
        )
        self.bResultDescription = (
            param[18] if len(param) > 18 else obj.bResultDescription
        )
        self.bUseBackground = param[19] if len(param) > 19 else obj.bUseBackground
        self.iColorFillBackground = (
            param[20] if len(param) > 20 else obj.iColorFillBackground
        )
        self.iColorBorderBackground = (
            param[21] if len(param) > 21 else obj.iColorBorderBackground
        )
        self.dPercentage = param[22] if len(param) > 22 else obj.dPercentage
        self.bAdjustTitlePos = param[23] if len(param) > 23 else obj.bAdjustTitlePos
        return self

    def __str__(self):
        obj = PostDataVizOptTitle()
        paramArgs = []
        if self.bResultName != obj.bResultName:
            paramArgs.append("bResultName={0}".format(getBoolStr(self.bResultName)))
        if self.bConvection != obj.bConvection:
            paramArgs.append("bConvection={0}".format(getBoolStr(self.bConvection)))
        if self.bUnit != obj.bUnit:
            paramArgs.append("bUnit={0}".format(getBoolStr(self.bUnit)))
        if self.bCoordinate != obj.bCoordinate:
            paramArgs.append("bCoordinate={0}".format(getBoolStr(self.bCoordinate)))
        if self.bTotalMaxMin != obj.bTotalMaxMin:
            paramArgs.append("bTotalMaxMin={0}".format(getBoolStr(self.bTotalMaxMin)))
        if self.bFileName != obj.bFileName:
            paramArgs.append("bFileName={0}".format(getBoolStr(self.bFileName)))
        if self.bLocation != obj.bLocation:
            paramArgs.append("bLocation={0}".format(getBoolStr(self.bLocation)))
        if self.bVisibleMaxMin != obj.bVisibleMaxMin:
            paramArgs.append(
                "bVisibleMaxMin={0}".format(getBoolStr(self.bVisibleMaxMin))
            )
        if self.bAnimation != obj.bAnimation:
            paramArgs.append("bAnimation={0}".format(getBoolStr(self.bAnimation)))
        if self.bDeformRatio != obj.bDeformRatio:
            paramArgs.append("bDeformRatio={0}".format(getBoolStr(self.bDeformRatio)))
        if self.bDetail != obj.bDetail:
            paramArgs.append("bDetail={0}".format(getBoolStr(self.bDetail)))
        if self.iSizeTitleTarget != obj.iSizeTitleTarget:
            paramArgs.append(
                "iSizeTitleTarget={0}".format(getValueStr(self.iSizeTitleTarget))
            )
        if self.iSizeDesTarget != obj.iSizeDesTarget:
            paramArgs.append(
                "iSizeDesTarget={0}".format(getValueStr(self.iSizeDesTarget))
            )
        if self.iResultTitle != obj.iResultTitle:
            paramArgs.append("iResultTitle={0}".format(getValueStr(self.iResultTitle)))
        if self.iColorResultTitle != obj.iColorResultTitle:
            paramArgs.append(
                "iColorResultTitle={0}".format(getValueStr(self.iColorResultTitle))
            )
        if self.bResultTitle != obj.bResultTitle:
            paramArgs.append("bResultTitle={0}".format(getBoolStr(self.bResultTitle)))
        if self.iResultDescription != obj.iResultDescription:
            paramArgs.append(
                "iResultDescription={0}".format(getValueStr(self.iResultDescription))
            )
        if self.iColorResultDescription != obj.iColorResultDescription:
            paramArgs.append(
                "iColorResultDescription={0}".format(
                    getValueStr(self.iColorResultDescription)
                )
            )
        if self.bResultDescription != obj.bResultDescription:
            paramArgs.append(
                "bResultDescription={0}".format(getBoolStr(self.bResultDescription))
            )
        if self.bUseBackground != obj.bUseBackground:
            paramArgs.append(
                "bUseBackground={0}".format(getBoolStr(self.bUseBackground))
            )
        if self.iColorFillBackground != obj.iColorFillBackground:
            paramArgs.append(
                "iColorFillBackground={0}".format(
                    getValueStr(self.iColorFillBackground)
                )
            )
        if self.iColorBorderBackground != obj.iColorBorderBackground:
            paramArgs.append(
                "iColorBorderBackground={0}".format(
                    getValueStr(self.iColorBorderBackground)
                )
            )
        if self.dPercentage != obj.dPercentage:
            paramArgs.append("dPercentage={0}".format(getValueStr(self.dPercentage)))
        if self.bAdjustTitlePos != obj.bAdjustTitlePos:
            paramArgs.append(
                "bAdjustTitlePos={0}".format(getBoolStr(self.bAdjustTitlePos))
            )
        return "PostDataVizOptTitle({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}".format(
                1 if self.bResultName else 0,
                1 if self.bConvection else 0,
                1 if self.bUnit else 0,
                1 if self.bCoordinate else 0,
                1 if self.bTotalMaxMin else 0,
                1 if self.bFileName else 0,
                1 if self.bLocation else 0,
                1 if self.bVisibleMaxMin else 0,
                1 if self.bAnimation else 0,
                1 if self.bDeformRatio else 0,
                1 if self.bDetail else 0,
                self.iSizeTitleTarget,
                self.iSizeDesTarget,
                self.iResultTitle,
                self.iColorResultTitle,
                1 if self.bResultTitle else 0,
                self.iResultDescription,
                self.iColorResultDescription,
                1 if self.bResultDescription else 0,
                1 if self.bUseBackground else 0,
                self.iColorFillBackground,
                self.iColorBorderBackground,
                self.dPercentage,
                1 if self.bAdjustTitlePos else 0,
            )
            + rightBracket
        )

class PostDataVizOptVector:
    def __init__(
        self,
        iScaleMethod=0,
        dRatioModel=0.03,
        dRatioScreen=0.03,
        dRatioValue=1.0,
        bUseArrow=True,
        iColorHighlight=255,  # RGB(255, 0, 0)
        iColorPositive=16777215,  # RGB(255, 255, 255)
        iColorNegative=51400,  # RGB(200, 200, 0)
        bUseContour=False,
        iHighlightTarget=0,
        dHighlightValue1=0.0,
        dHighlightValue2=1.0,
        iDisplayTarget=0,
        bReverse=False,
        bAllModelVector=False,
        iThresholdOpt=0,
        dThresholdValue=0.0,
        dThresholdValueMax=100,
        iComparisonOpt=0,
        iComparisonMinRangeOpt=0,
        iComparisonMaxRangeOpt=0,
        bAllSameLength=False,
    ):
        self.iScaleMethod = iScaleMethod
        self.dRatioModel = dRatioModel
        self.dRatioScreen = dRatioScreen
        self.dRatioValue = dRatioValue
        self.bUseArrow = bUseArrow
        self.iColorHighlight = iColorHighlight
        self.iColorPositive = iColorPositive
        self.iColorNegative = iColorNegative
        self.bUseContour = bUseContour
        self.iHighlightTarget = iHighlightTarget
        self.dHighlightValue1 = dHighlightValue1
        self.dHighlightValue2 = dHighlightValue2
        self.iDisplayTarget = iDisplayTarget
        self.bReverse = bReverse
        self.bAllModelVector = bAllModelVector
        self.iThresholdOpt = iThresholdOpt
        self.dThresholdValue = dThresholdValue
        self.dThresholdValueMax = dThresholdValueMax
        self.iComparisonOpt = iComparisonOpt
        self.iComparisonMinRangeOpt = iComparisonMinRangeOpt
        self.iComparisonMaxRangeOpt = iComparisonMaxRangeOpt
        self.bAllSameLength = bAllSameLength
        ...

    def isDefault(self):
        obj = PostDataVizOptVector()
        return (
            self.iScaleMethod == obj.iScaleMethod
            and self.dRatioModel == obj.dRatioModel
            and self.dRatioScreen == obj.dRatioScreen
            and self.dRatioValue == obj.dRatioValue
            and self.bUseArrow == obj.bUseArrow
            and self.iColorHighlight == obj.iColorHighlight
            and self.iColorPositive == obj.iColorPositive
            and self.iColorNegative == obj.iColorNegative
            and self.bUseContour == obj.bUseContour
            and self.iHighlightTarget == obj.iHighlightTarget
            and self.dHighlightValue1 == obj.dHighlightValue1
            and self.dHighlightValue2 == obj.dHighlightValue2
            and self.iDisplayTarget == obj.iDisplayTarget
            and self.bReverse == obj.bReverse
            and self.bAllModelVector == obj.bAllModelVector
            and self.iThresholdOpt == obj.iThresholdOpt
            and self.dThresholdValue == obj.dThresholdValue
            and self.dThresholdValueMax == obj.dThresholdValueMax
            and self.iComparisonOpt == obj.iComparisonOpt
            and self.iComparisonMinRangeOpt == obj.iComparisonMinRangeOpt
            and self.iComparisonMaxRangeOpt == obj.iComparisonMaxRangeOpt
            and self.bAllSameLength == obj.bAllSameLength
        )

    def fromList(self, param):
        obj = PostDataVizOptVector()
        self.iScaleMethod = param[0] if len(param) > 0 else obj.iScaleMethod
        self.dRatioModel = param[1] if len(param) > 1 else obj.dRatioModel
        self.dRatioScreen = param[2] if len(param) > 2 else obj.dRatioScreen
        self.dRatioValue = param[3] if len(param) > 3 else obj.dRatioValue
        self.bUseArrow = param[4] if len(param) > 4 else obj.bUseArrow
        self.iColorHighlight = param[5] if len(param) > 5 else obj.iColorHighlight
        self.iColorPositive = param[6] if len(param) > 6 else obj.iColorPositive
        self.iColorNegative = param[7] if len(param) > 7 else obj.iColorNegative
        self.bUseContour = param[8] if len(param) > 8 else obj.bUseContour
        self.iHighlightTarget = param[9] if len(param) > 9 else obj.iHighlightTarget
        self.dHighlightValue1 = param[10] if len(param) > 10 else obj.dHighlightValue1
        self.dHighlightValue2 = param[11] if len(param) > 11 else obj.dHighlightValue2
        self.iDisplayTarget = param[12] if len(param) > 12 else obj.iDisplayTarget
        self.bReverse = param[13] if len(param) > 13 else obj.bReverse
        self.bAllModelVector = param[14] if len(param) > 14 else obj.bAllModelVector
        self.iThresholdOpt = param[15] if len(param) > 15 else obj.iThresholdOpt
        self.dThresholdValue = param[16] if len(param) > 16 else obj.dThresholdValue
        self.dThresholdValueMax = (
            param[17] if len(param) > 17 else obj.dThresholdValueMax
        )
        self.iComparisonOpt = param[18] if len(param) > 18 else obj.iComparisonOpt
        self.iComparisonMinRangeOpt = (
            param[19] if len(param) > 19 else obj.iComparisonMinRangeOpt
        )
        self.iComparisonMaxRangeOpt = (
            param[20] if len(param) > 20 else obj.iComparisonMaxRangeOpt
        )
        self.bAllSameLength = param[21] if len(param) > 21 else obj.bAllSameLength
        return self

    def __str__(self):
        obj = PostDataVizOptVector()
        paramArgs = []
        if self.iScaleMethod != obj.iScaleMethod:
            paramArgs.append("iScaleMethod={0}".format(getValueStr(self.iScaleMethod)))
        if self.dRatioModel != obj.dRatioModel:
            paramArgs.append("dRatioModel={0}".format(getValueStr(self.dRatioModel)))
        if self.dRatioScreen != obj.dRatioScreen:
            paramArgs.append("dRatioScreen={0}".format(getValueStr(self.dRatioScreen)))
        if self.dRatioValue != obj.dRatioValue:
            paramArgs.append("dRatioValue={0}".format(getValueStr(self.dRatioValue)))
        if self.bUseArrow != obj.bUseArrow:
            paramArgs.append("bUseArrow={0}".format(getBoolStr(self.bUseArrow)))
        if self.iColorHighlight != obj.iColorHighlight:
            paramArgs.append(
                "iColorHighlight={0}".format(getValueStr(self.iColorHighlight))
            )
        if self.iColorPositive != obj.iColorPositive:
            paramArgs.append(
                "iColorPositive={0}".format(getValueStr(self.iColorPositive))
            )
        if self.iColorNegative != obj.iColorNegative:
            paramArgs.append(
                "iColorNegative={0}".format(getValueStr(self.iColorNegative))
            )
        if self.bUseContour != obj.bUseContour:
            paramArgs.append("bUseContour={0}".format(getBoolStr(self.bUseContour)))
        if self.iHighlightTarget != obj.iHighlightTarget:
            paramArgs.append(
                "iHighlightTarget={0}".format(getValueStr(self.iHighlightTarget))
            )
        if self.dHighlightValue1 != obj.dHighlightValue1:
            paramArgs.append(
                "dHighlightValue1={0}".format(getValueStr(self.dHighlightValue1))
            )
        if self.dHighlightValue2 != obj.dHighlightValue2:
            paramArgs.append(
                "dHighlightValue2={0}".format(getValueStr(self.dHighlightValue2))
            )
        if self.iDisplayTarget != obj.iDisplayTarget:
            paramArgs.append(
                "iDisplayTarget={0}".format(getValueStr(self.iDisplayTarget))
            )
        if self.bReverse != obj.bReverse:
            paramArgs.append("bReverse={0}".format(getBoolStr(self.bReverse)))
        if self.bAllModelVector != obj.bAllModelVector:
            paramArgs.append(
                "bAllModelVector={0}".format(getBoolStr(self.bAllModelVector))
            )
        if self.iThresholdOpt != obj.iThresholdOpt:
            paramArgs.append(
                "iThresholdOpt={0}".format(getValueStr(self.iThresholdOpt))
            )
        if self.dThresholdValue != obj.dThresholdValue:
            paramArgs.append(
                "dThresholdValue={0}".format(getValueStr(self.dThresholdValue))
            )
        if self.dThresholdValueMax != obj.dThresholdValueMax:
            paramArgs.append(
                "dThresholdValueMax={0}".format(getValueStr(self.dThresholdValueMax))
            )
        if self.iComparisonOpt != obj.iComparisonOpt:
            paramArgs.append(
                "iComparisonOpt={0}".format(getValueStr(self.iComparisonOpt))
            )
        if self.iComparisonMinRangeOpt != obj.iComparisonMinRangeOpt:
            paramArgs.append(
                "iComparisonMinRangeOpt={0}".format(
                    getValueStr(self.iComparisonMinRangeOpt)
                )
            )
        if self.iComparisonMaxRangeOpt != obj.iComparisonMaxRangeOpt:
            paramArgs.append(
                "iComparisonMaxRangeOpt={0}".format(
                    getValueStr(self.iComparisonMaxRangeOpt)
                )
            )
        if self.bAllSameLength != obj.bAllSameLength:
            paramArgs.append(
                "bAllSameLength={0}".format(getBoolStr(self.bAllSameLength))
            )
        return "PostDataVizOptVector({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}".format(
                self.iScaleMethod,
                self.dRatioModel,
                self.dRatioScreen,
                self.dRatioValue,
                self.bUseArrow,
                self.iColorHighlight,
                self.iColorPositive,
                self.iColorNegative,
                self.bUseContour,
                self.iHighlightTarget,
                self.dHighlightValue1,
                self.dHighlightValue2,
                self.iDisplayTarget,
                self.bReverse,
                self.bAllModelVector,
                self.iThresholdOpt,
                self.dThresholdValue,
                self.dThresholdValueMax,
                self.iComparisonOpt,
                self.iComparisonMinRangeOpt,
                self.iComparisonMaxRangeOpt,
                self.bAllSameLength,
            )
            + rightBracket
        )

class ADVC_CRACK_GROWTH:
    def __init__(self,
        iEvaluationPoint=2,
        iEvaluationValue=0):
        self.iEvaluationPoint = iEvaluationPoint
        self.iEvaluationValue = iEvaluationValue
    def isDefault(self):
        obj = ADVC_CRACK_GROWTH()
        return self.iEvaluationPoint == obj.iEvaluationPoint and \
            self.iEvaluationValue == obj.iEvaluationValue
    def fromList(self, param):
        obj = ADVC_CRACK_GROWTH()
        self.iEvaluationPoint = param[0] if len(param) > 0 else obj.iEvaluationPoint
        self.iEvaluationValue = param[1] if len(param) > 1 else obj.iEvaluationValue
        return self
    def __str__(self):
        obj = ADVC_CRACK_GROWTH()
        paramArgs = []
        if self.iEvaluationPoint != obj.iEvaluationPoint:
            paramArgs.append('iEvaluationPoint={0}'.format(getValueStr(self.iEvaluationPoint)))
        if self.iEvaluationValue != obj.iEvaluationValue:
            paramArgs.append('iEvaluationValue={0}'.format(getValueStr(self.iEvaluationValue)))
        return 'ADVC_CRACK_GROWTH({})'.format(', '.join(paramArgs))
    def __repr__(self):
        return self.__str__()
    def toNativeStr(self, isOneParam=True):
        leftBracket = '[' if isOneParam else ''
        rightBracket = ']' if isOneParam else ''
        return leftBracket + '{0}, {1}'.format(
            self.iEvaluationPoint,
            self.iEvaluationValue) + rightBracket

class ResultLoad:
    def __init__(
        self,
        iVrType=0,
        strResultName="",
        strLoadName="",
    ):
        self.iVrType = iVrType
        self.strResultName = strResultName
        self.strLoadName = strLoadName

    def isDefault(self):
        obj = ResultLoad()
        return (
            self.iVrType == obj.iVrType
            and self.strResultName == obj.strResultName
            and self.strLoadName == obj.strLoadName
        )

    def fromList(self, param):
        obj = ResultLoad()
        self.iVrType = param[0] if len(param) > 0 else obj.iVrType
        self.strResultName = param[1] if len(param) > 1 else obj.strResultName
        self.strLoadName = param[2] if len(param) > 2 else obj.strLoadName
        return self

    def __str__(self):
        obj = ResultLoad()
        paramArgs = []
        if self.iVrType != obj.iVrType:
            paramArgs.append("iVrType={0}".format(getValueStr(self.iVrType)))
        if self.strResultName != obj.strResultName:
            paramArgs.append("strResultName={0}".format('"' + self.strResultName + '"'))
        if self.strLoadName != obj.strLoadName:
            paramArgs.append("strLoadName={0}".format('"' + self.strLoadName + '"'))
        return "ResultLoad({})".format(", ".join(paramArgs))

    def __repr__(self):
        return self.__str__()

    def toNativeStr(self, isOneParam=True):
        leftBracket = "[" if isOneParam else ""
        rightBracket = "]" if isOneParam else ""
        return (
            leftBracket
            + "{0}, {1}, {2}".format(
                self.iVrType,
                '"' + self.strResultName + '"',
                '"' + self.strLoadName + '"',
            )
            + rightBracket
        )
