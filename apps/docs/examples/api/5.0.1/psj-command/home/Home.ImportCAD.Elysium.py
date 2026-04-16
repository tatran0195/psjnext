# Title:   Home.ImportCAD.Elysium()
# Desc:    Import a CAD file by using Elysium interface to the Jupiter Database
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/home/Home.ImportCAD.Elysium
# ---
imported_status = Home.ImportCAD.Elysium(strlPaths=[JPT.GetProgramPath() +  # [hl]
                                                    "SampleData/CAD_Model/IGES/A400MA.igs"],  # [hl]
                                         dAngleToleranceDegree=3.0,  # [hl]
                                         dPointCoincidentTolerance=1e-05,  # [hl]
                                         dIgesStitchtolerance=0.01)  # [hl]
JPT.Debugger(imported_status)
