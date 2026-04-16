# Title:   Analysis.AbaqusStep.DynamicExplicitStep()
# Desc:    Create Abaqus Step - Dynamic Explicit Type
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/analysis/Analysis.AbaqusStep.DynamicExplicitStep
# ---
process = Analysis.AbaqusStep.DynamicExplicitStep(strName="Step1",
  abaqusPair1=ABAQUS_PAIR(dlTList=[0.0]), listAbaqusOutputRequest=[])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
