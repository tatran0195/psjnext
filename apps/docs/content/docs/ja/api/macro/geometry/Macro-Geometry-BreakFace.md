---
title: "BreakFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Break selected face

## Syntax

```psj
BreakFace(Cursor[] FACE Cursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target face cursor(\[6:Face ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
BreakFace([6:64, 6:537, 6:531, 6:534])
```
