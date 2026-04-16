# Title:   Groups.RightClick.DeleteGroup()
# Desc:    Delete specified groups from the Group tree in the Group Window
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/groups/Groups.RightClick.DeleteGroup
# ---
Geometry.Part.Cube()

Tools.Group.CreateGroup(strGroupName="Group1",
                        crlTargets=[Face(26)])
Tools.Group.CreateGroup(strGroupName="Group2",
                        crlTargets=[Face(24)])

deleted_groups = Groups.RightClick.DeleteGroup(crlGroups=[Group(1,  # [hl]
                                                                2)])  # [hl]

JPT.Debugger(deleted_groups)
