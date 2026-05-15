---
title: "CreateAbaqusJob()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Abaqus Job

## Syntax

```psj
CreateAbaqusJob(string m _strName,bool m _bRBE2toMPC,bool m _bRenameProcess,
    int m _iCodeType,int m _iSurfDefType,int m _iUnit,int m _iWriteType,
    string m _strDescription,cursor[] m _taStepSequence,cursor m _crEditCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Job Name

<!-- @since:5.0.1 -->
### 2. Bool

Output REB3 as MPC

<!-- @since:5.0.1 -->
### 3. Bool

Rename Step or not

<!-- @since:5.0.1 -->
### 4. Int

Output REB3 as MPC

<!-- @since:5.0.1 -->
### 5. Int

Surface Definiation\[0:by element set 1:by element]

<!-- @since:5.0.1 -->
### 6. Int

unit system

<!-- @since:5.0.1 -->
### 7. Int

Output type\[0: by model 1: by selected bodies]

<!-- @since:5.0.1 -->
### 8. String

Description for this Job

<!-- @since:5.0.1 -->
### 9. Cursor\[]

Steps applied on this Job

<!-- @since:5.0.1 -->
### 10. Cursor

Edit Job cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateAbaqusJob("Abaqus", 0, 0, 0, 0, 1, 0, "", [], 0:0, [], 0, 0, 0, 0, 1, 22:2)
```
