# Title:   Analysis.AbaqusStep.ModalStep()
# Desc:    Create Abaqus Step - Modal Type
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.AbaqusStep.ModalStep
# ---
process = Analysis.AbaqusStep.ModalStep(strName="Step1", ilNFreqRequestTList=[DFLT_INT],  # [hl:start]
  ilFreqShiftTList=[DFLT_DBL], ilFreqRangeTList=[DFLT_DBL, DFLT_DBL],
  ilBlockSizeTList=[DFLT_DBL], ilMaxBlkNumofLanczosStepTList=[0], ilEvalPropFreqTList=[DFLT_DBL])  # [hl:end]

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
