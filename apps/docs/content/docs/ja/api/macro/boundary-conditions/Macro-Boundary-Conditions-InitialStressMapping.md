---
title: "InitialStressMapping()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create mapping stress

## Syntax

```psj
InitialStressMapping(String m _strName,int m _dim,String m _strMappingFilePath,Cursor m _crTable,Cursor m _crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of stress

<!-- @since:5.0.1 -->
### 2. Int

dimension\[0:3D]

<!-- @since:5.0.1 -->
### 3. String

file path

<!-- @since:5.0.1 -->
### 4. Cursor

select table

<!-- @since:5.0.1 -->
### 5. Cursor

edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
InitialStressMapping("Test",1,"Test",1:11,1:11)
```
