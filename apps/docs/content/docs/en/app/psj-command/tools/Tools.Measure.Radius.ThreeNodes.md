---
title: "Tools.Measure.Radius.ThreeNodes()"
description: "Measure arc radius by using 3 nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Radius > ThreeNodes"
---

## Description

Measure arc radius by using 3 nodes.

## Syntax

```psj
Tools.Measure.Radius.ThreeNodes(...)
```

## Inputs

### `crNode13` @type(Cursor) @required

- The first node on the arc whose radius is measured.

### `crNode23` @type(Cursor) @required

- The second node on the arc whose radius is measured.

### `crNode33` @type(Cursor) @required

- The third node on the arc whose radius is measured.

### `iPrecision` @type(Integer) @default(6)

- The number of digit after floating point. The greater`iPrecision`could be, the more accuracy of arc radius can be measured.

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
