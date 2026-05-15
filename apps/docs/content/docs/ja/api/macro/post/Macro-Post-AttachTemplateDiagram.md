---
title: "AttachTemplateDiagram()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Attach diagram setting to the specific template.

## Syntax

```psj
AttachTemplateDiagram(string templateName, int ScaleMethod, float ratioModel, float ratioScreen, color Highlight, color Positive, color Negative, bool UseContour, bool TwoSides, int HighlightTarget, float HighligValue1, float HighligValue2, int DisplayTarget)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Template name.

<!-- @since:5.0.1 -->
### 2. int

Scale Method. 0: Model size ratio, 1:Screen size ratio.

<!-- @since:5.0.1 -->
### 3. float

Model size ratio value.

<!-- @since:5.0.1 -->
### 4. float

Screen size ratio value.

<!-- @since:5.0.1 -->
### 5. color

Highlight color.

<!-- @since:5.0.1 -->
### 6. color

Positive color.

<!-- @since:5.0.1 -->
### 7. color

Negative color.

<!-- @since:5.0.1 -->
### 8. bool

Use Contour flag.

<!-- @since:5.0.1 -->
### 9. bool

Two Side flag.

<!-- @since:5.0.1 -->
### 10. int

Highlighting type

<!-- @since:5.0.1 -->
### 11. float

Highligting Value1

<!-- @since:5.0.1 -->
### 12. float

Highligting Value2

<!-- @since:5.0.1 -->
### 13. int

DisplayTarget

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
AttachTemplateDiagram("My Template", 0, 0.03, 0.03, 255, 16777215, 51400, 0, 0, 0, 1, 0)
```
