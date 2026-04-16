---
id: DeleteFace
title: DeleteFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Delete Face

## Syntax

```psj
DeleteFace(int[] taFaceID, bool bKeepSolid)
```

## Inputs

### `1. Int[]`

Face ID([*]\*=Face ID)

### `2. Bool`

Keep Solid flag true=1, false=0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DeleteFace([21], 1)
```
