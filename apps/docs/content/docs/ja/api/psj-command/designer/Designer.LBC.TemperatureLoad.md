---
title: "Designer.LBC.TemperatureLoad()"
description: "create temperature load Desiner"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Designer > LBC > TemperatureLoad"
---

## Description

Create temperature load Desiner

## Syntax

```psj
Designer.LBC.TemperatureLoad(strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTargets=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iDnType

- Specify the dn type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFTemp

- Specify the temperature.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strDstrFilePathName

- Specify the dstr file path name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crDcrTable

- Specify the dcr table.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### bDbUseAsMaterialReferenceTemp

- Specify the db use as material reference temperature.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Designer.LBC.TemperatureLoad(strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTargets=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False)
```
