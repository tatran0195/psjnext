# Title:   Assembly.RightClick.ChangeMeshLineColor()
# Desc:    Change the color of the mesh line of the selected part
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assembly/Assembly.RightClick.ChangeMeshLineColor
# ---
Geometry.Part.Cube()

changed_status = Assembly.RightClick.ChangeMeshLineColor(crlFaces=[Face(21,   # [hl]
                                                                        22,   # [hl]
                                                                        23,   # [hl]
                                                                        24,   # [hl]
                                                                        25,   # [hl]
                                                                        26)],   # [hl]
                                                         iColor=10535167)  # [hl]

JPT.Debugger(changed_status)
