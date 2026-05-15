---
title: "BeamMeshing()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Beam1D Meshing

## Syntax

```psj
BeamMeshing(int[] vcrCadEdgeKey, int[] vcrBarEdgeKey, int[] vcrBarBody, double dDocMeshSize, int iDocNumOfElem)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Edge cursor(\[Edge ID])

<!-- @since:5.0.1 -->
### 2. Int\[]

Bar and Edge cursor(\[BarEdge ID])

<!-- @since:5.0.1 -->
### 3. Int\[]

Bar cursor(\[Bar ID])

<!-- @since:5.0.1 -->
### 4. Double

Mesh size

<!-- @since:5.0.1 -->
### 5. Int

Number of Elements

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
BeamMeshing([], [155, 156], [5], 0, 5)
```
