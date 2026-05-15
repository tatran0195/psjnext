---
title: "JPT.GetEntitiesByAdjacent()"
description: "Get list of objects by adjacency based on the stop angle"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get _List of Objects_ by adjacency based on the stop angle.

## Syntax

```psj
JPT.GetEntitiesByAdjacent(DItemType, entityID, angleValue)
```

## Inputs

<!-- @since:5.0.1 @required -->
### DItemType

- Specify the_[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.

<!-- @since:5.0.1 @required -->
### entityID

- Specify the ID of the starting entity.

<!-- @since:5.0.1 @required -->
### angleValue

- Specify the stop angle between entities for searching.

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
