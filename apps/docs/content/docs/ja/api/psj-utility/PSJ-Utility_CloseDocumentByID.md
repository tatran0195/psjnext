---
title: "JPT.CloseDocumentByID()"
description: "Close indicated document by using its ID."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Close indicated document by using its ID.

## Syntax

```psj
JPT.CloseDocumentByID(docID)
```

## Inputs

<!-- @since:5.1.0 @required -->
### docID

- Specify the ID of document to be closed.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {6}
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
JPT.CreateNewDocument()
for doc in JPT.GetDocumentList():
    if doc.docName == "101 _solid":
        JPT.CloseDocumentByID(doc.docID)
```
