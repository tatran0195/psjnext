---
title: "Assembly.RightClick.TransferDocumentData()"
description: "Transfer data information of entity between documents"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assembly > Right Click > Copy"
macro_link: "[TransferDocumentData](../../macro/utility/TransferDocumentData)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Transfer data information of entity between documents.

## Syntax

```psj
Assembly.RightClick.TransferDocumentData(...)
```

## Inputs

### `strSourceDocTitle` @type(String)

- The name of source document.
- The is the required input.

### `strDestDocTitle` @type(String)

- The name of destination document. If the destination document does not exist before running this PSJ-Command, it will firsly create a new document with the name used in`strDestDocTitle`
- The is the required input.

### `crlParts` @type(List\[Cursor])

- The transformed parts.
- The is the required input.

### `strlNewPartName` @type(List\[String]) @default(\[])

- The new name of transformed parts in the destination document.

### `crDestAssemblyInstance` @type(Cursor) @since(5.1.0)

- The sub assembly where transformed parts moves.

### `bEnableCutOperation` @type(Boolean) @since(5.1.0)

- Cut or paste.
- False: cut, True: copy.

## Return Code

A _Cursor_ specifying the newly created parts in destination document.

:::note
PSJ interpreter will raise error (exception) when it can not find an entity in database (a database query error). With a wrong input argument (document name, part ID) then it can lead to a query error rather than return a failed result.
:::

## Sample Code

```psj {9-13}
# Create a Cube in 1st document.
doc1=JPT.GetActiveDocument()
Geometry.Part.Cube()

#2nd doc is created
doc2=JPT.CreateNewDocument()

# Copy/Transfer Cube into document 2: 
result = Assembly.RightClick.TransferDocumentData(
    strSourceDocTitle=doc1.docName, 
    strDestDocTitle=doc2.docName,
    crlParts=[Part(1)], 
    strlNewPartName=[])

# Check cube in both 1st and 2nd document.
Home.Windows.TileVertical(iMode=1)
Home.Synchronize()
JPT.ViewFitToModel()
```
