---
title: "MeasureDistanceByEdge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure the edge length

## Syntax

```psj
MeasureDistanceByEdge(cursor edge,Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

edge cursor(5:_,_=edge id)

<!-- @since:5.0.1 -->
### 2. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureDistanceByEdge(5:18,6)
```
