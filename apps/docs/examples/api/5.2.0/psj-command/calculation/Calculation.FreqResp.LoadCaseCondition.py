# Title:   Calculation.FreqResp.LoadCaseCondition()
# Desc:    Set the steady-state excitation input for frequency response (Solver)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.FreqResp.LoadCaseCondition
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Create a load condition
Calculation.FreqResp.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                    dAmplitude=10.0, crlTargets=[Node(1516)])

# Create a load case
loadCase = Calculation.FreqResp.LoadCaseCondition(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1",   # [hl:start]
                                            crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])  # [hl:end]
JPT.Debugger(loadCase)
