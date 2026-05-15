---
title: "TemperatureLoad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create temperature load

## Syntax

```psj
TemperatureLoad(string m _strName,int nType,double fTemp,string strFilePathName,
    Cursor crTable,Cursor[] m _taTarget,Cursor m _crEdit,bool bUseAsMaterialReferenceTemp)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of temperature load

<!-- @since:5.0.1 -->
### 2. Int

type\[0:Constant; 1:Nastran Punch]

<!-- @since:5.0.1 -->
### 3. Double

value of temperature

<!-- @since:5.0.1 -->
### 4. String

file path

<!-- @since:5.0.1 -->
### 5. Cursor

select table

<!-- @since:5.0.1 -->
### 6. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 7. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 8. Bool

if use as material reference temperature

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
TemperatureLoad("Test",1,0.001,"Test",1:11,[1:11,2:12],1:11,1)
```
