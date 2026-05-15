---
title: "ForceGeneral()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Force general

## Syntax

```psj
ForceGeneral(string name, vector force, vector moment, int arrowDir, int distributionMethod,
    cursor crCoordinate, cursor crTable, cursor crNodeSet, double phase, double delay,
    cursor crPhaseTable, string formulaFX, string formulaFY, string formulaFZ,
    string formulaMX, string formulaMY, string formulaMZ, Cursor[] targets, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name

<!-- @since:5.0.1 -->
### 2. Vector

force

<!-- @since:5.0.1 -->
### 3. Vector

moment

<!-- @since:5.0.1 -->
### 4. Int

arrorDir (0: Start at node, 1: End at node)

<!-- @since:5.0.1 -->
### 5. Int

distributionMethod (0: Per selected entity, 1: Per node, 2: Total of select

<!-- @since:5.0.1 -->
### 6. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 7. Cursor

table

<!-- @since:5.0.1 -->
### 8. Cursor

node set

<!-- @since:5.0.1 -->
### 9. Double

phase

<!-- @since:5.0.1 -->
### 10. Double

delay

<!-- @since:5.0.1 -->
### 11. Cursor

phase table

<!-- @since:5.0.1 -->
### 12. String

formula of Force X

<!-- @since:5.0.1 -->
### 13. String

formula of Force Y

<!-- @since:5.0.1 -->
### 14. String

formula of Force Z

<!-- @since:5.0.1 -->
### 15. String

formula of Moment X

<!-- @since:5.0.1 -->
### 16. String

formula of Moment Y

<!-- @since:5.0.1 -->
### 17. String

formula of Moment Z

<!-- @since:5.0.1 -->
### 18. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 19. Cursor

edit target

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ForceGeneral("Force2", [1, 2, 3], [0.004, 0.005, 0.006], 0, 0, 0:0, 0:0, 0:0,
    0, 0, 0:0, "", "", "", "", "", "", [6:25], 0:0)
```
