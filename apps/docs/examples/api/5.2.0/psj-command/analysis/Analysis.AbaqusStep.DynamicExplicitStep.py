# Title:   Analysis.AbaqusStep.DynamicExplicitStep()
# Desc:    Create Abaqus Step - Dynamic Explicit Type
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.AbaqusStep.DynamicExplicitStep
# ---
process = Analysis.AbaqusStep.DynamicExplicitStep(strName="Step1",  # [hl:start]
  abaqusPair1=ABAQUS_PAIR(dlTList=[0.0]), listAbaqusOutputRequest=[])  # [hl:end]

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
