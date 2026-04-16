# Title:   Calculation.Gururi.Sweep()
# Desc:    Output specified element/frequency result output to external file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.Gururi.Sweep
# ---
# Please set path to your result sample file
samplePath = "C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Create a load condition
Calculation.Gururi.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                dAmplitude=10.0, crlTargets=[Node(501)])

# Create a load case
loadCase = Calculation.Gururi.LoadCase(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
                                        crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])

# Sweep calculation
sweepResponse = Calculation.Gururi.Sweep(strExportPath="C:/temp/SweepResult.csv", crlTargets=[ROElem(1486)],   # [hl:start]
                                        crTargetAnalysis=PostFreqAnalysis(1), dlInputFrequency=[1000.0, 2000.0], 
                                        iStepNumber=30)  # [hl:end]
JPT.Debugger(sweepResponse)
