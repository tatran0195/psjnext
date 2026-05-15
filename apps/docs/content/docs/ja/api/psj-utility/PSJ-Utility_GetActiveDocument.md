---
title: "JPT.GetActiveDocument()"
description: "Get information of active document"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get information of active document.

## Syntax

```psj
JPT.GetActiveDocument()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of document.

## Sample Code

```psj {5}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Get information of active document
doc = JPT.GetActiveDocument()
JPT.Debugger(doc)
```
