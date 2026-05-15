---
title: "Property1DPlot()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create property 1D Plot

## Syntax

```psj
Property1DPlot(string strName, int iPlotID, cursor[] taTarget, cursor crCoord)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Plot name

<!-- @since:5.0.1 -->
### 2. Int

Plot ID

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target entity cursor

<!-- @since:5.0.1 -->
### 4. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property1DPlot("PLOT _4", 4, [5:104, 10:692], 0:0)
```
