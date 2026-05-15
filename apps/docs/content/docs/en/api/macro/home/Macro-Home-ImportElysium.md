---
title: "ImportElysium()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import CAD file by Elysium interface

## Syntax

```psj
ImportElysium(string[] vecPath, double height _tol, double angle _tolerance _degree,
    double iso _cur, double iges _fixedCurevePreference, double iges _autoStitch,
    double iges _stitchTolerance, double catia _convertNotShowedElement,
    double catia _convertNotShowedInstance, double catia _convertAxis, double step _createSeam,
    double step _pointTolerance, double acis _healAcisBeforeVersion, double jt _convertGeometryType,
    double jt _convertGeneralBody, double jt _convertAxis, double jt _convertCenterLine, bool m _setFaceColor,
    double dek _cleanSelfIntersectingLoop, double point _coincident _tolerance, double dek _volumeToBody)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String\[]

Path directory

<!-- @since:5.0.1 -->
### 2. Double

Height tolerance option

<!-- @since:5.0.1 -->
### 3. Double

Angle tolerance degree option

<!-- @since:5.0.1 -->
### 4. Double

Isolated curve

<!-- @since:5.0.1 -->
### 5. Double

Iges fixedCurvePreference option

<!-- @since:5.0.1 -->
### 6. Double

Iges autoStitch option

<!-- @since:5.0.1 -->
### 7. Double

Iges stitchTolerance option

<!-- @since:5.0.1 -->
### 8. Double

Catia convertNotShowedElement option

<!-- @since:5.0.1 -->
### 9. Double

Catia convertNotShowedInstance option

<!-- @since:5.0.1 -->
### 10. Double

Catia convertAxis option

<!-- @since:5.0.1 -->
### 11. Double

Step createSeam option

<!-- @since:5.0.1 -->
### 12. Double

Step pointTolerance option

<!-- @since:5.0.1 -->
### 13. Double

Acis healAcisBeforeVersio option

<!-- @since:5.0.1 -->
### 14. Double

jt convertGeometryType option

<!-- @since:5.0.1 -->
### 15. Double

jt convertGeneralBody option

<!-- @since:5.0.1 -->
### 16. Double

jt convertAxis option

<!-- @since:5.0.1 -->
### 17. Double

jt convertCenterLine option

<!-- @since:5.0.1 -->
### 18. Bool

M\_setFaceColor option

<!-- @since:5.0.1 -->
### 19. Double

dek\_cleanSelfIntersectingLoop option

<!-- @since:5.0.1 -->
### 20. Double

Point coincident tolerance option

<!-- @since:5.0.1 -->
### 21. Double

dek\_volumToBody option

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportElysium(["D:/Test.sat"], 1, 5, 0, 0, 1, 0.1, 0, 0, 1, 1, 0, 0, 2, 1, 1, 0, 1, 2, 0.01, 4)
```
