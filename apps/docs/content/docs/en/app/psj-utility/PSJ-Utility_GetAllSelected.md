---
title: "JPT.GetAllSelected()"
description: "Get all the information of all selected entities (Connections, Contacts, Parts, ...)"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get all the information of all selected entities (Connections, Contacts, Parts, ...).

## Syntax

```psj
JPT.GetAllSelected()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the selected entities.

## Sample Code

```psj {13}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Select part
listIDParts = [part.id for part in JPT.GetAllParts()]
strIDCursor = " ".join(str(cursor) for cursor in listIDParts)
Home.Find(strSearch=f"{strIDCursor}", strSelectedType="Part")

#Get the information of all selected parts
listSelParts = JPT.GetAllSelected()
JPT.Debugger(listSelParts)
```
