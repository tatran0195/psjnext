---
title: "Home.Preferences.Import()"
description: "Import settings of Preferences (.json file)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > Preferences > Import"
macro _link: "ImportPreferenceSettings"
---

## Description

Export settings of Preferences (.json file).

## Syntax

```psj
Home.Preferences.Import(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The import file path.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj
Home.Preferences.Import("C:/temp/DCADPreference.json")
```
