---
title: "ViewSelectDisplayed()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Select all targets of the same type as the specified target that are displayed in the current document.

## Syntax

```psj
ViewSelectDisplayed(int TargetType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

An Integer specifying the target type to be selected.

## Return Code

A List of Cursor specifying the selected faces or 2D elements.

## Sample Code

```psj
ViewSelectDisplayed(3)
```
