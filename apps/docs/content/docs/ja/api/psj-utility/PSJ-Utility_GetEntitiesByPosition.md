---
title: "JPT.GetEntitiesByPosition()"
description: "Get the entity satisfying the given conditions (X, Y, Z)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the entity satisfying the given conditions (X, Y, Z).

## Syntax

```psj
JPT.GetEntitiesByPosition(AssociateType, xCoordValue, yCoordValue, zCoordValue)
```

## Inputs

<!-- @since:5.0.1 @required -->
### AssociateType

- Specify the_[AssociateType](../data-type/psj-utility/pre-utility/enumeration-types/associate-types)_ describing the association type in Jupiter.

<!-- @since:5.0.1 @required -->
### xCoordValue

- Specify the value in X coordinate in millimeters \[mm] in the Cartesian coordinate system..

<!-- @since:5.0.1 @required -->
### yCoordValue

- Specify the value in Y coordinate in millimeters \[mm] in the Cartesian coordinate system..

<!-- @since:5.0.1 @required -->
### zCoordValue

- Specify the value in Z coordinate in millimeters \[mm] in the Cartesian coordinate system..

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the satisfied entity.

Note that to get the satisfied entity, please get the second element of the created _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get the information of the created cube
selPart = JPT.GetEntitiesByPosition(JPT.AssociateType.AS _BODY, 10, 10, 10)
JPT.Debugger(selPart[0]) # second element of the created list
```
