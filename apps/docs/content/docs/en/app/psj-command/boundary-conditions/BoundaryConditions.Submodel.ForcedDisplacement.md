---
title: "BoundaryConditions.Submodel.ForcedDisplacement()"
description: "Create a forced displacement boundary condition for node-based submodeling"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Submodel > Submodel Forced Displacement"
---

## Description

Create a forced displacement boundary condition for node-based submodeling.

## Syntax

```psj
BoundaryConditions.Submodel.ForcedDisplacement(...)
```

## Inputs

### `strName` @type(String) @default("SubmodelForcedDisplacement1")

- The new Boundary Condition name.

### `iSolver` @type(Integer) @default(0)

- The applied Solver. Possible value is 0 corresponding to ADVC solver.

### `strDataDirectory` @type(String) @default("/home/")

- The data directory name of the global model containing the model, result, and restart. It can be specified as either an absolute path or a relative path.

### `iProcessNo` @type(Integer) @default(0)

- The process number.

### `bMapX` @type(Boolean) @default(True)

- Whether to map the X translational degree of freedom.

### `bMapY` @type(Boolean) @default(True)

- Whether to map the Y translational degree of freedom.

### `bMapZ` @type(Boolean) @default(True)

- Whether to map the Z translational degree of freedom.

### `iReferType` @type(Integer) @default(0)

- The reference destination for the result directory of the global model.
  - 0: Not specified - Refers to the normal output result (dir name / result)
  - 1: Result - Refer to the normal output result (dir name / result)
  - 2: Restart - Refer to the restart output result (dir name / restart)

### `dExtensionRange` @type(Double) @default(DFLT\_DBL)

- The extension of the range in the global coordinate system. Extend the search range by range in the global coordinate system.

### `dExtensionTol` @type(Double) @default(DFLT\_DBL)

- The extension of the range in the element coordinate system. Extend the search range by tolerance in the element coordinate system. If specified value smaller tha&#x6E;_&#x64;ExtensionLimitTol_, the extension parameter in the element coordinate system i&#x73;_&#x64;ExtensionLimitTol_.

### `dExtensionLimitTol` @type(Double) @default(DFLT\_DBL)

- The Newton-Raphson iteration convergence tolerance for calculating the "global coordinates corresponding to the submodel".

### `strGlobalElementSet` @type(String) @default("")

- The element group name of the "global element containing submodel" that is known in advance.

### `iUseBucket` @type(Integer) @default(0)

- Whether to use the bucket method to speed up the search.
  - 0: Not specified - Use the bucket method
  - 1: Yes - Use the bucket method
  - 2: No - Do not use the bucket method

### `iNumBucketMaxX` @type(Integer) @default(DFLT\_INT)

- The maximum number of bucket divisions in the x-direction.

### `iNumBucketMaxY` @type(Integer) @default(DFLT\_INT)

- The maximum number of bucket divisions in the y-direction.

### `iNumBucketMaxZ` @type(Integer) @default(DFLT\_INT)

- The maximum number of bucket divisions in the z-direction.

### `iPrevBc` @type(Integer) @default(0)

- The specified boundary condition to maintain.
  - 0: Not specified
  - 1: Default Hold

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The targets to be applied. The target can be Face entities or Node entities. Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rForcedDispB&#x43;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `crForcedDispBC` @type(Cursor) @default(None)

- The existing Boundary Condition (Forced Displacement). If this argument is no&#x74;_&#x4E;one_, the specified Boundary Condition will be modified. Otherwise, a new Boundary Condition will be created. Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rForcedDispB&#x43;_&#x61;rguments are mutually exclusive. One of them must be specified.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {2}
Geometry.Part.Cube()
created_bcs = BoundaryConditions.Submodel.ForcedDisplacement(crlTargets=[Face(26)])
JPT.Debugger(created_bcs)
```
