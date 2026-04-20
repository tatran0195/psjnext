# Title:   JPT.DrawLine()
# Desc:    Draw a line in Main Window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_DrawLine
# ---
#Prepare a model for view
Geometry.Part.Cube(dlLength=[10.0, 10.0, 10.0])
JPT.ViewFitToModel()

# Draw a white line from [0, 0, 0] to [10, 20, 30] with the default color and width:
JPT.DrawLine([0, 0, 0], [10, 20, 30])  # [hl]

# Draw a red line from [5, 5, 5] to [15, 15, 15] with a width of 2.5:
JPT.DrawLine([5, 5, 5], [15, 15, 15], 255, 2.5)  # [hl]
        
# Draw a green line from [1, 1, 1] to [2, 2, 2] with a width of 1.5:
JPT.DrawLine([1, 1, 1], [2, 2, 2], 65280, 1.5)  # [hl]
