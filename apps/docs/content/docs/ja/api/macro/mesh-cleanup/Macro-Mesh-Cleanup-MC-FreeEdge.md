---
title: "MC _FreeEdge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Free Edge

## Syntax

```psj
MC _FreeEdge(cursor[] crBody, int iNolayer, bool bFreeEdge, bool bcheckFreeEdge,
    bool bNonman, int iNonThres, bool bErrText)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target body cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Int

Number of layers display

<!-- @since:5.0.1 -->
### 3. Bool

Free edges bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 4. Bool

Check Free edges by Part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

Nonmanifold bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Int

Nonmanifold Threshold value

<!-- @since:5.0.1 -->
### 7. Bool

Error text bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code
