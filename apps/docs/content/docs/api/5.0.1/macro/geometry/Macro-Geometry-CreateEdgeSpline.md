---
id: CreateEdgeSpline
title: CreateEdgeSpline()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create Edge Spline

## Syntax

```psj
CreateEdgeSpline(Cursor[] node_list, int arc, Cursor body_cursor, String name)
```

## Inputs

### `1. Cursor[]`

Target nodes list cursor([10:Node ID])

### `2. Int`

Arc type

- 0: Spline
- 1: Arc (3 Nodes)

### `3. Cursor`

Target body cursor([3:Part ID])

### `4. String`

Bar name

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateEdgeSpline([10:455, 10:462, 10:461, 10:469, 10:468], 0, 0:0, "curve")
```
