---
title: "FieldData()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create field data table

## Syntax

```psj
FieldData(String m _strName,int m _iType,TSheetd m _Sheet,Cursor m _crEdit, bool bAbaqusAmp, int iChartType, bool bFrequencyPSDLogX, bool bFrequencyPSDLogY)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of table

<!-- @since:5.0.1 -->
### 2. Int

type of table

<!-- @since:5.0.1 -->
### 3. TSheetd

data of table

<!-- @since:5.0.1 -->
### 4. Cursor

edit field table cursor(81:FieldData ID)

<!-- @since:5.0.1 -->
### 5. Bool

Abaqus Amp bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Int

Smooth step

<!-- @since:5.1.0 -->
### 7. Bool

A _Boolean_ specifying whether or not enable data interplation of LogX for Frequency-PSD table.

<!-- @since:5.1.0 -->
### 8. Bool

A _Boolean_ specifying whether or not enable data interplation of LogY for Frequency-PSD table.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
FieldData("Test", 15, [1, 2, 1000, 1e+08], 0:0, 0, 0, 0, 0)
```
