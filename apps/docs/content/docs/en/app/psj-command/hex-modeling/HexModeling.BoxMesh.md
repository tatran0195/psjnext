---
title: "HexModeling.BoxMesh()"
description: "Box hex mesh creator for parts"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > BoxMesh"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Box hex mesh creator for parts

## Syntax

```psj
HexModeling.BoxMesh(...)
```

## Inputs

### `ilPartIds` @type(List\[Integer]) @required

- The part ids.

### `dMeshSize` @type(Double) @required

- The mesh size.

### `strMaterialName` @type(String) @required

- The material name.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2}
Geometry.Part.Cube()
HexModeling.BoxMesh(ilPartIds=[1], dMeshSize=0.002, strMaterialName="")
```
