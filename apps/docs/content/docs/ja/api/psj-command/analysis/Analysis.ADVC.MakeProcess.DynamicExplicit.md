---
title: "Analysis.ADVC.MakeProcess.DynamicExplicit()"
description: "Create an ADVC Dynamic Explicit process. This process could be created in one time or multiple times"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > MakeProcess > DynamicExplicit"
macro _link: "[AdvcDynamicExplicitProcess](../../macro/analysis/AdvcDynamicExplicitProcess)"
---

## Description

Create an ADVC Dynamic Explicit process.
This process could be created in one time or multiple times.

## Syntax

```psj
Analysis.ADVC.MakeProcess.DynamicExplicit(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name of the process.

<!-- @since:5.0.1 @optional -->
### iGeomNonlinear

- Specify the geometric nonlinearity type:
  - If _iGeomNonlinear=0_, do not define the geometric nonlinearity type.
  - If _iGeomNonlinear=1_, a Linear geometric nonlinearity is specified.
  - If _iGeomNonlinear=2_, a Nonlinear geometric nonlinearity is specified.
  - If _iGeomNonlinear=3_, a Total Lagrange geometric nonlinearity is specified.
  - If _iGeomNonlinear=4_, a Updated Lagrange geometric nonlinearity is specified.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### advcStructTimeStep

- Specify the time step settings for ADVC solver.
- The default value is _[ADVC\_STRUCT\_TIME\_STEP](./../../data-type/psj-command/parameter-types/ADVC _STRUCT _TIME _STEP)_.

<!-- @since:5.0.1 @optional -->
### bConvergence

- Specify whether to apply the convergence parameters.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcConvergence

- Specify the convergence settings for ADVC solver. This argument must be specified when _bConvergence=True_.
- The default value is _[ADVC\_CONVERGENCE](./../../data-type/psj-command/parameter-types/ADVC _CONVERGENCE)_.

<!-- @since:5.0.1 @optional -->
### bContact

- Specify whether to apply the contact parameters.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcContactIter

- Specify the contact iterator settings for ADVC solver. This argument must be specified when _bContact=True_.
- The default value is _[ADVC\_CONTACT\_ITER](./../../data-type/psj-command/parameter-types/ADVC _CONTACT _ITER)_.

<!-- @since:5.0.1 @optional -->
### bAutoIncrement

- Specify whether to apply the auto increment parameters.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcAutoIncrement

- Specify the auto increment settings for ADVC solver. This argument must be specified when _bAutoIncrement=True_.
- The default value is _[ADVC\_AUTO\_INCREMENT](./../../data-type/psj-command/parameter-types/ADVC _AUTO _INCREMENT)_.

<!-- @since:5.0.1 @optional -->
### iLogMessageInterval

- Specify the log message interval.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iLinearApproximation

- Specify the linear approximation.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### dBulkViscosityCoef1

- Specify the first bulk viscosity coefficient.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dBulkViscosityCoef2

- Specify the second bulk viscosity coefficient.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMassScalingdt

- Specify the mass scaling of the dt time.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDtScaleFactor

- Specify the scale factor of the dt time.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dPenaltyScaleFactor

- Specify the penalty scale factor.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iContactSearchInterval

- Specify the contact search interval.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the existing process to be modified. If the default value is specified, a new process will be created, otherwise, the specified process will modified.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### listLoadNode

- Specify the load node.
- If this argument is specified, the `listLoadCaseNode` will be empty.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadCaseNode

- Specify the loadcase node.
- If this argument is specified, the `listLoadNode` will be empty.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadNodeContact

- Specify the load node contact.
- This argument uses the instance of [ADVC\_LOAD\_NODE](./../../data-type/psj-command/parameter-types/ADVC _LOAD _NODE) and won't be duplicated with `listLoadNode` or `listLoadCaseNode`
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilOutputParamList

- Specify the output parameters.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iRefType

- Specify the reference type.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### strRefPath

- Specify the reference path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### listAdvcRefStressResult

- Specify the advc reference stress result.
- The default value is \[].

## Return Code

A _Cursor_ specifying the created or the modified ADVC Dynamic Explicit process.

## Sample Code

```psj {1,2,3,4,5,6,7}
step = Analysis.ADVC.MakeProcess.DynamicExplicit(strName="Process _0", 
                                                 iGeomNonlinear=3,
                                                 advcStructTimeStep=ADVC _STRUCT _TIME _STEP(iNumOfInc=10), 
                                                 listLoadNode=[], 
                                                 listLoadCaseNode=[],
                                                 listLoadNodeContact=[], 
                                                 listAdvcRefStressResult=[])

JPT.Debugger(step)
```
