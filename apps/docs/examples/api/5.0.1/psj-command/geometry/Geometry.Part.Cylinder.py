# Title:   Geometry.Part.Cylinder()
# Desc:    Create a cylindrical body at a specific location. Its relative location is computed based on the specified local coordinate system
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Part.Cylinder
# ---
created_cylinder = Geometry.Part.Cylinder(dlOrigin=[0.005, 0.005, 0.005],  # [hl]
                                          strName="Cylinder_2",   # [hl]
                                          iPartColor=7463537)  # [hl]

JPT.Debugger(created_cylinder)
