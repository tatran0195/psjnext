---
title: 'Analysis.ADVC.MakeProcess.Dynamic()'
description: 'Create an ADVC Dynamic process. This process could be created in one time or multiple times'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > ADVC > Structure > Dynamic'
macro_link: '[AdvcDynamicProcess](../../macro/analysis/AdvcDynamicProcess)'
---

## Description

Create an ADVC Dynamic process.
This process could be created in one time or multiple times.

## Syntax

```psj
Analysis.ADVC.MakeProcess.Dynamic(...)
```

## Inputs

### `strName` @type(String) @required

- The name of the ADVC Dynamic process will be created.

### `iGeomNonlinear` @type(Integer) @default(0)

- The geometry nonlinear type:
    - 0: None
    - 1: Linear
    - 2: Nonlinear
    - 3: Total Lagrange
    - 4: Updated Lagrange

### `advcStructTimeStep` @type(ADVC_STRUCT_TIME_STEP) @default(ADVC_STRUCT_TIME_STEP)

- The time step parameters.

### `bConvergence` @type(Boolean) @default(False)

- Whether to apply the convergence parameters or not.

### `advcConvergence` @type(ADVC_CONVERGENCE) @default(ADVC_CONVERGENCE)

- The convergence parameters.
- This argument will be specified whe&#x6E;_&#x62;Convergence=True_.

### `bContact` @type(Boolean) @default(False)

- Whether to apply the contact parameters or not.

### `advcContactIter` @type(ADVC_CONTACT_ITER) @default(ADVC_CONTACT_ITER)

- The contact iteration parameters.
- This argument will be specified whe&#x6E;_&#x62;Contact=True_.

### `bAutoIncrement` @type(Boolean) @default(False)

- Whether to apply the auto increment parameters or not.

### `advcAutoIncrement` @type(ADVC_AUTO_INCREMENT) @default(ADVC_AUTO_INCREMENT)

- The auto increment parameters.
- This argument will be specified whe&#x6E;_&#x62;AutoIncrement=True_.

### `bDynamic` @type(Boolean) @default(False)

- Whether to apply the ADVC dynamic parameters or not.

### `advcDynamic` @type(ADVC_DYNAMIC) @default(ADVC_DYNAMIC)

- The ADVC dynamic parameters.
- This argument will be specified whe&#x6E;_&#x62;Dynamic=True_.

### `crEdit` @type(Cursor) @default(None)

- An ADVC Dynamic process.
    - If this parameter is used, the specified job will be modified.
    - If it is lef&#x74;_&#x4E;one_, a new job will be created.

### `listLoadNode` @type(List\[ADVC_LOAD_NODE]) @default(\[])

- The load node.
- If this argument is specified, the`listLoadCaseNode`will be empty.

### `listLoadCaseNode` @type(List\[ADVC_LOAD_NODE]) @default(\[])

- The loadcase node.
- If this argument is specified, the`listLoadNode`will be empty.

### `listLoadNodeContact` @type(List\[ADVC_LOAD_NODE]) @default(\[])

- The load node contact.
- This argument uses the instance of[ADVC_LOAD_NODE](./../../data-type/psj-command/parameter-types/ADVC_LOAD_NODE)and won't be duplicated with`listLoadNode`or`listLoadCaseNode`

### `ilOutputParamList` @type(List\[Integer]) @default(\[])

- The output param list.

### `iRefType` @type(Integer) @default(-1)

- The reference type.

### `strRefPath` @type(String) @default("")

- The reference path.

### `listAdvcRefStressResult` @type(List) @default(\[])

- The ADVC reference stress result.

## Return Code

A _Cursor_ specifying the created or the modified ADVC Dynamic process.

## Sample Code

```psj {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
step = Analysis.ADVC.MakeProcess.Dynamic(strName="Process_0",
                                         iGeomNonlinear=0,
                                         advcStructTimeStep=ADVC_STRUCT_TIME_STEP(),
                                         bConvergence=False,
                                         advcConvergence=ADVC_CONVERGENCE(),
                                         bContact=False,
                                         advcContactIter=ADVC_CONTACT_ITER(),
                                         bAutoIncrement=False,
                                         advcAutoIncrement=ADVC_AUTO_INCREMENT(),
                                         bDynamic=False,
                                         advcDynamic=ADVC_DYNAMIC(),
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
