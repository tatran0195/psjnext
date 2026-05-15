---
title: "Show _Entity()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Show/hide all hidden entities.

## Syntax

```psj
Show _Entity(cursor[] crlTargets, bool bShow)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor\[]

- A Cursor List specifying the target to be shown/hidden.

<!-- @since:5.1.0 -->
### 2. bool

- A Boolean specifying whether to show or hide the selected target.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
Show _Entity([164:1], 0)
```
