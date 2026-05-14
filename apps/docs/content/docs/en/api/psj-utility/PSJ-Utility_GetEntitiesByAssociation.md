---
title: "JPT.GetEntitiesByAssociation()"
description: "Get list of objects by associating from the inputted entity ID and its type"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get _List of Objects_ by associating from the inputted entity ID and its type.

## Syntax

```psj
JPT.GetEntitiesByAssociation(DItemType, AssociateType, entityID)
```

## Inputs

<!-- @since:5.0.1 @type:DItemType @required -->
### `DItemType`

- The _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.

<!-- @since:5.0.1 @type:AssociateType @required -->
### `AssociateType`

- The _[AssociateType](../data-type/psj-utility/pre-utility/enumeration-types/associate-types)_ describing the association type in Jupiter.

<!-- @since:5.0.1 @type:Integer @required -->
### `entityID`

- The ID of which is used as a starting entity.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of associated entities.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get all the associating faces existing on the part with ID = 1
listAssociatedEntities = JPT.GetEntitiesByAssociation(JPT.DItemType.BODY, JPT.AssociateType.AS _FACE, 1)
JPT.Debugger(listAssociatedEntities) # return value is a list DItem has size = 6
```
