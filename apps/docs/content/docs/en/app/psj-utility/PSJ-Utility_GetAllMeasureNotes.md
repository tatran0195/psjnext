---
title: "JPT.GetAllMeasureNotes()"
description: "Get all the information of all custom notes"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get all the information of all existing custom notes.

## Syntax

```psj
JPT.GetAllMeasureNotes()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _[MeasureNoteVector](../data-type/psj-utility/pre-utility/built-in-types/MeasureNotevector)_ object or _List of [DMeasureNote](../data-type/psj-utility/pre-utility/built-in-types/DMeasureNote)_ objects containing all the information of all the existing custom notes.

## Sample Code

```psj {21}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
    strNoteName="Distance_1", 
    crFirstNode=Node(250), 
    crSecondNode=Node(261)
    )
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
    strNoteName="Distance_1", 
    crFirstNode=Node(257), 
    crSecondNode=Node(291)
    )
Tools.Measure.Angle.CreateMeasureNote.ThreeNodes(
    strNoteName="Angle_1", 
    crFirstNode=Node(441), 
    crSecondNode=Node(438), 
    crThirdNode=Node(475)
    )

# Get the information of all existing measure notes
listDMeasureNotes = JPT.GetAllMeasureNotes()
JPT.Debugger(listDMeasureNotes)

# Print all the related information of each existing measure notes in list
for measure_note in listDMeasureNotes:
    JPT.Debugger(measure_note)
```
