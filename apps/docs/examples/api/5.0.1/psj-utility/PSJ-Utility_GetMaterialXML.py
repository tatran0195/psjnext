# Title:   JPT.GetMaterialXML()
# Desc:    Get the information of all user material in xml format
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetMaterialXML
# ---
# Create user material data base
Properties.Material.Add("Copper_Alloy", [Density([(DENSITY, 8.3e-09)]),
                        Elastic([(YOUNGS_MODULUS, 110000.0), (POISSONS_RATIO, 0.34)])])

# Get all the created user material and store it in XML format
createdMat = JPT.GetMaterialXML()  # [hl]
pprint(createdMat)
