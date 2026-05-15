---
title: "DoBoxMesh()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Box Mesh

## Syntax

```psj
DoBoxMesh(double size, cursor[] body, bool keep _reference)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

mesh size

<!-- @since:5.0.1 -->
### 2. Cursor\[]

body list

<!-- @since:5.0.1 -->
### 3. Bool

keep reference data 0=No 1=Yes

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DoBoxMesh(0.005, [3:1], 1)
```
