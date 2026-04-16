# Title:   Assembly.RightClick.AddToReference()
# Desc:    Add the current part to its Reference and use the added one as the current reference part
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assembly/Assembly.RightClick.AddToReference
# ---
Geometry.Part.Cube()

adding_status = Assembly.RightClick.AddToReference(crSrcPart=Part(1),   # [hl]
                                                   crDestPart=Part(1))  # [hl]

JPT.Debugger(adding_status)
