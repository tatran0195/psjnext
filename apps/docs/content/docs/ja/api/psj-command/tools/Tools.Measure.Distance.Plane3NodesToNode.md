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

<!-- @since:5.0.1 @required -->
### crNode1

- Specify the node1.

<!-- @since:5.0.1 @required -->
### crNode2

- Specify the node2.

<!-- @since:5.0.1 @required -->
### crNode3

- Specify the node3.

<!-- @since:5.0.1 @required -->
### crNode

- Specify the node.

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.Plane3NodesToNode(crNode1, crNode2, crNode3, crNode, iPrecision=6)
```
