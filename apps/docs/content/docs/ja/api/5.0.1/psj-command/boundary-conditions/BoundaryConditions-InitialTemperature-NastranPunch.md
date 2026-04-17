---
id: BoundaryConditions.InitialTemperature.NastranPunch
title: BoundaryConditions.InitialTemperature.NastranPunch()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Load the temperature result output in Nastran Punch format and set as the initial temperature
---

## Description

Load the temperature result output in Nastran Punch format and set as the initial temperature.

## Syntax

```psj
BoundaryConditions.InitialTemperature.NastranPunch(...)
```

Ribbon: <menuselection>BoundaryConditions &#187; InitialTemperature &#187; NastranPunch</menuselection>

## Inputs

### `strName`

- A _String_ specifying the initial temperature name.
- The default value is "InitialTemperature1".

### `strFilePathName`

- A _String_ specifying the Nastran temperature result file path.
- The default value is "".

### `bUseDefault`

- A _Boolean_ enable/disable default temperature.
- The default value is False.

### `crlTargets`

- A _List of Cursor_ specifying list the target parts for initial temperature.
- The default value is [].

### `crEdit`

- A _Cursor_ specifying the initial temperature item which use for editing.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.
