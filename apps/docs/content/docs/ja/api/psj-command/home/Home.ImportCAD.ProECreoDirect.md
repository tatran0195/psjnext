---
title: "Home.ImportCAD.ProECreoDirect()"
description: "Import CAD - ProE Creo"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ImportCAD > ProECreoDirect"
---

## Description

This method imports an assembly from a Pro Engineer/Creo file by Direct interface into the root assembly.

## Syntax

```psj
Home.ImportCAD.ProECreoDirect(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strlPaths

- Specify the list of the paths of the CAD files.

<!-- @since:5.0.1 @optional -->
### dChordHeightTolerance

- Specify the maximum distance from the actual surface to the facet face.
  The smaller the Chord Height, the smaller the facets the more accurate the curvature of the surface is represented.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dAngleToleranceDegree

- Specify the angle tolerance which influences the tessellation of curves with relatively small radii in comparison to the overall size of the CAD model.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMaxFaceWidth

- Specify the maximum value for the maximum face width used for surface tessellation.
- The default value is 0.1.

## Return Code

A _String_ of 1 if succeed, or 0 if fail.

## Sample Code

```psj
Home.ImportCAD.ProECreoDirect(strlPaths=[JPT.GetProgramPath() + "SampleData\\CAD _Model\\ProECreoDirect _File.prt"],
    dMaxFacetWidth=100.0)
```
