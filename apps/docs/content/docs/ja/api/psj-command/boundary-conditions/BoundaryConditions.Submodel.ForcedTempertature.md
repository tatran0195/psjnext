---
title: "BoundaryConditions.Submodel.ForcedTempertature()"
description: "Create a submodel by using temperature field from the coarse model and apply it to the submodel as a boundary condition to get the accurate highly-refined response in the area of interest"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Submodel > ForcedTempertature"
---

## Description

Create a submodel by using temperature field from the coarse model and apply it to the submodel as a boundary condition to get the accurate highly-refined response in the area of interest.

## Syntax

```psj
BoundaryConditions.Submodel.ForcedTempertature(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the submodel forced temperature name.
- The default value is "SubmodelForcedTemperature1".

<!-- @since:5.0.1 @optional -->
### iSolver

- Specify the solver type. Currently, there is only ADVC solver is available.
  - 0: ADVC solver.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strFilePathName

- Specify the file path name.
- The default value is "/home/".

<!-- @since:5.0.1 @optional -->
### iProcessNo

- Specify the process number of ADVC solver. The value must be greater than 0.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### iReferType

- Specify the refer type.
  - 0: Blank.
  - 1: Result.
  - 2: Restart.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dExtensionRange

- Specify the extension range value.
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
  - 0: Blank.
  - 1: Yes.
  - 2: No.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### iNumBucketMaxX

- Specify the number bucket maximum X.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iNumBucketMaxY

- Specify the number bucket maximum Y.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iNumBucketMaxZ

- Specify the number bucket maximum Z.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iPrevBc

- Specify the maintaining of the specified boundary conditions.
  - 0: Blank.
  - 1: Default hold.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target entities. The target entities could be Face or Nodes.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the cursor of boundary condition Forced Temperature need editing.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {2-4}
Geometry.Part.Cube()
created _lbc = BoundaryConditions.Submodel.ForcedTempertature(strName="SubmodelForcedTemperature1",
                                                             iReferType=-1,
                                                             crlTargets=[Face(26)])
JPT.Debugger(created _lbc)
```
