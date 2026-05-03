---
title: "HexModeling.Sweep.Linear()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > Sweep > Linear"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Linear(crlFaces=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `dLength` @type(Double) @default(10)

- The length.

### `iLayer` @type(Integer) @default(10)

- The layer.

### `dlSweepDirection` @type(Double List) @default(\[])

- The sweep direction.

### `bInterfaceElemFlag` @type(Boolean) @default(False)

- The interface element flag.

### `iLinearMethod` @type(Integer) @default(0)

- The linear method.

### `bDeleteOriginalParts` @type(Boolean) @default(False)

- The delete original parts.

### `bDeleteTargetParts` @type(Boolean) @default(False)

- The delete target parts.

### `iMethodBias` @type(Integer) @default(0)

- The method bias.

### `dFactor` @type(Double) @default(2.0)

- The factor.

### `iProgression` @type(Integer) @default(0)

- The progression.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Linear(crlFaces=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)
```
