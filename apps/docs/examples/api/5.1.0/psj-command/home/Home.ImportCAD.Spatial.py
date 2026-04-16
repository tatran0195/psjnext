# Title:   Home.ImportCAD.Spatial()
# Desc:    Import a CAD file by using Spatial interface to the Jupiter Database
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ImportCAD.Spatial
# ---
imported_status = Home.ImportCAD.Spatial(strlPaths=[JPT.GetProgramPath() +  # [hl]
                                                    "SampleData/CAD_Model/IGES/A400MA.igs"],  # [hl]
                                         bSetFaceColor=True)  # [hl]
JPT.Debugger(imported_status)
