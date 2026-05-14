---
title: "JPT.GetActiveDataOption()"
description: "Get the active Post Data Option of the working result"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the active Post Data Option of the working result.

## Syntax

```psj
JPT.GetActiveDataOption()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ object containing the active setting of the working result.

## Sample Code

```psj {19}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

default _result _option = \
    JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST _ANALYSIS _LINEAR _STATIC,
                               1,
                               1,
                               "Stress",
                               "XX",
                               JPT.PostResultDataLoc.POST _LOC _ON _ELEMENT _NODE)

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 2}, {1, 1, 0, 0, 16, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

active _result _option = JPT.GetActiveDataOption()
JPT.Debugger(default _result _option)
JPT.Debugger(active _result _option)
```
