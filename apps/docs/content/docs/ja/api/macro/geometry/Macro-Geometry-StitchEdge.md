---
title: "StitchEdge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Stitch Edge

## Syntax

```psj
StitchEdge(double dTolerance, bool keepSlave, cursor[] taMaster, cursor[] taSlave)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

Tolerance for stitch (m)

<!-- @since:5.0.1 -->
### 2. Bool

Whether keep slave or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Master edge for stitch -> edge cursor(\[5:Edge ID])

<!-- @since:5.0.1 -->
### 4. Cursor\[]

Slave edge for stitch -> edge cursor(\[5:Edge ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
StitchEdge(0.0003, 1, [5:18], [5:57])
```
