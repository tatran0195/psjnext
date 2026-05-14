---
title: "Tools.Measure.Distance.PlaneElemToNode()"
description: "Measure Distance between Node and plane (created by element)."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Distance > PlaneElemToNode"
---

## Description

Measure Distance between Node and plane (created by element).

## Syntax

```psj
Tools.Measure.Distance.PlaneElemToNode(crNode=None, crElem=None, iPrecision=6)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crNode`

- The node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crElem`

- The element.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The precision.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.PlaneElemToNode(crNode=None, crElem=None, iPrecision=6)
```
