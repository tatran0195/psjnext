# Title:   Groups.RightClick.ChangeMarkerColor()
# Desc:    Change marker color of the group
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/groups/Groups.RightClick.ChangeMarkerColor
# ---
# Prepare model
Geometry.Part.Cube()

# Create groups
Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Face(26)])
Tools.Group.CreateGroup(strGroupName="Group2", crlTargets=[Face(24)])

# Show marker color
JPT.Exec('ViewShowGroupMarker(1)')
# Change marker color
Groups.RightClick.ChangeMarkerColor(listGroupColors=[[Group(1), 10616736]])  # [hl]
Groups.RightClick.ChangeMarkerColor(listGroupColors=[[Group(2), 16716288]])  # [hl]
