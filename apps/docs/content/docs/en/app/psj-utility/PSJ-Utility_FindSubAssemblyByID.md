---
title: "JPT.FindSubAssemblyByID()"
description: "Get the related information of the target sub assembly by its ID"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the related information of the target sub assembly by its ID.

## Syntax

```psj
JPT.FindSubAssemblyByID(subAssemID)
```

## Inputs

### `subAssemID` @type(Integer) @required

- The ID of the target sub assembly.

## Return Code

A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the information of the target sub assembly.

## Sample Code

```psj {7}
# Create 2 sub assemblies under All Parts assembly
JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())
JPT.ViewFitToModel()

# Get the information of the sub assembly with ID = 1
JPT.Debugger(JPT.FindSubAssemblyByID(1))
```
