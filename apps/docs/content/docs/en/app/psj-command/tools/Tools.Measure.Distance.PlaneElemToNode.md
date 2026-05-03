---
title: "Tools.Measure.Distance.PlaneElemToNode()"
description: "Measure Distance between Node and plane (created by element)."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Distance > PlaneElemToNode"
---

## Description

Measure Distance between Node and plane (created by element).

## Syntax

```psj
Tools.Measure.Distance.PlaneElemToNode(crNode=None, crElem=None, iPrecision=6)
```

## Inputs

### `crNode` @type(Cursor) @default(None)

- The node.

### `crElem` @type(Cursor) @default(None)

- The element.

### `iPrecision` @type(Integer) @default(6)

- The precision.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.PlaneElemToNode(crNode=None, crElem=None, iPrecision=6)
```
