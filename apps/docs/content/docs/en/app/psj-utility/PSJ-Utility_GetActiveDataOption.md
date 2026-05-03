---
title: "JPT.GetActiveDataOption()"
description: "Get the active Post Data Option of the working result"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

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
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

default_result_option = \
    JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                               1,
                               1,
                               "Stress",
                               "XX",
                               JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE)

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 2}, {1, 1, 0, 0, 16, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                             0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, 0)')

active_result_option = JPT.GetActiveDataOption()
JPT.Debugger(default_result_option)
JPT.Debugger(active_result_option)
```
