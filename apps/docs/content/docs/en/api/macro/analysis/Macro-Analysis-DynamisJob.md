---
title: "DynamisJob()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Dynamis job

## Syntax

```psj
DynamisJob(string strName, string strDescription, TCursor[] taTarget, int solverType,
    int writeType, int gridFormatType, int deleteFloatingNodes, int continuanceMarker,
    int defineLbcId, int definedLoadId, int definedSpcId, int definedMpcId, int uniqueLbcId,
    int useCASI, double epsilon, int maxNumOfIter, int memory, int paramInrel, int ncpu,
    int solNo, string includeFilePath, [double startFreq, double endFreq, int noOfModes],
    [double startFrequency, double increment, int numOfInc, int tableId],
    [int numOfSteps, double timeIncrement, int outputInterval, int dampingType, int modalDampingTableId],
    [int value _Displacement, int value _SpcForces, int value _Oload, int value _MpcForces,
    int value _Stress, int value _Strain, int value _Force, int value _StrainEnergy, int value _Bcresults,
    int value _Bgresults, int value _Sdisplacement, int value _Acceleration, int value _Velocity,
    int value _Meffmass, int value _Thermal, int value _Flux, int type _Displacement,
    int type _SpcForces, int type _Oload, int type _MpcForces, int type _Stress, int type _Strain,
    int type _Force, int type _StrainEnergy, int type _Bcresults, int type _Bgresults, int type _Sdisplacement,
    int type _Acceleration, int type _Velocity, int type _Meffmass, int type _Thermal, int type _Flux],
    [int GEOMCHECK _NONE], [int ECHO, string title], [double subcaseIdForLoad, double subcaseIdForDload,
    double subcaseIdForSpc, double subcaseIdForMpc, double subcaseIdForTempInit, double subcaseIdForTempLoad],
    [int POST, int OGEOM, int AUTOSPC, string GRDPNT, string WTMASS, string K6ROT, string MAXRATIO,
    int BAILOUT, int PRGPST, int RESVEC, double G, double HFREQ, double LFREQ, int MEFFMASS, int MEFFMASS _GRID _ID],
    [int NINC, int KMETHOD, int MAXITER, int useEPSU, int useEPSP, int useEPSW, double EPSU, double EPSP, double EPSW],
    [int NDT, double DT, int MAXITER], [[int id, string title, string arbitraryText, int subcaseIdForLoad,
    int subcaseIdForDload, int subcaseIdForSpc, int subcaseIdForMpc, int subcaseIdForTempInit,
    int subcaseIdForTempLoad, int outputReq _Displacement, int outputReq _Stress, int outputReq _Strain,
    int outputReq _Acceleration, int outputReq _Velocity], ...], string systemCellText, string fileManagementText,
    string executiveControlText, string globalCaseControlText, string bulkDataText, TCursor crEdit)
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
### 4. Int

solverType parameter

<!-- @since:5.0.1 -->
### 5. Int

writeType parameter

<!-- @since:5.0.1 -->
### 6. Int

gridFormatType parameter

<!-- @since:5.0.1 -->
### 7. Int

deleteFloatingNodes parameter

<!-- @since:5.0.1 -->
### 8. Int

continuanceMarker parameter

<!-- @since:5.0.1 -->
### 9. Int

defineLbcId parameter

<!-- @since:5.0.1 -->
### 10. Int

definedLoadId parameter

<!-- @since:5.0.1 -->
### 11. Int

definedSpcId parameter

<!-- @since:5.0.1 -->
### 12. Int

definedMpcId parameter

<!-- @since:5.0.1 -->
### 13. Int

uniqueLbcId parameter

<!-- @since:5.0.1 -->
### 14. Int

useCASI parameter

<!-- @since:5.0.1 -->
### 15. Double

epsilon parameter

<!-- @since:5.0.1 -->
### 16. Int

maxNumOfIter parameter

<!-- @since:5.0.1 -->
### 17. Int

numOfThreads parameter

<!-- @since:5.0.1 -->
### 18. Int

memory parameter

<!-- @since:5.0.1 -->
### 19. Int

paramInrel parameter

<!-- @since:5.0.1 -->
### 20. Int

ncpu parameter

<!-- @since:5.0.1 -->
### 21. Int

solNo parameter

<!-- @since:5.0.1 -->
### 22. String

includeFilePath parameter

<!-- @since:5.0.1 -->
### 23. Double

startFreq parameter

<!-- @since:5.0.1 -->
### 24. Double

endFreq parameter

<!-- @since:5.0.1 -->
### 25. Int

noOfModes parameter

<!-- @since:5.0.1 -->
### 26. Double

startFrequency parameter

<!-- @since:5.0.1 -->
### 27. Double

increment parameter

<!-- @since:5.0.1 -->
### 28. Int

numOfInc parameter

<!-- @since:5.0.1 -->
### 29. Int

tableId parameter

<!-- @since:5.0.1 -->
### 30. Int

numOfSteps parameter

<!-- @since:5.0.1 -->
### 31. Double

timeIncrement parameter

<!-- @since:5.0.1 -->
### 32. Int

outputInterval parameter

<!-- @since:5.0.1 -->
### 33. Int

dampingType parameter

<!-- @since:5.0.1 -->
### 34. Int

modalDampingTableId parameter

<!-- @since:5.0.1 -->
### 35. Int

value\_Displacement parameter

<!-- @since:5.0.1 -->
### 36. Int

value\_SpcForces parameter

<!-- @since:5.0.1 -->
### 37. Int

value\_Oload parameter

<!-- @since:5.0.1 -->
### 38. Int

value\_MpcForces parameter

<!-- @since:5.0.1 -->
### 39. Int

value\_Stress parameter

<!-- @since:5.0.1 -->
### 40. Int

value\_Strain parameter

<!-- @since:5.0.1 -->
### 41. Int

value\_Force parameter

<!-- @since:5.0.1 -->
### 42. Int

value\_StrainEnergy parameter

<!-- @since:5.0.1 -->
### 43. Int

value\_Bcresults parameter

<!-- @since:5.0.1 -->
### 44. Int

value\_Bgresults parameter

<!-- @since:5.0.1 -->
### 45. Int

value\_Sdisplacement parameter

<!-- @since:5.0.1 -->
### 46. Int

value\_Acceleration parameter

<!-- @since:5.0.1 -->
### 47. Int

value\_Velocity parameter

<!-- @since:5.0.1 -->
### 48. Int

value\_Meffmass parameter

<!-- @since:5.0.1 -->
### 49. Int

value\_Thermal parameter

<!-- @since:5.0.1 -->
### 50. Int

value\_Flux parameter

<!-- @since:5.0.1 -->
### 51. Int

type\_Displacement parameter

<!-- @since:5.0.1 -->
### 52. Int

type\_SpcForces parameter

<!-- @since:5.0.1 -->
### 53. Int

type\_Oload parameter

<!-- @since:5.0.1 -->
### 54. Int

type\_MpcForces parameter

<!-- @since:5.0.1 -->
### 55. Int

type\_Stress parameter

<!-- @since:5.0.1 -->
### 56. Int

type\_Strain parameter

<!-- @since:5.0.1 -->
### 57. Int

type\_Force parameter

<!-- @since:5.0.1 -->
### 58. Int

type\_StrainEnergy parameter

<!-- @since:5.0.1 -->
### 59. Int

type\_Bcresults parameter

<!-- @since:5.0.1 -->
### 60. Int

type\_Bgresults parameter

<!-- @since:5.0.1 -->
### 61. Int

type\_Sdisplacement parameter

<!-- @since:5.0.1 -->
### 62. Int

type\_Acceleration parameter

<!-- @since:5.0.1 -->
### 63. Int

type\_Velocity parameter

<!-- @since:5.0.1 -->
### 64. Int

type\_Meffmass parameter

<!-- @since:5.0.1 -->
### 65. Int

type\_Thermal parameter

<!-- @since:5.0.1 -->
### 66. Int

type\_Flux parameter

<!-- @since:5.0.1 -->
### 67. Int

GEOMCHECK\_NONE parameter

<!-- @since:5.0.1 -->
### 68. Int

ECHO parameter

<!-- @since:5.0.1 -->
### 69. String

title parameter

<!-- @since:5.0.1 -->
### 70. Int

subcaseIdForLoad parameter

<!-- @since:5.0.1 -->
### 71. Int

subcaseIdForDload parameter

<!-- @since:5.0.1 -->
### 72. Int

subcaseIdForSpc parameter

<!-- @since:5.0.1 -->
### 73. Int

subcaseIdForMpc parameter

<!-- @since:5.0.1 -->
### 74. Int

subcaseIdForTempInit parameter

<!-- @since:5.0.1 -->
### 75. Int

subcaseIdForTempLoad parameter

<!-- @since:5.0.1 -->
### 76. Int

POST parameter

<!-- @since:5.0.1 -->
### 77. Int

OGEOM parameter

<!-- @since:5.0.1 -->
### 78. Int

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
### 83. Int

BAILOUT parameter

<!-- @since:5.0.1 -->
### 84. Int

PRGPST parameter

<!-- @since:5.0.1 -->
### 85. Int

RESVEC parameter

<!-- @since:5.0.1 -->
### 86. Double

G parameter

<!-- @since:5.0.1 -->
### 87. Double

HFREQ parameter

<!-- @since:5.0.1 -->
### 88. Double

LFREQ parameter

<!-- @since:5.0.1 -->
### 89. Double

W3 parameter

<!-- @since:5.0.1 -->
### 90. Double

W4 parameter

<!-- @since:5.0.1 -->
### 91. Int

MEFFMASS parameter

<!-- @since:5.0.1 -->
### 92. Int

MEFFMASS\_GRID\_ID parameter

<!-- @since:5.0.1 -->
### 93. Int

NINC parameter

<!-- @since:5.0.1 -->
### 94. Int

KMETHOD parameter

<!-- @since:5.0.1 -->
### 95. Int

MAXITER parameter

<!-- @since:5.0.1 -->
### 96. Int

useEPSU parameter

<!-- @since:5.0.1 -->
### 97. Int

useEPSP parameter

<!-- @since:5.0.1 -->
### 98. Int

useEPSW parameter

<!-- @since:5.0.1 -->
### 99. Double

EPSU parameter

<!-- @since:5.0.1 -->
### 100. Double

EPSP parameter

<!-- @since:5.0.1 -->
### 101. Double

EPSW parameter

<!-- @since:5.0.1 -->
### 102. Int

NDT parameter

<!-- @since:5.0.1 -->
### 103. Double

DT parameter

<!-- @since:5.0.1 -->
### 104. Int

MAXITER parameter

<!-- @since:5.0.1 -->
### 105. Int

id parameter

<!-- @since:5.0.1 -->
### 106. String

title parameter

<!-- @since:5.0.1 -->
### 107. String

arbitraryText parameter

<!-- @since:5.0.1 -->
### 108. Int

subcaseIdForLoad parameter

<!-- @since:5.0.1 -->
### 109. Int

subcaseIdForDload parameter

<!-- @since:5.0.1 -->
### 110. Int

subcaseIdForSpc parameter

<!-- @since:5.0.1 -->
### 111. Int

subcaseIdForMpc parameter

<!-- @since:5.0.1 -->
### 112. Int

subcaseIdForTempInit parameter

<!-- @since:5.0.1 -->
### 113. Int

subcaseIdForTempLoad parameter

<!-- @since:5.0.1 -->
### 114. Int

outputReq\_Displacement parameter

<!-- @since:5.0.1 -->
### 115. Int

outputReq\_Stress parameter

<!-- @since:5.0.1 -->
### 116. Int

outputReq\_Strain parameter

<!-- @since:5.0.1 -->
### 117. Int

outputReq\_Acceleration parameter

<!-- @since:5.0.1 -->
### 118. Int

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
DynamisJob("TS-Solver", "", [], 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1.79769e+308, 2147483647,
    0, 1024, 0, 0, 101, "", [1.79769e+308, 1.79769e+308, 2147483647], [0, 1.79769e+308,
    1.79769e+308, 2147483647, 0, 0, 1.79769e+308, 1.79769e+308, 2147483647], [1.79769e+308,
    1.79769e+308, 2147483647, 0], [2147483647, 1.79769e+308, 2147483647, 2, 0],
    [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647,
    0, 0, 2147483647, 0, 0, 0, 0, 0, 0, 0, 2147483647, 2147483647, 1, 0, 0, 0, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0], [0, ""], [2147483647, 2147483647, 2147483647,
    2147483647, 2147483647, 2147483647], [-1, 0, 0, "", "", "", "", 2147483647, 2, 0,
    1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 2147483647, 1, 0],
    [1, 3, 2147483647, 0, 0, 1, 1.79769e+308, 1.79769e+308, 0.01], [2147483647, 1.79769e+308, 2147483647],
    [], "", "", "", "", "", 0, 0:0)
```
