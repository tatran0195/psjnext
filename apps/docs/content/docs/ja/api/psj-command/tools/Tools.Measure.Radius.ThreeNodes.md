---
title: "Tools.Measure.Radius.ThreeNodes()"
description: "Measure arc radius by using 3 nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Radius > ThreeNodes"
---

## Description

Measure arc radius by using 3 nodes.

## Syntax

```psj
Tools.Measure.Radius.ThreeNodes(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crNode13

- Specify the first node on the arc whose radius is measured.

<!-- @since:5.0.1 @required -->
### crNode23

- Specify the second node on the arc whose radius is measured.

<!-- @since:5.0.1 @required -->
### crNode33

- Specify the third node on the arc whose radius is measured.

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the number of digit after floating point. The greater`iPrecision` could be, the more accuracy of arc radius can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the arc radius value.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cylinder()

radius = Tools.Measure.Radius.ThreeNodes(crNode13=Node(18), 
                                         crNode23=Node(14), 
                                         crNode33=Node(8))

JPT.Debugger(radius)
```
