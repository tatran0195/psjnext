# Title:   Home.ImportResults.Nastran()
# Desc:    Import Nastran / Vibro result file.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.ImportResults.Nastran
# ---
import os
NastranFile = os.path.join(
    JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH), 
    'SampleData/PSJ/PSJ-Utility/PostSample/101_solid.op2')
Home.ImportResults.Nastran(strPath=NastranFile)  # [hl]
