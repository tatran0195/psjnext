---
title: "ToPre()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Convert Post document to Pre document.

## Syntax

```psj
ToPre(string docName, int[] options)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

The name of target document to convert.

<!-- @since:5.1.0 -->
### 2. int \[]

The option corresponding to the number specified in the list is turned on.

- 0: Takes over Groups
- 1: Takes over Boundary Conditions
- 2: Takes over Connections
- 3: Takes over Local Coordinates
- 4: Takes over Properties

## Return Code

Nothing.

## Sample Code

```psj
ToPre("Jupiter1", [0, 1, 2, 3, 4])
```
