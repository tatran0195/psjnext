# Title:   Geometry.Part.Cube()
# Desc:    Create a cuboid body in a specific location. This relative location is computed to the specified local coordinate system
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Part.Cube
# ---
created_cube = Geometry.Part.Cube(dlOrigin=[0.005, 0.005, 0.005],   # [hl]
                                  strName="Cube_1",   # [hl]
                                  iPartColor=13259210)  # [hl]

JPT.Debugger(created_cube)
