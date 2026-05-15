---
title: "JPT.GetActivePostJob()"
description: "Get information of active Post Job"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get information of active Post Job.

## Syntax

```psj
JPT.GetActivePostJob()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the information of the active Post Job.

## Sample Code

```psj {5}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

post _job = JPT.GetActivePostJob()
JPT.Debugger(post _job)
```
