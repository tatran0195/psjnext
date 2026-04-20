# Title:   JPT.GetCurrentViewPoint()
# Desc:    Get all current settings of ViewPoint
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCurrentViewPoint
# ---
# Get all currently settings of ViewPoint
viewDict = JPT.GetCurrentViewPoint()  # [hl]

# Dump out result
pprint(viewDict)

# Print out the Scale factor
print("Scale Factor: " + str(viewDict["ScaleFactor"]))
