---
title: "JPT.GetAllPartsInSubAssembly()"
description: "Get all the information of all parts under the inputted sub-assembly"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all the information of all parts under the inputted sub-assembly.

## Syntax

```psj
JPT.GetAllPartsInSubAssembly(subAssem)
```

## Inputs

<!-- @since:5.0.1 @required -->
### subAssem

- Specify the inputted sub-assembly.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects specifying the parts belonging to the inputted sub-assembly.

## Sample Code

```psj {16}
# Prepare model
Geometry.Part.Cube(iPartColor=15426917)
Geometry.Part.Cube(strName="Cube _2", iPartColor=13390932)
Geometry.Part.Cube(strName="Cube _3", iPartColor=16448103)
Geometry.Part.Cube(strName="Cube _4", iPartColor=13619046)
Geometry.Part.Cube(strName="Cube _5", iPartColor=7861111)
JPT.ViewFitToModel()
Assembly.RightClick.AddSubAssembly()

# Copy all parts to the created Subassembly
currentDoc = JPT.GetActiveDocument()
Assembly.RightClick.TransferDocumentData(strSourceDocTitle=currentDoc.docName, 
                                        strDestDocTitle=currentDoc.docName, 
                                        crlParts=[Part(part.id) for part in JPT.GetAllParts()], 
                                        strlNewPartName=[], 
                                        crDestAssemblyInstance=Inst(1))

# Get the information of all parts belonging to the inputted sub-assembly
listPartsInSubAssembly = JPT.GetAllPartsInSubAssembly(JPT.FindSubAssemblyByID(1))
JPT.Debugger(listPartsInSubAssembly)
```
