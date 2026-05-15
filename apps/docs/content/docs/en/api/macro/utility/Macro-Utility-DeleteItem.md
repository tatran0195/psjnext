---
title: "DeleteItem()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Delete inticated item

## Syntax

```psj
DeleteItem(bool bModel, Cursor[] DeleteTarges, Cursor[] NA, Cusror[] NA, bool bRelated)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. bool

Delete Model.

- 0: Delete specified entities in the model only.
- 1: Delete model.

<!-- @since:5.1.0 -->
### 2. Cursor\[]

Target items to delete.

<!-- @since:5.1.0 -->
### 3. Cursor\[]

Items to be checked for deletion depending on the deletion targets.

<!-- @since:5.1.0 -->
### 4. Cursor\[]

Items where the deletion targets removed from.

<!-- @since:5.1.0 -->
### 5. bool

Delete the related item of the deletion taregets.

## Return Code

- "1": The function can be executed

## Sample Code

```psj
DeleteItem(0, [3:1], [], [], 1)
```
