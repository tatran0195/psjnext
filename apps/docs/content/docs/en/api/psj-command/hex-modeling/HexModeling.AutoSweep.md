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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMeshSize`

- The mesh size.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bLayers`

- The layers.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iLayers`

- The layers.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {1}
Geometry.Part.Cube()
HexModeling.AutoSweep(crlParts=[Part(1)], dMeshSize=0.002, iLayers=5)
```
