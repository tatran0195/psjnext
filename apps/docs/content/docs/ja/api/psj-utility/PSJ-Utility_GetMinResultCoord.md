---
title: "JPT.GetMinResultCoord()"
description: "Get coordinate of the node/center node of the element having the minimum value of the plotting result"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get coordinate of the node/center node of the element having the minimum value of the plotting result.

## Syntax

```psj
JPT.GetMinResultCoord(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### bVisible

- Specify whether to restrict the target to only visible entity (_True_) or not(_False_)
- The default value is _False_.

## Return Code

A _[DoubleVector](../data-type/psj-utility/pre-utility/built-in-types/DoubleVector)_ specifying the coordinate of the node/center node of the element (Based on the **Display At** type) having the minimum value of the plotting result.

:::note

In case the result has not been plotted yet, this utility will return a list = **\[-1.79769e+308, -1.79769e+308, -1.79769e+308]**.

:::

## Sample Code

```psj {11,20}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, 0, \
                             0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                             0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                             0.000000, 0}, 0, 0)')

# Get the coordinate of the node having the minimum value of the plotting result
minNodeCoord = JPT.GetMinResultCoord()
JPT.Debugger(minNodeCoord)

# Get the coordinate of the center of an element having the minimum value of the plotting result
JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 2}, {2, 1, 0, 0, 0, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

minElemCenterCoord = JPT.GetMinResultCoord()
JPT.Debugger(minElemCenterCoord)
```
