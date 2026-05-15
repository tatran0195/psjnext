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

<!-- @since:5.0.1 @optional -->
### iPartType

- Specify the part type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dlOrigin

- Specify the original.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### dlLength

- Specify the length.
- The default value is \[0.1, 0.1, 0.1].

<!-- @since:5.0.1 @optional -->
### dlCenterPt

- Specify the center point.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### dlAxisPt1

- Specify the axis point 1.
- The default value is \[0.0,0.0,0.1].

<!-- @since:5.0.1 @optional -->
### dlAxisPt2

- Specify the axis point 2.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### bEnclosed

- Specify the enclosed.
- The default value is _False_.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Meshing.LocalSetting.SearchTargetFaces(iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1],
    dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False)
```
