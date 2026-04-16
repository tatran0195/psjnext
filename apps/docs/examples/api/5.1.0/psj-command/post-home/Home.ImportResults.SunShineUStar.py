# Title:   Home.ImportResults.SunShineUStar()
# Desc:    Import a SunShine UStar file to the Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.ImportResults.SunShineUStar
# ---
import os
UstarFile = os.path.join(JPT.GetAppPathInfo(JPT.PathType.APPDATA_PATH), 'SampleData/PSJ/PSJ-Utility/PostSample/plate_beam_ustar.op2')
Home.ImportResults.SunShineUStar(strPath=UstarFile)  # [hl]
