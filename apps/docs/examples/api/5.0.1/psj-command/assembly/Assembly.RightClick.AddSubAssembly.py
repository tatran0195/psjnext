# Title:   Assembly.RightClick.AddSubAssembly()
# Desc:    Add a new assembly (Sub-assembly) to the selected assembly
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assembly/Assembly.RightClick.AddSubAssembly
# ---
Geometry.Part.Cube()

Assembly.RightClick.AddSubAssembly()  # [hl]
created_sub_assem = Assembly.RightClick.AddSubAssembly(crInst=Inst(1))  # [hl]

JPT.Debugger(created_sub_assem)
