---
id: CreateBar
title: CreateBar()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create Bar Body

## Syntax

```psj
CreateBar(string bodyName, int meshCount, cursor startNode, cursor endNode)
```

## Inputs

### `1. String`

Insert body name

### `2. Int`

Mesh counting

### `3. Cursor`

Start node cursor(10:Node ID)

### `4. Cursor`

End node cursor(10:Node ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateBar("Bar_1", 7, 10:1, 10:2)
```
