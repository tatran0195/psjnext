# Title:   Assemble.AddRibEx.FromEdge()
# Desc:    Specify an edge to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assemble/Assemble.AddRibEx.FromEdge
# ---
Geometry.Part.Cube(iPartColor=11776856)

Geometry.Edge.Spline(
    dllPoints=[
        [0.003333333333333333, 0.001111111111111111, 0.01], 
        [0.002222222222222222, 0.007777777777777778, 0.01], 
        [0.006666666666666666, 0.005555555555555556, 0.01], 
        [0.008888888888888889, 0.006666666666666666, 0.01]], 
    crlFaces=[Face(26)])

Assemble.AddRibEx.FromEdge(  # [hl:start]
    crlFaces=[Face(26)], 
    crlEdges=[Edge(41)], 
    dThickness=0.001, 
    dHeight=0.001)  # [hl:end]
