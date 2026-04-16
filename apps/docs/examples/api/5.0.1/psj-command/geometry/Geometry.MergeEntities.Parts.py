# Title:   Geometry.MergeEntities.Parts()
# Desc:    Merge several parts into a single part. The first selected part will be retained, others will be merged into the first part. Load conditions and material properties, etc., which have been set on faces and edges, will be updated to the merged part automatically
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.MergeEntities.Parts
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0],
                   strName="Cube_2")
merged_part = Geometry.MergeEntities.Parts(crlParts=[Part(1, 2)],  # [hl]
                                           dMergeTolerance=1e-05)  # [hl]
JPT.Debugger(merged_part)
