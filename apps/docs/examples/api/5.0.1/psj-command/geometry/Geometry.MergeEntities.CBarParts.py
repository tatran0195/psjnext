# Title:   Geometry.MergeEntities.CBarParts()
# Desc:    Merge CBar Parts
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.MergeEntities.CBarParts
# ---
MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.0, 0.0, 0.0]], ilNewNodeID=[1])

MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.01, 0.0, 0.0]], ilNewNodeID=[2])

MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.01, 0.01, 0.0]], ilNewNodeID=[3])

MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.01, 0.01, 0.01]], ilNewNodeID=[4])

Geometry.Bar.TwoNodes(iMeshCount=4, crStartNode=Node(1), crEndNode=Node(2))

Geometry.Bar.TwoNodes(strName="Bar_2", iMeshCount=4, crStartNode=Node(2), crEndNode=Node(3))

Geometry.Bar.TwoNodes(strName="Bar_3", iMeshCount=4, crStartNode=Node(3), crEndNode=Node(4))

Geometry.MergeEntities.CBarParts(crlCBarPart=[Part(1, 2, 3)])
