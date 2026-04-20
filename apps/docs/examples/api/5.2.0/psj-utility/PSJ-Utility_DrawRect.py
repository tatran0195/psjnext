# Title:   JPT.DrawRect()
# Desc:    Draw a rectangle on Main Window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_DrawRect
# ---
JPT.ClearDraw()
# Draw a rectangle with 
# top-left corner at (10, 20) 
# bottom-right corner at (50, 100)
# in pixels
JPT.DrawRect(10, 20, 50, 100)  # [hl]

# Draw a rectangle in red with  
# top-left corner at (100, 200) 
# and bottom-right corner at (400, 400)
# in pixels
JPT.DrawRect(100, 200, 400, 400, 255)  # [hl]

# Draw a rectangle in yellow, width=5 with 
# top-left corner at (100, 10) 
# bottom-right corner at (200, 100)
# in pixels
JPT.DrawRect(100, 10, 200, 100, JPT.ConvertRGBToJPTColor(255,255,0), 5)  # [hl]

