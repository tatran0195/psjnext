# Title:   JPT.RemoveAllFieldTables()
# Desc:    Remove all the existing field tables
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_RemoveAllFieldTables
# ---
# Create sample fields data
BoundaryConditions.FieldData(strName="test_1", iType=1,
                             ilSheet=[3, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
BoundaryConditions.FieldData(strName="test_2", iType=4,
                             ilSheet=[3, 2, 1, 1, 2, 2, 3, 3])
BoundaryConditions.FieldData(strName="test_3", iType=3,
                             ilSheet=[3, 2, 1, 1, 2, 2, 3, 3])

# Remove all the created fields data
JPT.RemoveAllFieldTables()  # [hl]
