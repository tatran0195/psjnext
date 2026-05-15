---
title: "JPT.RemoveEntitiesByID()"
description: "Delete specified entity by inputting its type and its ID"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Remove specified entity by inputting its DItem type and its ID.

## Syntax

```psj
JPT.RemoveEntitiesByID(DItemType, itemID)
```

## Inputs

<!-- @since:5.0.1 @required -->
### DItemType

- Specify the_[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.

<!-- @since:5.0.1 @required -->
### itemID

- Specify the ID of the target entity to be removed.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube(iPartColor=12829526)
Geometry.Part.Cube(strName="Cube _2", iPartColor=8060538)
Geometry.Part.Cube(strName="Cube _3", iPartColor=13787489)
JPT.ViewFitToModel()

# Delete Cube _2 part
JPT.RemoveEntitiesByID(JPT.DItemType.BODY, 2)
```
