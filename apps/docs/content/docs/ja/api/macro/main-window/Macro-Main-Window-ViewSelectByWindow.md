---
title: "ViewSelectByWindow()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Select all targets in the same plane as the selected targets.

## Syntax

```psj
ViewSelectByWindow(int TargetType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

An Integer specifying the target type to be selected.

## Return Code

A Cursor List specifying the selected faces or 2D elements.

## Sample Code

```psj
ViewSelectByWindow(3)
```
