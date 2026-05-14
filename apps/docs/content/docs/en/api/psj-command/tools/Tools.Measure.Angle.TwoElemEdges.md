---
title: "Tools.Measure.Angle.TwoElemEdges()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Angle > TwoElemEdges"
---

## Description

## Syntax

```psj
Tools.Measure.Angle.TwoElemEdges(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor Pair @required -->
### `crpElemEdge1`

- The element edge1 - two nodes.

<!-- @since:5.0.1 @type:Cursor Pair @required -->
### `crpElemEdge2`

- The element edge2 - two nodes.

<!-- @since:5.0.1 @type:String @optional @default:"Angle" -->
### `strTarget`

- The target.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The precision.

## Return Code

Value measured with the precision set in iPrecision in _String_ format.

## Sample Code

```psj {3-5}
Geometry.Part.Cube()

angle = Tools.Measure.Angle.TwoElemEdges(
            crpElemEdge1=CursorPair(Node(95), Node(487)), 
            crpElemEdge2=CursorPair(Node(453), Node(462)))

JPT.Debugger(angle)
```
