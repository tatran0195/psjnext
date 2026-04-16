# Title:   Home.ImportMesh.Universal()
# Desc:    Import an Universal file (*.unv) to the Jupiter Database (Mesh, boundary conditions, etc.)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ImportMesh.Universal
# ---
from os import environ

unv_file_path = environ["Temp"] + "/TechnoStar/Exported_Universal_File_EXPORT_unv.bdf"

Geometry.Part.Cube(ilAxialNodes=[3, 3, 3])
Meshing.SolidMeshing(crlParts=[Part(1)], bTet10=True, 
                    dGradingFactor=1.0, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    bSafeMode=False, 
                    iParallel=8, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)

Home.EXPORT_UNIVERSAL(strFileName=unv_file_path, crlParts=[Part(1)])

JPT.CreateNewDocument()

import_status = Home.ImportMesh.Universal(strlPaths=[unv_file_path])  # [hl]

JPT.Debugger(import_status)
