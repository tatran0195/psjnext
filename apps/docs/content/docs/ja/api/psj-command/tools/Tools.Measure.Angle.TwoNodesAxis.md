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

<!-- @since:5.0.1 @required -->
### crNode1

- Specify the node1.

<!-- @since:5.0.1 @required -->
### crNode2

- Specify the node2.

<!-- @since:5.0.1 @optional -->
### dlAxis

- Specify the axis.
- The default value is \[1,0,0].

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

```psj {3-6}
Geometry.Part.Cube()

angle=Tools.Measure.Angle.TwoNodesAxis(
    crNode1=Node(462), 
    crNode2=Node(466), 
    dlAxis=[0.0, 1.0, 0.0])

JPT.Debugger(angle)
```
