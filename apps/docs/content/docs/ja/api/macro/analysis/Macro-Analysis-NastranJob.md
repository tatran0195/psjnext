---
title: "NastranJob()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Nastran job

## Syntax

```psj
NastranJob(string strName, string strDescription, TCursor[] taTarget, int solverType,
    int writeType, int gridFormatType, int deleteFloatingNodes, int continuanceMarker,
    int defineLbcId, int definedLoadId, int definedSpcId, int definedMpcId,
    int uniqueLbcId, int useCASI, double epsilon, int maxNumOfIter, int memory,
    int paramInrel, int ncpu, int solNo, string includeFilePath, [double startFreq,
    double endFreq, int noOfModes], [double startFrequency, double increment, int numOfInc,
    int tableId], [int numOfSteps, double timeIncrement, int outputInterval, int dampingType,
    int modalDampingTableId], [int value _Displacement, int value _SpcForces, int value _Oload,
    int value _MpcForces, int value _Stress, int value _Strain, int value _Force,
    int value _StrainEnergy, int value _Bcresult, int value _Sdisplacement, int value _Acceleration,
    int value _Velocity, int value _Meffmass, int value _Thermal, int value _Flux, int type _Displacement,
    int type _SpcForces, int type _Oload, int type _MpcForces, int type _Stress, int type _Strain,
    int type _Force, int type _StrainEnergy, int type _Bcresult, int type _Sdisplacement,
    int type _Acceleration, int type _Velocity, int type _Meffmass, int type _Thermal,
    int type _Flux], [int GEOMCHECK _NONE], [int ECHO, string title],
    [double subcaseIdForLoad, double subcaseIdForDload, double subcaseIdForSpc, double subcaseIdForMpc,
    double subcaseIdForTempInit, double subcaseIdForTempLoad], [int POST, int OGEOM, int AUTOSPC,
    string GRDPNT, string WTMASS, string K6ROT, string MAXRATIO, int BAILOUT,
    int PRGPST, int RESVEC, double G, double HFREQ, double LFREQ, double W3, double W4 int MEFFMASS,
    int MEFFMASS _GRID _ID], [int NINC, int KMETHOD, int MAXITER, int useEPSU, int useEPSP, int useEPSW,
    double EPSU, double EPSP, double EPSW], [int NDT, double DT, int MAXITER], [[int id, string title,
    string arbitraryText, int subcaseIdForLoad, int subcaseIdForDload, int subcaseIdForSpc,
    int subcaseIdForMpc, int subcaseIdForTempInit, int subcaseIdForTempLoad, int outputReq _Displacement,
    int outputReq _Stress, int outputReq _Strain, int outputReq _Acceleration, int outputReq _Velocity], ...],
    string systemCellText, string fileManagementText, string executiveControlText, string globalCaseControlText,
    string bulkDataText, int exportModelUnitSystem, TCursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Job name

<!-- @since:5.0.1 -->
### 2. String

Job description

<!-- @since:5.0.1 -->
### 3. TCursor\[]

target

<!-- @since:5.0.1 -->
### 4. int

solverType parameter

<!-- @since:5.0.1 -->
### 5. int

writeType parameter

<!-- @since:5.0.1 -->
### 6. int

gridFormatType parameter

<!-- @since:5.0.1 -->
### 7. int

deleteFloatingNodes parameter

<!-- @since:5.0.1 -->
### 8. int

continuanceMarker parameter

<!-- @since:5.0.1 -->
### 9. int

defineLbcId parameter

<!-- @since:5.0.1 -->
### 10. int

definedLoadId parameter

<!-- @since:5.0.1 -->
### 11. int

definedSpcId parameter

<!-- @since:5.0.1 -->
### 12. int

definedMpcId parameter

<!-- @since:5.0.1 -->
### 13. int

uniqueLbcId parameter

<!-- @since:5.0.1 -->
### 14. int

useCASI parameter

<!-- @since:5.0.1 -->
### 15. double

epsilon parameter

<!-- @since:5.0.1 -->
### 16. int

maxNumOfIter parameter

<!-- @since:5.0.1 -->
### 17. int

numOfThreads parameter

<!-- @since:5.0.1 -->
### 18. int

memory parameter

<!-- @since:5.0.1 -->
### 19. int

paramInrel parameter

<!-- @since:5.0.1 -->
### 20. int

ncpu parameter

<!-- @since:5.0.1 -->
### 21. int

solNo parameter

<!-- @since:5.0.1 -->
### 22. String

includeFilePath parameter

<!-- @since:5.0.1 -->
### 23. double

startFreq parameter

<!-- @since:5.0.1 -->
### 24. double

endFreq parameter

<!-- @since:5.0.1 -->
### 25. int

noOfModes parameter

<!-- @since:5.0.1 -->
### 26. double

startFrequency parameter

<!-- @since:5.0.1 -->
### 27. double

increment parameter

<!-- @since:5.0.1 -->
### 28. int

numOfInc parameter

<!-- @since:5.0.1 -->
### 29. int

tableId parameter

<!-- @since:5.0.1 -->
### 30. int

numOfSteps parameter

<!-- @since:5.0.1 -->
### 31. double

timeIncrement parameter

<!-- @since:5.0.1 -->
### 32. int

outputInterval parameter

<!-- @since:5.0.1 -->
### 33. int

dampingType parameter

<!-- @since:5.0.1 -->
### 34. int

modalDampingTableId parameter

<!-- @since:5.0.1 -->
### 35. int

value\_Displacement parameter

<!-- @since:5.0.1 -->
### 36. int

value\_SpcForces parameter

<!-- @since:5.0.1 -->
### 37. int

value\_Oload parameter

<!-- @since:5.0.1 -->
### 38. int

value\_MpcForces parameter

<!-- @since:5.0.1 -->
### 39. int

value\_Stress parameter

<!-- @since:5.0.1 -->
### 40. int

value\_Strain parameter

<!-- @since:5.0.1 -->
### 41. int

value\_Force parameter

<!-- @since:5.0.1 -->
### 42. int

value\_StrainEnergy parameter

<!-- @since:5.0.1 -->
### 43. int

value\_Bcresults parameter

<!-- @since:5.0.1 -->
### 44. int

value\_Bgresults parameter

<!-- @since:5.0.1 -->
### 45. int

value\_Sdisplacement parameter

<!-- @since:5.0.1 -->
### 46. int

value\_Acceleration parameter

<!-- @since:5.0.1 -->
### 47. int

value\_Velocity parameter

<!-- @since:5.0.1 -->
### 48. int

value\_Meffmass parameter

<!-- @since:5.0.1 -->
### 49. int

value\_Thermal parameter

<!-- @since:5.0.1 -->
### 50. int

value\_Flux parameter

<!-- @since:5.0.1 -->
### 51. int

type\_Displacement parameter

<!-- @since:5.0.1 -->
### 52. int

type\_SpcForces parameter

<!-- @since:5.0.1 -->
### 53. int

type\_Oload parameter

<!-- @since:5.0.1 -->
### 54. int

type\_MpcForces parameter

<!-- @since:5.0.1 -->
### 55. int

type\_Stress parameter

<!-- @since:5.0.1 -->
### 56. int

type\_Strain parameter

<!-- @since:5.0.1 -->
### 57. int

type\_Force parameter

<!-- @since:5.0.1 -->
### 58. int

type\_StrainEnergy parameter

<!-- @since:5.0.1 -->
### 59. int

type\_Bcresults parameter

<!-- @since:5.0.1 -->
### 60. int

type\_Bgresults parameter

<!-- @since:5.0.1 -->
### 61. int

type\_Sdisplacement parameter

<!-- @since:5.0.1 -->
### 62. int

type\_Acceleration parameter

<!-- @since:5.0.1 -->
### 63. int

type\_Velocity parameter

<!-- @since:5.0.1 -->
### 64. int

type\_Meffmass parameter

<!-- @since:5.0.1 -->
### 65. int

type\_Thermal parameter

<!-- @since:5.0.1 -->
### 66. int

type\_Flux parameter

<!-- @since:5.0.1 -->
### 67. int

GEOMCHECK\_NONE parameter

<!-- @since:5.0.1 -->
### 68. int

ECHO parameter

<!-- @since:5.0.1 -->
### 69. String

title parameter

<!-- @since:5.0.1 -->
### 70. int

subcaseIdForLoad parameter

<!-- @since:5.0.1 -->
### 71. int

subcaseIdForDload parameter

<!-- @since:5.0.1 -->
### 72. int

subcaseIdForSpc parameter

<!-- @since:5.0.1 -->
### 73. int

subcaseIdForMpc parameter

<!-- @since:5.0.1 -->
### 74. int

subcaseIdForTempInit parameter

<!-- @since:5.0.1 -->
### 75. int

subcaseIdForTempLoad parameter

<!-- @since:5.0.1 -->
### 76. int

POST parameter

<!-- @since:5.0.1 -->
### 77. int

OGEOM parameter

<!-- @since:5.0.1 -->
### 78. int

AUTOSPC parameter

<!-- @since:5.0.1 -->
### 79. String

GRDPNT parameter

<!-- @since:5.0.1 -->
### 80. String

WTMASS parameter

<!-- @since:5.0.1 -->
### 81. String

K6ROT parameter

<!-- @since:5.0.1 -->
### 82. String

MAXRATIO parameter

<!-- @since:5.0.1 -->
### 83. int

BAILOUT parameter

<!-- @since:5.0.1 -->
### 84. int

PRGPST parameter

<!-- @since:5.0.1 -->
### 85. int

RESVEC parameter

<!-- @since:5.0.1 -->
### 86. double

G parameter

<!-- @since:5.0.1 -->
### 87. double

HFREQ parameter

<!-- @since:5.0.1 -->
### 88. double

LFREQ parameter

<!-- @since:5.0.1 -->
### 89. double

W3 parameter

<!-- @since:5.0.1 -->
### 90. double

W4 parameter

<!-- @since:5.0.1 -->
### 91. int

MEFFMASS parameter

<!-- @since:5.0.1 -->
### 92. int

MEFFMASS\_GRID\_ID parameter

<!-- @since:5.0.1 -->
### 93. int

NINC parameter

<!-- @since:5.0.1 -->
### 94. int

KMETHOD parameter

<!-- @since:5.0.1 -->
### 95. int

MAXITER parameter

<!-- @since:5.0.1 -->
### 96. int

useEPSU parameter

<!-- @since:5.0.1 -->
### 97. int

useEPSP parameter

<!-- @since:5.0.1 -->
### 98. int

useEPSW parameter

<!-- @since:5.0.1 -->
### 99. double

EPSU parameter

<!-- @since:5.0.1 -->
### 100. double

EPSP parameter

<!-- @since:5.0.1 -->
### 101. double

EPSW parameter

<!-- @since:5.0.1 -->
### 102. int

NDT parameter

<!-- @since:5.0.1 -->
### 103. double

DT parameter

<!-- @since:5.0.1 -->
### 104. int

MAXITER parameter

<!-- @since:5.0.1 -->
### 105. int

id parameter

<!-- @since:5.0.1 -->
### 106. String

title parameter

<!-- @since:5.0.1 -->
### 107. String

arbitraryText parameter

<!-- @since:5.0.1 -->
### 108. int

subcaseIdForLoad parameter

<!-- @since:5.0.1 -->
### 109. int

subcaseIdForDload parameter

<!-- @since:5.0.1 -->
### 110. int

subcaseIdForSpc parameter

<!-- @since:5.0.1 -->
### 111. int

subcaseIdForMpc parameter

<!-- @since:5.0.1 -->
### 112. int

subcaseIdForTempInit parameter

<!-- @since:5.0.1 -->
### 113. int

subcaseIdForTempLoad parameter

<!-- @since:5.0.1 -->
### 114. int

outputReq\_Displacement parameter

<!-- @since:5.0.1 -->
### 115. int

outputReq\_Stress parameter

<!-- @since:5.0.1 -->
### 116. int

outputReq\_Strain parameter

<!-- @since:5.0.1 -->
### 117. int

outputReq\_Acceleration parameter

<!-- @since:5.0.1 -->
### 118. int

outputReq\_Velocity parameter

<!-- @since:5.0.1 -->
### 119. String

systemCellText parameter

<!-- @since:5.0.1 -->
### 120. String

fileManagementText parameter

<!-- @since:5.0.1 -->
### 121. String

executiveControlText parameter

<!-- @since:5.0.1 -->
### 122. String

globalCaseControlText parameter

<!-- @since:5.0.1 -->
### 123. String

bulkDataText parameter

<!-- @since:5.0.1 -->
### 124. TCursor

Cursor for edit mode

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
NastranJob("TS-Solver1", "", [], 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1.79769e+308,
    2147483647, 0, 2147483647, 0, 1, 101, "", [1.79769e+308, 1.79769e+308, 2147483647],
    [0, 1.79769e+308, 1.79769e+308, 2147483647, 0, 0, 1.79769e+308, 1.79769e+308, 2147483647],
    [1.79769e+308, 1.79769e+308, 2147483647, 0], [2147483647, 1.79769e+308, 2147483647, 2, 0],
    [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647,
    0, 0, 2147483647, 0, 2147483647, 2147483647, 0, 0, 0, 0, 2147483647, 2147483647, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0], [0, ""], [2147483647, 2147483647,
    2147483647, 2147483647, 2147483647, 2147483647], [-1, 0, 0, "", "", "", "", 2147483647, 2,
    0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 2147483647, 1, 0],
    [1, 3, 1, 0, 0, 1, 0.01, 0.01, 0.01], [2147483647, 1.79769e+308, 2147483647], [],
    "", "", "", "", "", 0, 1, 2, 0:0)
```
