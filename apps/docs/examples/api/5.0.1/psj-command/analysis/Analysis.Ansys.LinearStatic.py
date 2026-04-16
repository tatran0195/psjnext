# Title:   Analysis.Ansys.LinearStatic()
# Desc:    Export the Ansys Linear Static Structural solver file
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/analysis/Analysis.Ansys.LinearStatic
# ---
Geometry.Part.Cube()

Analysis.Ansys.LinearStatic("Job1", ansysAnalysisBasic=BASIC(dTimeStepSize=1.0, dMinTimeStep=1.0),  # [hl:start]
    iLoadCaseId=1, strFileName="D:/Job1.dat")  # [hl:end]
