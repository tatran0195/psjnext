# Title:   Analysis.Ansys.LinearStatic()
# Desc:    Export the Ansys Linear Static Structural solver file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.Ansys.LinearStatic
# ---
Geometry.Part.Cube()

Analysis.Ansys.LinearStatic(strJobName="Job1", iVersion=1, strAnsysJobName="Job1", ansysAnalysisBasic=BASIC(dTimeStepSize=1.0, dMinTimeStep=1.0), iLoadCaseId=1, strFileName="C:/temp/Job1.dat")  # [hl:start]
