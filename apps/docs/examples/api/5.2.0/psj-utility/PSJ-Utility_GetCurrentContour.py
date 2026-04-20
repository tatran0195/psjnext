# Title:   JPT.GetCurrentContour()
# Desc:    Get all current settings of Contour
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCurrentContour
# ---
# Get all currently settings of Contour
contourDict = JPT.GetCurrentContour()  # [hl]

# Dump out result
pprint(contourDict)

# Print out the Upper color
colorRGB = JPT.ConvertJPTColorToRGB(contourDict["UpperColor"])
print("Upper Color: " + colorRGB)
