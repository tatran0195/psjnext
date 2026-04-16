---
id: CreateElement
title: CreateElement()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Add Element Items from Element Edges

## Syntax

```psj
CreateElement(int Elem Type, int Parent Entity ID, int[] Node ID)
```

## Inputs

### `Int`

Element Type of Newly Created Element

### `Int`

Parent Entity ID

### `Int[]`

Target Nodes for Creating New Element

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateElement(0, 0, [187,196,205])
```
