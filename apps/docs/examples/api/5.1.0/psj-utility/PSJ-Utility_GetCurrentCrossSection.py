# Title:   JPT.GetCurrentCrossSection()
# Desc:    Get all current settings of Cross Section
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCurrentCrossSection
# ---
# Get all currently settings of Cross Section
crossDict = JPT.GetCurrentCrossSection()  # [hl]

# Dump out result
pprint(crossDict)

# Print out the current position
print("Current Position: " + str(crossDict["CurrentPosition"]))
