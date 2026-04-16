# Title:   Assembly.RightClick.ChangeEntityColor()
# Desc:    Change color of a specific entity/a list of entities (By ID)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assembly/Assembly.RightClick.ChangeEntityColor
# ---
Geometry.Part.Cube()
changed_color = Assembly.RightClick.ChangeEntityColor(crlEntities=[Face(26, 24, 22)], iColor=16777088)  # [hl]
JPT.Debugger(changed_color)
