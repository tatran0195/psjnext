---
title: "JPT.CloseDocumentByID()"
description: "Close indicated document by using its ID."
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Close indicated document by using its ID.

## Syntax

```psj
JPT.CloseDocumentByID(docID)
```

## Inputs

### `docID` @type(String) @required

- The ID of document to be closed.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {6}
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
JPT.CreateNewDocument()
for doc in JPT.GetDocumentList():
    if doc.docName == "101_solid":
        JPT.CloseDocumentByID(doc.docID)
```
