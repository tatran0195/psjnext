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

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlParts`

- The target parts.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlRefEdges`

- The reference edges.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iGroupOption`

- The grouping option.
  - 0: Do not create the Group.
  - 1: Create a group containing all searched results (faces, edges) of all specified shape types for searching in the selected parts.
  - 2: Create separate groups containing the searched results (faces, edges) corresponding to each specified shape type for searching in the selected parts.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strGroupName`

- The name of the group.

<!-- @since:5.1.0 @type:List[SHAPE _SEARCH _OPTION] @optional @default:SHAPE _SEARCH _OPTION -->
### `listShapeSearchOptions`

- The geometry options required for searching.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bConvexOption`

- Whether to include convex shapes.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bConcaveOption `

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
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE _SEARCH _OPTION(iType=4, bAll=1)])
print(f"There are {len(result)} planar faces.")

JPT.ClearAllSelection()
# Search full cylinder faces and select.
result=Geometry.ShapeSearch(crlParts=[Part(1, 2)], listShapeSearchOptions=[SHAPE _SEARCH _OPTION(iType=8, bAll=1)])
print(f"There are {len(result)} full cylinder faces.")
```
