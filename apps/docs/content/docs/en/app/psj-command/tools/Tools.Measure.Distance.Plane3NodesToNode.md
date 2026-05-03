---
title: "Tools.Measure.Distance.Plane3NodesToNode()"
description: "measure the distance from node to plane(defined by 3 nodes)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Distance > Plane3NodesToNode"
---

## Description

Measure the distance from node to plane(defined by 3 nodes)

## Syntax

```psj
Tools.Measure.Distance.Plane3NodesToNode(crNode1, crNode2, crNode3, crNode, iPrecision=6)
```

## Inputs

### `crNode1` @type(Cursor) @required

- The node1.

### `crNode2` @type(Cursor) @required

- The node2.

### `crNode3` @type(Cursor) @required

- The node3.

### `crNode` @type(Cursor) @required

- The node.

### `iPrecision` @type(Integer) @default(6)

- The precision.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.Plane3NodesToNode(crNode1, crNode2, crNode3, crNode, iPrecision=6)
```
