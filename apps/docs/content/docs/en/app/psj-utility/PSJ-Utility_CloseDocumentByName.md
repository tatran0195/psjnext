---
title: "JPT.CloseDocumentByName()"
description: "Close indicated document by using its name."
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Close indicated document by using its name.

## Syntax

```psj
JPT.CloseDocumentByName(docName)
```

## Inputs

### `docName` @type(String) @required

- The name of document to be closed.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {4}
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
JPT.CreateNewDocument()
JPT.CloseDocumentByName("101_solid")
```
