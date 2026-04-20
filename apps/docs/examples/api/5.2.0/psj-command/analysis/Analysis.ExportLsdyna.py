# Title:   Analysis.ExportLsdyna()
# Desc:    Export LS-Dyna Analysis Job
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.ExportLsdyna
# ---
Geometry.Part.Cube(iPartColor=12999622)

Analysis.LSDYNAJob()

Analysis.ExportLsdyna(strPath="C:/Job_1.k", crJob=LSDynaJob(1))
