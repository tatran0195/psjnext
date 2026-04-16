# Title:   Home.RectangularCapture()
# Desc:    Save the specified range of Jupiter's display window to the clipboard
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/home/Home.RectangularCapture
# ---
Geometry.Part.Cube()

copy = Home.RectangularCapture(iLeft=477,  # [hl]
                               iTop=159,  # [hl]
                               iRight=900,  # [hl]
                               iBottom=562)  # [hl]

JPT.Debugger(copy)
