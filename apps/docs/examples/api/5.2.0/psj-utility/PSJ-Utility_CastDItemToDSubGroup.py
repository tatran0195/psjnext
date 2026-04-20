# Title:   JPT.CastDItemToDSubGroup()
# Desc:    Convert DItem object to DSubGroup object
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_CastDItemToDSubGroup
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=7697908)

Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0], 
    strName="Cube_2", 
    iPartColor=14903267)

mating_faces=Assemble.FindMatingFaceEx(
    crlTaBodies=[Part(1, 2)], 
    dMatingTol=0.000222222)

Assemble.AssembleFaceEx(
    ilPairFaceToMakeShareFace=mating_faces, 
    dTolerance=0.000222222, 
    iTypeConnectPos=0)

# Get Sub Group object as DItem object from the created list of DItem objects
listDItemSubGroups = JPT.GetAllByTypeID(JPT.DItemType.SUP_GROUP)
dItemSubGroup = listDItemSubGroups[0]
JPT.Debugger(dItemSubGroup)

# Convert from the above DItem object to DGroup object
dSubGroup = JPT.CastDItemToDSubGroup(dItemSubGroup)  # [hl]
JPT.Debugger(dSubGroup)
