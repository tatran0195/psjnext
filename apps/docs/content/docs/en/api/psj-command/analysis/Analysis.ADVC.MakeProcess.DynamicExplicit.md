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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name of the process.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGeomNonlinear`

- The geometric nonlinearity type:
  - If _iGeomNonlinear=0_, do not define the geometric nonlinearity type.
  - If _iGeomNonlinear=1_, a Linear geometric nonlinearity is specified.
  - If _iGeomNonlinear=2_, a Nonlinear geometric nonlinearity is specified.
  - If _iGeomNonlinear=3_, a Total Lagrange geometric nonlinearity is specified.
  - If _iGeomNonlinear=4_, a Updated Lagrange geometric nonlinearity is specified.

<!-- @since:5.0.1 @type:ADVC _STRUCT _TIME _STEP @optional @default:ADVC _STRUCT _TIME _STEP -->
### `advcStructTimeStep`

- The time step settings for ADVC solver.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bConvergence`

- Whether to apply the convergence parameters.

<!-- @since:5.0.1 @type:ADVC _CONVERGENCE @optional @default:ADVC _CONVERGENCE -->
### `advcConvergence`

- The convergence settings for ADVC solver. This argument must be specified when _bConvergence=True_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bContact`

- Whether to apply the contact parameters.

<!-- @since:5.0.1 @type:ADVC _CONTACT _ITER @optional @default:ADVC _CONTACT _ITER -->
### `advcContactIter`

- The contact iterator settings for ADVC solver. This argument must be specified when _bContact=True_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAutoIncrement`

- Whether to apply the auto increment parameters.

<!-- @since:5.0.1 @type:ADVC _AUTO _INCREMENT @optional @default:ADVC _AUTO _INCREMENT -->
### `advcAutoIncrement`

- The auto increment settings for ADVC solver. This argument must be specified when _bAutoIncrement=True_.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iLogMessageInterval`

- The log message interval.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iLinearApproximation`

- The linear approximation.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dBulkViscosityCoef1`

- The first bulk viscosity coefficient.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dBulkViscosityCoef2`

- The second bulk viscosity coefficient.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMassScalingdt`

- The mass scaling of the dt time.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDtScaleFactor`

- The scale factor of the dt time.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dPenaltyScaleFactor`

- The penalty scale factor.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iContactSearchInterval`

- The contact search interval.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The existing process to be modified. If the default value is specified, a new process will be created, otherwise, the specified process will modified.

<!-- @since:5.0.1 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadNode`

- The load node.
- If this argument is specified, the `listLoadCaseNode` will be empty.

<!-- @since:5.0.1 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadCaseNode`

- The loadcase node.
- If this argument is specified, the `listLoadNode` will be empty.

<!-- @since:5.0.1 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadNodeContact`

- The load node contact.
- This argument uses the instance of [ADVC\_LOAD\_NODE](./../../data-type/psj-command/parameter-types/ADVC _LOAD _NODE) and won't be duplicated with `listLoadNode` or `listLoadCaseNode`

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilOutputParamList`

- The output parameters.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iRefType`

- The reference type.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strRefPath`

- The reference path.

<!-- @since:5.0.1 @type:List @optional @default:[] -->
### `listAdvcRefStressResult`

- The advc reference stress result.

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
