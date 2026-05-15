---
title: "ConcentrateFlux()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create concentrate flux

## Syntax

```psj
ConcentrateFlux(String m _strName,double fflux,Cursor crTable,Cursor[] m _taTarget,Cursor m _crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of concentrate flux

<!-- @since:5.0.1 -->
### 2. Double

value of concentrate flux

<!-- @since:5.0.1 -->
### 3. Cursor

select table

<!-- @since:5.0.1 -->
### 4. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 5. Cursor

edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ConcentrateFlux("Test",0.001,1:11,[1:11,2:12],1:11)
```
