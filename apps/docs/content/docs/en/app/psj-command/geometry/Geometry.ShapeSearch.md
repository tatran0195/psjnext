---
title: "Geometry.ShapeSearch()"
description: "Search shape in specified parts."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Geometry > ShapeSearch"
macro_link: ""
---

## Description

Search shape in specified parts.

## Syntax

```psj
Geometry.ShapeSearch(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The target parts.

### `crlRefEdges` @type(List\[Cursor]) @default(\[])

- The reference edges.

### `iGroupOption` @type(Integer) @default(0)

- The grouping option.
  - 0: Do not create the Group.
  - 1: Create a group containing all searched results (faces, edges) of all specified shape types for searching in the selected parts.
  - 2: Create separate groups containing the searched results (faces, edges) corresponding to each specified shape type for searching in the selected parts.

### `strGroupName` @type(String) @default("")

- The name of the group.

### `listShapeSearchOptions` @type(List\[SHAPE\_SEARCH\_OPTION]) @default(SHAPE\_SEARCH\_OPTION)

- The geometry options required for searching.

### `bConvexOption` @type(Boolean) @default(False)

- Whether to include convex shapes.

### `bConcaveOption ` @type(Boolean) @default(False)

- Whether to include concave shapes.

## Return Code

- A _List of Cursor_ specifying the entities (face or edge) found.

## Sample Code

```psj {7,12}
# Prepare model
Geometry.Part.Cylinder(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], iPartColor=7434735)

JPT.ClearAllSelection()
# Search planar faces and select.
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE_SEARCH_OPTION(iType=4, bAll=1)])
print(f"There are {len(result)} planar faces.")

JPT.ClearAllSelection()
# Search full cylinder faces and select.
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE_SEARCH_OPTION(iType=8, bAll=1)])
print(f"There are {len(result)} full cylinder faces.")
```
