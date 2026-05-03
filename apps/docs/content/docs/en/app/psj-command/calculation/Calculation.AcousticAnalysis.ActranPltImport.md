---
title: "Calculation.AcousticAnalysis.ActranPltImport()"
description: "Create intensity from the sound pressure and particle velocity results"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > AcousticAnalysis > ActranPltImport"
macro_link: "[PostImportActranPlt](../../macro/calculation/PostImportActranPlt)"
---

## Description

Create intensity from the sound pressure and particle velocity results.

## Syntax

```psj
Calculation.AcousticAnalysis.ActranPltImport(...)
```

## Inputs

### `strPath` @type(String) @required

- The Actran (\*.plt) file to be imported.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {4}
#Please set path to your sample actran file.
filePath="C:/Temp/Sample.plt"

plt = Calculation.AcousticAnalysis.ActranPltImport(strPath=filePath)
JPT.Debugger(plt)
```
