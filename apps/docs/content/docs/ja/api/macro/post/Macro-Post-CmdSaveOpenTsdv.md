---
title: "CmdSaveOpenTsdv()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Save / Load calculation results in Post Tools Window into / from csv file.

## Syntax

```psj
CmdSaveOpenTsdv(string fileName, bool SaveLoad, cursor[] calculations, bool bdfMode)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Save / Load file path.

<!-- @since:5.1.0 -->
### 2. bool

Save or Load. 0: save, 1: load.

<!-- @since:5.1.0 -->
### 3. cursor\[]

Target calculations.

<!-- @since:5.1.0 -->
### 4. bool

Specifying the condition to read/write the load in bdf or normal format.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 2. int

Save or Load. 0: save, 1: load.

## Return Code

Nothing.

## Sample Code

```psj
CmdSaveOpenTsdv("C:/Temp/frequency.tsdv", 0, [195:1, 195:2], 0)
```
