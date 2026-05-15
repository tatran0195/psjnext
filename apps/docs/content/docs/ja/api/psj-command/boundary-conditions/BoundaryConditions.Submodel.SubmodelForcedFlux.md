---
title: "BoundaryConditions.Submodel.SubmodelForcedFlux()"
description: "Create submodel forced flux"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Submodel > SubmodelForcedFlux"
---

## Description

Create submodel forced flux.

## Syntax

```psj
BoundaryConditions.Submodel.SubmodelForcedFlux(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @optional -->
### iSolver

- Specify the solver.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strFilePathName

- Specify the file path name.
- The default value is "/home/".

<!-- @since:5.0.1 @optional -->
### iProcessNo

- Specify the process no.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iReferType

- Specify the refer type.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### dExtensionRange

- Specify the extension range.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dExtensionTol

- Specify the extension tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dExtensionLimitTol

- Specify the extension limit tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### strGlobalElementSet

- Specify the global element set.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iUseBucket

- Specify the use bucket.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### iNumBucketMaxX

- Specify the number bucket maximum x.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iNumBucketMaxY

- Specify the number bucket maximum y.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iNumBucketMaxZ

- Specify the number bucket maximum z.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iPrevBc

- Specify the prev bc.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Submodel.SubmodelForcedFlux(strName, iSolver=0, strFilePathName="/home/", iProcessNo=0, iReferType=-1, dExtensionRange=DFLT _DBL, dExtensionTol=DFLT _DBL, dExtensionLimitTol=DFLT _DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT _INT, iNumBucketMaxY=DFLT _INT, iNumBucketMaxZ=DFLT _INT, iPrevBc=-1, crlTargets=[], crEdit=None)
```
