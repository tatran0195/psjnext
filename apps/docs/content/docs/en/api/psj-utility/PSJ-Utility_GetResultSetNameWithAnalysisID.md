---
title: "JPT.GetResultSetNameWithAnalysisID()"
description: "Get the name of Result Set (Subcase)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get the name of Result Set (Subcase).

## Syntax

```psj
JPT.GetResultSetNameWithAnalysisID(PostAnalysisType,
                     analysisID,
                     resultSet)
```

## Inputs

<!-- @since:5.1.0 @type:PostAnalysisType @required -->
### `PostAnalysisType`

- The _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.

<!-- @since:5.1.0 @type:Integer @required -->
### `analysisID`

- The analysis ID of the imported result.

<!-- @since:5.1.0 @type:Integer @required -->
### `resultSet`

- The step ID of the imported result.

## Return Code

A _String_ specifying the name of Result Set (Subcase).

## Sample Code

```psj {5}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

result _set _name = JPT.GetResultSetNameWithAnalysisID(1,0,1)
JPT.Debugger(result _set _name)
```
