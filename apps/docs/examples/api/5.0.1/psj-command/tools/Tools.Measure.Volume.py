# Title:   Tools.Measure.Volume()
# Desc:    Measure volume of the specified parts
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/tools/Tools.Measure.Volume
# ---
Geometry.Part.Cylinder()

volume = Tools.Measure.Volume(crlParts=[Part(1)])  # [hl]

JPT.Debugger(volume)
