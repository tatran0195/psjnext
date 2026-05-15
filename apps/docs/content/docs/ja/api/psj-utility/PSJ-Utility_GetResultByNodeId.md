---
title: "JPT.GetResultByNodeId()"
description: "Get the result value of specified Node by ID"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the result value of specified Node by ID.
If multiple result data are retrieved (e.g., Mises & Principal), please use JPT.GetAllResultsByNodeId.

## Syntax

```psj
JPT.GetResultByNodeId(nodeID)
```

## Inputs

<!-- @since:5.0.1 @required -->
### nodeID

- Specify the ID of Node to be checked the result value.

## Return Code

A _Double_ specifying the result of Node.

## Sample Code

```psj {11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Displacement, X, 1}, {1, 1, 0, \
                             0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the result value of Node ID = 62
valueNodeID = JPT.GetResultByNodeId(62)
print("Displacement of X component of Node ID = 62: " + str(valueNodeID))
```
