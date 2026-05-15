---
title: "HexSweepCurve()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Hex mesh by curve sweep

## Syntax

```psj
HexSweepCurve(int[] nFaceIds, int[] nEdgeIds, double dMeshSize)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Face Id array for circular sweep

<!-- @since:5.0.1 -->
### 2. Int\[]

Edge Id array for circular sweep

<!-- @since:5.0.1 -->
### 3. Double

Mesh Size

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
HexSweepCurve([247], [44], 0.0001)
```
