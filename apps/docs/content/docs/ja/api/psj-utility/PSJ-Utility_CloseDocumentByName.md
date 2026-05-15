---
title: "JPT.CloseDocumentByName()"
description: "Close indicated document by using its name."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Close indicated document by using its name.

## Syntax

```psj
JPT.CloseDocumentByName(docName)
```

## Inputs

<!-- @since:5.1.0 @required -->
### docName

- Specify the name of document to be closed.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {4}
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
JPT.CreateNewDocument()
JPT.CloseDocumentByName("101 _solid")
```
