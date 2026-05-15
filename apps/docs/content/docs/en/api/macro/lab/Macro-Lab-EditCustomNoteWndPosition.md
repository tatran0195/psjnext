---
title: "EditCustomNoteWndPosition()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Move custom note to specified position indicated in screen coordinate system.
The position specifies center position of the note.

\*The screen coordinate system is expressed in two-dimensional coordinates with the origin (0,0) at the upper left edge of the main window.

## Syntax

```psj
EditCustomNoteWndPosition(cursor customNote, double x, double y)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

Specify the custom note to move.

<!-- @since:5.1.0 -->
### 2. double

Specify the x position by screen coordinate.

<!-- @since:5.1.0 -->
### 3. bool

Specify the y position by screen coordinate.

## Return Code

Nothing.

## Sample Code

```psj
EditCustomNoteWndPosition(270:1,100,200)
```
