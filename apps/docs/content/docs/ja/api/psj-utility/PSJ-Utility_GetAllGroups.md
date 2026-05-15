---
title: "JPT.GetAllGroups()"
description: "Get all the information of all existing groups"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all the information of all existing groups.

## Syntax

```psj
JPT.GetAllGroups()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[GroupVector](../data-type/psj-utility/pre-utility/built-in-types/GroupVector)_ object or _List of [DGroup](../data-type/psj-utility/pre-utility/built-in-types/DGroup)_ objects containing all the information of all the existing groups.

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Part(1)])
Tools.Group.CreateGroup(strGroupName="Group2", crlTargets=[Face(47, 48, 49, 50, 51, 52)])
Tools.Group.CreateGroup(strGroupName="Group3", crlTargets=[Elem(2784, 2296, 2677, 2295, 3144, 2977)])
JPT.ViewFitToModel()

# Get the information of all existing groups
listDGroups = JPT.GetAllGroups()
JPT.Debugger(listDGroups)

# Print all the related information of each existing group in list
for group in listDGroups:
    JPT.Debugger(group)
```
