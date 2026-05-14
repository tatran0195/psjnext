---
title: "Meshing.LocalSetting.SearchTargetFaces()"
description: "Search Target Faces for Local mesh setting"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > LocalSetting > SearchTargetFaces"
macro _link: "[SearchTargetFacesInModel](../../macro/meshing/SearchTargetFacesInModel)"
---

## Description

Search Target Faces for Local mesh setting

## Syntax

```psj
Meshing.LocalSetting.SearchTargetFaces(iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1],
    dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPartType`

- The part type.

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 0, 0] -->
### `dlOrigin`

- The original.

<!-- @since:5.0.1 @type:Double List @optional @default:[0.1, 0.1, 0.1] -->
### `dlLength`

- The length.

<!-- @since:5.0.1 @type:Double List @optional @default:[0.0,0.0,0.0] -->
### `dlCenterPt`

- The center point.

<!-- @since:5.0.1 @type:Double List @optional @default:[0.0,0.0,0.1] -->
### `dlAxisPt1`

- The axis point 1.

<!-- @since:5.0.1 @type:Double List @optional @default:[0.0,0.0,0.0] -->
### `dlAxisPt2`

- The axis point 2.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bEnclosed`

- The enclosed.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Meshing.LocalSetting.SearchTargetFaces(iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1],
    dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False)
```
