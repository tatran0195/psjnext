# Title:   Groups.RightClick.AddSubGroup()
# Desc:    Create a sub group to the Group tree in the Group Window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/groups/Groups.RightClick.AddSubGroup
# ---
# Prepare model
Geometry.Part.Cube()

# Create groups
Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Face(26)])
Tools.Group.CreateGroup(strGroupName="Group2", crlTargets=[Face(24)])

# Add subgroups
created_sub_group = Groups.RightClick.AddSubGroup()  # [hl]
Assembly.RightClick.Rename(strNewName="SubGroup - 1", crItem=SubGroup(1))
JPT.Debugger(created_sub_group)
