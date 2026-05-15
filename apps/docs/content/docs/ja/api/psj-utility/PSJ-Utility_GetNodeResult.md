---
title: "JPT.GetNodeResult()"
description: "Get all nodes with the loaded nodal results that satisfy a condition"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get nodes with loaded results satisfy a condition.

## Syntax

```psj
JPT.GetNodeResult(PostDataRangeType,
                     resultValue,
                     adjustment)
```

## Inputs

<!-- @since:5.0.1 @required -->
### PostDataRangeType

- Specify the_[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ describing the condition to get the nodal results.

<!-- @since:5.0.1 @required -->
### resultValue

- Specify the referenced value.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### tolerance

- Specify the adjustment to the base value_[resultValue](#resultvalue)_:
  - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a scalar type (i.e. EQ, NE, LT, GT, LE, GE), then the range to get the result is from (resultValue - adjustment) to (resultValue + adjustment)
  - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a range type (i.e. IR, OR, IRE, ORE), then the range to get the result is from (resultValue) to (adjustment)
- The default value is 1E-5.

## Return Code

A _List of Cursor_ containing nodes with loaded nodal results satisfy the given condition.

## Sample Code

```psj {10,14}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Max Principal Stress, 4}, {1, 1, 0, 0, 1, 8, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, \
                             0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Create a nodal group whose nodal results greater than 1 (tolerance=10E-3)
list _node _1= JPT.GetNodeResult(JPT.PostDataRangeType.GT,1,10E-3)
Tools.Group.CreateGroup(strGroupName="Group _Node _1", crlTargets=list _node _1)

# Create a nodal group  whose nodal results in range (1,5)
list _node _2= JPT.GetNodeResult(JPT.PostDataRangeType.IR,1,5)
Tools.Group.CreateGroup(strGroupName="Group _Node _2", crlTargets=list _node _2)
```
