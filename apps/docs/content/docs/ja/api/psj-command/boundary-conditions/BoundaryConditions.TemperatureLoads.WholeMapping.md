---
title: "BoundaryConditions.TemperatureLoads.WholeMapping()"
description: "Map temperagure load from solver data or csv."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > WholeMapping"
---

## Description

Map temperagure load from solver data or csv.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.WholeMapping(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "TemperatureLoadsWholeMapping".

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iMAPPos

- Specify the m a p position.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iViewCp

- Specify the view component.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCp

- Specify the component.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iSrcType

- Specify the source type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMappedCpIndexArr0

- Specify the mapped component index arr0.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMappedCpIndexArr1

- Specify the mapped component index arr1.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDScaleFactor

- Specify the d scale factor.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### posOffset

- Specify the offset.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### posRotate

- Specify the rotate.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dCorScale

- Specify the cor scale.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dSearchRange

- Specify the search range.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strPath

- Specify the path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iMappingMethod

- Specify the mapping method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSubmodelBCMappingType

- Specify the submodel c mapping type.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### iMappingFromStepNo

- Specify the mapping from step no.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bSetADVCFile

- Specify the set ADVC file.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### strADVCResultFile

- Specify the ADVC result file.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### bSetDetATol

- Specify the set det a tolerance.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dDetATol

- Specify the det a tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### bSetElementSet

- Specify the set element set.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### strElementSet

- Specify the element set.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### iTemperature

- Specify the unit of temperature.
  - 0: K
  - 1: deg C
  - 2: deg F
- The default value is 1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```pj {8-11}
# Put solver data that includes temperature data.
mapping _data _file = "C:/Temp/sol159.op2"

# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

# Map temperature load
BoundaryConditions.TemperatureLoads.WholeMapping(
    strName = "TemperatureLoadsWholeMapping _1", 
    strPath = mapping _data _file, 
    iMappingFromStepNo = 0)
```
