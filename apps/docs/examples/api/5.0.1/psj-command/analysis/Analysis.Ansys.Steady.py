# Title:   Analysis.Ansys.Steady()
# Desc:    Export the Ansys Steady Static Heat Transfer solver file
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/analysis/Analysis.Ansys.Steady
# ---
Geometry.Part.Cube()

Analysis.Ansys.Steady("Job1", ansysAnalysisBasic=BASIC(dTimeStepSize=1.0, dMinTimeStep=1.0),  # [hl:start]
    iLoadCaseId=1, ansysAnalysisSteadyStatic=STEADY_STATIC(bSteadyStaticMemorySave=True), strFileName="D:/Job1.dat")  # [hl:end]
