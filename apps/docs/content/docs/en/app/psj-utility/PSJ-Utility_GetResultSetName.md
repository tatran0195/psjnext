---
title: "JPT.GetResultSetName()"
description: "Get the name of Result Set (Subcase)"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the name of Result Set (Subcase).

## Syntax

```psj
JPT.GetResultSetName(PostAnalysisType,
                     resultSet)
```

## Inputs

### `PostAnalysisType` @type(Enum) @required

- Th&#x65;_[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_&#x64;escribing the type of analysis result.

### `resultSet` @type(Integer) @required

- The step ID of the imported result.

## Return Code

A _String_ specifying the name of Result Set (Subcase).

## Sample Code

```psj {5}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result_set_name = JPT.GetResultSetName(1,1)
JPT.Debugger(result_set_name)
```
