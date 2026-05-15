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

<!-- @since:5.0.1 @required -->
### strName

- Specify the name of the ADVC Dynamic process will be created.

<!-- @since:5.0.1 @optional -->
### iGeomNonlinear

- Specify the geometry nonlinear type:
  - 0: None
  - 1: Linear
  - 2: Nonlinear
  - 3: Total Lagrange
  - 4: Updated Lagrange
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### advcStructTimeStep

- Specify the time step parameters.
- The default value is _[ADVC\_STRUCT\_TIME\_STEP](./../../data-type/psj-command/parameter-types/ADVC _STRUCT _TIME _STEP)_.

<!-- @since:5.0.1 @optional -->
### bConvergence

- Specify whether to apply the convergence parameters or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcConvergence

- Specify the convergence parameters.
- This argument will be specified when _bConvergence=True_.
- The default value is _[ADVC\_CONVERGENCE](./../../data-type/psj-command/parameter-types/ADVC _CONVERGENCE)_.

<!-- @since:5.0.1 @optional -->
### bContact

- Specify whether to apply the contact parameters or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcContactIter

- Specify the contact iteration parameters.
- This argument will be specified when _bContact=True_.
- The default value is _[ADVC\_CONTACT\_ITER](./../../data-type/psj-command/parameter-types/ADVC _CONTACT _ITER)_.

<!-- @since:5.0.1 @optional -->
### bAutoIncrement

- Specify whether to apply the auto increment parameters or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcAutoIncrement

- Specify the auto increment parameters.
- This argument will be specified when _bAutoIncrement=True_.
- The default value is _[ADVC\_AUTO\_INCREMENT](./../../data-type/psj-command/parameter-types/ADVC _AUTO _INCREMENT)_.

<!-- @since:5.0.1 @optional -->
### bDynamic

- Specify whether to apply the ADVC dynamic parameters or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcDynamic

- Specify the ADVC dynamic parameters.
- This argument will be specified when _bDynamic=True_.
- The default value is _[ADVC\_DYNAMIC](./../../data-type/psj-command/parameter-types/ADVC _DYNAMIC)_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an ADVC Dynamic process.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.
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

- Specify the output param list.
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

- Specify the ADVC reference stress result.
- The default value is \[].

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
