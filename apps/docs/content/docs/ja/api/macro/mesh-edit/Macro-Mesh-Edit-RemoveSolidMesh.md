---
title: "RemoveSolidMesh()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Remove Solid Mesh

## Syntax

```psj
RemoveSolidMesh(cursor[] taBody, bool bConvToFirst)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target body cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Bool

Convert to First order bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
RemoveSolidMesh([3:1], 0)
```
