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

<!-- @since:5.0.1 @required -->
### crpElemEdge1

- Specify the element edge1 - two nodes.

<!-- @since:5.0.1 @required -->
### crpElemEdge2

- Specify the element edge2 - two nodes.

<!-- @since:5.0.1 @optional -->
### strTarget

- Specify the target.
- The default value is "Angle".

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

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
