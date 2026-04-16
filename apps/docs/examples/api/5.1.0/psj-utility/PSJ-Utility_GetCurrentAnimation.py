# Title:   JPT.GetCurrentAnimation()
# Desc:    Get all current settings of Animation
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCurrentAnimation
# ---
# Get all currently settings of Animation
animationDict = JPT.GetCurrentAnimation()  # [hl]

# Dump out result
pprint(animationDict)

# Print out the Frame number
print("Frame Number: " + str(animationDict["FrameNumber"]))
