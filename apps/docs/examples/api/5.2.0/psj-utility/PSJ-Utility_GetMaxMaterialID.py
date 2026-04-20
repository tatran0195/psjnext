# Title:   JPT.GetMaxMaterialID()
# Desc:    Get the maximum ID of the user material in the user material database
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetMaxMaterialID
# ---
# Create user material data base
Properties.Material.Add("Stainless_Steel", [Density([(DENSITY, 7.75e-09)]),
                        Elastic([(YOUNGS_MODULUS, 193000.0), (POISSONS_RATIO, 0.31)])])
Properties.Material.Add("Titanium_Alloy", [Density([(DENSITY, 4.62e-09)]),
                        Elastic([(YOUNGS_MODULUS, 96000.0), (POISSONS_RATIO, 0.36)])])
Properties.Material.Add("Aluminum_Alloy", [Density([(DENSITY, 2.7699999999999997e-09)]),
                        Elastic([(YOUNGS_MODULUS, 71000.0), (POISSONS_RATIO, 0.33)])])

# Get the maximum ID of the user material in the User material Database
iMaxMaterialID = JPT.GetMaxMaterialID()  # [hl]
JPT.Debugger(iMaxMaterialID) # Return an integer object with value = 3
