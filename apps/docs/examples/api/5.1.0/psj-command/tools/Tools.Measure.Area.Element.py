# Title:   Tools.Measure.Area.Element()
# Desc:    Measure Area By Element
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Area.Element
# ---
Geometry.Part.Cube()

area=Tools.Measure.Area.Element(crlElems=[Elem(1025,1026)])  # [hl]
JPT.Debugger(area)

area=Tools.Measure.Area.Element(crlElems=[Elem(1025,1026)], iPrecision=15)  # [hl]
JPT.Debugger(area)

