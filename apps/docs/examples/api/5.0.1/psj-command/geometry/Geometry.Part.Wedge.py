# Title:   Geometry.Part.Wedge()
# Desc:    Create a wedge shaped body in a specific location. This relative location is computed to the specified local coordinate system
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Part.Wedge
# ---
wedge = Geometry.Part.Wedge(dlOrigin=[0.005, 0.005, 0.005], strName="Wedge", iPartColor=6409934)  # [hl]

JPT.Debugger(wedge)
