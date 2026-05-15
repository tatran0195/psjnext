---
title: "ViewSelectByFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Select all targets in the same plane as the selected targets.

## Syntax

```psj
ViewSelectByFace(int TargetType, cursor[] Targets)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

An Integer specifying the target type to be selected.

<!-- @since:5.1.0 -->
### 2. Cursor\[]

A Cursor List specifying the targets to select other targets in the same plane as them.

## Return Code

A Cursor List specifying the selected parts (faces or 2D elements).

## Sample Code

```psj
ViewSelectByFace(3,[])
```
