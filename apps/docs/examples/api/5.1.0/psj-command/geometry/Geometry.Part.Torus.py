# Title:   Geometry.Part.Torus()
# Desc:    Create a donut body in a specific location. Its relative location is computed to the specified local coordinate system
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Part.Torus
# ---
torus = Geometry.Part.Torus(dlOrigin=[0.005, 0.005, 0.005], strName="Torus", iPartColor=7697908)  # [hl]
JPT.Debugger(torus)
