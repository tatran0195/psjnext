---
title: "Tools.CustomNote.Copy()"
description: "Copy custom notes."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > CustomNote > Copy"
macro_link: "CopyCustomNote"
---

## Description

Copy custom notes.

## Syntax

```psj
Tools.CustomNote.Copy(...)
```

## Inputs

### `strSrcDocumentName` @type(String) @default('')

- Name of document that have original custom notes to copy.

### `strDestDocumentName` @type(String) @default('')

- Name of document that the indicated custom notes will be copied.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- Original custom notes to copy.

### `strlNames` @type(List\[String]) @default(\[])

- Names of copied custom notes.

### `crCollection` @type(Cursor) @default(None)

- A collection where original custom notes will be copied.

### `bKeep` @type(Boolean) @default(False)

- Whether or not

## Return Code

A _Boolean_ specifying copy custom note works successfully or not.

## Sample Code

```psj{26-31}
# Create a custom note and collection in document 1.
doc1=JPT.GetActiveDocument()
original_cnote=Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection_1", 
    listContent=["Original Note"], 
    iAlignment=1)

# Prepare a new document.
doc2=JPT.CreateNewDocument()

# Create a custom note and collection in a new document (document 2).
Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection_1", 
    listContent=["Note in new doc"], 
    iAlignment=1)

cnotes_collections=JPT.GetAllByTypeID(JPT.DItemType.CUSTOM_NOTE_COLLECTION)

# Copy custom note in document 1 to document 2.

if cnotes_collections:
    Tools.CustomNote.Copy(
        strSrcDocumentName=doc1.docName, 
        strDestDocumentName=doc2.docName, 
        crlTargets=[original_cnote], 
        strlNames=["CustomNote_1(Copied)"], 
        crCollection=CustomNoteCollection(cnotes_collections[0].id))

JPT.Exec('ViewSpreadNote()')
```
