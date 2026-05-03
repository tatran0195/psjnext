---
title: "JPT.DeleteSubAssembly()"
description: "Delete the inputted sub assembly"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Delete the inputted sub assembly.

## Syntax

```psj
JPT.DeleteSubAssembly(subAssembly)
```

## Inputs

### `subAssembly` @type(DItem) @required

- Object specifying the sub assembly which will be deleted.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {7}
# Create 2 sub assemblies under All Parts assemly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())

# Delete the created CreateSubAsm1
subAssem = JPT.FindSubAssemblyByID(2)
JPT.DeleteSubAssembly(subAssem)
```
