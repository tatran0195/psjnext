---
title: "Analysis.ADVC.MakeProcess.DynamicExplicit()"
description: "Create an ADVC Dynamic Explicit process. This process could be created in one time or multiple times"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > ADVC > MakeProcess > DynamicExplicit"
macro_link: "[AdvcDynamicExplicitProcess](../../macro/analysis/AdvcDynamicExplicitProcess)"
---

## Description

Create an ADVC Dynamic Explicit process.
This process could be created in one time or multiple times.

## Syntax

```psj
Analysis.ADVC.MakeProcess.DynamicExplicit(...)
```

## Inputs

### `strName` @type(String) @required

- The name of the process.

### `iGeomNonlinear` @type(Integer) @default(0)

- The geometric nonlinearity type:
  - I&#x66;_&#x69;GeomNonlinear=0_, do not define the geometric nonlinearity type.
  - I&#x66;_&#x69;GeomNonlinear=1_, a Linear geometric nonlinearity is specified.
  - I&#x66;_&#x69;GeomNonlinear=2_, a Nonlinear geometric nonlinearity is specified.
  - I&#x66;_&#x69;GeomNonlinear=3_, a Total Lagrange geometric nonlinearity is specified.
  - I&#x66;_&#x69;GeomNonlinear=4_, a Updated Lagrange geometric nonlinearity is specified.

### `advcStructTimeStep` @type(ADVC\_STRUCT\_TIME\_STEP) @default(ADVC\_STRUCT\_TIME\_STEP)

- The time step settings for ADVC solver.

### `bConvergence` @type(Boolean) @default(False)

- Whether to apply the convergence parameters.

### `advcConvergence` @type(ADVC\_CONVERGENCE) @default(ADVC\_CONVERGENCE)

- The convergence settings for ADVC solver. This argument must be specified whe&#x6E;_&#x62;Convergence=True_.

### `bContact` @type(Boolean) @default(False)

- Whether to apply the contact parameters.

### `advcContactIter` @type(ADVC\_CONTACT\_ITER) @default(ADVC\_CONTACT\_ITER)

- The contact iterator settings for ADVC solver. This argument must be specified whe&#x6E;_&#x62;Contact=True_.

### `bAutoIncrement` @type(Boolean) @default(False)

- Whether to apply the auto increment parameters.

### `advcAutoIncrement` @type(ADVC\_AUTO\_INCREMENT) @default(ADVC\_AUTO\_INCREMENT)

- The auto increment settings for ADVC solver. This argument must be specified whe&#x6E;_&#x62;AutoIncrement=True_.

### `iLogMessageInterval` @type(Integer) @default(DFLT\_INT)

- The log message interval.

### `iLinearApproximation` @type(Integer) @default(-1)

- The linear approximation.

### `dBulkViscosityCoef1` @type(Double) @default(DFLT\_DBL)

- The first bulk viscosity coefficient.

### `dBulkViscosityCoef2` @type(Double) @default(DFLT\_DBL)

- The second bulk viscosity coefficient.

### `dMassScalingdt` @type(Double) @default(DFLT\_DBL)

- The mass scaling of the dt time.

### `dDtScaleFactor` @type(Double) @default(DFLT\_DBL)

- The scale factor of the dt time.

### `dPenaltyScaleFactor` @type(Double) @default(DFLT\_DBL)

- The penalty scale factor.

### `iContactSearchInterval` @type(Integer) @default(DFLT\_INT)

- The contact search interval.

### `crEdit` @type(Cursor) @default(None)

- The existing process to be modified. If the default value is specified, a new process will be created, otherwise, the specified process will modified.

### `listLoadNode` @type(List\[ADVC\_LOAD\_NODE]) @default(\[])

- The load node.
- If this argument is specified, the`listLoadCaseNode`will be empty.

### `listLoadCaseNode` @type(List\[ADVC\_LOAD\_NODE]) @default(\[])

- The loadcase node.
- If this argument is specified, the`listLoadNode`will be empty.

### `listLoadNodeContact` @type(List\[ADVC\_LOAD\_NODE]) @default(\[])

- The load node contact.
- This argument uses the instance of[ADVC\_LOAD\_NODE](./../../data-type/psj-command/parameter-types/ADVC_LOAD_NODE)and won't be duplicated with`listLoadNode`or`listLoadCaseNode`

### `ilOutputParamList` @type(List\[Integer]) @default(\[])

- The output parameters.

### `iRefType` @type(Integer) @default(-1)

- The reference type.

### `strRefPath` @type(String) @default("")

- The reference path.

### `listAdvcRefStressResult` @type(List) @default(\[])

- The advc reference stress result.

## Return Code

A _Cursor_ specifying the created or the modified ADVC Dynamic Explicit process.

## Sample Code

```psj {1,2,3,4,5,6,7}
step = Analysis.ADVC.MakeProcess.DynamicExplicit(strName="Process_0", 
                                                 iGeomNonlinear=3,
                                                 advcStructTimeStep=ADVC_STRUCT_TIME_STEP(iNumOfInc=10), 
                                                 listLoadNode=[], 
                                                 listLoadCaseNode=[],
                                                 listLoadNodeContact=[], 
                                                 listAdvcRefStressResult=[])

JPT.Debugger(step)
```
