---
title: "CmdPostVectorSettings()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Vector setting.

## Syntax

```psj
CmdPostVectorSettings(int ScaleMethod, float ratioModel, float ratioScreen, float ratioValue, bool UseArrow, color Highlight, color Positive, color Negative, bool UseContour, int HighlightTarget, float HighligValue1, float HighligValue2, int DisplayTarget, bool Reverse, bool AllModelVector, int ThresholdOpt, float ThresholdValue, float ThresholdValueMax, int ComparisonOpt, bool AllSameLength)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Scale Method. 0: Model size ratio, 1: Screen size ratio.

<!-- @since:5.0.1 -->
### 2. float

Model size ratio value.

<!-- @since:5.0.1 -->
### 3. float

Screen size ratio value.

<!-- @since:5.0.1 -->
### 4. float

Ratio value.

<!-- @since:5.0.1 -->
### 5. bool

Use Arrow flag.

<!-- @since:5.0.1 -->
### 6. color

Highlight color.

<!-- @since:5.0.1 -->
### 7. color

Positive color.

<!-- @since:5.0.1 -->
### 8. color

Negative color.

<!-- @since:5.0.1 -->
### 9. bool

Use Contour flag.

<!-- @since:5.0.1 -->
### 10. int

Highlighting target.

<!-- @since:5.0.1 -->
### 11. float

Highlight Value1,

<!-- @since:5.0.1 -->
### 12. float

Highlight Value2,

<!-- @since:5.0.1 -->
### 13. int

Display Target.

<!-- @since:5.0.1 -->
### 14. bool

Reverse flag.

<!-- @since:5.0.1 -->
### 15. bool

All Model Vector flag.

<!-- @since:5.0.1 -->
### 16. int

Threshold target.

<!-- @since:5.0.1 -->
### 17. float

Threshold Value.

<!-- @since:5.0.1 -->
### 18. float

Threshold Value Max.

<!-- @since:5.0.1 -->
### 19. int

Comparison Opt

<!-- @since:5.0.1 -->
### 20. bool

All in the same length.

## Return Code

Nothing.

## Sample Code

```psj
CmdPostVectorSettings(0, 0.03, 0.03, 1, 1, 255, 16777215, 51400, 0, 0, 0, 1, 0, 0, 0, 0, 0, 100, 0, 0)
```
