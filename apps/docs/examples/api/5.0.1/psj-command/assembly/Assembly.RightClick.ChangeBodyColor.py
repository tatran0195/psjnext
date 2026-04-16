# Title:   Assembly.RightClick.ChangeBodyColor()
# Desc:    Change the color of the selected part
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assembly/Assembly.RightClick.ChangeBodyColor
# ---
Geometry.Part.Cube()

adding_status = Assembly.RightClick.ChangeBodyColor(listPartColorPair=[PART_COLOR_PAIR(crPart=Part(1),  # [hl]
                                                                                       iColor=6409934)])  # [hl]

JPT.Debugger(adding_status)
