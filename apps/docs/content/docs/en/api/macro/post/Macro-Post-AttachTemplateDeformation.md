---
title: "AttachTemplateDeformation()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Attach contour setting to specific template.

## Syntax

```psj
AttachTemplateDeformation(string templateName, float DispRatioEach0, float DispRatioEach1, float DispRatioEach2, float DispRatio, int ScaleMethod, bool EachDispComp, bool ShowOriginalShade, bool ShowOriginalMesh, bool ShowOriginalEdge, color OriginalShade, color OriginalMesh, color OriginalEdge, float OriginalShadeTrans)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Template name.

<!-- @since:5.0.1 -->
### 2. float

X direction ratio

<!-- @since:5.0.1 -->
### 3. float

Y direction ratio

<!-- @since:5.0.1 -->
### 4. float

Z direction ratio

<!-- @since:5.0.1 -->
### 5. float

Ratio

<!-- @since:5.0.1 -->
### 6. int

Displacement Scale. 0:Percentage of Model Size; 1:Percentage of Result.

<!-- @since:5.0.1 -->
### 7. bool

Each direction ratio flag.

<!-- @since:5.0.1 -->
### 8. bool

Show Shade of Original Shape.

<!-- @since:5.0.1 -->
### 9. bool

Show Mesh of Original Shape.

<!-- @since:5.0.1 -->
### 10. bool

Show Edge of Original Shape.

<!-- @since:5.0.1 -->
### 11. color

Shade color of Original Shape

<!-- @since:5.0.1 -->
### 12. color

Mesh color of Original Shape.

<!-- @since:5.0.1 -->
### 13. color

Edge color of Original Shape.

<!-- @since:5.0.1 -->
### 14. float

Transparency of Original Shape.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
AttachTemplateDeformation("AllDefault", 0.07, 0.07, 0.07, 0.07, 0, 0, 0, 1, 1, 13158600, 11184810, 11184810, 0.8)
```
