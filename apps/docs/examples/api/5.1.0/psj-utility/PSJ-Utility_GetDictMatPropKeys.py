# Title:   JPT.GetDictMatPropKeys()
# Desc:    Get list keys from dictMatProps
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetDictMatPropKeys
# ---
# Get 1st material in the library materials
mat0 = JPT.GetAllLibraryMaterials()[0]

# Get & print dicMatProps
dict1 = mat0.dictMatProps
pprint(dict1)
