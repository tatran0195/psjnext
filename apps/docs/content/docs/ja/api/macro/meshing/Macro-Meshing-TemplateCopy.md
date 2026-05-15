---
title: "TemplateCopy()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Template Copy (include Window to Window)

## Syntax

```psj
TemplateCopy(cursor[] entityMaster, cursor[] entitySlave, int iMethod, bool bCopySub, double dTolerance)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target entity master cursor(\[CursorType:CursorType ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target entity slave cursor(\[CursorType:CursorType ID])

<!-- @since:5.0.1 -->
### 3. Int

Copy settings method

- 0: By Shape
- 1: By Topology

<!-- @since:5.0.1 -->
### 4. Bool

Include sub entity bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Double

Tolerance (m)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
TemplateCopy([3:1], [3:2], 0, 1, 1e-06)
```
