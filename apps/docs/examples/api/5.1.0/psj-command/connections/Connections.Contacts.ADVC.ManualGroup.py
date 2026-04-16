# Title:   Connections.Contacts.ADVC.ManualGroup()
# Desc:    Define contact settings between specified groups for the ADVC solver
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.ADVC.ManualGroup
# ---
# Prepare model
Geometry.Part.Cube(
    iPartColor=6409934
)
Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7463537
)

# Prepare groups to set contact
Tools.Group.CreateGroup(
    strGroupName="Group1", crlTargets=[Face(24)]
)
Tools.Group.CreateGroup(
    strGroupName="Group2", crlTargets=[Face(49)]
)

# Create contact by group selection
Connections.Contacts.ADVC.ManualGroup(
    strName="ContactADVC_1", 
    iSlidingType=1, 
    dClearance=0.2, 
    dInterference=0.2, iAdvAdjust=1, 
    crplTarget=[CursorPair(Group(1), Group(2))]
)
