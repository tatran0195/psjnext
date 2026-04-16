# Title:   Geometry.Part.Tube()
# Desc:    Create a tubular body around specific edge(s)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Part.Tube
# ---
Geometry.Part.Cube()

created_tube = Geometry.Part.Tube(strName="Tube_1",   # [hl]
                                  crlEdges=[Edge(19)])  # [hl]

JPT.Debugger(created_tube)
