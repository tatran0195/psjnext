# Title:   Tools.Measure.Mass.Material()
# Desc:    Measure mass by using the specified material's density
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Mass.Material
# ---
Geometry.Part.Cube()

mass = Tools.Measure.Mass.Material(crlParts=[Part(1)],   # [hl]
                                   dMaterialDensity=2300.0)  # [hl]

JPT.Debugger(mass)
