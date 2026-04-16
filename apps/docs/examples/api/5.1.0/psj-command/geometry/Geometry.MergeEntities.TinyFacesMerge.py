# Title:   Geometry.MergeEntities.TinyFacesMerge()
# Desc:    Merge tiny faces either by extending the user selection or using only the selected faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.MergeEntities.TinyFacesMerge
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=6409934)
Geometry.Edge.Angle([CursorPair(Node(945), Node(953))])
Geometry.Edge.Angle([CursorPair(Node(464), Node(472))])
Geometry.Edge.Angle([CursorPair(Node(79), Node(432))])
Geometry.Edge.Angle([CursorPair(Node(96), Node(487))])
Geometry.Edge.Angle([CursorPair(Node(470), Node(479))])
Geometry.Edge.Angle([CursorPair(Node(471), Node(479))])
Geometry.Edge.Angle([CursorPair(Node(946), Node(954))])
Geometry.Edge.Angle([CursorPair(Node(953), Node(954))])
Geometry.Edge.Angle([CursorPair(Node(961), Node(962))])
Geometry.Edge.Angle([CursorPair(Node(953), Node(962))])
merged_entities = Geometry.MergeEntities.TinyFacesMerge(crlTargets=[Part(1, 2)],  # [hl]
                                                        bCreateRefPart=True)  # [hl]
JPT.Debugger(merged_entities)
