---
title: "CreateEdgeByElemEdge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Edge By Element Edge

## Syntax

```psj
CreateEdgeByElemEdge(ElemEdge[] elem _edge,bool break _face)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. ElemEdge\[]

Select (multiple) element edges cursor(\[10:Node ID-10:Node ID])

<!-- @since:5.0.1 -->
### 2. Bool

Whether break edge or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateEdgeByElemEdge([10:59-10:227, 10:219-10:227, 10:211-10:219, 10:203-10:211], 1)
```
