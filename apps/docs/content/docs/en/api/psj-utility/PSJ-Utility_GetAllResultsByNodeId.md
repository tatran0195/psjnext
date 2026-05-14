---
title: "JPT.GetAllResultsByNodeId()"
description: "Get all result values of specified Node by ID"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all result values of specified Node by ID.

## Syntax

```psj
JPT.GetAllResultsByNodeId(nodeID)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @required -->
### `nodeID`

- The ID of Node to be checked the result value.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bReturnBlank`

- The option to express the blank value.

## Return Code

A List specifying all results of Node.

## Sample Code

```psj {11}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 4}, \
                            {1, 1, 0, 0, 16, 0, 0, 0.000000, 0}, 0, \
                            {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, \
                            {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the result values of Node ID = 60
valuesNodeID = JPT.GetAllResultsByNodeId(60)
for data in valuesNodeID:
    type, id, value= data
    print(f'Type:{type} ID:{id} Value:{value}')
```
