---
title: "JPT.GetAllMeasureNoteCollections()"
description: "Get all the information of all measure note collections"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all the information of all existing measure note collections.

## Syntax

```psj
JPT.GetAllMeasureNoteCollections()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[MeasureNoteVector](../data-type/psj-utility/pre-utility/built-in-types/MeasureNoteVector)_ object or _List of [DMeasureNote](../data-type/psj-utility/pre-utility/built-in-types/DMeasureNote)_ objects containing all the information of all the existing edges.

## Sample Code

```psj {25}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

Tools.Measure.Angle.CreateMeasureNote.ThreeNodes(
    strNoteName="Angle _1", 
    crFirstNode=Node(472), 
    crSecondNode=Node(83), 
    crThirdNode=Node(447)
    )

Tools.Measure.Area.CreateMeasureNote.Element(
    strNoteName="Area _1", 
    crlElements=[Elem(1001)]
    )

Tools.Measure.Radius.CreateMeasureNote.ThreeNodes(
    strNoteName="Radius _1", 
    crFirstNode=Node(189), 
    crSecondNode=Node(191), 
    crThirdNode=Node(216)
    )

JPT.ViewFitToModel()

listDMeasureNoteCollections = JPT.GetAllMeasureNoteCollections()
JPT.Debugger(listDMeasureNoteCollections)
```
