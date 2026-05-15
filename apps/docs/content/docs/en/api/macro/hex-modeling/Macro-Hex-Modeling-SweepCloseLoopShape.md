---
title: "SweepCloseLoopShape()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Hex mesh by curve sweep

## Syntax

```psj
SweepCloseLoopShape(cursor crFace, cursor[] vcrEdges, cursor[] vcrRefEdges, double dMeshSize)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Target face cursor(6:Face ID)

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target edge cursor(\[5:Edge ID])

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target reference edge cursor(\[14:RefEdge ID])

<!-- @since:5.0.1 -->
### 4. Double

Mesh size value

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SweepCloseLoopShape(6:6, [5:3, 5:1, 5:2], [], 0.0001)
```
