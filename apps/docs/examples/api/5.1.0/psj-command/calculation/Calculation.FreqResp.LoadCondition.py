# Title:   Calculation.FreqResp.LoadCondition()
# Desc:    Set the steady-state excitation input for frequency response
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.FreqResp.LoadCondition
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
loadCondition = Calculation.FreqResp.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0],   # [hl:start]
                                                    dAmplitude=10.0, crlTargets=[Node(1516)])  # [hl:end]
JPT.Debugger(loadCondition)
