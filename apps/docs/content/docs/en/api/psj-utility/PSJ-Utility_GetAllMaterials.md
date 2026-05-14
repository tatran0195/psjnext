---
title: "JPT.GetAllMaterials()"
description: "Get all the information of all existing user materials"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all the information of all existing user materials.

## Syntax

```psj
JPT.GetAllMaterials()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[MaterialVector](../data-type/psj-utility/pre-utility/built-in-types/MaterialVector)_ object or _List of [DMaterial](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_ objects containing all the information of all the existing user materials.

## Sample Code

```psj {11}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static _Renkon.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)
# Convert to Pre
data = Tools.ToPre(strName="Static _Renkon", ilOptions=[0, 1, 2, 3, 4])
JPT.SetActiveDocumentByName("Static _Renkon _Converted _Pre",1)
# Get all user materials
userMat = JPT.GetAllMaterials()
JPT.Debugger(userMat)
JPT.Debugger(userMat[0])
```
