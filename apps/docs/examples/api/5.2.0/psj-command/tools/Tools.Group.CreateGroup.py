# Title:   Tools.Group.CreateGroup()
# Desc:    Create a group of arbitrary entities.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Group.CreateGroup
# ---
Geometry.Part.Cube(iPartColor=6409934)
created_group = Tools.Group.CreateGroup(strGroupName="Part_Group1", crlTargets=[Part(1)])  # [hl]
for group in created_group:
    JPT.Debugger(JPT.MacroTCursorToDItem(str(group)))
