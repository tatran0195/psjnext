# Title:   Connections.SolidBoltModeling()
# Desc:    Create a solid bolt composed of hexa elements.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.SolidBoltModeling
# ---
##################
# Prepare model
##################

# Create a cube
cube=Geometry.Part.Cube(
    ilAxialNodes=[3, 3, 3], 
    strName="Cube_3", 
    iPartColor=6409934)

# Get top face
maxface=JPT.Exec(f'FindFacesInPart({cube},"MaxZFACE")')

# Imprint circle on the top face.
Geometry.Edge.Circle(
    veclPositions=[[0.005, 0.005, 0.01]], 
    crlTargetFace=maxface, 
    dOutRadius=2.0, 
    iNoOfDiv=8)

# Get newly created edge - > top edge.
edge1=JPT.GetMaxIDEntity(JPT.DItemType.EDGE)

# Delete newly created face.
face=JPT.GetMaxIDEntity(JPT.DItemType.FACE)
JPT.Exec(f'DeleteFace([{face}], 1)')

# Get bottom face
minface=JPT.Exec(f'FindFacesInPart({cube},"MinZFACE")')

# Imprint circle on the bottom face.
Geometry.Edge.Circle(
    veclPositions=[[0.005, 0.005, 0.0]], 
    crlTargetFace=minface, 
    dOutRadius=2.0, 
    iNoOfDiv=8)
# Get newly created edge - > bottom edge.
edge2=JPT.GetMaxIDEntity(JPT.DItemType.EDGE)

# Delete newly created face.
face=JPT.GetMaxIDEntity(JPT.DItemType.FACE)
JPT.Exec(f'DeleteFace([{face}], 1)')

# Create side face of bolt hole.
Geometry.Face.Edges(crlEdges=[Edge(edge1, edge2)])

# Create a solid bolt at the hole.
Connections.SolidBoltModeling(  # [hl:start]
    crlTopTargets=[Edge(edge1)], 
    crlBottomTargets=[Edge(edge2)], 
    strName="Bolt_1", iBoltType=1, 
    dMaxHeight=10,     
    dDiameter=3, 
    dBoltHeadWidthAcrossFlat=5.5,
    dBoltHeadHeight=2, 
    dShaftLength=10, 
    dPitch=1, 
    iTopHeadHeightDivision=2,
    iTopHeadRadialDivision=2)
