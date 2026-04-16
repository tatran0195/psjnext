# Title:   Geometry.Edge.ProjectLine()
# Desc:    Create new edges by projecting the selected edges onto the selected faces
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.ProjectLine
# ---
test=Geometry.Part.Cube(iPartColor=13064794)
edge1=Geometry.Edge.Line(dllPoints=[[0.004444444444444444, 0.01, 0.01], [0.007777777777777778, 0, 0.01]], crlFaces=[Face(26)])
edge2=Geometry.Edge.ProjectLine(crlCrEdges=edge1, crlCrFaces=[Face(25)])  # [hl]
JPT.Debugger(edge2)
