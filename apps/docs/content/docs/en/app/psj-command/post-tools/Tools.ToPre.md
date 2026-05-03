---
title: "Tools.ToPre()"
description: "Convert the model’s data and the related settings from an opening Post document to a new Pre document. All part names, setting item names and data of setting items in the model are preserved during conversion"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > ToPre"
macro_link: "[ToPre](../../macro/tools/ToPre)"
---

## Description

Convert the model’s data and the related settings from an opening Post document to a new Pre document. All part names, setting item names and data of setting items in the model are preserved during conversion.

## Syntax

```psj
Tools.ToPre(...)
```

## Inputs

### `strName` @type(String) @required

- The name of Pre document will be converted.

### `ilOptions` @type(List\[Integer]) @default(\[])

- The related settings will be converted with model.
  - 0: Group
  - 1: LBC
  - 2: Connection
  - 3: Coordinate
  - 4: Property

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)
# Convert to Pre
data = Tools.ToPre(strName="Static_Renkon", ilOptions=[0, 1, 2, 3, 4])
JPT.SetActiveDocumentByName("Static_Renkon",1)
JPT.Debugger(data)
```
