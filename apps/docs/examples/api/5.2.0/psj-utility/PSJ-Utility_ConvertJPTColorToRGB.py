# Title:   JPT.ConvertJPTColorToRGB()
# Desc:    Convert color value in Jupiter to a string specifying RGB (Red, Green, Blue) code
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_ConvertJPTColorToRGB
# ---
# Convert the color code = 255 in Jupiter to RGB color code
stringRGB = JPT.ConvertJPTColorToRGB(255) # Return RGB(255,0,0)  # [hl]
# Split the RGB code and store it as Red Green Blue color code
r, g, b = stringRGB[4:-1].strip().split(",") # String = RGB(255,0,0) -> List = [255, 0, 0]
print(f"Output value of this function: {stringRGB}")
print(f"It means: Red = {r} | Green = {g} | Blue = {b}")
