# Title:   JPT.GetCurrentVector()
# Desc:    Get all current settings of Vector
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCurrentVector
# ---
# Get all currently settings of Vector
vectorDict = JPT.GetCurrentVector()  # [hl]

# Dump out result
pprint(vectorDict)

# Print out the Positive color
colorRGB = JPT.ConvertJPTColorToRGB(vectorDict["PositiveColor"])
print("Positive Color: " + colorRGB)
