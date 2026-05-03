---
title: "Home.Preferences.SaveLoad.CalculateTrescaStress()"
description: "Calculate the Tresca stress and add it to the results tree."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Preferences > SaveLoad > CalculateTrescaStress"
macro_link: "[SetDisplayPostAssemblyTree](../../macro/preferences/SetDisplayPostAssemblyTree)"
---

## Description

Calculate the Tresca Stress automatically when the result file is opened.

## Syntax

```psj
Home.Preferences.SaveLoad.CalculateTrescaStress(...)
```

## Inputs

### `bUseTrescaStress` @type(Boolean) @default(True)

- Whether to use Tresca Stress calculation.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj
Home.Preferences.SaveLoad.CalculateTrescaStress(bUseTrescaStress = False)
```
