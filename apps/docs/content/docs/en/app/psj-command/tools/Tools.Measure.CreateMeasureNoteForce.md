---
title: "Tools.Measure.CreateMeasureNoteForce()"
description: "Create a Measure Note for Measure > Force function"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > CreateMeasureNoteForce"
macro_link: "[CreateMeasureNoteForce]"
---

## Description

Create a Measure Note for Measure > Force function.

## Syntax

```psj
Tools.Measure.CreateMeasureNoteForce(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `crlTargets` @type(List\[Cursor]) @required

- Target entities.

### `iFontSize` @type(Integer) @default(16)

- Font size.

### `iFontColor` @type(Integer) @default(0)

- Font color.

### `bBold` @type(Boolean) @default(False)

- Bold type or not.

### `iBackgroundColor` @type(Integer) @default(16777215)

- Background color.

### `iOutlineWidth` @type(Integer) @default(1)

- Outline width.

### `iOutlineColor` @type(Integer) @default(0)

- Outline color.

### `iArrowWidth` @type(Integer) @default(1)

- Arrow width.

### `iArrowColor` @type(Integer) @default(0)

- Arrow color.

### `iArrowType` @type(Integer) @default(1)

- Arrow type.
  - 0: None.
  - 1: Arrow.

### `iTitleType` @type(Integer) @default(1)

- Title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.

## Return Code

A _CursorStr_ specifying created note.

## Sample Code

```psj{4-6}
#Please load result contains force result here.
#Input IDs of nodes to measure.
n1=1
n2=2
n3=3

Tools.Measure.CreateMeasureNoteForce(
        strNoteName="Force1", 
        crlTargets=[Node(n1, n2, n3)])
```
