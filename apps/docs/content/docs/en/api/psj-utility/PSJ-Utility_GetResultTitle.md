---
title: "JPT.GetResultTitle()"
description: "Get contents of title when result is loaded."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get contents of title when result is loaded.

## Syntax

```psj
JPT.GetResultTitle()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ containing all the information of title.

## Sample Code

```psj {17}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

#Load result and deformation.
JPT.Exec('CmdShowPostContour(183:1, \
        {2, 0, 1, 6, Displacement, Translational, 1}, \
        {1, 1, 0, 0, 0, 0, 0, 0.000000, 0}, 0, \
        {0, 0, 0, 0, , , 0}, \
        {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, \
        {0, 0, 0, 0, , , 0}, \
        {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
JPT.Exec('CmdShowPostDeformation(183:1, 2, 0, 1, 6, Displacement, Translational, \
        0, 0.000000, 0, 0.070000, 0, 0.070000, 0.070000, 0.070000, 0)')
JPT.Exec('CmdEnableMiddleNodes(1)')

title=JPT.GetResultTitle()
pprint(title)
```
