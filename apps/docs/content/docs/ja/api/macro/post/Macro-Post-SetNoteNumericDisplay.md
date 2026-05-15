---
title: "SetNoteNumericDisplay()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set numeric display of notes.

## Syntax

```psj
SetNoteNumericDisplay(bool type, int width, int precision)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. bool

Type of numeric display.

- 0: Real type.
- 1: Power type.

<!-- @since:5.1.0 -->
### 2. int

Specify numeric width.

<!-- @since:5.1.0 -->
### 2. int

Specify numeric precision.

## Return Code

Nothing.

## Sample Code

```psj
SetNoteNumericDisplay(0, 10, 5)
```
