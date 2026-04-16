# Title:   JPT.Exec()
# Desc:    Run Jupiter macro
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_Exec
# ---
# Create a cube and store its cursor
createdCube = JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], \  # [hl]
                        [10, 10, 10], "Cube_1", 12999622, 0:0)')  # [hl]
JPT.Debugger(createdCube) # Return a string object with value = 3:1
