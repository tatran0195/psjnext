---
title: "Home.Preferences.Export()"
description: "Export settings of Preferences (.json file)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > Preferences > Export"
macro _link: "ExportPreferenceSettings"
---

## Description

Export settings of Preferences (.json file).

## Syntax

```psj
Home.Preferences.Export(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The export file path.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj
Home.Preferences.Export("C:/temp/DCADPreference.json")
```
