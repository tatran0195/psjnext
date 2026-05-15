---
title: "AdvcJob()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC job

## Syntax

```psj
AdvcJob(string Name, string Description, int eJobType, cursor[] processSequence,
    cursor[] elemLocationGroup, cursor[] nodeLocationGroup, bool WriteGroup,
    cursor Edit, bool ResultReference, int iSeparateFile, bool ExportRelatedAllLBCs,
    bool UseEntityName, bool MatrixSloverParam, int PreconditionType,
    int MatrixStructure, cursor[] Target, int LoadType,bool SameOutputOnAllProcess,
    bool DeleteFloatingNode, bool BC, bool CheckBCDuplicate, bool AutoAssignDummyProp,
    cursor crDummyPropMaterial, bool ReferenceRestartData, string ReferenceRestartDataPath,
    int ReferenceRestartDataProcessNum, int ReferenceRestartDataStepNum,int ReferenceRestartDataCoordType,
    int ReferenceRestartDataUpdateContactSearch, LoadNodeData[] LoadData, int HeatConvection)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Name of ADVC Job

<!-- @since:5.0.1 -->
### 2. String

Description of ADVC Job

<!-- @since:5.0.1 -->
### 3. Int

Job type\[0:Structural; 1:Heat Transfer]

<!-- @since:5.0.1 -->
### 4. Cursor\[]

Advc process sequence

<!-- @since:5.0.1 -->
### 5. Cursor\[]

Element location group

<!-- @since:5.0.1 -->
### 6. Cursor\[]

Node location group

<!-- @since:5.0.1 -->
### 7. Bool

Write group flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 8. Cursor

Edit ADVC Job

<!-- @since:5.0.1 -->
### 9. Bool

Result reference flag true = 1, flase = 0

<!-- @since:5.0.1 -->
### 10. Int

Separated file type\[0:None; 1:By Model; 2:By Body; 3:By Selected Body]

<!-- @since:5.0.1 -->
### 11. Bool

Export all related LBCs flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 12. Bool

Use entity name flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 13. Bool

Define matrix solver parameter flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 14. Int

Precondition type\[0:Scaling; 1:CGCG; 2:CGCG2; 3:CGCG2\_Diag; 4:CGCG2-SOR]

<!-- @since:5.0.1 -->
### 15. Int

Matrix structure \[0:Symmetry; 1:Asymmetry]

<!-- @since:5.0.1 -->
### 16. Cursor\[]

Target list

<!-- @since:5.0.1 -->
### 17. Int

Load type \[0:Load Case; 1:Load]

<!-- @since:5.0.1 -->
### 18. Bool

All outputs are same flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 19. Bool

Delete floating node flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 20. Bool

Boundary condition flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 21. Bool

Check Boundary condition Duplicate flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 22. Bool

Auto Assign Dummy Property

<!-- @since:5.0.1 -->
### 23. Cursor

Dummy Property Material

<!-- @since:5.0.1 -->
### 24. Bool

Reference Restart Data flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 25. String

Reference Restart Data Path

<!-- @since:5.0.1 -->
### 26. Int

Reference Restart Data Process Num

<!-- @since:5.0.1 -->
### 27. Int

Reference Restart Data Step Num

<!-- @since:5.0.1 -->
### 28. Int

Reference Restart Data Coord Type

<!-- @since:5.0.1 -->
### 29. Int

Reference Restart Data Update Contact Search

<!-- @since:5.0.1 -->
### 30. LoadNodeData\[]

LoadNodeData list

<!-- @since:5.0.1 -->
### 31. LoadNodeData

(Cursor data, Cursor modify, int flag, double contactInterference, bool shrink, int Stabilized, double residualFactor, double EffectiveDist, int Type, double CN, double CT)

<!-- @since:5.0.1 -->
### 32. Int

Heat Convection

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AdvcJob("ADVC", "", 1, [128:2], [], [], 0, 0:0, 0, 0, 0, 0, 0, 0, 0, [3:1],
    1, 1, 1, 1, 0, 1, 22:2, 0, "", 2147483647, 2147483647, 0, 1, [], 1)
```
