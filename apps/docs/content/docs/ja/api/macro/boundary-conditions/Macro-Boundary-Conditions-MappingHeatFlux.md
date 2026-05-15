---
title: "MappingHeatFlux()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create mapping pressure

## Syntax

```psj
MappingHeatFlux(string strName, cursor[] taTarget, int pos, int iViewCp, int iCp,
    int iSrcType, int iMappedCpIndexArr0, double dScaleFactor, cursor[] crTrans,
    cursor[] crRotate, double dCoordScale, double dSearchTol, int iUnit,
    string strPath, cursor crEdit, int iMappingMethod, int submodelBCMappingType,
    int iMappingFromStepNo, bool bSetADVCFile, string strADVCResultFile, bool bSetDetATol,
    double dDetATol, bool bSetElementSet, string strElementSet)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Mapping heat flux name

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 -->
### 3. Int

Mapping positon

- 0: Surface node
- 1: Solid node
- 2:surface element
- 3: Solid element

<!-- @since:5.0.1 -->
### 4. Int

View Heat flux

<!-- @since:5.0.1 -->
### 5. Int

N/A

<!-- @since:5.0.1 -->
### 6. Int

Source data type

- 0: Fluent
- 1: StarCD

<!-- @since:5.0.1 -->
### 7. Int

Heat flux data index in file

<!-- @since:5.0.1 -->
### 8. Double

Scale factor value

<!-- @since:5.0.1 -->
### 9. Cursor\[]

Translation X Y Z direction value

<!-- @since:5.0.1 -->
### 10. Cursor\[]

Rotation X Y Z direction value

<!-- @since:5.0.1 -->
### 11. Double

Coordinate scale value

<!-- @since:5.0.1 -->
### 12. Double

Search range tolerance

<!-- @since:5.0.1 -->
### 13. Int

Input unit type

- 0: MW/mm^2
- 1: W/m^2
- 2: MiuW/mm^2
- 3: kcal/mm^2\*h
- 4: Lbf/ft\*s
- 5: Lbf/in\*s

<!-- @since:5.0.1 -->
### 14. String

directory path name

<!-- @since:5.0.1 -->
### 15. Cursor

Edit cursor

<!-- @since:5.0.1 -->
### 16. Int

Mapping method

<!-- @since:5.0.1 -->
### 17. Int

Submodel IBC mapping type

<!-- @since:5.0.1 -->
### 18. Int

Mapping from step

<!-- @since:5.0.1 -->
### 19. Bool

Set ADVC file bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 20. String

N/A ADVC result file

<!-- @since:5.0.1 -->
### 21. Bool

N/A Set tolerance bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 22. Double

N/A set tolerance

<!-- @since:5.0.1 -->
### 23. Bool

Set element

<!-- @since:5.0.1 -->
### 24. String

Element set

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MappingHeatFlux("MappingHeatFlux1", [3:1], 2, 0, 1, 0, 0, 1.5, [4, 5, 6], [1, 2, 3], 0.5,
    0.003, 0, "D:/Fluent.dat", 0:0, 1, 0, 0, 0, "", 0, 1e-08, 0, "all")
```
