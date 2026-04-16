# Title:   JPT.UpdateCheckboxAssembly()
# Desc:    Set state of checkbox of item in Assembly Tree
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_UpdateCheckboxAssembly
# ---
# prepare model...
JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_1", 7105764, 0:0)')
JPT.Exec('CreateCube([0.02, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_2", 6409934, 0:0)')
JPT.Exec('CreateCube([0, 0.02, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_3", 13259210, 0:0)')

parts = JPT.GetAllParts()

# update checkbox from assembly tree
for part in parts:
    JPT.UpdateCheckboxAssembly(JPT.DItemType.BODY, part.id, 1) # turn on checkbox  # [hl:start]
    JPT.UpdateCheckboxAssembly(JPT.DItemType.BODY, part.id, 0) # turn off checkbox  # [hl:end]
