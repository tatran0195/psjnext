---
title: "JPT.RemoveAllFieldTables()"
description: "Remove all the existing field tables"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Remove all the existing field tables.

## Syntax

```psj
JPT.RemoveAllFieldTables()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {10}
# Create sample fields data
BoundaryConditions.FieldData(strName="test _1", iType=1,
                             ilSheet=[3, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
BoundaryConditions.FieldData(strName="test _2", iType=4,
                             ilSheet=[3, 2, 1, 1, 2, 2, 3, 3])
BoundaryConditions.FieldData(strName="test _3", iType=3,
                             ilSheet=[3, 2, 1, 1, 2, 2, 3, 3])

# Remove all the created fields data
JPT.RemoveAllFieldTables()
```
