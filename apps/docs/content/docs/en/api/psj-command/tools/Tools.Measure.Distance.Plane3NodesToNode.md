---
title: "Tools.Measure.Distance.Plane3NodesToNode()"
description: "measure the distance from node to plane(defined by 3 nodes)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Distance > Plane3NodesToNode"
---

## Description

Measure the distance from node to plane(defined by 3 nodes)

## Syntax

```psj
Tools.Measure.Distance.Plane3NodesToNode(crNode1, crNode2, crNode3, crNode, iPrecision=6)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode1`

- The node1.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode2`

- The node2.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode3`

- The node3.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode`

- The node.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The precision.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.Plane3NodesToNode(crNode1, crNode2, crNode3, crNode, iPrecision=6)
```
