---
title: "MeasureAreaByEntity()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure the Area

## Syntax

```psj
MeasureAreaByEntity(cursor[] entitycursor,String Target,Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

entity cursor(s)(\[\*,\*\*],\*=EntityID,\*\*=ID in Entity)

<!-- @since:5.0.1 -->
### 2. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureAreaByEntity([3:1],3)
```

or

```psj
MeasureAreaByEntity([6:24,6:23],6)
```

or

```psj
MeasureAreaByEntity([11:379],0)
```
