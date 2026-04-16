# Title:   Meshing.BarMeshing()
# Desc:    Mesh 1D edge/bar part
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.BarMeshing
# ---
MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.0, 0.0, 0.0]], 
                             ilNewNodeID=[1])
MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.001, 0.0, 0.0]], 
                             ilNewNodeID=[2])
Geometry.Bar.TwoNodes(iMeshCount=1, 
                      crStartNode=Node(2), 
                      crEndNode=Node(1))

mesh_status = Meshing.BarMeshing(crlCadEdge=[],   # [hl]
                                 crlBarEdge=[1],   # [hl]
                                 crlBarPart=[],   # [hl]
                                 iDocNumofElem=10)  # [hl]

JPT.Debugger(mesh_status)
