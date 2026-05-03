---
title: "Home.ImportCAD.ProECreoDirect()"
description: "Import CAD - ProE Creo"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ImportCAD > ProECreoDirect"
---

## Description

This method imports an assembly from a Pro Engineer/Creo file by Direct interface into the root assembly.

## Syntax

```psj
Home.ImportCAD.ProECreoDirect(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- The list of the paths of the CAD files.

### `dChordHeightTolerance` @type(Double) @default(0.0)

- The maximum distance from the actual surface to the facet face.
  The smaller the Chord Height, the smaller the facets the more accurate the curvature of the surface is represented.

### `dAngleToleranceDegree` @type(Double) @default(0.0)

- The angle tolerance which influences the tessellation of curves with relatively small radii in comparison to the overall size of the CAD model.

### `dMaxFaceWidth` @type(Double) @default(0.1)

- The maximum value for the maximum face width used for surface tessellation.

## Return Code

A _String_ of 1 if succeed, or 0 if fail.

## Sample Code

```psj
Home.ImportCAD.ProECreoDirect(strlPaths=[JPT.GetProgramPath() + "SampleData\\CAD_Model\\ProECreoDirect_File.prt"],
    dMaxFacetWidth=100.0)
```
