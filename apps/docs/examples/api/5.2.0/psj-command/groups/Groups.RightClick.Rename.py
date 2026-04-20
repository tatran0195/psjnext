# Title:   Groups.RightClick.Rename()
# Desc:    Rename the specified group in the Group tree of the Group Window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/groups/Groups.RightClick.Rename
# ---
Geometry.Part.Cube()

Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Part(1)])

rename_status = Groups.RightClick.Rename(strNewName = "new name", crItem = Group(1))  # [hl]

JPT.Debugger(rename_status)
