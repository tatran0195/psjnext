---
title: "JPT.GetAllCustomNoteCollections()"
description: "Get all the information of all custom note collections"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get all the information of all existing custom note collections.

## Syntax

```psj
JPT.GetAllCustomNoteCollections()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[CustomNoteVector](../data-type/psj-utility/pre-utility/built-in-types/CustomNoteVector)_ object or _List of [DCustomNote](../data-type/psj-utility/pre-utility/built-in-types/DCustomNote)_ objects containing all the information of all the existing CustomNotes.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection_1", 
    listContent=["Note 1"], 
    iBackgroundColor=15794160, 
    iOutlineColor=14772545, 
    iArrowColor=16711680, 
    iFontSize=16, 
    iAlignment=1
    )
Tools.CustomNote.Create(
    strNoteName="CustomNote_2", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection_2", 
    listContent=["Note 2"], 
    iFontSize=16, 
    iBackgroundColor=11394815, 
    iOutlineColor=128, 
    iArrowColor=3937500, 
    iAlignment=1
    )
Tools.CustomNote.Create(
    strNoteName="CustomNote_3", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    crParentCollection=CustomNoteCollection(2), 
    listContent=["Note 3"], 
    iFontSize=16, bBold=True, 
    iBackgroundColor=14480885, 
    iOutlineWidth=2, 
    iOutlineColor=25600, 
    iArrowColor=9498256, 
    iArrowType=0
    )
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()
JPT.Exec('ViewSpreadNote()')

# Get the information of all existing Custom Notes
listDCustomNoteCollections = JPT.GetAllCustomNoteCollections()
JPT.Debugger(listDCustomNoteCollections)

# Print all the related information of each existing custom note in list
for custom_note in listDCustomNoteCollections:
    JPT.Debugger(custom_note)
```
