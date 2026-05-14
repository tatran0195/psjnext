---
title: "Tools.RenumberByFile()"
description: "Renumber the model by a CSV file. The renumber targets are Nodes, 2D Elements, 3D Elements"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > RenumberByFile"
---

## Description

Renumber the model by a CSV file. The renumber targets are Nodes, 2D Elements, 3D Elements.

## Syntax

```psj
Tools.RenumberByFile(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strCSVPath`

- The path of CSV file. The CSV file must correspond correctly with the model, can not use a different CSV for a different model.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConflictStrategy`

- The conflict strategy. This parameter is used to apply to Share Face/Node case, by choosing the method that assigning ID of Share Face/Nodes would belong to which part.
  - If _iConflictStrategy=0_: Less ID({'<'}) method, when the Share Face/Nodes existing in model, the ID of them when renumber will belong to the Part has smaller ID.
  - If _iConflictStrategy=1_: Great ID({'<'}) method, when the Share Face/Nodes existing in model, the ID of them when renumber will belong to the Part has larger ID.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bNeedToUpdateCount`

- The option to activate the counter update of each model for each component(Nodes, 2D, 3D). The counter is a value that represents the total amount of each component.
  - If _True_: The counter will update
  - If _False_: The counter will not update

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {10}
jpt _path = JPT.GetAppPathInfo((JPT.PathType.PROGRAM _PATH))

sample _model = jpt _path + 'SampleData\\PSJ\\PSJ-Utility\\JtdbSample\\RenumberByFile.jth5'
sample _csv = jpt _path + 'SampleData\\PSJ\\PSJ-Utility\\Utils\\RenumberByFile.csv'

#import model
FileMenu.LoadJTH5(sample _model)
JPT.ViewFitToModel()

result = Tools.RenumberByFile(strCSVPath = sample _csv)
JPT.Debugger(result)
```
