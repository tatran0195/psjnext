---
title: "ExportVTFxFile()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export the VTFX file.

## Syntax

```psj
ExportVTFxFile(str strPath, int iModelType, bool bExcludeBarPart, bool bSurfaceElementOnly, int iData2D, list lSelectedResults, bool bDisplayPostAddTrescaStress, int iCurUnitLength, int iCurUnitTime, int iCurUnitMass, int iCurUnitForce, int iCurUnitAngle, int iCurUnitTemperature, bool bSetDefaultResult)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A string specifying the path to the VTFX file.

<!-- @since:5.1.0 -->
### 2. int

- An integer specifying the model type.

<!-- @since:5.1.0 -->
### 3. bool

- A boolean specifying whether to exclude bar parts.

<!-- @since:5.1.0 -->
### 4. bool

- A boolean specifying whether to include only surface elements.

<!-- @since:5.1.0 -->
### 5. int

- An integer specifying the data type for 2D data.

<!-- @since:5.1.0 -->
### 6. list

- A list of selected results to be included in the export.

<!-- @since:5.1.0 -->
### 7. bool

- A boolean specifying whether to display post-processed Tresca stress.

<!-- @since:5.1.0 -->
### 8. int

- An integer specifying the current unit for length.

<!-- @since:5.1.0 -->
### 9. int

- An integer specifying the current unit for time.

<!-- @since:5.1.0 -->
### 10. int

- An integer specifying the current unit for mass.

<!-- @since:5.1.0 -->
### 11. int

- An integer specifying the current unit for force.

<!-- @since:5.1.0 -->
### 12. int

- An integer specifying the current unit for angle.

<!-- @since:5.1.0 -->
### 13. int

- An integer specifying the current unit for temperature.

<!-- @since:5.1.0 -->
### 14. bool

A boolean specifying whether to set the default result for the exported file.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ExportVTFxFile("path/to/the/file", 1, 0, 0, 0, [], 0, 0, 0, 0, 0, 1, 1, 0)
```
