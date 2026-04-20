# Title:   Assemble.BooleanEx()
# Desc:    Conduct a Boolean operation on selected bodies
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assemble/Assemble.BooleanEx
# ---
cube1 = Geometry.Part.Cube(iPartColor=4934581)
cube2 = Geometry.Part.Cube(dlOrigin=[0.005, 0.005, 0.005], 
                           strName="Cube_2", 
                           iPartColor=6215639)

boolean_status = Assemble.BooleanEx([cube1, cube2],   # [hl]
                                    iTargetPart=1)  # [hl]

JPT.Debugger(boolean_status)
