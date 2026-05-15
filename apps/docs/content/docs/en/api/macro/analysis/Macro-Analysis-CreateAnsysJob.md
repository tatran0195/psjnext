---
title: "CreateAnsysJob()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Ansys Job

## Syntax

```psj
CreateAnsysJob(string name, int analysisType, int SolverType, string JobName,
    string JobDescription, bool bOutputDisplacements, bool bOutputReactionLoad,
    bool bOutputStrain, bool bOutputStress, int iAnalysisOpt, bool bCal _Press _effects,
    double fUniTem, double fRefTemp, double fEndLoadtime, int iTimeStep, int iStepChosen,
    int iSubStepNum, int iMaxSubStep, int iMinStepNum, double fTimeStepSize,
    double fMinTimeStep, double fMaxTimeStep, int iWriteReslutFre, int iN, bool bRunAPDL,
    bool bWriteResultDB, double fEndFreq, double fStartFreq, int iSolutionOption,
    double fPropChange, int iPointNum, double fMinTemp, double fMaxTemp, int EquationSolv,
    double fTolLevel, double fMultiplier, bool bSignlePrecision, double fTempDiff,
    double fStartFreq, double fEndFreq, int nSubsteps, double fAlphad, double fBetad,
    double fDmprat, bool bOutputDisplacements, bool bOutputStrain, bool bOutputStress,
    int iLCId, int imodeShape, int iModeMethod, int iExtractNum, bool bExpandShape,
    int iExpandNum, bool bUseApprox, bool bInclPrssEff, bool bMemorySave, bool bRsvec,
    bool bOutputDisplacements, bool bOutputStrain, bool bOutputStress, int iPrintNum,
    bool bMemorySave, bool bOutputHeatFlux, bool bOutputTemperature, bool bPivotsCheck,
    bool bSignlePrecision, double fMultiplier, double fTempDiff, double fTolLevel,
    int iAdaptiveDes, int iEquationSolv, int iNPOption, string AnsysVersion,
    string CommandLineOption, bool OutputSOLVE, int iRigidMode, int iWorkSize,
    int iNPADNum, int iBlockNum, int iMaxiteratCnt, int iMinNShift, int iSeqCheck,
    bool bTranEffect, int iLoadingType, double fMassMatrixMult, double fStiffMatrixMult,
    bool bMidStep, double fToleranceBisection, double fToleranceTimeStep,
    int iTimeInterAlgor, int iTimeInter, double fGAMMA, double fALPHA, double fDELTA,
    double fALPHAF, double fALPHAM, bool bOutputTemperature, bool bOutputHeatFlux, Cursor Edit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Name Job

<!-- @since:5.0.1 -->
### 2. Int

Analysis Type\[0:none 1:struct 2:thermal]

<!-- @since:5.0.1 -->
### 3. Int

Solver Type \[0:none 1:modal 2:hamonic 3:static 4:struct transient 5:steady state 6:thermal transient]

<!-- @since:5.0.1 -->
### 4. String

Name Job

<!-- @since:5.0.1 -->
### 5. String

Job description

<!-- @since:5.0.1 -->
### 6. Bool

Output Displacements

<!-- @since:5.0.1 -->
### 7. Bool

Output Reaction Load

<!-- @since:5.0.1 -->
### 8. Bool

Output Strain

<!-- @since:5.0.1 -->
### 9. Bool

Output Stress

<!-- @since:5.0.1 -->
### 10. Int

Analysis Opt \[0 = small displacement,1 = large displacement ]

<!-- @since:5.0.1 -->
### 11. Bool

Cal Press effects

<!-- @since:5.0.1 -->
### 12. Double

Uniform temperature

<!-- @since:5.0.1 -->
### 13. Double

Reference temperature

<!-- @since:5.0.1 -->
### 14. Double

End load time

<!-- @since:5.0.1 -->
### 15. Int

Time step \[0 = Prog chosen, 1 = On, 2 = Off, 3 = Arc-Length]

<!-- @since:5.0.1 -->
### 16. Int

Step chosen \[0 = Number of SubSteps, 1 = Time Increment]

<!-- @since:5.0.1 -->
### 17. Int

Number of substep

<!-- @since:5.0.1 -->
### 18. Int

Max Number of substep

<!-- @since:5.0.1 -->
### 19. Int

Min Number of substep

<!-- @since:5.0.1 -->
### 20. Double

Time step size

<!-- @since:5.0.1 -->
### 21. Double

Min time step

<!-- @since:5.0.1 -->
### 22. Double

Max time step

<!-- @since:5.0.1 -->
### 23. Int

Write result fre \[0=write every subStep, 1=Do not write any substeps,2=Write last subStep only,3= Write every Nth Substep,4=Write N Number subStep]

<!-- @since:5.0.1 -->
### 24. Int

iN

<!-- @since:5.0.1 -->
### 25. Bool

Run APDL

<!-- @since:5.0.1 -->
### 26. Bool

Write result DB

<!-- @since:5.0.1 -->
### 27. Double

End frequency

<!-- @since:5.0.1 -->
### 28. Double

Start frequency

<!-- @since:5.0.1 -->
### 29. Int

Solution option \[0=Full,=1=Quasi,2=Linear]

<!-- @since:5.0.1 -->
### 30. Double

Property change for reformation

<!-- @since:5.0.1 -->
### 31. Int

Number of poInts in fast table

<!-- @since:5.0.1 -->
### 32. Double

Min temperature for fast table

<!-- @since:5.0.1 -->
### 33. Double

Max temperature for fast table

<!-- @since:5.0.1 -->
### 34. Int

Equation solver\[0=Program Chosen,1=Frontal solver,2=Sparse solver,3=Jacobi Conj Grad,4=JCG out-of-core,5=Precondition CG,6=PCG out-of-core,7=Algebraic M-grid,8=Inc Cholesky CG,9=Iter auto select]

<!-- @since:5.0.1 -->
### 35. Double

Tolerance/Level

<!-- @since:5.0.1 -->
### 36. Double

Multiplier

<!-- @since:5.0.1 -->
### 37. Bool

Single Precision

<!-- @since:5.0.1 -->
### 38. Bool

Memory save

<!-- @since:5.0.1 -->
### 39. Double

Temperature difference

<!-- @since:5.0.1 -->
### 40. Double

Start frequency

<!-- @since:5.0.1 -->
### 41. Double

End frequency

<!-- @since:5.0.1 -->
### 42. Int

Substeps

<!-- @since:5.0.1 -->
### 43. Double

Alfhad

<!-- @since:5.0.1 -->
### 44. Double

Betad

<!-- @since:5.0.1 -->
### 45. Double

Dmprat

<!-- @since:5.0.1 -->
### 46. Bool

Output displacement

<!-- @since:5.0.1 -->
### 47. Bool

Output Strain

<!-- @since:5.0.1 -->
### 48. Bool

Output Stress

<!-- @since:5.0.1 -->
### 49. Int

Load case id

<!-- @since:5.0.1 -->
### 50. Int

Nrmkey Normalize mode shapes \[0=To mass matrix, 1= To unity]

<!-- @since:5.0.1 -->
### 51. Int

Mode Method \[0=Block,1=Subspace,2=Reduced]

<!-- @since:5.0.1 -->
### 52. Int

Extract Num

<!-- @since:5.0.1 -->
### 53. Bool

Expand mode shape

<!-- @since:5.0.1 -->
### 54. Int

No. of modes to expand

<!-- @since:5.0.1 -->
### 55. Bool

Use lumped mass approx.

<!-- @since:5.0.1 -->
### 56. Bool

Incl prestress effects

<!-- @since:5.0.1 -->
### 57. Bool

Memory save

<!-- @since:5.0.1 -->
### 58. Bool

Residual Vector

<!-- @since:5.0.1 -->
### 59. Bool

Output displacement

<!-- @since:5.0.1 -->
### 60. Bool

Output Strain

<!-- @since:5.0.1 -->
### 61. Bool

Output Stress

<!-- @since:5.0.1 -->
### 62. Int

Num of modes to prInt

<!-- @since:5.0.1 -->
### 63. Bool

Memory save for steady state

<!-- @since:5.0.1 -->
### 64. Bool

Output heat flux

<!-- @since:5.0.1 -->
### 65. Bool

Output temperature

<!-- @since:5.0.1 -->
### 66. Bool

Pivots check

<!-- @since:5.0.1 -->
### 67. Bool

single precision

<!-- @since:5.0.1 -->
### 68. Double

Multiplier

<!-- @since:5.0.1 -->
### 69. Double

Temperature difference

<!-- @since:5.0.1 -->
### 70. Double

Tolerance level

<!-- @since:5.0.1 -->
### 71. Int

Adaptive descent \[0 = ON if necessary, 1 = ON, 2 = OFF]

<!-- @since:5.0.1 -->
### 72. Int

Equation solver \[0= Program Chosen,1= Frontal solver]

<!-- @since:5.0.1 -->
### 73. Int

Newton-Raphson option\[0= Program chosen, 1= Full N-R, 2= Modified N-R, 3= Initial stiffnes, 4= Full N-R unsymm]

<!-- @since:5.0.1 -->
### 74. String

Ansys version

<!-- @since:5.0.1 -->
### 75. String

Command line option

<!-- @since:5.0.1 -->
### 76. Bool

Output solver

<!-- @since:5.0.1 -->
### 77. Int

Rigid mode

<!-- @since:5.0.1 -->
### 78. Int

Work size

<!-- @since:5.0.1 -->
### 79. Int

No of extra vectors

<!-- @since:5.0.1 -->
### 80. Int

NPERBK No of modes/memory block

<!-- @since:5.0.1 -->
### 81. Int

NUMSSI Maximum number of iterations

<!-- @since:5.0.1 -->
### 82. Int

NSHIFT Min, before shift

<!-- @since:5.0.1 -->
### 83. Int

Strmck Sturm sequence check \[0 =At shift+end pts, 1= At shift pts, 2 = No Sturm check]

<!-- @since:5.0.1 -->
### 84. Bool

Transient effects

<!-- @since:5.0.1 -->
### 85. Int

Loading type \[0= Stepped Loading,1= Ramped Loading]

<!-- @since:5.0.1 -->
### 86. Double

Mass matrix multiplier

<!-- @since:5.0.1 -->
### 87. Double

Stiffness matrix multiplier

<!-- @since:5.0.1 -->
### 88. Bool

MidStep Criterion

<!-- @since:5.0.1 -->
### 89. Double

Tolerance for Bisection

<!-- @since:5.0.1 -->
### 90. Double

Tolerance for TimeStep

<!-- @since:5.0.1 -->
### 91. Int

Time Intergration algorithm \[0 =Newmark,1=HHT]

<!-- @since:5.0.1 -->
### 92. Int

Time Intergration\[0 =Amplitude decay ,1= Integration parameters]

<!-- @since:5.0.1 -->
### 93. Double

Gamma

<!-- @since:5.0.1 -->
### 94. Double

Alpha

<!-- @since:5.0.1 -->
### 95. Double

Delta

<!-- @since:5.0.1 -->
### 96. Double

AlphaF

<!-- @since:5.0.1 -->
### 97. Double

AlphaM

<!-- @since:5.0.1 -->
### 98. Bool

Output temperature

<!-- @since:5.0.1 -->
### 99. Bool

Output heat flux

<!-- @since:5.0.1 -->
### 100. Cursor

Edit job

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateAnsysJob("Ansys", 2, 5, "Nastran4", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    , 0, 0, 1, 1, 0, 0, 1.79769e+308, 1.79769e+308, 0, 0.05, 64, 0, 0, 0, 0, 0, 0, 0,
    1.1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, "", "", 0, 0, 8, 4, 5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0.005, 0.252506, 0.505, 0.005, 0, 0, 0, 0:0)
```
