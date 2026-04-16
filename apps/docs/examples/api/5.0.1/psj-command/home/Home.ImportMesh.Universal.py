# Title:   Home.ImportMesh.Universal()
# Desc:    Import an Universal file (*.unv) to the Jupiter Database (Mesh, boundary conditions, etc.)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/home/Home.ImportMesh.Universal
# ---
import_status = Home.ImportMesh.Universal(strPath=JPT.GetProgramPath() + \  # [hl]
                                                  "SampleData/Mesh_Model/Universal/Exported_Universal_File_EXPORT_UNI.unv")  # [hl]
JPT.Debugger(import_status)
