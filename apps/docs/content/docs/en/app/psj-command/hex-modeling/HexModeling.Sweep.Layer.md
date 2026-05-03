---
title: "HexModeling.Sweep.Layer()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > Sweep > Layer"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Layer(crlFaces=[], dFrontWidth=0.0, dBackWidth=0.0, iFrontLayers=1, iBackLayers=0, iBaseFaceType=0, iSeparate=0)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `dFrontWidth` @type(Double) @default(0.0)

- The front width.

### `dBackWidth` @type(Double) @default(0.0)

- The back width.

### `iFrontLayers` @type(Integer) @default(1)

- The front layers.

### `iBackLayers` @type(Integer) @default(0)

- The back layers.

### `iBaseFaceType` @type(Integer) @default(0)

- The base face type.

### `iSeparate` @type(Integer) @default(0)

- The separate.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Layer(crlFaces=[], dFrontWidth=0.0, dBackWidth=0.0, iFrontLayers=1, iBackLayers=0, iBaseFaceType=0, iSeparate=0)
```
