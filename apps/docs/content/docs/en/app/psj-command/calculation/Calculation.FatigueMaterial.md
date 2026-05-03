---
title: "Calculation.FatigueMaterial()"
description: "Load the fatigue limit diagrams for each material"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Calculation > FatigueMaterial"
macro_link: ""
---

## Description

Load the fatigue limit diagrams for each material.

## Syntax

```psj
Calculation.FatigueMaterial(...)
```

## Inputs

### `strlFilePaths` @type(List\[String]) @required

- The path of fatigue limit diagram file (\*.csv).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {12,13}
# Please prepare the input files for Durability > Fatigue Material calculation
op2_path = ".../FatigueMaterial.op2"
csv_path = [".../FatigueMaterial.csv"]
# Import result model
Home.ImportResults.Nastran(
    strPath=op2_path, 
    bReadLoadAndConstraint=True, 
    bReadConnection=True, 
    bCreateResultsAtMidNode=True)

# Durability > Fatigue Material
ret = Calculation.FatigueMaterial(
    strlFilePaths=csv_path)
print(ret)
```
