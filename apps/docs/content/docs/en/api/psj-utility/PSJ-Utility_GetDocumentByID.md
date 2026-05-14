---
title: "JPT.GetDocumentByID()"
description: "Get information of an indicated document by using its ID"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get information of an indicated document by using its ID.

## Syntax

```psj
JPT.GetDocumentByID(docID)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `docID`

- The ID of document to get information.

## Return Code

A _[Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of document.

## Sample Code

```psj {2}
doc = JPT.CreateNewDocument()
docInfor = JPT.GetDocumentByID(doc.docID)
JPT.Debugger(docInfor)
```
