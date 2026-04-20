# Title:   Home.ImportCAD.VRML()
# Desc:    Import a Virtual Reality Modeling Language file (*.wrl) to the Jupiter Database
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ImportCAD.VRML
# ---
imported_status = Home.ImportCAD.VRML(strlPaths=[JPT.GetProgramPath() +  # [hl]
                                                 "SampleData/CAD_Model/WRML/GrabCAD 2-SHIP.wrl"],  # [hl]
                                      iVRMLColorGroups=1,  # [hl]
                                      dScale=0.001)  # [hl]
JPT.Debugger(imported_status)
