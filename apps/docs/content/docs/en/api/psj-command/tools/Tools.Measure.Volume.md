---
title: "Tools.Measure.Volume()"
description: "Measure volume of the specified parts"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Volume"
---

## Description

Measure volume of the specified parts.

## Syntax

```psj
Tools.Measure.Volume(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part to measure volume.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The number of digit after floating point. The greater`iPrecision` could be, the more accuracy of volume can be measured.

## Return Code

A _Double_ specifying the volume value.

## Sample Code

```psj {3}
Geometry.Part.Cylinder()

volume = Tools.Measure.Volume(crlParts=[Part(1)])

JPT.Debugger(volume)
```
