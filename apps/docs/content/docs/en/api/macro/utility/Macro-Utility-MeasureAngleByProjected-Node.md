---
title: "MeasureAngleByProjected _Node()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure the angle between the node and the plane of coordinate system.

## Syntax

```psj
MeasureAngleByProjected _Node(cursor node,String Target,Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

node cursor(10:_;_=node id)

<!-- @since:5.0.1 -->
### 2. String

Target (XY or YZ or ZX or ALL)

<!-- @since:5.0.1 -->
### 3. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureAngleByProjected _Node(10:331,"XY",6)
```

or

```psj
MeasureAngleByProjected _Node(10:331,"ALL",6)
```
