---
title: "DeleteFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Delete Face

## Syntax

```psj
DeleteFace(int[] taFaceID, bool bKeepSolid)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Face ID(\[\*]\*=Face ID)

<!-- @since:5.0.1 -->
### 2. Bool

Keep Solid flag true=1, false=0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DeleteFace([21], 1)
```
