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

<!-- @since:5.1.0 @optional -->
### strSrcDocumentName

- Specify name of document that have original custom notes to copy.
- The default value is ''.

<!-- @since:5.1.0 @optional -->
### strDestDocumentName

- Specify name of document that the indicated custom notes will be copied.
- The default value is ''.

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify original custom notes to copy.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### strlNames

- Specify names of copied custom notes.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crCollection

- Specify a collection where original custom notes will be copied.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bKeep

- Specify whether or not
- The default value is _False_.

## Return Code

A _Boolean_ specifying copy custom note works successfully or not.

## Sample Code

```pj {26-31}
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
