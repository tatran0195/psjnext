# Title:   JPT.RemoveAllMaterials()
# Desc:    Remove all the existing material in the User material database
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_RemoveAllMaterials
# ---
# Create materials
Properties.Material.Add("Copper_Alloy", [Density([(DENSITY, 8.3e-09)]),
                                         Elastic([(YOUNGS_MODULUS, 110000.0),
                                                  (POISSONS_RATIO, 0.34)])])
Properties.Material.Add("Stainless_Steel", [Density([(DENSITY, 7.75e-09)]),
                                            Elastic([(YOUNGS_MODULUS, 193000.0),
                                                     (POISSONS_RATIO, 0.31)])])
Properties.Material.Add("Titanium_Alloy", [Density([(DENSITY, 4.62e-09)]),
                                           Elastic([(YOUNGS_MODULUS, 96000.0),
                                                    (POISSONS_RATIO, 0.36)])])

# Remove all the created materials in the User material database
JPT.RemoveAllMaterials()  # [hl]
