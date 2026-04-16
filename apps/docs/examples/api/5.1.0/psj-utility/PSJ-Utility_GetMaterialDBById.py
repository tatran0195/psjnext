# Title:   JPT.GetMaterialDBById()
# Desc:    Check whether the inputted material ID is existing in the user material database or not
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetMaterialDBById
# ---
# Create user material data base
Properties.Material.Add("Copper_Alloy", [Density([(DENSITY, 8.3e-09)]),
                        Elastic([(YOUNGS_MODULUS, 110000.0), (POISSONS_RATIO, 0.34)])])
                        # User material ID = 1 (Existing in the Library material database)

# Check the ID of the created material whether it's existing in the
# user material database or not

# Return 1 - The checked material is existing in the user material database and
# return the ID of its which is the same as inputted ID
firstMat = JPT.GetMaterialDBById(1)  # [hl]
JPT.Debugger(firstMat)

# Return 0 - Does not exist in the user material database
# with inputted material ID = 2
secondMat = JPT.GetMaterialDBById(2)  # [hl]
JPT.Debugger(secondMat)
