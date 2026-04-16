# Title:   Home.ImportCAD.STL()
# Desc:    Import a Standard Tessellation Language file (*.stl) to the Jupiter Database
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.ImportCAD.STL
# ---
imported_status = Home.ImportCAD.STL(strlPaths=[JPT.GetProgramPath() +  # [hl]
                                                "SampleData/CAD_Model/STL/Macbook Pro 15.stl"],  # [hl]
                                     dScale=0.001)  # [hl]
JPT.Debugger(imported_status)
