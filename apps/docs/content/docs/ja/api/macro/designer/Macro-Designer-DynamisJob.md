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
DynamisJob(String strName, String strDescription, Cursor[] taTarget, int writeType,
    int gridFormatType, int deleteFloatingNodes, int continuanceMarker, int defineLbcId,
    int definedLoadId, int definedSpcId, int definedMpcId, int useCASI, double epsilon,
    int maxNumOfIter, int memory, int paramInrel, int ncpu, int solNo, String includeFilePath,
    [double startFreq, double endFreq, int noOfModes], [double startFrequency, double increment,
    int numOfInc, int tableId], [int numOfSteps, double timeIncrement, int outputInterval,
    int modalDampingTableId], [int value _Displacement, int value _SpcForces, int value _Oload,
    int value _MpcForces, int value _Stress, int value _Strain, int value _Force, int value _StrainEnergy,
    int value _Sdisplacement, int value _Acceleration, int value _Velocity, int value _Meffmass,
    int value _Thermal, int value _Flux, int type _Displacement, int type _SpcForces, int type _Oload,
    int type _MpcForces, int type _Stress, int type _Strain, int type _Force, int type _StrainEnergy,
    int type _Sdisplacement, int type _Acceleration, int type _Velocity, int type _Meffmass,
    int type _Thermal, int type _Flux], [int GEOMCHECK _NONE], [int ECHO, String title],
    [double subcaseIdForLoad, double subcaseIdForDload, double subcaseIdForSpc,
    double subcaseIdForMpc, double subcaseIdForTempInit, double subcaseIdForTempLoad],
    [int POST, int OGEOM, int AUTOSPC, String GRDPNT, String WTMASS, String K6ROT,
    string MAXRATIO, int BAILOUT, int PRGPST], [int NINC, int KMETHOD, int MAXITER, int useEPSU,
    int useEPSP, int useEPSW, double EPSU, double EPSP, double EPSW], [int NDT, double DT, int MAXITER],
    [[int id, int title, int subcaseIdForLoad, int subcaseIdForDload, int subcaseIdForSpc,
    int subcaseIdForMpc, int subcaseIdForTempInit, int subcaseIdForTempLoad, int outputReq _Displacement,
    int outputReq _Stress, int outputReq _Strain, int outputReq _Acceleration, int outputReq _Velocity], ...],
    Cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Job name

<!-- @since:5.0.1 -->
### 2. String

Job description

<!-- @since:5.0.1 -->
### 3. Cursor\[]

target

<!-- @since:5.0.1 -->
### 4. Int

writeType parameter

<!-- @since:5.0.1 -->
### 5. Int

gridFormatType parameter

<!-- @since:5.0.1 -->
### 6. Int

deleteFloatingNodes parameter

<!-- @since:5.0.1 -->
### 7. Int

continuanceMarker parameter

<!-- @since:5.0.1 -->
### 8. Int

defineLbcId parameter

<!-- @since:5.0.1 -->
### 9. Int

definedLoadId parameter

<!-- @since:5.0.1 -->
### 10. Int

definedSpcId parameter

<!-- @since:5.0.1 -->
### 11. Int

definedMpcId parameter

<!-- @since:5.0.1 -->
### 12. Int

useCASI parameter

<!-- @since:5.0.1 -->
### 13. Double

epsilon parameter

<!-- @since:5.0.1 -->
### 14. Int

maxNumOfIter parameter

<!-- @since:5.0.1 -->
### 15. Int

memory parameter

<!-- @since:5.0.1 -->
### 16. Int

paramInrel parameter

<!-- @since:5.0.1 -->
### 17. Int

ncpu parameter

<!-- @since:5.0.1 -->
### 18. Int

solNo parameter

<!-- @since:5.0.1 -->
### 19. String

includeFilePath parameter

<!-- @since:5.0.1 -->
### 20. Double

startFreq parameter

<!-- @since:5.0.1 -->
### 21. Double

endFreq parameter

<!-- @since:5.0.1 -->
### 22. Int

noOfModes parameter

<!-- @since:5.0.1 -->
### 23. Double

startFrequency parameter

<!-- @since:5.0.1 -->
### 24. Double

increment parameter

<!-- @since:5.0.1 -->
### 25. Int

numOfInc parameter

<!-- @since:5.0.1 -->
### 26. Int

tableId parameter

<!-- @since:5.0.1 -->
### 27. Int

numOfSteps parameter

<!-- @since:5.0.1 -->
### 28. Double

timeIncrement parameter

<!-- @since:5.0.1 -->
### 29. Int

outputInterval parameter

<!-- @since:5.0.1 -->
### 30. Int

modalDampingTableId parameter

<!-- @since:5.0.1 -->
### 31. Int

value\_Displacement parameter

<!-- @since:5.0.1 -->
### 32. Int

value\_SpcForces parameter

<!-- @since:5.0.1 -->
### 33. Int

value\_Oload parameter

<!-- @since:5.0.1 -->
### 34. Int

value\_MpcForces parameter

<!-- @since:5.0.1 -->
### 35. Int

value\_Stress parameter

<!-- @since:5.0.1 -->
### 36. Int

value\_Strain parameter

<!-- @since:5.0.1 -->
### 37. Int

value\_Force parameter

<!-- @since:5.0.1 -->
### 38. Int

value\_StrainEnergy parameter

<!-- @since:5.0.1 -->
### 39. Int

value\_Sdisplacement parameter

<!-- @since:5.0.1 -->
### 40. Int

value\_Acceleration parameter

<!-- @since:5.0.1 -->
### 41. Int

value\_Velocity parameter

<!-- @since:5.0.1 -->
### 42. Int

value\_Meffmass parameter

<!-- @since:5.0.1 -->
### 43. Int

value\_Thermal parameter

<!-- @since:5.0.1 -->
### 44. Int

value\_Flux parameter

<!-- @since:5.0.1 -->
### 45. Int

type\_Displacement parameter

<!-- @since:5.0.1 -->
### 46. Int

type\_SpcForces parameter

<!-- @since:5.0.1 -->
### 47. Int

type\_Oload parameter

<!-- @since:5.0.1 -->
### 48. Int

type\_MpcForces parameter

<!-- @since:5.0.1 -->
### 49. Int

type\_Stress parameter

<!-- @since:5.0.1 -->
### 50. Int

type\_Strain parameter

<!-- @since:5.0.1 -->
### 51. Int

type\_Force parameter

<!-- @since:5.0.1 -->
### 52. Int

type\_StrainEnergy parameter

<!-- @since:5.0.1 -->
### 53. Int

type\_Sdisplacement parameter

<!-- @since:5.0.1 -->
### 54. Int

type\_Acceleration parameter

<!-- @since:5.0.1 -->
### 55. Int

type\_Velocity parameter

<!-- @since:5.0.1 -->
### 56. Int

type\_Meffmass parameter

<!-- @since:5.0.1 -->
### 57. Int

type\_Thermal parameter

<!-- @since:5.0.1 -->
### 58. Int

type\_Flux parameter

<!-- @since:5.0.1 -->
### 59. Int

GEOMCHECK\_NONE parameter

<!-- @since:5.0.1 -->
### 60. Int

ECHO parameter

<!-- @since:5.0.1 -->
### 61. String

title parameter

<!-- @since:5.0.1 -->
### 62. Double

subcaseIdForLoad parameter

<!-- @since:5.0.1 -->
### 63. Double

subcaseIdForDload parameter

<!-- @since:5.0.1 -->
### 64. Double

subcaseIdForSpc parameter

<!-- @since:5.0.1 -->
### 65. Double

subcaseIdForMpc parameter

<!-- @since:5.0.1 -->
### 66. Double

subcaseIdForTempInit parameter

<!-- @since:5.0.1 -->
### 67. Double

subcaseIdForTempLoad parameter

<!-- @since:5.0.1 -->
### 68. Int

POST parameter

<!-- @since:5.0.1 -->
### 69. Int

OGEOM parameter

<!-- @since:5.0.1 -->
### 70. Int

AUTOSPC parameter

<!-- @since:5.0.1 -->
### 71. String

GRDPNT parameter

<!-- @since:5.0.1 -->
### 72. String

WTMASS parameter

<!-- @since:5.0.1 -->
### 73. String

K6ROT parameter

<!-- @since:5.0.1 -->
### 74. String

MAXRATIO parameter

<!-- @since:5.0.1 -->
### 75. Int

BAILOUT parameter

<!-- @since:5.0.1 -->
### 76. Int

PRGPST parameter

<!-- @since:5.0.1 -->
### 77. Int

NINC parameter

<!-- @since:5.0.1 -->
### 78. Int

KMETHOD parameter

<!-- @since:5.0.1 -->
### 79. Int

MAXITER parameter

<!-- @since:5.0.1 -->
### 80. Int

useEPSU parameter

<!-- @since:5.0.1 -->
### 81. Int

useEPSP parameter

<!-- @since:5.0.1 -->
### 82. Int

useEPSW parameter

<!-- @since:5.0.1 -->
### 83. Double

EPSU parameter

<!-- @since:5.0.1 -->
### 84. Double

EPSP parameter

<!-- @since:5.0.1 -->
### 85. Double

EPSW parameter

<!-- @since:5.0.1 -->
### 86. Int

NDT parameter

<!-- @since:5.0.1 -->
### 87. Double

DT parameter

<!-- @since:5.0.1 -->
### 88. Int

MAXITER parameter

<!-- @since:5.0.1 -->
### 89. Int

id parameter

<!-- @since:5.0.1 -->
### 90. Int

title parameter

<!-- @since:5.0.1 -->
### 91. Int

subcaseIdForLoad parameter

<!-- @since:5.0.1 -->
### 92. Int

subcaseIdForDload parameter

<!-- @since:5.0.1 -->
### 93. Int

subcaseIdForSpc parameter

<!-- @since:5.0.1 -->
### 94. Int

subcaseIdForMpc parameter

<!-- @since:5.0.1 -->
### 95. Int

subcaseIdForTempInit parameter

<!-- @since:5.0.1 -->
### 96. Int

subcaseIdForTempLoad parameter

<!-- @since:5.0.1 -->
### 97. Int

outputReq\_Displacement parameter

<!-- @since:5.0.1 -->
### 98. Int

outputReq\_Stress parameter

<!-- @since:5.0.1 -->
### 99. Int

outputReq\_Strain parameter

<!-- @since:5.0.1 -->
### 100. Int

outputReq\_Acceleration parameter

<!-- @since:5.0.1 -->
### 101. Int

outputReq\_Velocity parameter

<!-- @since:5.0.1 -->
### 102. Cursor

Cursor for edit mode

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DynamisJob("Job1", "", [], 0, 1, 1, 0, 0, 0, 0, 0, 1, 1.79769e+308, 2147483647, 4, 1024,
    0, 1, 101, "", [1.79769e+308, 1.79769e+308, 2147483647], [1.79769e+308, 1.79769e+308, 2147483647, 0],
    [2147483647, 1.79769e+308, 2147483647, 0], [2147483647, 0, 0, 0, 2147483647, 0, 0, 0, 0, 0, 0, 0,
    2147483647, 2147483647, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0], [0, ""],
    [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647],
    [-1, 0, 0, "", "", "", "", 2147483647, 2], [1, 3, 2147483647, 0, 0, 1, 1.79769e+308, 1.79769e+308, 0.01],
    [2147483647, 1.79769e+308, 2147483647], [], 0:0)
```
