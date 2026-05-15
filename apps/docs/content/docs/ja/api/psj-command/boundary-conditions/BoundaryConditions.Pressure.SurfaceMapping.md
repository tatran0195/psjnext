---
title: "BoundaryConditions.Pressure.SurfaceMapping()"
description: "Create mapping pressure"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > SurfaceMapping"
---

## Description

Create mapping pressure.

## Syntax

```psj
BoundaryConditions.Pressure.SurfaceMapping(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "MappingPressure".

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
### iMappedCpIndexArr

- Specify the mapped component index arr.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dScaleFactor

- Specify the scale factor.
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
### iUnit

- Specify the unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strPath

- Specify the path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Pressure.SurfaceMapping(strName="MappingPressure", crlTargets=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strPath="", crEdit=None)
```
