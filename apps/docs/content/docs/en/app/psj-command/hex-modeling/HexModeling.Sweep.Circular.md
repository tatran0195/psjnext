---
title: "HexModeling.Sweep.Circular()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > Sweep > Circular"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Circular(crlFaces=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `dAngle` @type(Double) @default(360)

- The angle.

### `dTol` @type(Double) @default(0.0000001)

- The tolerance.

### `iLayer` @type(Integer) @default(36)

- The layer.

### `vecAxisPt` @type(Vector) @default(\[0.0,0.0,0.0])

- The axis point.

### `vecAxisVect` @type(Vector) @default(\[1.0,0.0,0.0])

- The axis vector.

### `bInterfaceElem` @type(Boolean) @default(False)

- The interface element.

### `bExtrusion` @type(Boolean) @default(False)

- The extrusion.

### `dTranslationExtrusion` @type(Double) @default(0.0)

- The translation extrusion.

### `dBDeleteOriginalParts` @type(Double) @default(0.0)

- The delete original parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Circular(crlFaces=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)
```
