---
title: "JPT.GetDocumentByName()"
description: "Get information of an indicated document by using its name"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get information of an indicated document by using its name.

## Syntax

```psj
JPT.GetDocumentByName(docName)
```

## Inputs

### `docName` @type(String) @required

- The name of document to get information.

## Return Code

A _[Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of document.

## Sample Code

```psj {3}
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
docInfor = JPT.GetDocumentByName("101_solid")
JPT.Debugger(docInfor)
```
