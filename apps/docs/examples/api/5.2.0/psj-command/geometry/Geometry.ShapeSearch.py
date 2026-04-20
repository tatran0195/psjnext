# Title:   Geometry.ShapeSearch()
# Desc:    Search shape in specified parts.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.ShapeSearch
# ---
# Prepare model
Geometry.Part.Cylinder(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], iPartColor=7434735)

JPT.ClearAllSelection()
# Search planar faces and select.
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE_SEARCH_OPTION(iType=4, bAll=1)])  # [hl]
print(f"There are {len(result)} planar faces.")

JPT.ClearAllSelection()
# Search full cylinder faces and select.
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE_SEARCH_OPTION(iType=8, bAll=1)])  # [hl]
print(f"There are {len(result)} full cylinder faces.")
