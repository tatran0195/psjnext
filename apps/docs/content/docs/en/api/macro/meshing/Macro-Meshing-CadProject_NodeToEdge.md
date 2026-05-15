---
title: "CadProject _NodeToEdge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Project nodes in Meshed Nodes toward a CAD Edge

## Syntax

```psj
CadProject _NodeToFace(cursor taCadEdge, cursor[] taNodes, int Direction)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Target reference CAD Edge (14:RefFace ID)

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target nodes (\[10:Node IDs])

<!-- @since:5.0.1 -->
### 3. int

Direction Min=0, X=1, Y=2, Z=3, -X=4, -Y=5, -Z=6

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CadProject _NodeToEdge(14:2, [10:378, 10:377, 10:376], 0)
```
