# Title:   JPT.CreateSubAssembly()
# Desc:    Create a new sub assembly under the indicated parent sub assembly
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_CreateSubAssembly
# ---
# Create 2 sub assemblies under All Parts assembly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())  # [hl]
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())  # [hl]

# Create a sub assembly under CreateSubAsm0 (ID = 1)
JPT.CreateSubAssembly('CreateSubAsm2',JPT.FindSubAssemblyByID(1))  # [hl]
