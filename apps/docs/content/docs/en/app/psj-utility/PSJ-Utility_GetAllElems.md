---
title: "JPT.GetAllElems()"
description: "Get all the information of all existing elements"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Get all the information of all existing elements.

:::note

If this function is executed on a Post document, it returns 0. If you want to get all Post elements, please use  _[GetAllPostElems](JPT.GetAllPostElems)_.

:::

## Syntax

```psj
JPT.GetAllElems()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _[ElemVector](../data-type/psj-utility/pre-utility/built-in-types/ElemVector)_ object or _List of [DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ objects containing all the information of all the existing elements.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing elements
listDElems = JPT.GetAllElems()
JPT.Debugger(listDElems)

# Print all the related information of each existing element in list
for elem in listDElems:
    JPT.Debugger(elem)
```
