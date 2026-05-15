---
title: "CreateElement()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add Element Items from Element Edges

## Syntax

```psj
CreateElement(int Elem Type, int Parent Entity ID, int[] Node ID)
```

## Inputs

<!-- @since:5.0.1 -->
### Int

Element Type of Newly Created Element

<!-- @since:5.0.1 -->
### Int

Parent Entity ID

<!-- @since:5.0.1 -->
### Int\[]

Target Nodes for Creating New Element

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateElement(0, 0, [187,196,205])
```
