---
title: "JPT.GetElementResult()"
description: "Get all elements with the loaded element results that satisfy a condition"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [param_decorator_changed] Param 'adjustment' @default changed from '10E-5' to '1E-5' in v5.1.0
     context: {"param":"adjustment","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"10E-5","toDefault":"1E-5"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get elements with loaded results satisfy a condition.

## Syntax

```psj
JPT.GetElementResult(PostDataRangeType,
                     resultValue,
                     adjustment)
```

## Inputs

### `PostDataRangeType` @type(Enum) @required

- Th&#x65;_[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_&#x64;escribing the condition to get the element results.

### `resultValue` @type(Double) @required

- The referenced value.

### `adjustment` @type(Double) @default(1E-5)

- The adjustment to the referenced valu&#x65;_[resultValue](#resultvalue)_:
  - I&#x66;_[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_&#x69;s a scalar type (i.e. EQ, NE, LT, GT, LE, GE), then the range to get the result is from (resultValue - adjustment) to (resultValue + adjustment)
  - I&#x66;_[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_&#x69;s a range type (i.e. IR, OR, IRE, ORE), then the range to get the result is from (resultValue) to (adjustment)

## Return Code

A _List of Cursor_ containing elements with loaded element results satisfy the given condition.

## Sample Code

```psj {11,15}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Max Principal Stress, 2}, {2, 1, 0, 0, 0, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, \
                             0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Create a elemental group whose element results greater than 1 (tolerance=10E-3)
list_element_1= JPT.GetElementResult(JPT.PostDataRangeType.GT,1,10E-3)
Tools.Group.CreateGroup(strGroupName="Group_Element_1", crlTargets=list_element_1)

# Create a elemental group whose element results in range (1,5)
list_element_2= JPT.GetElementResult(JPT.PostDataRangeType.IR,1,5)
Tools.Group.CreateGroup(strGroupName="Group_Element_2", crlTargets=list_element_2)
```
