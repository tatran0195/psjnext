---
title: "Geometry.Edge.Angle()"
description: "Create a new edge by convert angle"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Angle"
---

## Description

This method generates an Edge entity by given the element edges and recursively finding adjacent element edges that are at an angle greater than or equal to the specified angle.
The direction of the automatic selection can be changed by selecting an element edge.

## Syntax

```psj
Geometry.Edge.Angle(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Pairs of Cursor] @required -->
### `crplElemEdges`

- The element edges used for automatic selection.

<!-- @since:5.0.1 @type:Double @optional @default:135.0 -->
### `dEdgeAngle`

- The angle in degrees.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCurvature`

- Whether to find the adjacent element edges which can be chained to form a circle.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bBreakFace`

- Whether to break the face which the given element edges lie on where possible.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5,6,7}
Geometry.Part.Cube()

created _edges = Geometry.Edge.Angle(crplElemEdges=[CursorPair(Node(461), Node(470)), 
                                        CursorPair(Node(445), Node(446))], 
                                    dEdgeAngle=135.0, 
                                    bCurvature=False, 
                                    bBreakFace=True)
JPT.Debugger(created _edges)
```
