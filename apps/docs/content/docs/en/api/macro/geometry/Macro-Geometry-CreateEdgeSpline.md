---
title: "CreateEdgeSpline()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Edge Spline

## Syntax

```psj
CreateEdgeSpline(Cursor[] node _list, int arc, Cursor body _cursor, String name)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target nodes list cursor(\[10:Node ID])

<!-- @since:5.0.1 -->
### 2. Int

Arc type

- 0: Spline
- 1: Arc (3 Nodes)

<!-- @since:5.0.1 -->
### 3. Cursor

Target body cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 4. String

Bar name

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateEdgeSpline([10:455, 10:462, 10:461, 10:469, 10:468], 0, 0:0, "curve")
```
