---
title: "MeshCopy()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Mesh Copy

## Syntax

```psj
MeshCopy(cursor[] taFace, cursor[] taNode)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target face cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target node cursor(\[10:Node ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeshCopy([6:58, 6:22], [10:500, 10:8])
```
