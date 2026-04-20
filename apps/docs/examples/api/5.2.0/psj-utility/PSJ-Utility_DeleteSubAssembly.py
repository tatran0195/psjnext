# Title:   JPT.DeleteSubAssembly()
# Desc:    Delete the inputted sub assembly
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_DeleteSubAssembly
# ---
# Create 2 sub assemblies under All Parts assemly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())

# Delete the created CreateSubAsm1
subAssem = JPT.FindSubAssemblyByID(2)
JPT.DeleteSubAssembly(subAssem)  # [hl]
