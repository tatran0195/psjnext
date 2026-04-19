---
id: BoundaryConditions.TemperatureLoads.NastranPunch
title: BoundaryConditions.TemperatureLoads.NastranPunch()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create temperature load by using Nastran punch
---

## Description

Create temperature load by using Nastran punch.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.NastranPunch(...)
```

Ribbon: <menuselection>BoundaryConditions &#187; TemperatureLoads &#187; NastranPunch</menuselection>

## Inputs

### `strName`

- A _String_ specifying the name.
- The default value is "TemperatureLoadsPunch1".

### `strFilePathName`

- A _String_ specifying the file path name.
- The default value is "".

### `crTable`

- A _Cursor_ specifying the table.
- The default value is None.

### `crlTargets`

- A _List of Cursor_ specifying the target.
- The default value is [].

### `crEdit`

- A _Cursor_ specifying the edit.
- The default value is None.

### `bUseAsMaterialReferenceTemp`

- A _Boolean_ specifying the use as material reference temperature.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.
