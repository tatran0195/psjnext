---
title: "Tools.Measure.Distance.LineNode()"
description: "Measures the distance of a perpendicular line from a node toward the line defined by the two nodes."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Distance > LineNode"
---

## Description

Measures the distance of a perpendicular line from a node toward the line defined by the two nodes.

## Syntax

```psj
Tools.Measure.Distance.LineNode(crlNodes, iPrecision=6)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @required

- The target node.

### `iPrecision` @type(Integer) @default(6)

- The precision.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.LineNode(crlNodes, iPrecision=6)
```
