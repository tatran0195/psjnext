---
title: "HexModeling.Sweep.Circular()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Sweep > Circular"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Circular(crlFaces=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Double @optional @default:360 -->
### `dAngle`

- The angle.

<!-- @since:5.0.1 @type:Double @optional @default:0.0000001 -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:36 -->
### `iLayer`

- The layer.

<!-- @since:5.0.1 @type:Vector @optional @default:[0.0,0.0,0.0] -->
### `vecAxisPt`

- The axis point.

<!-- @since:5.0.1 @type:Vector @optional @default:[1.0,0.0,0.0] -->
### `vecAxisVect`

- The axis vector.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bInterfaceElem`

- The interface element.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bExtrusion`

- The extrusion.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTranslationExtrusion`

- The translation extrusion.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dBDeleteOriginalParts`

- The delete original parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Circular(crlFaces=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)
```
