# Title:   JPT.GetCurrentDeformation()
# Desc:    Get all current settings of Deformation
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCurrentDeformation
# ---
# Get all currently settings of Deformation
deformDict = JPT.GetCurrentDeformation()  # [hl]

# Dump out result
pprint(deformDict)

# Print out the Edge color
colorRGB = JPT.ConvertJPTColorToRGB(deformDict["EdgeColor"])
print("Edge Color: " + colorRGB)
