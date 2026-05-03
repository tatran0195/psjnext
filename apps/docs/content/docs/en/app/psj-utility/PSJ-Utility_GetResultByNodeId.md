---
title: "JPT.GetResultByNodeId()"
description: "Get the result value of specified Node by ID"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get the result value of specified Node by ID.
If multiple result data are retrieved (e.g., Mises & Principal), please use JPT.GetAllResultsByNodeId.

## Syntax

```psj
JPT.GetResultByNodeId(nodeID)
```

## Inputs

### `nodeID` @type(Integer) @required

- The ID of Node to be checked the result value.

## Return Code

A _Double_ specifying the result of Node.

## Sample Code

```psj {11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Displacement, X, 1}, {1, 1, 0, \
                             0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                             {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the result value of Node ID = 62
valueNodeID = JPT.GetResultByNodeId(62)
print("Displacement of X component of Node ID = 62: " + str(valueNodeID))
```
