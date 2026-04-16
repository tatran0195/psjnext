# Title:   Tools.GroupByDCS()
# Desc:    Create node groups according to the nodal coordinate system.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.GroupByDCS
# ---
#Prepare model
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], 
    iPartColor=7463537)
Tools.Coordinates.Face(
    strName="CRect_4", 
    veclPoint=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], 
    crItem=Face(24))

#Find target face
faces=JPT.Exec('FindEntities("-10,5,5","Face", 0)')

#Get ids from the result and input into Face function.

ditem_list=JPT.MacroListTCursorToListDItem(faces)
ids=[ditem.id for ditem in ditem_list]

#Create nodal coordinate system for the nodes in the selected face. 
Tools.DisplacementCS(crlInst=[Face(*ids)], crCoordSystem=Coord(1))

#Create node groups according to the nodal coordinate system.
Tools.GroupByDCS()  # [hl]
