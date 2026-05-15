---
title: "AddRib()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add Rib

## Syntax

```psj
AddRib(cursor part, cursor[] face _list, Cursor[] node _list, int width, int depth)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Part

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Face List

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Node list

<!-- @since:5.0.1 -->
### 4. Int

Rib width

<!-- @since:5.0.1 -->
### 5. Int

Rib depth

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AddRib(3:10, [6:260, 6:26], [], 10, 0)
```
