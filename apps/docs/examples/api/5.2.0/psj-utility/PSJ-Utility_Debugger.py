# Title:   JPT.Debugger()
# Desc:    Console debugger for PSJ
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_Debugger
# ---
# Prepare model
Geometry.Part.Cube()
# Get the information of all existing parts
allParts = JPT.GetAllParts()
# Print all the related information of the first part to the screen
JPT.Debugger(allParts[0])  # [hl]
