---
title: "JPT.GetEntitiesByAdjacent()"
description: "Get list of objects by adjacency based on the stop angle"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get _List of Objects_ by adjacency based on the stop angle.

## Syntax

```psj
JPT.GetEntitiesByAdjacent(DItemType, entityID, angleValue)
```

## Inputs

### `DItemType` @type(Enum) @required

- Th&#x65;_[DItemType](../data-type/psj-command/DItem-types)_&#x6F;f entity in Jupiter.

### `entityID` @type(Integer) @required

- The ID of the starting entity.

### `angleValue` @type(Integer) @required

- The stop angle between entities for searching.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of found entities.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get the faces relating to the face with ID = 26 based on angle = 30
adjacentFaces = JPT.GetEntitiesByAdjacent(JPT.DItemType.FACE, 26, 30)
JPT.Debugger(adjacentFaces)
```
