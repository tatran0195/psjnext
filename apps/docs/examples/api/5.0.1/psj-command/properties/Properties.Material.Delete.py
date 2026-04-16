# Title:   Properties.Material.Delete()
# Desc:    Delete an existing material in the User database by inputting its ID
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/properties/Properties.Material.Delete
# ---
structure_steel = Properties.Material.Add(strMaterialName = "Structural_Steel",
                                          listMaterialProperty = [Density([(DENSITY, 
                                                                            7.85e-09)]),
                                                                  Elastic([(YOUNGS_MODULUS, 
                                                                            200000.0), 
                                                                           (POISSONS_RATIO, 
                                                                            0.3)])])

del_mat = Properties.Material.Delete(1) # 1 is the ID of the created material  # [hl]

JPT.Debugger(del_mat) # For checking return value
