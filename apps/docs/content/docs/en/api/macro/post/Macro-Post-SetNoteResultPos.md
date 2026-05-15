---
title: "SetNoteResultPos()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Sets the position label to be displayed in the notes for the positions.

## Syntax

```psj
SetNoteResultPos(bool diplay, bool useDefault, string labelName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. bool

Specify whether display position label on the notes or not.

- 0 : Do not display
- 1 : Display

<!-- @since:5.1.0 -->
### 2. bool

Specify whether use default label name or not.

- 0 : Use default label name (Pos)
- 1 : Use user defined label name

<!-- @since:5.1.0 -->
### 3. string

Specify user defined label name. It is shown if use User defined label name is selected.

## Return Code

Nothing.

## Sample Code

```psj
SetNoteResultPos(0, 0, "")
```
