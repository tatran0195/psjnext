---
title: "Tools.Measure.Volume()"
description: "Measure volume of the specified parts"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Volume"
---

## Description

Measure volume of the specified parts.

## Syntax

```psj
Tools.Measure.Volume(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The part to measure volume.

### `iPrecision` @type(Integer) @default(6)

- The number of digit after floating point. The greater`iPrecision`could be, the more accuracy of volume can be measured.

## Return Code

A _Double_ specifying the volume value.

## Sample Code

```psj {3}
Geometry.Part.Cylinder()

volume = Tools.Measure.Volume(crlParts=[Part(1)])

JPT.Debugger(volume)
```
