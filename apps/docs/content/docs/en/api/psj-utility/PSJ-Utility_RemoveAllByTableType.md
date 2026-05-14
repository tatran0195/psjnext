---
title: "JPT.RemoveAllByTableType()"
description: "Remove all the entities relating to the inputted DTableType"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Remove all the entities relating to the inputted _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_.

## Syntax

```psj
JPT.RemoveAllByTableType(DTableType)
```

## Inputs

<!-- @since:5.0.1 @type:DTableType @required -->
### `DTableType`

- The _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of the entities which will be removed.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {9}
# Prepare model
Geometry.Part.Cube(iPartColor=5955674)
Geometry.Part.Cube(strName="Cube _2", iPartColor=5682356)
Geometry.Part.Cube(strName="Cube _3", iPartColor=12237393)
Geometry.Part.Cube(strName="Cube _4", iPartColor=6740326)
Geometry.Part.Cube(strName="Cube _5", iPartColor=7335919)

# Remove all the created parts
JPT.RemoveAllByTableType(JPT.DTableType.DTABLE _BODY)
```
