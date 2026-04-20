# Title:   Home.AddResults.ADVC()
# Desc:    Add ADVC results to the current Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.ADVC
# ---
#Please set path to your sample ADVC folder.
meshfile='C:/Sample/mesh.adx'
folderpath="C:/Temp/SampleADVC"

Home.ImportResults.ImportMesh.ADVC(folderpath)
Home.AddResults.ADVC(strlPaths=[folderpath], bMergeTree=False, bADVCProcessNameRule=False, bDisplayNAResult=False)  # [hl]
