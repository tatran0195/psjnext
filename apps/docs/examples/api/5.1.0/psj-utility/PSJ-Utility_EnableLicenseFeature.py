# Title:   JPT.EnableLicenseFeature()
# Desc:    Enable or disable an inputted license feature
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_EnableLicenseFeature
# ---
# Disable license JPT_BASE
JPT.EnableLicenseFeature("JPT_BASE",  # [hl]
                         JPT.BoolType.FALSE_VAL)  # [hl]
# Or
# JPT.EnableLicenseFeature("JPT_BASE", 0)  # [hl]

# Enable license JPT_BASE
JPT.EnableLicenseFeature("JPT_BASE",  # [hl]
                         JPT.BoolType.TRUE_VAL)  # [hl]
# Or
# JPT.EnableLicenseFeature("JPT_BASE", 1)  # [hl]
