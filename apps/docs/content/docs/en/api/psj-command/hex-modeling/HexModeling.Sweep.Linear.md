---
title: "HexModeling.Sweep.Linear()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Sweep > Linear"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Linear(crlFaces=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Double @optional @default:10 -->
### `dLength`

- The length.

<!-- @since:5.0.1 @type:Integer @optional @default:10 -->
### `iLayer`

- The layer.

<!-- @since:5.0.1 @type:Double List @optional @default:[] -->
### `dlSweepDirection`

- The sweep direction.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bInterfaceElemFlag`

- The interface element flag.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLinearMethod`

- The linear method.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDeleteOriginalParts`

- The delete original parts.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDeleteTargetParts`

- The delete target parts.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethodBias`

- The method bias.

<!-- @since:5.0.1 @type:Double @optional @default:2.0 -->
### `dFactor`

- The factor.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iProgression`

- The progression.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Linear(crlFaces=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)
```
