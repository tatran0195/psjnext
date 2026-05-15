---
title: "JPT.CastDItemToDRONode()"
description: "Convert DItem object to DPostNode object"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DPostNode](../data-type/psj-utility/post-utility/post-built-in-types/DPostNode)_ object to get the information of the selected Post node.

## Syntax

```psj
JPT.CastDItemToDRONode(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.

## Return Code

A _[DPostNode](../data-type/psj-utility/post-utility/post-built-in-types/DPostNode)_ object (Post node with relating information).

## Sample Code

```psj {11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

# Get LBC object (Pressure) as DItem object from the created list of DItem objects
listDItemPostNodes = JPT.GetAllByTypeID(JPT.DItemType.POST _NODE)
dItemPostNode = listDItemPostNodes[0]
JPT.Debugger(dItemPostNode)

# Convert from the above DItem object to DPostNode object
dPostNode = JPT.CastDItemToDRONode(dItemPostNode)
JPT.Debugger(dPostNode)
```
