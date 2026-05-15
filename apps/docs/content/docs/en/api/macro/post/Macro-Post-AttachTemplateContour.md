---
title: "AttachTemplateContour()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Attach contour setting to specific template.

## Syntax

```psj
AttachTemplateContour(string templateName, int Contour, int ContourType, int MaxMinType, float MaxUser, float MinUser, float MaxTotal, 
float MinTotal, int SpectrumType, color UpperColor, color LowerColor, color FrameColor, string strColors, int Log, bool ShowBlankValueAs0, 
bool OptimizedShape, float contours)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Template name.

<!-- @since:5.0.1 -->
### 2. int

Step number

<!-- @since:5.0.1 -->
### 3. int

ContourType

<!-- @since:5.0.1 -->
### 4. int

Max Min Type
0: Visible Entity, 1: Total Entity, 2: User Define, 3: Multiple Result

<!-- @since:5.0.1 -->
### 5. float

Maximum value.

<!-- @since:5.0.1 -->
### 6. float

Minimum value.

<!-- @since:5.0.1 -->
### 7. float

Total maximum value.

<!-- @since:5.0.1 -->
### 8. float

Total Minimum value.

<!-- @since:5.0.1 -->
### 9. int

Spectrum Type

<!-- @since:5.0.1 -->
### 10. color

Out of Maximum color

<!-- @since:5.0.1 -->
### 11. color

Out of Minimum color

<!-- @since:5.0.1 -->
### 12. color

Contour Frame Color

<!-- @since:5.0.1 -->
### 13. string

Colors

<!-- @since:5.0.1 -->
### 14. int

Log type

<!-- @since:5.0.1 -->
### 15. bool

Show blank value as 0 flag.

<!-- @since:5.0.1 -->
### 16. bool

Optimization Toolkit flag.

<!-- @since:5.0.1 -->
### 17. float \[]

Contour step value.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
AttachTemplateContour("New Template", 10, 1, 0, 0.000177567, 0, 0.000177567, 0, 2, 255, 16711680, 65535, [], 0, 0, 0, [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0])
```
