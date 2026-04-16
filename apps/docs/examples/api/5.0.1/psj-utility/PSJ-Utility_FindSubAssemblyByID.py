# Title:   JPT.FindSubAssemblyByID()
# Desc:    Get the related information of the target sub assembly by its ID
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_FindSubAssemblyByID
# ---
# Create 2 sub assemblies under All Parts assembly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())
JPT.ViewFitToModel()

# Get the information of the sub assembly with ID = 1
JPT.Debugger(JPT.FindSubAssemblyByID(1))  # [hl]
