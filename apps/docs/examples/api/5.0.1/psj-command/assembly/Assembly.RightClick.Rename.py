# Title:   Assembly.RightClick.Rename()
# Desc:    Rename a specified entity
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assembly/Assembly.RightClick.Rename
# ---
Geometry.Part.Cube()

rename_status = Assembly.RightClick.Rename(strNewName="Box",   # [hl]
                                           crItem=Part(1))  # [hl]

JPT.Debugger(rename_status)
