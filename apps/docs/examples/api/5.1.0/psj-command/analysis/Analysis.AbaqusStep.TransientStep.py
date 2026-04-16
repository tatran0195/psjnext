# Title:   Analysis.AbaqusStep.TransientStep()
# Desc:    Create Abaqus Step - Transient Type
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.AbaqusStep.TransientStep
# ---
process = Analysis.AbaqusStep.TransientStep(strName="Step1", iMaxInc=100, dInitSize=1.0,  # [hl:start]
  dMinSize=1e-05, dMaxSize=1.0, dMaxAllowEmissivityChange=0.1, iAllowedIters=8,
  dAdjustFactor=1.0, iMaxContactIter=30, dTimePeriod=1.0, iRamp=1, listAbaqusOutputRequest=[])  # [hl:end]

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
