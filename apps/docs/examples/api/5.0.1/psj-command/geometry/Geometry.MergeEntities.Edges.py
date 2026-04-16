# Title:   Geometry.MergeEntities.Edges()
# Desc:    Merge all the selected edges into uninterrupted edges
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.MergeEntities.Edges
# ---
Geometry.Part.Cube()
Geometry.BreakEntity.Edge(crlNodes=[Node(95, 92, 90)])

merged_edges = Geometry.MergeEntities.Edges(crlEdges=[Edge(9,   # [hl]
                                                           10,   # [hl]
                                                           11,   # [hl]
                                                           12,   # [hl]
                                                           13,   # [hl]
                                                           14,   # [hl]
                                                           15,   # [hl]
                                                           16,   # [hl]
                                                           17,   # [hl]
                                                           18,   # [hl]
                                                           20,   # [hl]
                                                           28,   # [hl]
                                                           32,   # [hl]
                                                           34,   # [hl]
                                                           35)])  # [hl]

JPT.Debugger(merged_edges)
