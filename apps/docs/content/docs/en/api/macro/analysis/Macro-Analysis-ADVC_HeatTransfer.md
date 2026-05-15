---
title: "ADVC _HeatTransfer()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC job (ADVC\_HeatTransfer)

## Syntax

```psj
ADVC _Structure(string Name, string Description, int JobType, cursor[] processSequence,
    cursor[] elemLocationGroup, cursor[] nodeLocationGroup, bool WriteGroup,
    cursor Edit, bool ResultReference, int iSeparateFile, bool ExportRelatedAllLBCs,
    bool UseEntityName, bool MatrixSloverParam, int PreconditionType,
    int MatrixStructure, cursor[] Target, int LoadType,bool SameOutputOnAllProcess,
    bool DeleteFloatingNode, bool BC, bool CheckBCDuplicate, bool AutoAssignDummyProp,
    cursor crDummyPropMaterial, bool ReferenceRestartData, string ReferenceRestartDataPath,
    int ReferenceRestartDataProcessNum, int ReferenceRestartDataStepNum,
    int ReferenceRestartDataCoordType, int ReferenceRestartDataUpdateContactSearch, 
    LoadNodeData[] LoadData, int HeatConvection, string Path, int NumType, int UiWidth, 
    int UiPrecision, bool ExportGeometryID, bool SeparatePartInfoFile,
    string ADVCTemplateFilePath, bool OutputDefinition, int DetaFormatType
)
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

Job type \[1:Heat Transfer]

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

Separated file type\[0:None; 1:By Model; 2:By Body; 3:By Selected Body; 4:Select LBCs]

<!-- @since:5.0.1 -->
### 11. Bool

Export all related LBCs flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 12. Bool

Use entity name flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 13. Bool

MatrixSolverParam (not used for Heat Transfer), set false = 0

<!-- @since:5.0.1 -->
### 14. int

iPreconditionType (not used for Heat Transfer), set 0.

<!-- @since:5.0.1 -->
### 15. int

MatrixStructure (not used for Heat Transfer), set 0.

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
### 31. int

Heat convection \[0:Direct; 1:Indirect]

<!-- @since:5.0.1 -->
### 32. String

Exported adx file path

<!-- @since:5.0.1 -->
### 33. int

Numric type.  \[0:Real; 1:Power, 2:Auto]

<!-- @since:5.0.1 -->
### 34. int

UI Width

<!-- @since:5.0.1 -->
### 35. int

UI Precision

<!-- @since:5.0.1 -->
### 36. bool

Export geometry id flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 37. bool

Separate part info file flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 38. string

ADVC Template file path

<!-- @since:5.0.1 -->
### 39. bool

Output definition flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 40. bool

Data format type. \[0:Single; 1:Double]

## Return Code

- "1": The function can be executed
- "FAILED": The function cannot be executed

## Sample Code

```psj
ADVC _HeatTransfer("Job _1", "", 1, [128:1], [], [], 0, 0:0, 0, 0, 0, 0, 0, 0, 0, [3:1], 1, 1, 1, 1, 0, 1, 22:1, 0, "", 2147483647, 2147483647, 0, 1, [], 1, "C:/Temp/Job _1.adx", 0, 10, 7, 0, 0, "", 1, 0)
```
