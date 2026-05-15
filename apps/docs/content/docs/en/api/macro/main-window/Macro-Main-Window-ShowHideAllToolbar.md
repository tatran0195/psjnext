---
title: "ShowHideAllToolbar()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Show/hide the toolbar on working document.

## Syntax

```psj
ShowHideAllToolbar(int Type, bool Show)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

An Integer specifying toolbar type to be shown/hidden.

<!-- @since:5.1.0 -->
### 2. bool

A Boolean specifying whether to show/hide the toolbar.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
ShowHideAllToolbar(0, True)
```
