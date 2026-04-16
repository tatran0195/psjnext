# Title:   Tools.Measure.Volume()
# Desc:    Measure volume of the specified parts
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Volume
# ---
Geometry.Part.Cylinder()

volume = Tools.Measure.Volume(crlParts=[Part(1)])  # [hl]

JPT.Debugger(volume)
