---
title: "JPT.SetActiveDocumentByName()"
description: "Set indicated document in active by using its name"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set indicated document in active by using its name.

## Syntax

```psj
JPT.SetActiveDocumentByName(docName, BoolType)
```

## Inputs

<!-- @since:5.1.0 @required -->
### docName

- Specify the name of document to activate.

<!-- @since:5.1.0 @required -->
### BoolType

- Specify the_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
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
