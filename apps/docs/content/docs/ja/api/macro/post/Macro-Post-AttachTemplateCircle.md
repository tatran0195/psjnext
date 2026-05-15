---
title: "AttachTemplateCircle()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create a new template.

## Syntax

```psj
AttachTemplateCircle(string templateName, int ScaleMethod, float ratioModel, float ratioScreen, float ratioValue, color Highlight, color Positive, color Negative, bool UseContour, int HighlightTarget, float HighligValue1, float HighligValue2, int DisplayTarget, bool Reverse)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Template name.

<!-- @since:5.0.1 -->
### 2. int

Scale method. 0: Model size ratio, 1: Screen size ratio.

<!-- @since:5.0.1 -->
### 3. float

Value of Model size ratio.

<!-- @since:5.0.1 -->
### 4. float

Value of Screen size ratio.

<!-- @since:5.0.1 -->
### 5. float

Ratio value = 1.0,

<!-- @since:5.0.1 -->
### 6. color

Highlight color.

<!-- @since:5.0.1 -->
### 7. color

Positive color.

<!-- @since:5.0.1 -->
### 8. color

Negative color

<!-- @since:5.0.1 -->
### 9. bool

UseContour flag.

<!-- @since:5.0.1 -->
### 10 . int

Highlighting target.

<!-- @since:5.0.1 -->
### 11. float

Highlighting Value 1. Used in GREATER THAN, GREATER THAN ABS and minimum value of RANGE.

<!-- @since:5.0.1 -->
### 12. float

Highlighting Value 2. Used in maximum value of RANGE.

<!-- @since:5.0.1 -->
### 13 . int

Threshold

<!-- @since:5.0.1 -->
### 14. bool

Reverse flag.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
AttachTemplateCircle("My Template", 0, 0.03, 0.03, 1, 255, 16777215, 51400, 0, 0, 0, 1, 0, 0)
```
