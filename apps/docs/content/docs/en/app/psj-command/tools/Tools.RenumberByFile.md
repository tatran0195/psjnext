---
title: "Tools.RenumberByFile()"
description: "Renumber the model by a CSV file. The renumber targets are Nodes, 2D Elements, 3D Elements"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > RenumberByFile"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Renumber the model by a CSV file. The renumber targets are Nodes, 2D Elements, 3D Elements.

## Syntax

```psj
Tools.RenumberByFile(...)
```

## Inputs

### `strCSVPath` @type(String) @required

- The path of CSV file. The CSV file must correspond correctly with the model, can not use a different CSV for a different model.

### `iConflictStrategy` @type(Integer) @default(0)

- The conflict strategy. This parameter is used to apply to Share Face/Node case, by choosing the method that assigning ID of Share Face/Nodes would belong to which part.
  - I&#x66;_&#x69;ConflictStrategy=0_: Less ID({'<'}) method, when the Share Face/Nodes existing in model, the ID of them when renumber will belong to the Part has smaller ID.
  - I&#x66;_&#x69;ConflictStrategy=1_: Great ID({'<'}) method, when the Share Face/Nodes existing in model, the ID of them when renumber will belong to the Part has larger ID.

### `bNeedToUpdateCount` @type(Boolean) @default(False)

- The option to activate the counter update of each model for each component(Nodes, 2D, 3D). The counter is a value that represents the total amount of each component.
  - I&#x66;_&#x54;rue_: The counter will update
  - I&#x66;_&#x46;alse_: The counter will not update

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {10}
jpt_path = JPT.GetAppPathInfo((JPT.PathType.PROGRAM_PATH))

sample_model = jpt_path + 'SampleData\\PSJ\\PSJ-Utility\\JtdbSample\\RenumberByFile.jth5'
sample_csv = jpt_path + 'SampleData\\PSJ\\PSJ-Utility\\Utils\\RenumberByFile.csv'

#import model
FileMenu.LoadJTH5(sample_model)
JPT.ViewFitToModel()

result = Tools.RenumberByFile(strCSVPath = sample_csv)
JPT.Debugger(result)
```
