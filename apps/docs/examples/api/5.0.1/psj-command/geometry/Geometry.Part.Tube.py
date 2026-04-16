# Title:   Geometry.Part.Tube()
# Desc:    Create a tubular body around specific edge(s)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Part.Tube
# ---
Geometry.Part.Cube()

created_tube = Geometry.Part.Tube(strName="Tube_1",   # [hl]
                                  crlEdges=[Edge(19)])  # [hl]

JPT.Debugger(created_tube)
