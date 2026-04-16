# Title:   Geometry.Transform.ThreePoints()
# Desc:    Move the parts by selecting three pairs of nodes. The selected parts are moved onto the target position in a one-to-one correspondence between source and target
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Transform.ThreePoints
# ---
target_part = Geometry.Part.Cube()
move_part = Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], 
                               strName="Cube_2", 
                               iPartColor=6409934)

created_parts = Geometry.Transform.ThreePoints(crlTargetParts=[move_part],  # [hl]
                                               poslOriginalPoints=[[0.022, 0, 0.01],   # [hl]
                                                                   [0.022, 0.01, 0.01],   # [hl]
                                                                   [0.012, 0, 0.01]],  # [hl]
                                               poslNextPoints=[[0.01, 0, 0.01],   # [hl]
                                                               [0, 0, 0.01],   # [hl]
                                                               [0, 0.01, 0.01]],  # [hl]
                                               bCreateNewPart=True,   # [hl]
                                               bCopyLBC=True,   # [hl]
                                               bCopyProperty=True,  # [hl]
                                               bCopyReference=True)  # [hl]

JPT.Debugger(created_parts)
