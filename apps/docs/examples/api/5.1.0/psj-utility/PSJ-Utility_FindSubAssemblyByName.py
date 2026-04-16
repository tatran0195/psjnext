# Title:   JPT.FindSubAssemblyByName()
# Desc:    Get the related information of the target sub assembly by its name
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_FindSubAssemblyByName
# ---
# Create 2 sub assemblies under All Parts assembly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())
JPT.ViewFitToModel()

# Get the information of the sub assembly with name = CreateSubAsm0
JPT.Debugger(JPT.FindSubAssemblyByName('CreateSubAsm0'))  # [hl]

