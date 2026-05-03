---
title: "JPT.GetResultSteps()"
description: "Get all the existing result types and their time steps of the current result"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get all the existing result types and their time steps of the current result.

## Syntax

```psj
JPT.GetResultSteps()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _List of Integer Triple_ containing information of result types, id and their steps.

:::note

To get their output values, you can use the below code (as an example):

```psj
result_types_steps = JPT.GetResultSteps()
for item in result_types_steps:
    result_type = item.first
    result_id = item.second
    result_step = item.third
    print("Result type: " + str(result_type))
    print("Result ID: " + str(result_id))
    print("Result step: " + str(result_step))
```

For your reference, to printout all the properties and methods of the **JPT.GetResultSteps()** API, you can use **print(dir(JPT.GetResultSteps()))**.

Besides, the output value is an integer number that specifying the result type. So, for checking the available result type, you can refer to **[PostAnalysisTypes](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)**.

:::

## Sample Code

```psj {5}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_types_steps = JPT.GetResultSteps()

print("Result type: " + str(result_types_steps[0].first)) #2: JPT.PostAnalysisType.POST_ANALYSIS_MODAL
print("Result ID: " + str(result_types_steps[0].second))
print("Result step: " + str(result_types_steps[0].third))
```
