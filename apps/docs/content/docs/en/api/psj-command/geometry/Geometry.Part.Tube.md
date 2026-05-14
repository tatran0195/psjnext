---
title: "Geometry.Part.Tube()"
description: "Create a tubular body around specific edge(s)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Tube"
---

## Description

Create a tubular body around specific edge(s).

## Syntax

```psj
Geometry.Part.Tube(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The edges which will be the center axis of the created tube.

<!-- @since:5.0.1 @type:String @optional @default:"Tube _1" -->
### `strName`

- The name of the newly created part.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bTri`

- The mesh type of newly created part.
  - If _True_, Tri3 element will be used.
  - If _False_, Quad4 element will be used.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dRadius`

- The radius of the tube.

<!-- @since:5.0.1 @type:Double @optional @default:0.005 -->
### `dMeshSizeAxis`

- The mesh size of the center axis.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dWMeshSizeCirc`

- The mesh size of the circle at both ends (circumference).
  - If this parameter is used, [`iCircularNodes`](#icircularnodes) will be ignored (equal to -1).

<!-- @since:5.0.1 @type:Integer @optional @default:36 -->
### `iCircularNodes`

- The number of nodes to be generated on the circle at both ends (circumference).
  - If this parameter is used, [`dWMeshSizeCirc`](#dwmeshsizecirc) will be ignored (equal to -1.0).

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created _tube = Geometry.Part.Tube(strName="Tube _1", 
                                  crlEdges=[Edge(19)])

JPT.Debugger(created _tube)
```
