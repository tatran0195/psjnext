# Title:   Properties.Material.Modify()
# Desc:    Modify an existing material in the User database library by inputting all information of the modifying material
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/properties/Properties.Material.Modify
# ---
structure_steel = Properties.Material.Add(strMaterialName = "Structural_Steel",
    listMaterialProperty = [Density([(DENSITY, 7.85e-09)]),
    Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])])

mod_mat = Properties.Material.Modify(iMaterialID = 1,  # [hl:start]
    listMaterialProperty = [Density([(DENSITY, 7.85e-05)]),
    Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])])  # [hl:end]
JPT.Debugger(mod_mat) #for checking return value
