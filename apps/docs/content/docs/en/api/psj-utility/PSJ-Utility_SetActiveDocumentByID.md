---
title: "JPT.SetActiveDocumentByID()"
description: "Set indicated document in active by using its ID"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set indicated document in active by using its ID.

## Syntax

```psj
JPT.SetActiveDocumentByID(docID, BoolType)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `docID`

- The ID of document to activate.

<!-- @since:5.1.0 @type:BoolType @required -->
### `BoolType`

- The _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
  - _True_: Activate the indicated document.
  - _False_: Do not activate the indicated document.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {3}
doc1 = JPT.CreateNewDocument()
doc2 = JPT.CreateNewDocument()
JPT.SetActiveDocumentByID(doc1.docID, 1)
Geometry.Part.Cube()
JPT.ViewFitToModel()
```
