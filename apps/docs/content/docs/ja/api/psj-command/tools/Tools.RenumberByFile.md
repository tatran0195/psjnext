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

<!-- @since:5.0.1 @required -->
### strCSVPath

- Specify the path of CSV file. The CSV file must correspond correctly with the model, can not use a different CSV for a different model.

<!-- @since:5.0.1 @optional -->
### iConflictStrategy

- Specify the conflict strategy. This parameter is used to apply to Share Face/Node case, by choosing the method that assigning ID of Share Face/Nodes would belong to which part.
  - If _iConflictStrategy=0_: Less ID({'<'}) method, when the Share Face/Nodes existing in model, the ID of them when renumber will belong to the Part has smaller ID.
  - If _iConflictStrategy=1_: Great ID({'<'}) method, when the Share Face/Nodes existing in model, the ID of them when renumber will belong to the Part has larger ID.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bNeedToUpdateCount

- Specify the option to activate the counter update of each model for each component(Nodes, 2D, 3D). The counter is a value that represents the total amount of each component.
  - If _True_: The counter will update
  - If _False_: The counter will not update
- The default value is _False_.

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
