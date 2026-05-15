---
title: "ImportDirect()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import Direct

## Syntax

```psj
ImportDirect(string[] strFiles, double dChordHeightTol, double dChordAngleTol,
    bool nConvertIsolatedCurve, double dSurfacePlaneTol, double dSurfacePlaneAngle,
    double dMaxFacetWidth, double dMinFacetWidth, bool nICADFlag, int VRMLColorGroups,
    double dScale)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String\[]

Multiple CAD Files

<!-- @since:5.0.1 -->
### 2. Double

Chord Height Tolerance

<!-- @since:5.0.1 -->
### 3. Double

Chord Angle Tolerance in degree

<!-- @since:5.0.1 -->
### 4. Bool

Convert Isolated curve on or off flag true=1, false=0

<!-- @since:5.0.1 -->
### 5. Double

Surface Plane Tolerance

<!-- @since:5.0.1 -->
### 6. Double

Surface Plane Angle Tolerance in degree

<!-- @since:5.0.1 -->
### 7. Double

Max Facet width

<!-- @since:5.0.1 -->
### 8. Double

Min Facet width

<!-- @since:5.0.1 -->
### 9. Bool

iCAD flag (true=1, false=0)

<!-- @since:5.0.1 -->
### 10. Int

VRML Color groups

<!-- @since:5.0.1 -->
### 11. Double

Scale value

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportDirect(["D:/Test.x _t"], 0, 7, 0, 0, 20, 0.1, 0, 0, 0, 0.001)
```
