# Title:   Home.ImportCAD.Parasolid()
# Desc:    Import a parasolid file (*.x_t) to the Jupiter Database
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ImportCAD.Parasolid
# ---
imported_status = Home.ImportCAD.Parasolid(strlPaths=[JPT.GetProgramPath() +  # [hl]
                                                      "SampleData/CAD_Model/Parasolid/BWM_GRABCAD.x_t"],  # [hl]
                                           dAngleToleranceDegree=7.0,  # [hl]
                                           dScale=0.001)  # [hl]
JPT.Debugger(imported_status)
