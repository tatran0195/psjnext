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

<!-- @since:5.0.1 @type:String @optional @default:"SubmodelForcedDisplacement1" -->
### `strName`

- The new Boundary Condition name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSolver`

- The applied Solver. Possible value is 0 corresponding to ADVC solver.

<!-- @since:5.0.1 @type:String @optional @default:"/home/" -->
### `strDataDirectory`

- The data directory name of the global model containing the model, result, and restart. It can be specified as either an absolute path or a relative path.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iProcessNo`

- The process number.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bMapX`

- Whether to map the X translational degree of freedom.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bMapY`

- Whether to map the Y translational degree of freedom.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bMapZ`

- Whether to map the Z translational degree of freedom.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iReferType`

- The reference destination for the result directory of the global model.
  - 0: Not specified - Refers to the normal output result (dir name / result)
  - 1: Result - Refer to the normal output result (dir name / result)
  - 2: Restart - Refer to the restart output result (dir name / restart)

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dExtensionRange`

- The extension of the range in the global coordinate system. Extend the search range by range in the global coordinate system.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dExtensionTol`

- The extension of the range in the element coordinate system. Extend the search range by tolerance in the element coordinate system. If specified value smaller than _dExtensionLimitTol_, the extension parameter in the element coordinate system is _dExtensionLimitTol_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dExtensionLimitTol`

- The Newton-Raphson iteration convergence tolerance for calculating the "global coordinates corresponding to the submodel".

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strGlobalElementSet`

- The element group name of the "global element containing submodel" that is known in advance.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iUseBucket`

- Whether to use the bucket method to speed up the search.
  - 0: Not specified - Use the bucket method
  - 1: Yes - Use the bucket method
  - 2: No - Do not use the bucket method

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumBucketMaxX`

- The maximum number of bucket divisions in the x-direction.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumBucketMaxY`

- The maximum number of bucket divisions in the y-direction.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumBucketMaxZ`

- The maximum number of bucket divisions in the z-direction.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPrevBc`

- The specified boundary condition to maintain.
  - 0: Not specified
  - 1: Default Hold

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The targets to be applied. The target can be Face entities or Node entities. The _crlTargets_ and _crForcedDispBC_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crForcedDispBC`

- The existing Boundary Condition (Forced Displacement). If this argument is not _None_, the specified Boundary Condition will be modified. Otherwise, a new Boundary Condition will be created. The _crlTargets_ and _crForcedDispBC_ arguments are mutually exclusive. One of them must be specified.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {2}
Geometry.Part.Cube()
created _bcs = BoundaryConditions.Submodel.ForcedDisplacement(crlTargets=[Face(26)])
JPT.Debugger(created _bcs)
```
