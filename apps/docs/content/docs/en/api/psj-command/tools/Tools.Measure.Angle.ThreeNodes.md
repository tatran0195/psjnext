---
title: "Tools.Measure.Angle.ThreeNodes()"
description: "Measure the angle by using the specified 3 nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Angle > ThreeNodes"
---

---

## Description

Measure the angle by using the specified 3 nodes.

## Syntax

```psj
Tools.Measure.Angle.ThreeNodes(...)
```

## Inputs

### `crNode1`

\- A _Cursor_ specifying the first node (A) to measure angle.
\- This is a required input.

### `crNode2`

\- A _Cursor_ specifying the second node (B) to measure angle.
\- This is a required input.

### `crNode3`

\- A _Cursor_ specifying the third node (C) to measure angle. Note that the angle to be measured is formed by vector BA and vector BC.
\- This is a required input.

### `strTarget`

\- A _String_ specifying the target projection plane (2D), or the three-dimensional space (3D) to refer to measure. This parameter can be one of the following:
\- If _strTarget="XY"_: Return the angle that will project on plane Oxy.
\- If _strTarget="YZ"_: Return the angle that will project on plane Oyz.
\- If _strTarget="ZX"_: Return the angle that will project on plane Ozx.
\- If _strTarget="Angle"_: Return the angle in 3D space.
\- If _strTarget="All"_: Return all the 4 angle values in a list, in order "Angle", "XY", "YZ", "ZX".
\- The default value is "All".

### `crCoord`

\- A _Cursor_ specifying the coordinate reference system in which the angle will refer to measure.
\- The default value is _None_.

### `iPrecision`

\- An _Integer_ specifying the number of digit after floating point. The greater `iPrecision` could be, the more accuracy of angle can be measured.
\- The default value is 6.

## Return Code

A _List of Double_ specifying the angles between 3 nodes.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube()

angle = Tools.Measure.Angle.ThreeNodes(crNode1=Node(445), 
                                       crNode2=Node(454),
                                       crNode3=Node(469), 
                                       strTarget="XY")
JPT.Debugger(angle)
```
