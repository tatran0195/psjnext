---
title: "Assembly.RightClick.TransferDocumentData()"
description: "Transfer data information of entity between documents"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assembly > Right Click > Copy"
macro _link: "[TransferDocumentData](../../macro/utility/TransferDocumentData)"
---

## Description

Transfer data information of entity between documents.

## Syntax

```psj
Assembly.RightClick.TransferDocumentData(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional -->
### `strSourceDocTitle`

- The name of source document.
- The is the required input.

<!-- @since:5.0.1 @type:String @optional -->
### `strDestDocTitle`

- The name of destination document. If the destination document does not exist before running this PSJ-Command, it will firsly create a new document with the name used in`strDestDocTitle`
- The is the required input.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlParts`

- The transformed parts.
- The is the required input.

<!-- @since:5.0.1 @type:List[String] @optional @default:[] -->
### `strlNewPartName`

- The new name of transformed parts in the destination document.

<!-- @since:5.1.0 @type:Cursor @optional -->
### `crDestAssemblyInstance`

- The sub assembly where transformed parts moves.

<!-- @since:5.1.0 @type:Boolean @optional -->
### `bEnableCutOperation`

- The cut or paste.
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
