---
title: "CreateBar()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Bar Body

## Syntax

```psj
CreateBar(string bodyName, int meshCount, cursor startNode, cursor endNode)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Insert body name

<!-- @since:5.0.1 -->
### 2. Int

Mesh counting

<!-- @since:5.0.1 -->
### 3. Cursor

Start node cursor(10:Node ID)

<!-- @since:5.0.1 -->
### 4. Cursor

End node cursor(10:Node ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateBar("Bar _1", 7, 10:1, 10:2)
```
