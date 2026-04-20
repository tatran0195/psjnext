# Title:   JPT.DrawPoint()
# Desc:    Draw a point in Main Window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_DrawPoint
# ---
#Prepare a model for view
Geometry.Part.Cube(dlLength=[10.0, 10.0, 10.0])
JPT.ViewFitToModel()

# Draw a green point at position [10, 20, 30] with the default color and width:
JPT.DrawPoint([10, 20, 30])  # [hl]

# Draw a red point at position [5, 15, 25] with a width of 2.5:
JPT.DrawPoint([5, 15, 25], 255, 2.5)  # [hl]

# Draw a blue point at position [0, 0, 0] with a width of 1.5:
JPT.DrawPoint([0, 0, 0], 16711680, 1.5)  # [hl]
