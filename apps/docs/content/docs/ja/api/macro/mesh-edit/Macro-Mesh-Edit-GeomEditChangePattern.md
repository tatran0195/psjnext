---
title: "GeomEditChangePattern()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Change Pattern

## Syntax

```psj
GeomEditChangePattern(int[] Face Key, int Pattern Type)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Target Faces for Change Pattern

<!-- @since:5.0.1 -->
### 2. Int

Change Pattern Type\[Standard/Union Jack]

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeomEditChangePattern([24, 26], 1))
```
