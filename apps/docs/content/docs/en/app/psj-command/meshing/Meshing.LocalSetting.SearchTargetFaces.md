---
title: "Meshing.LocalSetting.SearchTargetFaces()"
description: "Search Target Faces for Local mesh setting"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalSetting > SearchTargetFaces"
macro_link: "[SearchTargetFacesInModel](../../macro/meshing/SearchTargetFacesInModel)"
---

## Description

Search Target Faces for Local mesh setting

## Syntax

```psj
Meshing.LocalSetting.SearchTargetFaces(iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1],
    dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False)
```

## Inputs

### `iPartType` @type(Integer) @default(0)

- The part type.

### `dlOrigin` @type(Double List) @default(\[0, 0, 0])

- The original.

### `dlLength` @type(Double List) @default(\[0.1, 0.1, 0.1])

- The length.

### `dlCenterPt` @type(Double List) @default(\[0.0,0.0,0.0])

- The center point.

### `dlAxisPt1` @type(Double List) @default(\[0.0,0.0,0.1])

- The axis point 1.

### `dlAxisPt2` @type(Double List) @default(\[0.0,0.0,0.0])

- The axis point 2.

### `bEnclosed` @type(Boolean) @default(False)

- The enclosed.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Meshing.LocalSetting.SearchTargetFaces(iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1],
    dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False)
```
