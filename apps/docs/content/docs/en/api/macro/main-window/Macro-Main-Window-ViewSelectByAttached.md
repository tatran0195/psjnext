---
title: "ViewSelectByAttached()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Invert hide targets by context menu.

## Syntax

```psj
ViewSelectByAttached(int TargetType, cursor[] Targets)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

An Integer specifying the target type to be selected.

<!-- @since:5.1.0 -->
### 2. Cursor\[]

A List of Cursor specifying the targets to select the attached ones from them.

## Return Code

A Cursor List specifying the selected parts (faces or 2D elements).

## Sample Code

```psj
ViewSelectByAttached(3,[])
```
