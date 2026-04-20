# Title:   MeshCleanup.Intersection()
# Desc:    Detect element intersection errors.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Intersection
# ---
#Prepare Model
Geometry.Part.Cube(strName="Cube_1", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=13259210)
Geometry.Edge.Angle(
    [CursorPair(Node(452), Node(460)), 
    CursorPair(Node(92), Node(200)), 
    CursorPair(Node(28), Node(392)), 
    CursorPair(Node(12), Node(108))])

Geometry.Face.Edges(crlEdges=[Edge(60, 58)])

#Check body intersection
res=MeshCleanup.Intersection(crlParts=[Part(1,2)], dTolerance=1e-06, iDisplayTypeOption=0)  # [hl]
JPT.Debugger(res)

#Check intersection between bodies
res=MeshCleanup.Intersection(crlParts=[Part(1,2)], dTolerance=1e-06, iDisplayTypeOption=2)  # [hl]
JPT.Debugger(res)

