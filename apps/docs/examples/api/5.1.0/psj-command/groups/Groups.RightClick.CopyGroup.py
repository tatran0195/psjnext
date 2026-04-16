# Title:   Groups.RightClick.CopyGroup()
# Desc:    Copy the inputted groups in the Group tree and paste them to a specified sub group
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/groups/Groups.RightClick.CopyGroup
# ---
Geometry.Part.Cube()

Tools.Group.CreateGroup(strGroupName="Group1", 
                        crlTargets=[Face(22)])
Tools.Group.CreateGroup(strGroupName="Group2", 
                        crlTargets=[Face(24)])
Tools.Group.CreateGroup(strGroupName="Group3",
                        crlTargets=[Face(26)])

Groups.RightClick.AddSubGroup()

pasted_groups = Groups.RightClick.CopyGroup(crlGroups=[Group(1, 2, 3)],   # [hl]
                                            crSubGroup=SubGroup(1))  # [hl]

JPT.Debugger(pasted_groups)
