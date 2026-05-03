---
title: "HexModeling.AutoSweep()"
description: "Hex Modeling Auto Sweep"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > AutoSweep"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Hex Modeling Auto Sweep

## Syntax

```psj
HexModeling.AutoSweep(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `dMeshSize` @type(Double) @default(0.0)

- The mesh size.

### `bLayers` @type(Boolean) @default(False)

- The layers.

### `iLayers` @type(Integer) @default(2)

- The layers.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {1}
Geometry.Part.Cube()
HexModeling.AutoSweep(crlParts=[Part(1)], dMeshSize=0.002, iLayers=5)
```
