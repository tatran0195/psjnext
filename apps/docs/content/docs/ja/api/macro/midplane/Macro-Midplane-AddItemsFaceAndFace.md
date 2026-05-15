---
title: "AddItemsFaceAndFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add Items Edge by projecting Extend Face's Edge at the extended end of Reference Face

## Syntax

```psj
AddItemsFaceAndFace(Cursor[] Face, int Extend Type)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor \[]

Face List

<!-- @since:5.0.1 -->
### 2. Int

Extend Type \[Extend,Intersect]

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AddItemsEdgeFaceandFace([6:62, 6:51],0)
```
