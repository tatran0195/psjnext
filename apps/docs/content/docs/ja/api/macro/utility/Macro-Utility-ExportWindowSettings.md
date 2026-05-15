---
title: "ExportWindowSettings()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export the settings of dockable windows into the .reg file.

## Syntax

```psj
ExportWindowSettings(String FilePath)
```

## Inputs

### \`1. String

Export file name (.reg)

## Return Code

This function does not have return value.

## Sample Code

```psj
JPT.Exec('ExportWindowSettings("C:/Temp/JupiterWindowSettings.reg")')
```
