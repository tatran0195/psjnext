# Title:   JPT.GetCurrentDiagram()
# Desc:    Get all current settings of Diagram
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCurrentDiagram
# ---
# Get all currently settings of Diagram
diagramDict = JPT.GetCurrentDiagram()  # [hl]

# Dump out result
pprint(diagramDict)

# Print out the Positive color
colorRGB = JPT.ConvertJPTColorToRGB(diagramDict["PositiveColor"])
print("Positive Color: " + colorRGB)
