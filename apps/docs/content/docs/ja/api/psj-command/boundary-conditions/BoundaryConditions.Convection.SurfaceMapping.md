---
title: "BoundaryConditions.Convection.SurfaceMapping()"
description: "Create load boundary condition of convection surface mapping"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Convection > SurfaceMapping"
---

## Description

Create load boundary condition of convection surface mapping.

## Syntax

```psj
BoundaryConditions.Convection.SurfaceMapping(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the Mapping Convection name.
- The default value is "MappingConvection\_1".

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the targets.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iPos

- Specify the MAP position.
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
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSrcType

- Specify the source type of the fluid analysis solver from which the result file was output.
  - 0: Fluent.
    - 1: Star CD.
    - 2: CSV.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMappedCpIndex0

- Specify the mapped component index0.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMappedCpIndex1

- Specify the mapped component index1.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dRScale

- Specify the rotation scale.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### posOffset

- Specify the offset.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### posAxis

- Specify the axis.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dTScale

- Specify the translation scale.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dSearchRange

- Specify the search range.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iHTCUnit

- Specify the HTC unit.
  - 0: mW/mm^2.
  - 1: W/mm^2.
  - 2: miuW/mm^2.
  - 3: lcal/mm^2\*h.
  - 4: lbf/ft\*s.
  - 5: lbf/in\*s.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iTempUnit

- Specify the temperature unit.
  - 0: degree Kenvil (K).
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

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
result = BoundaryConditions.Convection.SurfaceMapping(strName="MappingConvection _5",
    crlTargets=[], iPos=0, iViewCp=0, iCp=0, iSrcType=0, iMappedCpIndex0=0,
    iMappedCpIndex1=0, dRScale=1.0, posOffset=[0,0,0], posAxis=[0,0,0], dTScale=1.0,
    dSearchRange=1.0, iHTCUnit=0, iTempUnit=0, strPath="", crEdit=None)

print(result) #for checking return value
```
