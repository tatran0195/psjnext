---
title: "Assemble _Faces _MatingStep()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Find mating faces

## Syntax

```psj
Assemble _Faces _MatingStep(cursor[] face _id _master _list, cursor[] face _id _slave _list, cursor[] body _id _list, double tol)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

List ID master faces. Empty is okay

<!-- @since:5.0.1 -->
### 2. Cursor\[]

List ID slave faces. Empty is okay

<!-- @since:5.0.1 -->
### 3. Cursor\[]

List ID bodies. Empty is okay

<!-- @since:5.0.1 -->
### 4. Double

Tolerance to find mating faces

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Assemble _Faces _MatingStep([6:50, 6:47], [6:23, 6:21], [3:1, 3:2], 0.00022222)
```
