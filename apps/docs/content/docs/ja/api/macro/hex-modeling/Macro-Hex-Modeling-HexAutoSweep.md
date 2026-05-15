---
title: "HexAutoSweep()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Automatic hex mesh creator for parts if possible

## Syntax

```psj
HexAutoSweep(int[] nPartIds, double dMeshSize, int nFlagForLayerMesh, int nLayers
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

nPartIds-specify the parts

<!-- @since:5.0.1 -->
### 2. Double

Mesh Size

<!-- @since:5.0.1 -->
### 3. Int

Flag for layer mesh (0-no layer mesh, 1-layer mesh)

<!-- @since:5.0.1 -->
### 4. Int

Total Layers

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
HexAutoSweep([1], 0.002, 1, 3)
```
