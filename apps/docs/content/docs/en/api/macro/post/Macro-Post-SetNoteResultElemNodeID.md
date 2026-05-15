---
title: "SetNoteResultElemNodeID()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set the node ID or element ID of the entity to be displayed in the note window.

## Syntax

```psj
SetNoteResultElemNodeID(bool NoteResultElemNodeID, int NoteResultElemNodeID, string NoteResultElemNodeID)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. bool

A Boolean specifying whether to display the ID of Elements/Nodes in the note window.

<!-- @since:5.1.0 -->
### 2. int

An Integer specifying the method to display the Element/Node ID title as default or user-defined name.

<!-- @since:5.1.0 -->
### 3. string

A String specifying an arbitrary user-defined name for the Element/Node ID title.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
SetNoteResultElemNodeID(True, 0, "ELem/NodeID")
```
