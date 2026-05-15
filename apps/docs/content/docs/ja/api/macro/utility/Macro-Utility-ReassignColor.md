---
title: "ReassignColor()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Change the color of the surface of each part by the color ofr Material/Property which the part has.

## Syntax

```psj
ReassignColor(int type)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

Specify reassign color type.

- "0": Surface color is set the same as Material Color.
- "1": Surface color is set the same as Property Color.
- "2": Surface color is set at random.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ReassignColor(0)
```
