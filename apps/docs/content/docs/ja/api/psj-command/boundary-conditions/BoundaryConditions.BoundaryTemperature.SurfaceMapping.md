---
title: "BoundaryConditions.BoundaryTemperature.SurfaceMapping()"
description: "Create surface mapping boundary temperature"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > BoundaryTemperature > SurfaceMapping"
---

## Description

Create surface mapping boundary temperature.

## Syntax

```psj
BoundaryConditions.BoundaryTemperature.SurfaceMapping(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the mapping temperature name.
- The default value is "MappingTemperature".

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the targets.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iMAPPos

- Specify the map position.
  - 0: MAP\_POS\_SURFACE\_NODE.
    - 1: MAP\_POS\_SOLID\_NODE.
    - 2: MAP\_POS\_SURFACE\_ELEM.
    - 3: MAP\_POS\_SOLID\_ELEM.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iViewCp

- Specify the component index that to be previewed.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCp

- Specify the component.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iSrcType

- Specify the source type of the fluid analysis solver from which the result file was output.
  - 0: Fluent.
    - 1: Star CD.
    - 2: Convection Text.
    - 3: SZText.
    - 4: ADVC.
    - 5: SubmodelBC ADVC.
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
### dScaleFactor

- Specify the scale factor.
- The default value is 1.0.

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

- Specify the coordinate scale.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dSearchRange

- Specify the search range.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iUnit

- Specify the unit.
  \- 0: degree Kenvil (K).
  - 1: degree Celsius (deg C).
  - 2: degree Fahrenheit (deg F).
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strPath

- Specify the path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the cursor of boundary condition need editing.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iMappingMethod

- Specify the mapping method.
  - 0: Mapping Nearest.
    - 1: Mapping CMLS.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSubmodeLBCMappingType

- Specify the submode load boundary condition mapping type.
  - 0: Mapping type FORCED DISPLACEMENT.
    - 1: Mapping type LOAD FORCE.
    - 2: Mapping type EMPERATURE.
    - 3: Mapping type FORCED TEMPERATURE.
    - 4: Mapping type HEAT FLUX.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### iMappingFromStepNo

- Specify the mapping from step number.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bSetADVCFile

- Specify whether set ADVC file.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### strADVCResultFile

- Specify the ADVC result file.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### bSetDetATol

- Specify whether set det a tolerance.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dDetATol

- Specify the det a tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### bSetElementSet

- Specify whether set element set.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### strElementSet

- Specify the element set.
- The default value is "all".

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
result = BoundaryConditions.BoundaryTemperature.SurfaceMapping(strName="MappingTemperature",
        crlTargets=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0,
        iMappedCpIndexArr1=0, dScaleFactor=1.0, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1.0,
        dSearchRange=0.0, iUnit=0, strPath="", crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=3,
        iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False,
        dDetATol=DFLT _DBL, bSetElementSet=False, strElementSet="all")
        
print(result) #for checking return value
```
