---
title: "HexModeling.Sweep.Layer()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Sweep > Layer"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Layer(crlFaces=[], dFrontWidth=0.0, dBackWidth=0.0, iFrontLayers=1, iBackLayers=0, iBaseFaceType=0, iSeparate=0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFrontWidth`

- The front width.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dBackWidth`

- The back width.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iFrontLayers`

- The front layers.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBackLayers`

- The back layers.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBaseFaceType`

- The base face type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSeparate`

- The separate.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Layer(crlFaces=[], dFrontWidth=0.0, dBackWidth=0.0, iFrontLayers=1, iBackLayers=0, iBaseFaceType=0, iSeparate=0)
```
