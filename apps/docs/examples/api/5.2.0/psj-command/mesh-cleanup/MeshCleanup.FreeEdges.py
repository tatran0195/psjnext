# Title:   MeshCleanup.FreeEdges()
# Desc:    Check free edges and non-manifolds.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.FreeEdges
# ---
#Create a model.
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
mating_face=Assemble.FindMatingFaceEx(
    crlTaBodies=[Part(1, 2)], 
    dMatingTol=0.000222222)
Assemble.AssembleFaceEx(
    ilPairFaceToMakeShareFace=mating_face, 
    dTolerance=0.000222222, 
    iTypeConnectPos=0)
JPT.Exec('DeleteFace([49], 1)')
Geometry.Part.Cube(dlOrigin=[0.01, 0.015, 0.0], strName="Cube_3", iPartColor=7697908)
Geometry.Edge.Angle([
    CursorPair(Node(1069), Node(1461)), 
    CursorPair(Node(1069), Node(1184)), 
    CursorPair(Node(1005), Node(1376)), 
    CursorPair(Node(989), Node(1085))])
Geometry.Face.Edges(crlEdges=[Edge(98, 97, 96, 95)])
Geometry.Part.Cube(dlOrigin=[0.0, 0.015, 0.0], strName="Cube_4", iPartColor=7463537)
JPT.Exec('DeleteFace([133], 1)')
JPT.Exec('DeleteFace([129], 1)')
JPT.Exec('DeleteFace([132], 1)')
JPT.Exec('DeleteFace([128], 1)')
JPT.Exec('DeleteFace([131], 1)')

#Check free edges and non-manifolds.
ret=MeshCleanup.FreeEdges(crlParts=[Part(1, 2, 3, 4)], bFreeEdgeByPart=True, bErrorText=True)  # [hl]
print(f"{ret.iFreeEdges}/72")
print(f"{ret.iNonManifoldEdges}/36")
