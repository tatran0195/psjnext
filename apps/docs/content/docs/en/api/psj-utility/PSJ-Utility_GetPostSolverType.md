---
title: "JPT.GetPostSolverType()"
description: "Get the Post Job type of the current importing result"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get the result type of the current importing result file.

## Syntax

```psj
JPT.GetPostSolverType()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _Enum_ specifying the [Post Job type](../data-type/psj-utility/post-utility/enumeration-types/post-job-types) of importing result.

## Sample Code

```psj {6}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Get Post Job type
type = JPT.GetPostSolverType()
print(type)
```
