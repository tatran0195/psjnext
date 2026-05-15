---
title: "Geometry.ShapeSearch()"
description: "Search shape in specified parts."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Geometry > ShapeSearch"
macro _link: ""
---

## Description

Search shape in specified parts.

## Syntax

```psj
Geometry.ShapeSearch(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlParts

- Specify the target parts.

<!-- @since:5.1.0 @optional -->
### crlRefEdges

- Specify the reference edges.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iGroupOption

- Specify the grouping option.
  - 0: Do not create the Group.
  - 1: Create a group containing all searched results (faces, edges) of all specified shape types for searching in the selected parts.
  - 2: Create separate groups containing the searched results (faces, edges) corresponding to each specified shape type for searching in the selected parts.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strGroupName

- Specify the name of the group.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### listShapeSearchOptions

- Specify the geometry options required for searching.
- The default value is _[SHAPE\_SEARCH\_OPTION](../../data-type/psj-command/parameter-types/SHAPE _SEARCH _OPTION)_.

<!-- @since:5.1.0 @optional -->
### bConvexOption

- Specify whether to include convex shapes.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bConcaveOption

- Specify whether to include concave shapes.
- The default value is _False_.

## Return Code

- A _List of Cursor_ specifying the entities (face or edge) found.

## Sample Code

```psj {7,12}
# Prepare model
Geometry.Part.Cylinder(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], iPartColor=7434735)

JPT.ClearAllSelection()
# Search planar faces and select.
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE _SEARCH _OPTION(iType=4, bAll=1)])
print(f"There are {len(result)} planar faces.")

JPT.ClearAllSelection()
# Search full cylinder faces and select.
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE _SEARCH _OPTION(iType=8, bAll=1)])
print(f"There are {len(result)} full cylinder faces.")
```
