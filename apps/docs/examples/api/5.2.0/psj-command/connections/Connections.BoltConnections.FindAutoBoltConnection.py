# Title:   Connections.BoltConnections.FindAutoBoltConnection()
# Desc:    Get table data of Auto Bolt Connection.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.BoltConnections.FindAutoBoltConnection
# ---
def delete_newly_created_face():
    new_face=JPT.GetMaxIDEntity(JPT.DItemType.FACE)
    print(new_face)
    if new_face:
        JPT.Exec(f'DeleteFace([{new_face}], 1)')

#Prepare a model

Geometry.Part.Cube(
    ilAxialNodes=[3, 3, 3], 
    iPartColor=7463537)
Geometry.Part.Cube(
    dlOrigin=[0.0, 0.0, 0.01], 
    ilAxialNodes=[3, 3, 3], 
    strName="Cube_2", 
    iPartColor=11842649)

top_edge_1st=Geometry.Edge.Circle(
    veclPositions=[[0.005, 0.005, 0.02]], 
    crlTargetFace=[Face(52)], 
    dOutRadius=2.0)
    delete_newly_created_face()

bottom_edge_1st=Geometry.Edge.ProjectLine(
    crlEdges=top_edge_1st, 
    crlFaces=[Face(51)])
delete_newly_created_face()

Geometry.Face.Edges(
    

top_edge_2nd=Geometry.Edge.ProjectLine(
    crlEdges=top_edge_1st, crlFaces=[Face(25)])
delete_newly_created_face()

bottom_edge_2nd=Geometry.Edge.ProjectLine(
    crlEdges=top_edge_1st, crlFaces=[Face(26)])
delete_newly_created_face()

Geometry.Face.Edges(crlEdges=top_edge_2nd+bottom_edge_2nd)

Meshing.SetMeshAttribute(
    crlParts=[Part(2, 1)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.003, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0)
    )

Meshing.SurfaceMeshing(
    crlParts=[Part(2, 1)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.003, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True, 
    iNextEntityOffsetId=0)
)

bolt_connections=Connections.BoltConnections.FindAutoBoltConnection(
    crMasterPart=Part(2), 
    crSlavePart=Part(1), 
    dMinCircleDiameter=0.00324, 
    dMaxCircleDiameter=0.004)

JPT.Debugger(bolt_connections)

#How to use
Connections.BoltConnections.AutoBoltConnection(strName="Bolt", 
    listBoltHoles=bolt_connections, 
        crlMatingFaces=[Face(26, 51)])
