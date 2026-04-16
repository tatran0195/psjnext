# Title:   Calculation.TransResp.ResponseCondition()
# Desc:    Output the result of the response point for transient response
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.TransResp.ResponseCondition
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
Calculation.TransResp.LoadCondition(strName="TRNLoad_2", iLoadType=1, iLoadDirection=2, 
                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, dT2=0.5, 
                                    dFrequency=10.0, crlTargets=[Node(1516)])

# Create a loadcase
Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), strName="LoadCase_1",
                                        crlSelectedLoad=[PostTransLoad(1)], dlTargetFactor=[1.0])

# Create response condition
respCondition = Calculation.TransResp.ResponseCondition(crTargetAnalysis=PostTransAnalysis(1), dDampingFactor=0.02,   # [hl:start]
                                                        iCurveStyle=0, dStyleParamMid=80.0, dStyleParamBot=0.0125, 
                                                        strlResultNames=["TZ"], crlTargets=[Node(1516, 1016)])  # [hl:end]
Chart.CreateGraph(crTargetCurve=PostTransResultCurve(1), strChartTitle="Transient Analysis Displacement", 
                strAxisTitleX="Time", strAxisTitleY="Data")
Chart.CreateGraph(crTargetCurve=PostTransResultCurve(3), strChartTitle="Transient Analysis Displacement", 
                strAxisTitleX="Time", strAxisTitleY="Data", bNewChart=False)
JPT.Debugger(respCondition) # for checking the return value
