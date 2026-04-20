# Title:   Geometry.Part.Trapezoid()
# Desc:    Create a trapezoid body in a specific location. Its relative location is computed to the specified local coordinate system
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Part.Trapezoid
# ---
trapezoid = Geometry.Part.Trapezoid(dlLength=[0.02, 0.01, 0.01],  # [hl]
                                    strName="Trapezoid_5",  # [hl]
                                    iPartColor=7961077)  # [hl]
JPT.Debugger(trapezoid)
