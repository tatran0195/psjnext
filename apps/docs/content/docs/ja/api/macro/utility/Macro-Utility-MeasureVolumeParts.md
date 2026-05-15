---
title: "MeasureVolumeParts()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Measure the Volume

## Syntax

```psj
MeasureVolumeParts(cursor[] Part cursor,Integer N)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

Part cursor(s)(\[3,\*],\*=part Id)

<!-- @since:5.1.0 -->
### 2. Integer N

Specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureVolumeParts([3:1,3:2],6)
```
