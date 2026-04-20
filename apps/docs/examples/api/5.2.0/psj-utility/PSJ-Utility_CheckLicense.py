# Title:   JPT.CheckLicense()
# Desc:    Check whether the inputted license is activated or not
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_CheckLicense
# ---
# Get the status of the JPT_BASE feature license and print to the screen
lic = JPT.CheckLicense("JPT_BASE")  # [hl]
print(lic)
