# Title:   Analysis.Ansys.NormalModes()
# Desc:    Export the Ansys Normal Modes Structural solver file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.Ansys.NormalModes
# ---
Geometry.Part.Cube()

Analysis.Ansys.NormalModes("Job1", iLoadCaseId=1, strFileName="C:/Job1.dat")  # [hl]
