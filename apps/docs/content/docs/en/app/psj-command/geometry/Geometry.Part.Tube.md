---
title: "Geometry.Part.Tube()"
description: "Create a tubular body around specific edge(s)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Part > Tube"
---

## Description

Create a tubular body around specific edge(s).

## Syntax

```psj
Geometry.Part.Tube(...)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- Edges which will be the center axis of the created tube.

### `strName` @type(String) @default("Tube\_1")

- The name of the newly created part.

### `bTri` @type(Boolean) @default(True)

- The mesh type of newly created part.
  - I&#x66;_&#x54;rue_, Tri3 element will be used.
  - I&#x66;_&#x46;alse_, Quad4 element will be used.

### `dRadius` @type(Double) @default(0.01)

- The radius of the tube.

### `dMeshSizeAxis` @type(Double) @default(0.005)

- The mesh size of the center axis.

### `dWMeshSizeCirc` @type(Double) @default(0.001)

- The mesh size of the circle at both ends (circumference).
  - If this parameter is used,[`iCircularNodes`](#icircularnodes)will be ignored (equal to -1).

### `iCircularNodes` @type(Integer) @default(36)

- The number of nodes to be generated on the circle at both ends (circumference).
  - If this parameter is used,[`dWMeshSizeCirc`](#dwmeshsizecirc)will be ignored (equal to -1.0).

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created_tube = Geometry.Part.Tube(strName="Tube_1", 
                                  crlEdges=[Edge(19)])

JPT.Debugger(created_tube)
```
