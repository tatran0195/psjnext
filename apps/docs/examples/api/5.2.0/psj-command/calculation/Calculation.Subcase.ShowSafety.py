# Title:   Calculation.Subcase.ShowSafety()
# Desc:    Create a subcase by calculating the safety factor from the selected subcases based on the tolerance of each part
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.Subcase.ShowSafety
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Subcase.RelativeOffset
showSafety = Calculation.Subcase.ShowSafety(  # [hl:start]
    iAnalysisType=2, 
    listSubcaseIDs=[1, 2, 3, 4, 5], 
    listSafetyItems=[
        SAFETY_ITEM(crPart=Part(1), dThreshold=1), 
        SAFETY_ITEM(crPart=Part(2), dThreshold=1), 
        SAFETY_ITEM(crPart=Part(3), dThreshold=1)])  # [hl:end]
JPT.Debugger(showSafety)
