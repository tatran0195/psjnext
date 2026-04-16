# Title:   Geometry.Edge.NodeShortestPath()
# Desc:    Create an edge by converting the element edges on the shortest path between two nodes into edge
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.NodeShortestPath
# ---
Geometry.Part.Cube(iPartColor=6215639)

created_edges = Geometry.Edge.NodeShortestPath(crFirstNode=Node(79),   # [hl]
                                               crSecondNode=Node(91),   # [hl]
                                               bBreakFace=0)  # [hl]
JPT.Debugger(created_edges)
