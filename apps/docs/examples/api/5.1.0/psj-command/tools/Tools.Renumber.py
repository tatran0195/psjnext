# Title:   Tools.Renumber()
# Desc:    Renumber the IDs of the model such as Face, Edge, Elements(1D,2D,3D) and Nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Renumber
# ---
Geometry.Part.Cube()

result = Tools.Renumber(listRenumberItem=[RENUMBER_ITEM(crTarget=Part(1),   # [hl]
                                                        iBeginID=1000,   # [hl]
                                                        iCount=488,   # [hl]
                                                        ilOffset=[10000, 100, 1],   # [hl]
                                                        dlCoordTolerance=[0.1, 0.1, 0.1],   # [hl]
                                                        bEnable=True)])  # [hl]

JPT.Debugger(result)
