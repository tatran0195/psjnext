---
title: "SetPartAppearance()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set appearance of a part.

## Syntax

```psj
SetPartAppearance(Cursor[] tacursor, String Type, Bool Show)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

Cursor list of target entities

<!-- @since:5.1.0 -->
### 2. String

- A _String_ specifying appearance target.
  - "Surface"
  - "Mesh"
  - "Edge"
  - "Node"

<!-- @since:5.1.0 -->
### 3. Bool

-A _Boolean_ specifying Show or Hide.

- The default value is _True_ (Show).

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SetPartAppearance([3:1], "Mesh", 1)
```
