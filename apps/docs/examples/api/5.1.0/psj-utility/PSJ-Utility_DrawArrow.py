# Title:   JPT.DrawArrow()
# Desc:    Draw an arrow in Main Window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_DrawArrow
# ---
#Prepare a model for view
Geometry.Part.Cube(dlLength=[10.0, 10.0, 10.0])
JPT.ViewFitToModel()

#Draw a cyan arrow from [0, 0, 0] to [10, 20, 30] with default width and style:
JPT.DrawArrow([0, 0, 0], [10, 20, 30])  # [hl]

#Draw a red arrow from [5, 5, 5] to [15, 15, 15] with width 2.5 pixels:
JPT.DrawArrow([5, 5, 5], [15, 15, 15], 255, 2.5)  # [hl]

#Draw a green arrow with arrows pointing in both directions:
JPT.DrawArrow([1, 1, 1], [4, 4, 4], 65280, 1.5, True)  # [hl]

#Draw a blue arrow in 2D style from [2, 2, 0] to [4, 4, 0] with default width:  # [hl]
JPT.DrawArrow([2, 2, 0], [4, 4, 0], 16711680, 1.0, False, False)
