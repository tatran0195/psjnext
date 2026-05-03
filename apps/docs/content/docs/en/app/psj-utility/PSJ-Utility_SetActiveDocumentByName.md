---
title: "JPT.SetActiveDocumentByName()"
description: "Set indicated document in active by using its name"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Set indicated document in active by using its name.

## Syntax

```psj
JPT.SetActiveDocumentByName(docName, BoolType)
```

## Inputs

### `docName` @type(String) @required

- The name of document to activate.

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the selection mode:
  - _True_: Activate the indicated document.
  - _False_: Do not activate the indicated document.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {4}
doc1 = JPT.CreateNewDocument()
doc2 = JPT.CreateNewDocument()
doc3 = JPT.CreateNewDocument()
JPT.SetActiveDocumentByName(doc2.docName,1)
Geometry.Part.Cube()
JPT.ViewFitToModel()
print("Created a Cube in " + str(doc2.docName) + " document")
```
