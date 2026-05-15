---
title: "PostToolsSubcaseSafetyFactor()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create a subcase by calculating the safety factor from the selected subcases based on the tolerance of each part.

## Syntax

```psj
PostToolsSubcaseSafetyFactor(int iAnalysisType, int iResultSet, list int listSubcases, list SAFETY _ITEM listSafetyItems, int iSafetyType, str strResultName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

- An Integer specifying the analysis type.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying result set.

<!-- @since:5.1.0 -->
### 3. list int

- A List of Integer specifying the IDs of selected subcases.

<!-- @since:5.1.0 -->
### 4. list SAFETY\_ITEM

- A _List of [SAFETY\_ITEM](../../data-type/psj-command/parameter-types/SAFETY _ITEM)_ specifying the safety information of each selected target.

<!-- @since:5.1.0 -->
### 5. int

- An Integer specifying the type of safety calculation.

<!-- @since:5.1.0 -->
### 6. str

- A String specifying the name of subcase to be created.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostToolsSubcaseSafetyFactor(2, 1, [(1, "", 1, 1), (2, "", 1, 1), (3, "", 1, 1), (4, "", 1, 1), (5, "", 1, 1)], [(3:1, 1), (3:2, 1), (3:3, 1)], 1, "Safety Break2")
```
