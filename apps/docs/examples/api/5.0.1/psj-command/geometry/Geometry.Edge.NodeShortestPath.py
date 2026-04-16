# Title:   Geometry.Edge.NodeShortestPath()
# Desc:    Create an edge using the shortest path between two nodes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.NodeShortestPath
# ---
Geometry.Part.Cube(iPartColor=6215639)

created_edges = Geometry.Edge.NodeShortestPath(crFirstNode=Node(79),   # [hl]
                                               crSecondNode=Node(91),   # [hl]
                                               iEnableBreakFace=0)  # [hl]

JPT.Debugger(created_edges)
