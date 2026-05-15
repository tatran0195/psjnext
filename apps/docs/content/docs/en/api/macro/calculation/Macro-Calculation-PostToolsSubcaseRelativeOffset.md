---
title: "PostToolsSubcaseRelativeOffset()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create a subcase of relative displacement with zero displacement for any selected nodal ID.

## Syntax

```psj
PostToolsSubcaseRelativeOffset(int iAnalysisType, int iResultSet, int iTimeStep, int iNodeID, int iSubcaseID, str strSubcaseName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

- An Integer specifying the analysis type.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying the result set.

<!-- @since:5.1.0 -->
### 3. int

- An Integer specifying the time step.

<!-- @since:5.1.0 -->
### 4. int

- An Integer specifying the ID of the selected node.

<!-- @since:5.1.0 -->
### 5. int

- An Integer specifying the ID of the subcase to be created.

<!-- @since:5.1.0 -->
### 6. str

- A String specifying the name of subcase to be created.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostToolsSubcaseRelativeOffset(1, 1, 0, 0, 0, "strSubcaseName")
```
