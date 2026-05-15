---
title: "SetNoteResultTitle()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Sets the data label to be displayed in the notes.
Also, set whether display labels in the notes or not.

## Syntax

```psj
SetNoteResultTitle(bool diplay, bool useDefault, string labelName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. bool

Specify whether display labels on the notes or not.

- 0 : Do not display
- 1 : Display

<!-- @since:5.1.0 -->
### 2. bool

Specify whether use default label name for data or not.

- 0 : Use default label name (Data)
- 1 : Use user defined label name

<!-- @since:5.1.0 -->
### 3. string

Specify user defined label name for data. It is shown if use User defined label name is selected.

## Return Code

Nothing.

## Sample Code

```psj
SetNoteResultTitle(1, 0, ")
```
