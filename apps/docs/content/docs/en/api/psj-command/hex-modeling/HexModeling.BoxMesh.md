---
title: "HexModeling.BoxMesh()"
description: "Box hex mesh creator for parts"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > BoxMesh"
---

## Description

Box hex mesh creator for parts

## Syntax

```psj
HexModeling.BoxMesh(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Integer] @required -->
### `ilPartIds`

- The part ids.

<!-- @since:5.0.1 @type:Double @required -->
### `dMeshSize`

- The mesh size.

<!-- @since:5.0.1 @type:String @required -->
### `strMaterialName`

- The material name.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2}
Geometry.Part.Cube()
HexModeling.BoxMesh(ilPartIds=[1], dMeshSize=0.002, strMaterialName="")
```
