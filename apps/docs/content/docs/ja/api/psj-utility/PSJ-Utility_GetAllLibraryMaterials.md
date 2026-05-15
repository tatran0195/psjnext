---
title: "JPT.GetAllLibraryMaterials()"
description: "Get all the information of all library materials"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all the information of all library materials.

## Syntax

```psj
JPT.GetAllLibraryMaterials()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[MaterialLibVector](../data-type/psj-utility/pre-utility/built-in-types/MaterialLibVector)_ object or _List of [DMaterialLib](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_ objects containing all the information of all the existing user materials.

## Sample Code

```psj {11}
# Get all library materials
libMat = JPT.GetAllLibraryMaterials()
print(f"There are {len(libMat)} materials in the library")
JPT.Debugger(libMat)
JPT.Debugger(libMat[0])
```
