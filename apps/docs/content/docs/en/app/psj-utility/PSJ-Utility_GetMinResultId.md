---
title: "JPT.GetMinResultId()"
description: "Get the ID of the node/element having the minimum value of the plotting result"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get the ID of the node/element having the minimum value of the plotting result.

## Syntax

```psj
JPT.GetMinResultId(...)
```

## Inputs

### `bVisible ` @type(Bool) @default(False) @since(5.1.0)

- Whether to restrict the target to only visible entity (_True_) or not(_False_)

## Return Code

An _Integer_ specifying the ID of the node/element (Based on the **Display At** type) having the minimum value of the plotting result.

:::note

In case the result has not been plotted yet, this utility will return **-1**.

:::

## Sample Code

```psj {11,20}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

# Get the ID of the node having the minimum value of the plotting result
minNodeID = JPT.GetMinResultId()
JPT.Debugger(minNodeID)

# Get the ID of the element having the minimum value of the plotting result
JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 2}, {2, 1, 0, 0, 0, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

minElemID = JPT.GetMinResultId()
JPT.Debugger(minElemID)
```
