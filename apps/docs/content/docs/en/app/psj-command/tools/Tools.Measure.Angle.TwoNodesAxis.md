---
title: "Tools.Measure.Angle.TwoNodesAxis()"
description: "Measure the angle created by 2 nodes and Axis."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Angle > TwoNodesAxis"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Measure the angle created by 2 nodes and Axis.

## Syntax

```psj
Tools.Measure.Angle.TwoNodesAxis(...)
```

## Inputs

### `crNode1` @type(Cursor) @required

- The node1.

### `crNode2` @type(Cursor) @required

- The node2.

### `dlAxis` @type(Double List) @default(\[1,0,0])

- The axis.

### `strTarget` @type(String) @default("Angle")

- The target.

### `iPrecision` @type(Integer) @default(6)

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
