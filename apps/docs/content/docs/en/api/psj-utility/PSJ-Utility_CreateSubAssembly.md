---
title: "JPT.CreateSubAssembly()"
description: "Create a new sub assembly under the indicated parent sub assembly"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create a new sub assembly under the indicated parent sub assembly.

## Syntax

```psj
JPT.CreateSubAssembly(subAssemName, parentAssem)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `subAssemName`

- The name of the creating sub assembly.

<!-- @since:5.0.1 @type:DItem @required -->
### `parentAssem`

- The object specifying the parent sub assembly of the creating sub assembly.
- If the parent sub assembly is `All Parts` assembly, assigns an instance object _[JPT.DItem()](../data-type/psj-utility/pre-utility/built-in-types/DItem)_.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2,3,6}
# Create 2 sub assemblies under All Parts assembly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())

# Create a sub assembly under CreateSubAsm0 (ID = 1)
JPT.CreateSubAssembly('CreateSubAsm2',JPT.FindSubAssemblyByID(1))
```
