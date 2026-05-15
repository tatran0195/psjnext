---
title: "BoundaryConditions.Submodel.ForcedDisplacement()"
description: "Create a forced displacement boundary condition for node-based submodeling"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Submodel > Submodel Forced Displacement"
---

## Description

Create a forced displacement boundary condition for node-based submodeling.

## Syntax

```psj
BoundaryConditions.Submodel.ForcedDisplacement(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the new Boundary Condition name.
- The default value is "SubmodelForcedDisplacement1".

<!-- @since:5.0.1 @optional -->
### iSolver

- Specify the applied Solver. Possible value is 0 corresponding to ADVC solver.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strDataDirectory

- Specify the data directory name of the global model containing the model, result, and restart. It can be specified as either an absolute path or a relative path.
- The default value is "/home/".

<!-- @since:5.0.1 @optional -->
### iProcessNo

- Specify the process number.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bMapX

- Specify whether to map the X translational degree of freedom.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bMapY

- Specify whether to map the Y translational degree of freedom.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bMapZ

- Specify whether to map the Z translational degree of freedom.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### iReferType

- Specify the reference destination for the result directory of the global model.
  - 0: Not specified - Refers to the normal output result (dir name / result)
  - 1: Result - Refer to the normal output result (dir name / result)
  - 2: Restart - Refer to the restart output result (dir name / restart)
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dExtensionRange

- Specify the extension of the range in the global coordinate system. Extend the search range by range in the global coordinate system.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dExtensionTol

- Specify the extension of the range in the element coordinate system. Extend the search range by tolerance in the element coordinate system. If specified value smaller than _dExtensionLimitTol_, the extension parameter in the element coordinate system is _dExtensionLimitTol_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dExtensionLimitTol

- Specify the Newton-Raphson iteration convergence tolerance for calculating the "global coordinates corresponding to the submodel".
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### strGlobalElementSet

- Specify the element group name of the "global element containing submodel" that is known in advance.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iUseBucket

- Specify whether to use the bucket method to speed up the search.
  - 0: Not specified - Use the bucket method
  - 1: Yes - Use the bucket method
  - 2: No - Do not use the bucket method
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iNumBucketMaxX

- Specify the maximum number of bucket divisions in the x-direction.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iNumBucketMaxY

- Specify the maximum number of bucket divisions in the y-direction.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iNumBucketMaxZ

- Specify the maximum number of bucket divisions in the z-direction.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iPrevBc

- Specify the specified boundary condition to maintain.
  - 0: Not specified
  - 1: Default Hold
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the targets to be applied. The target can be Face entities or Node entities. The _crlTargets_ and _crForcedDispBC_ arguments are mutually exclusive. One of them must be specified.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crForcedDispBC

- Specify the existing Boundary Condition (Forced Displacement). If this argument is not _None_, the specified Boundary Condition will be modified. Otherwise, a new Boundary Condition will be created. The _crlTargets_ and _crForcedDispBC_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {2}
Geometry.Part.Cube()
created _bcs = BoundaryConditions.Submodel.ForcedDisplacement(crlTargets=[Face(26)])
JPT.Debugger(created _bcs)
```
