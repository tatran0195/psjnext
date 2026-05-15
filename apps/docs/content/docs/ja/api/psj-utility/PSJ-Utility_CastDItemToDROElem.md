---
title: "JPT.CastDItemToDROElem()"
description: "Convert DItem object to DPostElem object"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DPostElem](../data-type/psj-utility/post-utility/post-built-in-types/DPostElem)_ object to get the information of the selected Post element.

## Syntax

```psj
JPT.CastDItemToDROElem(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.

## Return Code

A _[DPostElem](../data-type/psj-utility/post-utility/post-built-in-types/DPostElem)_ object (Post element with relating information).

## Sample Code

```psj {11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

# Get Element object as DItem object from the created list of DItem objects
listDItemPostElems = JPT.GetAllByTypeID(JPT.DItemType.POST _ELEM)
dItemPostElem = listDItemPostElems[0]
JPT.Debugger(dItemPostElem)

# Convert from the above DItem object to DElem object
dPostElem = JPT.CastDItemToDROElem(dItemPostElem)
JPT.Debugger(dPostElem)
```
