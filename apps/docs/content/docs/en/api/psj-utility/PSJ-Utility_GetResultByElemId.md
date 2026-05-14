---
title: "JPT.GetResultByElemId()"
description: "Get the result value of specified Element by ID"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the result value of specified Element by ID.
If multiple result data are retrieved (e.g., Mises & Principal), please use JPT.GetAllResultsByElemId.

## Syntax

```psj
JPT.GetResultByElemId(elementID)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `elementID`

- The ID of Element to be checked the result value.

## Return Code

A _Double_ specifying the result of Element.

## Sample Code

```psj {11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 2}, {2, 1, 0, 0, 0, 0, 0, \
                             0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                             0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                             0.000000, 0}, 0, 0)')

# Get the result value of Element ID = 658
valueElementID = JPT.GetResultByElemId(658)
print("Stress of XX component of Element ID = 658: " + str(valueElementID))
```
