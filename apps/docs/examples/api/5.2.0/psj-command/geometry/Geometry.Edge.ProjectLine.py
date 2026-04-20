# Title:   Geometry.Edge.ProjectLine()
# Desc:    Create new edges by projecting the selected edges onto the selected faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.ProjectLine
# ---
Geometry.Part.Cube(iPartColor=13064794)
line = Geometry.Edge.Line(dllPoints=[[0.004444444444444444, 0.01, 0.01], [0.007777777777777778, 0, 0.01]], 
                          crlFaces=[Face(26)])

project_lines = Geometry.Edge.ProjectLine(crlEdges=line, crlFaces=[Face(25)])  # [hl]
JPT.Debugger(project_lines)
