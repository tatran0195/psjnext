---
title: "HexModeling.AutoSweep()"
description: "Hex Modeling Auto Sweep"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > AutoSweep"
---

## Description

Hex Modeling Auto Sweep

## Syntax

```psj
HexModeling.AutoSweep(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dMeshSize

- Specify the mesh size.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bLayers

- Specify the layers.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iLayers

- Specify the layers.
- The default value is 2.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {1}
Geometry.Part.Cube()
HexModeling.AutoSweep(crlParts=[Part(1)], dMeshSize=0.002, iLayers=5)
```
