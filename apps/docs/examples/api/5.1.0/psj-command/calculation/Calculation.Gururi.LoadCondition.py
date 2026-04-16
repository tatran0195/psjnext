# Title:   Calculation.Gururi.LoadCondition()
# Desc:    Set the frequency response steady-state excitation input for the Gururi
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.Gururi.LoadCondition
# ---
# Please set path to your result sample file
samplePath = "C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Create a load condition
loadcondition = Calculation.Gururi.LoadCondition(strName="FRQLoad_1", iLoadDirection=2,   # [hl:start]
                                                dlForce=[0.0, 0.0, 10.0], dAmplitude=10.0, 
                                                crlTargets=[Node(501)])  # [hl:end]
JPT.Debugger(loadcondition)
