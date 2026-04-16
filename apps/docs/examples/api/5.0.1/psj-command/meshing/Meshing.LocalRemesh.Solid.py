# Title:   Meshing.LocalRemesh.Solid()
# Desc:    Mesh the selected solid elements locally without affecting the other positions
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.LocalRemesh.Solid
# ---
cube = Geometry.Part.Cube(iPartColor=12603072)
MeshEdit.MoveNode.CADFollows(crlNodes=[Node(453)], 
                             dMovedPosX=5.527019999999999, 
                             dMovedPosY=5.43058, 
                             dMovedPosZ=10.0)

Meshing.SolidMeshing(crlParts=[cube], 
                     bTet10=True, 
                     dGradingFactor=1.05, 
                     dStretchLimit=0.1, 
                     iSpeedVsQual=1, 
                     iRegion=1, 
                     bSafeMode=False, 
                     iParallel=4, 
                     bSurfaceNodes=False, 
                     bEdgeNodes=False, 
                     bPreservation=False, 
                     iPartColor=65280)

remesh_status = Meshing.LocalRemesh.Solid(crlParts=[cube],   # [hl]
                                          dlCenter=[0.005555555555555556,   # [hl]
                                                    0.005555555555555556,   # [hl]
                                                    0.01],   # [hl]
                                          dRadius=2.0)  # [hl]

JPT.Debugger(remesh_status)
