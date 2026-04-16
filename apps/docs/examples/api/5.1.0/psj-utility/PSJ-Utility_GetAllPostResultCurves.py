# Title:   JPT.GetAllPostResultCurves()
# Desc:    Get all the information of all existing Post result curves
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllPostResultCurves
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Create a load condition
Calculation.FreqResp.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                    dAmplitude=10.0, crlTargets=[Node(1516)]) 

# Create a load case
Calculation.FreqResp.LoadCaseCondition(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
                                crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])

# Create a response condition
respCondition = Calculation.FreqResp.ResponseCondition(crTargetAnalysis=PostFreqAnalysis(1), 
                                                        dDampingFactor=0.02, dStyleParamMid=10.0, 
                                                        dStyleParamBot=200.0, strlResultNames=["TZ"], 
                                                        crlTargets=[Node(1516, 1016)])
Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(1), strChartTitle="Frequency Analysis Displacement", 
                strAxisTitleX="Frequency", strAxisTitleY="Amplitude", bNewChart=False)
Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(3), strChartTitle="Frequency Analysis Displacement", 
                strAxisTitleX="Frequency", strAxisTitleY="Amplitude", bNewChart=False)
# Get all Post result curves
listCurves = JPT.GetAllPostResultCurves()  # [hl]
JPT.Debugger(listCurves)
for curve in listCurves:
    if "MPF" not in curve.name:
        print(curve.name)
        print(curve.rowCount)
        print(curve.colCount)
        print(curve.typeID)
        print(curve.curveType)
        JPT.Debugger(curve.allData)
        JPT.Debugger(curve.frequency)
        JPT.Debugger(curve.amplitude)
        JPT.Debugger(curve.phase)
        JPT.Debugger(curve.real)
        JPT.Debugger(curve.imagine)
    else:
        print(curve.name)
        print(curve.rowCount)
        print(curve.colCount)
        print(curve.typeID)
        print(curve.curveType)
