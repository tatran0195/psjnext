# Title:   Calculation.Gururi.LoadCase()
# Desc:    Create a load case for Gururi analysis
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.Gururi.LoadCase
# ---
# Please set path to your result sample file
samplePath = "C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Create a load condition
Calculation.Gururi.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                dAmplitude=10.0, crlTargets=[Node(501)])

# Create a load case
loadCase = Calculation.Gururi.LoadCase(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1",   # [hl:start]
                                        crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])  # [hl:end]
JPT.Debugger(loadCase)
