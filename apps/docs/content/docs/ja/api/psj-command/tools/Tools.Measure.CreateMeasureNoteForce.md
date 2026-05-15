---
title: "Tools.Measure.CreateMeasureNoteForce()"
description: "Create a Measure Note for Measure > Force function"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > CreateMeasureNoteForce"
macro _link: "[CreateMeasureNoteForce]"
---

## Description

Create a Measure Note for Measure > Force function.

## Syntax

```psj
Tools.Measure.CreateMeasureNoteForce(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strNoteName

- Specify the name of the created note.

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify target entities.

<!-- @since:5.1.0 @optional -->
### iFontSize

- Specify font size.
- The default value is 16.

<!-- @since:5.1.0 @optional -->
### iFontColor

- Specify font color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bBold

- Specify bold type or not.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iBackgroundColor

- Specify background color.
- The default value is 16777215.

<!-- @since:5.1.0 @optional -->
### iOutlineWidth

- Specify outline width.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iOutlineColor

- Specify outline color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iArrowWidth

- Specify arrow width.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iArrowColor

- Specify arrow color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iArrowType

- Specify arrow type.
  - 0: None.
  - 1: Arrow.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iTitleType

- Specify title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.
- The default value is 1.

## Return Code

A _CursorStr_ specifying created note.

## Sample Code

```psj {4-6}
#Please load result contains force result here.
#Input IDs of nodes to measure.
n1=1
n2=2
n3=3

Tools.Measure.CreateMeasureNoteForce(
        strNoteName="Force1", 
        crlTargets=[Node(n1, n2, n3)])
```
