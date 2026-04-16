# Title:   JPT.GetAllLibraryMaterials()
# Desc:    Get all the information of all library materials
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllLibraryMaterials
# ---
# Get all library materials
libMat = JPT.GetAllLibraryMaterials()
print(f"There are {len(libMat)} materials in the library")
JPT.Debugger(libMat)
JPT.Debugger(libMat[0])
