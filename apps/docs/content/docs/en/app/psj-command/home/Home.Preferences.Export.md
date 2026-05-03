---
title: "Home.Preferences.Export()"
description: "Export settings of Preferences (.json file)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Preferences > Export"
macro_link: "ExportPreferenceSettings"
---

## Description

Export settings of Preferences (.json file).

## Syntax

```psj
Home.Preferences.Export(...)
```

## Inputs

### `strPath` @type(String) @required

- Export file path.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj
Home.Preferences.Export("C:/temp/DCADPreference.json")
```
