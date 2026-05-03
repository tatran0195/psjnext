---
title: "JPT.GetEntitiesByAssociation()"
description: "Get list of objects by associating from the inputted entity ID and its type"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get _List of Objects_ by associating from the inputted entity ID and its type.

## Syntax

```psj
JPT.GetEntitiesByAssociation(DItemType, AssociateType, entityID)
```

## Inputs

### `DItemType` @type(Enum) @required

- Th&#x65;_[DItemType](../data-type/psj-command/DItem-types)_&#x6F;f entity in Jupiter.

### `AssociateType` @type(Enum) @required

- Th&#x65;_[AssociateType](../data-type/psj-utility/pre-utility/enumeration-types/associate-types)_&#x64;escribing the association type in Jupiter.

### `entityID` @type(Integer) @required

- The ID of which is used as a starting entity.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of associated entities.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get all the associating faces existing on the part with ID = 1
listAssociatedEntities = JPT.GetEntitiesByAssociation(JPT.DItemType.BODY, JPT.AssociateType.AS_FACE, 1)
JPT.Debugger(listAssociatedEntities) # return value is a list DItem has size = 6
```
