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

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify edges which will be the center axis of the created tube.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the newly created part.
- The default value is "Tube\_1".

<!-- @since:5.0.1 @optional -->
### bTri

- Specify the mesh type of newly created part.
  - If _True_, Tri3 element will be used.
  - If _False_, Quad4 element will be used.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### dRadius

- Specify the radius of the tube.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### dMeshSizeAxis

- Specify the mesh size of the center axis.
- The default value is 0.005.

<!-- @since:5.0.1 @optional -->
### dWMeshSizeCirc

- Specify the mesh size of the circle at both ends (circumference).
  - If this parameter is used, [`iCircularNodes`](#icircularnodes) will be ignored (equal to -1).
- The default value is 0.001.

<!-- @since:5.0.1 @optional -->
### iCircularNodes

- Specify the number of nodes to be generated on the circle at both ends (circumference).
  - If this parameter is used, [`dWMeshSizeCirc`](#dwmeshsizecirc) will be ignored (equal to -1.0).
- The default value is 36.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created _tube = Geometry.Part.Tube(strName="Tube _1", 
                                  crlEdges=[Edge(19)])

JPT.Debugger(created _tube)
```
