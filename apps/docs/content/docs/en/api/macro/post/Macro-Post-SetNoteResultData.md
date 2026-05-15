---
title: "SetNoteResultData()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set the display of result data title in the note window.

## Syntax

```psj
SetNoteResultData(int NoteResultTitle, string NoteResultTitle)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

An Integer specifying the method to display the result data title as default or user-defined name.

<!-- @since:5.1.0 -->
### 2. String

A String specifying an arbitrary user-defined name for result data title.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
SetNoteResultData(1, "Result Data")
```
