---
title: "JPT.RemoveAllByTableType()"
description: "Remove all the entities relating to the inputted DTableType"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Remove all the entities relating to the inputted _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_.

## Syntax

```psj
JPT.RemoveAllByTableType(DTableType)
```

## Inputs

### `DTableType` @type(Enum) @required

- Th&#x65;_[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_&#x6F;f the entities which will be removed.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {9}
# Prepare model
Geometry.Part.Cube(iPartColor=5955674)
Geometry.Part.Cube(strName="Cube_2", iPartColor=5682356)
Geometry.Part.Cube(strName="Cube_3", iPartColor=12237393)
Geometry.Part.Cube(strName="Cube_4", iPartColor=6740326)
Geometry.Part.Cube(strName="Cube_5", iPartColor=7335919)

# Remove all the created parts
JPT.RemoveAllByTableType(JPT.DTableType.DTABLE_BODY)
```
