# Title:   JPT.GetCurrentCircle()
# Desc:    Get all current settings of Circle
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCurrentCircle
# ---
# Get all currently settings of Circle
circleDict = JPT.GetCurrentCircle()  # [hl]

# Dump out result
pprint(circleDict)

# Print out the Highlight color
colorRGB = JPT.ConvertJPTColorToRGB(circleDict["HighlightColor"])
print("Highlight Color: " + colorRGB)
