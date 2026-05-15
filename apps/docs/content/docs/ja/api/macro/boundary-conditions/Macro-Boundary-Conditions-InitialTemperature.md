---
title: "InitialTemperature()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

create initial temperature

## Syntax

```psj
InitialTemperature(string strName, int iLocalTemperatureUnit, int nType, double dTemp, string strFilePathName, bool bUseDefault, cursor crTable, cursor[] taTarget, cursor crEdit, int iTimeID, bool bSkipUnvailableNode, int[] vecUnvailableNodeId)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Initial temperature name

<!-- @since:5.0.1 -->
### 2. Int

Unit of local temperature

<!-- @since:5.1.0 -->
### 3. Int

Thermal type

- 0: Constant
- 2: ADVC File
- 3: Nastran Punch

<!-- @since:5.1.0 -->
### 4. Double

Temperature value

<!-- @since:5.1.0 -->
### 5. String

directory file path
Corresponding to Thermal type 2 and 3

<!-- @since:5.1.0 -->
### 6. Bool

Use default temperature bool flag True = 1, False = 0; corresponding to Thermal type 2 and 3

<!-- @since:5.1.0 -->
### 7. Cursor

Table cursor

<!-- @since:5.1.0 -->
### 8. Cursor\[]

Target entities cursor

<!-- @since:5.1.0 -->
### 9. Cursor

Edit cursor

<!-- @since:5.1.0 -->
### 10. Int

Time Step ID in Result
Corresponding to Thermal type 3.

<!-- @since:5.1.0 -->
### 11. Bool

Skip inexistent nodes or not.
Corresponding to Thermal type 3.

<!-- @since:5.1.0 -->
### 12. Int\[]

The list of skip nodes' ID
Corresponding to Thermal type 3.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Double

Temperature value

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 4. String

directory file path

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 5. Bool

Use default temperature bool flag True = 1, False = 0; corresponding to Type 2, 3

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 6. Cursor

Table cursor

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 7. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 8. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
InitialTemperature("InitialTemperature _1", 1, 0, 274.15, "", 1, 0:0, [], 0:0, 0, 0, [])
```
