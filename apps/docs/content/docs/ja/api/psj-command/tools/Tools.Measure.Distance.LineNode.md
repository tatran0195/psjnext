---
title: "Tools.Measure.Distance.LineNode()"
description: "Measures the distance of a perpendicular line from a node toward the line defined by the two nodes."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Distance > LineNode"
---

## Description

Measures the distance of a perpendicular line from a node toward the line defined by the two nodes.

## Syntax

```psj
Tools.Measure.Distance.LineNode(crlNodes, iPrecision=6)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlNodes

- Specify the target node.

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.LineNode(crlNodes, iPrecision=6)
```
