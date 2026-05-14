---
title: "Tools.CustomNote.Copy()"
description: "Copy custom notes."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > CustomNote > Copy"
macro _link: "CopyCustomNote"
---

## Description

Copy custom notes.

## Syntax

```psj
Tools.CustomNote.Copy(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:'' -->
### `strSrcDocumentName`

- The name of document that have original custom notes to copy.

<!-- @since:5.1.0 @type:String @optional @default:'' -->
### `strDestDocumentName`

- The name of document that the indicated custom notes will be copied.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The original custom notes to copy.

<!-- @since:5.1.0 @type:List[String] @optional @default:[] -->
### `strlNames`

- The names of copied custom notes.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCollection`

- A collection where original custom notes will be copied.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bKeep`

- Whether or not

## Return Code

A _Boolean_ specifying copy custom note works successfully or not.

## Sample Code

```psj {26-31}
# Create a custom note and collection in document 1.
doc1=JPT.GetActiveDocument()
original _cnote=Tools.CustomNote.Create(
    strNoteName="CustomNote _1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection _1", 
    listContent=["Original Note"], 
    iAlignment=1)

# Prepare a new document.
doc2=JPT.CreateNewDocument()

# Create a custom note and collection in a new document (document 2).
Tools.CustomNote.Create(
    strNoteName="CustomNote _1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection _1", 
    listContent=["Note in new doc"], 
    iAlignment=1)

cnotes _collections=JPT.GetAllByTypeID(JPT.DItemType.CUSTOM _NOTE _COLLECTION)

# Copy custom note in document 1 to document 2.

if cnotes _collections:
    Tools.CustomNote.Copy(
        strSrcDocumentName=doc1.docName, 
        strDestDocumentName=doc2.docName, 
        crlTargets=[original _cnote], 
        strlNames=["CustomNote _1(Copied)"], 
        crCollection=CustomNoteCollection(cnotes _collections[0].id))

JPT.Exec('ViewSpreadNote()')
```
