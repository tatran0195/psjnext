---
title: "Analysis.ADVC.MakeProcess.Dynamic()"
description: "Create an ADVC Dynamic process. This process could be created in one time or multiple times"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > Structure > Dynamic"
macro _link: "[AdvcDynamicProcess](../../macro/analysis/AdvcDynamicProcess)"
---

## Description

Create an ADVC Dynamic process.
This process could be created in one time or multiple times.

## Syntax

```psj
Analysis.ADVC.MakeProcess.Dynamic(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name of the ADVC Dynamic process will be created.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGeomNonlinear`

- The geometry nonlinear type:
  - 0: None
  - 1: Linear
  - 2: Nonlinear
  - 3: Total Lagrange
  - 4: Updated Lagrange

<!-- @since:5.0.1 @type:ADVC _STRUCT _TIME _STEP @optional @default:ADVC _STRUCT _TIME _STEP -->
### `advcStructTimeStep`

- The time step parameters.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bConvergence`

- Whether to apply the convergence parameters or not.

<!-- @since:5.0.1 @type:ADVC _CONVERGENCE @optional @default:ADVC _CONVERGENCE -->
### `advcConvergence`

- The convergence parameters.
- This argument will be specified when _bConvergence=True_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bContact`

- Whether to apply the contact parameters or not.

<!-- @since:5.0.1 @type:ADVC _CONTACT _ITER @optional @default:ADVC _CONTACT _ITER -->
### `advcContactIter`

- The contact iteration parameters.
- This argument will be specified when _bContact=True_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAutoIncrement`

- Whether to apply the auto increment parameters or not.

<!-- @since:5.0.1 @type:ADVC _AUTO _INCREMENT @optional @default:ADVC _AUTO _INCREMENT -->
### `advcAutoIncrement`

- The auto increment parameters.
- This argument will be specified when _bAutoIncrement=True_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDynamic`

- Whether to apply the ADVC dynamic parameters or not.

<!-- @since:5.0.1 @type:ADVC _DYNAMIC @optional @default:ADVC _DYNAMIC -->
### `advcDynamic`

- The ADVC dynamic parameters.
- This argument will be specified when _bDynamic=True_.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An ADVC Dynamic process.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.

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

- The output param list.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iRefType`

- The reference type.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strRefPath`

- The reference path.

<!-- @since:5.0.1 @type:List @optional @default:[] -->
### `listAdvcRefStressResult`

- The ADVC reference stress result.

## Return Code

A _Cursor_ specifying the created or the modified ADVC Dynamic process.

## Sample Code

```psj {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
step = Analysis.ADVC.MakeProcess.Dynamic(strName="Process _0", 
                                         iGeomNonlinear=0,
                                         advcStructTimeStep=ADVC _STRUCT _TIME _STEP(), 
                                         bConvergence=False,
                                         advcConvergence=ADVC _CONVERGENCE(), 
                                         bContact=False,
                                         advcContactIter=ADVC _CONTACT _ITER(),
                                         bAutoIncrement=False, 
                                         advcAutoIncrement=ADVC _AUTO _INCREMENT(), 
                                         bDynamic=False,
                                         advcDynamic=ADVC _DYNAMIC(), 
                                         crEdit=None, 
                                         listLoadNode=[], 
                                         listLoadCaseNode=[],
                                         listLoadNodeContact=[], 
                                         ilOutputParamList=[], 
                                         iRefType=-1, 
                                         strRefPath="",
                                         listAdvcRefStressResult=[])

JPT.Debugger(step)
```
