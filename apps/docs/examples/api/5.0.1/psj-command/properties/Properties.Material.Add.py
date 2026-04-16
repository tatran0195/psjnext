# Title:   Properties.Material.Add()
# Desc:    Create a new material to the current User database library
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/properties/Properties.Material.Add
# ---
structure_steel = Properties.Material.Add(strMaterialName="Structural_Steel",  # [hl:start]
    listMaterialProperty=[Density([(DENSITY, 7.85e-09)]),
    Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])],
    iMaterialID=5)  # [hl:end]

JPT.Debugger(structure_steel) #for checking return value
