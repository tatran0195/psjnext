---
title: "Tools.Measure.Angle.TwoNodesAxis()"
description: "Measure the angle created by 2 nodes and Axis."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Angle > TwoNodesAxis"
---

## Description

Measure the angle created by 2 nodes and Axis.

## Syntax

```psj
Tools.Measure.Angle.TwoNodesAxis(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode1`

- The node1.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode2`

- The node2.

<!-- @since:5.0.1 @type:Double List @optional @default:[1,0,0] -->
### `dlAxis`

- The axis.

<!-- @since:5.0.1 @type:String @optional @default:"Angle" -->
### `strTarget`

- The target.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The precision.

## Return Code

Value measured with the precision set in iPrecision in _String_ format.

## Sample Code

```psj {3-6}
Geometry.Part.Cube()

angle=Tools.Measure.Angle.TwoNodesAxis(
    crNode1=Node(462), 
    crNode2=Node(466), 
    dlAxis=[0.0, 1.0, 0.0])

JPT.Debugger(angle)
```
