# Title:   Home.ImportMesh.Marc()
# Desc:    Import a Marc file (*.t16, *.t19) to the Jupiter Database (Mesh, boundary conditions, etc.)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ImportMesh.Marc
# ---
#Prepare your data
marc_file_path="C:/Temp/sample.t16"

import_status = Home.ImportMesh.Marc(strPath=marc_file_path)  # [hl]
JPT.Debugger(import_status)
