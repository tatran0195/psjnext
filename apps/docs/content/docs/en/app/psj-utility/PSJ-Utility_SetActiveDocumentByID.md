---
title: "JPT.SetActiveDocumentByID()"
description: "Set indicated document in active by using its ID"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Set indicated document in active by using its ID.

## Syntax

```psj
JPT.SetActiveDocumentByID(docID, BoolType)
```

## Inputs

### `docID` @type(String) @required

- The ID of document to activate.

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the selection mode:
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
