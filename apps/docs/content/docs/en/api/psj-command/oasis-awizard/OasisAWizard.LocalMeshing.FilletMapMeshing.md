---
title: "OasisAWizard.LocalMeshing.FilletMapMeshing()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "OasisAWizard > LocalMeshing > FilletMapMeshing"
---

## Description

## Syntax

```psj
OasisAWizard.LocalMeshing.FilletMapMeshing(crlParts=[], crlFaces=[], dMinLength=0.0, dMaxLength=1.0, dMinRadius=0.0, dMaxRadius=9e-3, bConvex=True, bConcave=True, iTmp=0, dLengthSingleLayer=0, dBMinLengthForSingleLayer=0, dRadiusSingleLayer=0, dBMinRadiusForSingleLayer=0, iMinlayer=0, bMinLayer=False)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMinLength`

- The minimum length.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dMaxLength`

- The maximum length.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMinRadius`

- The minimum radius.

<!-- @since:5.0.1 @type:Double @optional @default:9e-3 -->
### `dMaxRadius`

- The maximum radius.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bConvex`

- The convex.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bConcave`

- The concave.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTmp`

- The temporary.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dLengthSingleLayer`

- The length single layer.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dBMinLengthForSingleLayer`

- The minimum length for single layer.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dRadiusSingleLayer`

- The radius single layer.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dBMinRadiusForSingleLayer`

- The minimum radius for single layer.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMinlayer`

- The minlayer.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMinLayer`

- The minimum layer.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
OasisAWizard.LocalMeshing.FilletMapMeshing(crlParts=[], crlFaces=[], dMinLength=0.0, dMaxLength=1.0, dMinRadius=0.0, dMaxRadius=9e-3, bConvex=True, bConcave=True, iTmp=0, dLengthSingleLayer=0, dBMinLengthForSingleLayer=0, dRadiusSingleLayer=0, dBMinRadiusForSingleLayer=0, iMinlayer=0, bMinLayer=False)
```
