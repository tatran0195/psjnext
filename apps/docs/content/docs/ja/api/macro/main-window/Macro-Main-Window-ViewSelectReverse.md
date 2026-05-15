---
title: "ViewSelectReverse()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Select all targets of the same type as the specified target that are displayed in the current document.

## Syntax

```psj
ViewSelectReverse(int TargetType, cursor[] Targets)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

An Integer specifying the target type to be selected.

<!-- @since:5.1.0 -->
### 2. Cursor\[]

A Cursor List specifying the targets.

## Return Code

A List of Cursor specifying the selected entities in revert.

## Sample Code

```psj
ViewSelectReverse(3,[])
```
