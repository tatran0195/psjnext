---
title: "JPT.GetElementResult()"
description: "Get all elements with the loaded element results that satisfy a condition"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get elements with loaded results satisfy a condition.

## Syntax

```psj
JPT.GetElementResult(PostDataRangeType,
                     resultValue,
                     adjustment)
```

## Inputs

<!-- @since:5.0.1 @required -->
### PostDataRangeType

- Specify the_[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ describing the condition to get the element results.

<!-- @since:5.0.1 @required -->
### resultValue

- Specify the referenced value.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### adjustment

- Specify the adjustment to the referenced value_[resultValue](#resultvalue)_:
  - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a scalar type (i.e. EQ, NE, LT, GT, LE, GE), then the range to get the result is from (resultValue - adjustment) to (resultValue + adjustment)
  - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a range type (i.e. IR, OR, IRE, ORE), then the range to get the result is from (resultValue) to (adjustment)
- The default value is 1E-5.

## Return Code

A _List of Cursor_ containing elements with loaded element results satisfy the given condition.

## Sample Code

```psj {11,15}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Max Principal Stress, 2}, {2, 1, 0, 0, 0, 0, \
                             0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                             0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, \
                             0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')

# Create a elemental group whose element results greater than 1 (tolerance=10E-3)
list _element _1= JPT.GetElementResult(JPT.PostDataRangeType.GT,1,10E-3)
Tools.Group.CreateGroup(strGroupName="Group _Element _1", crlTargets=list _element _1)

# Create a elemental group whose element results in range (1,5)
list _element _2= JPT.GetElementResult(JPT.PostDataRangeType.IR,1,5)
Tools.Group.CreateGroup(strGroupName="Group _Element _2", crlTargets=list _element _2)
```
