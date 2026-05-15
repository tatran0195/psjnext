---
title: "FrontISTR _LinearElasticStaticAnalysis()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create FrontISTR job (Linear Elastic Static Analysis)

## Syntax

```psj
FrontISTR _LinearStatic(string strFilePath, cursor[] stepSequence, int nOpn, String jobName, 
	int solverVersion, int iterCount, int iterCountSchwartz, int numKrylov,
	int numColor, double threhold, double sigma _diag, double sigma,
	int numStepThermal, int intialStepNumber, String resultFileNameThermal,
	String stepName, bool bSetAutoIncrement, [String name, double RS, int NS _MAX, int NS _SUM,
	int NS _COUNT, int N _S, double RL, int NL _MAX,
	int NL _SUM, int NL _COUNT, int N _L, double RC,int N _C],
	bool bSetTimePoints, [String name, BOOL bIsGenerate, int type, double time,
	double eTime, double sTime, double interval] , double converg,
	int substeps, int maxiter, double dtime, double etime,
	String outputInterval, String outputFileName, int numComputationNodes,
	int numProcessorPerComputationNodes, int refineLevel, int analysisType,
	int stepType, int methodMatrixSolver, int preconditioner, int outputIteration,
	int outputElapsedTime, int outputModelInfoToLogFile, int visualizeFileType,
	int parallelSetting, int algorithm, bool resultData, bool visualizeData, 
	bool disp _result, bool disp _visual, bool velocity _result, bool velocity _visual, 
	bool acceleration _result, bool acceleration _visual, bool nodal _strain _result,
	bool nodal _strain _visual, bool nodal _stress _result, bool nodal _stress _visual,
	bool nodal _mises _stress _result, bool nodal _mises _stress _visual,
	bool elemental _strain _result, bool elemental _stress _result,
	bool elemental _mises _stress _result, bool strain _integration _point _result,
	bool stress _integration _point _result, bool reaction _force _result, 
	bool reaction _force _visual, bool contact _NForce _result,
	bool contact _NForce _visual, bool contact _Friction _result,
	bool contact _Friction _visual, bool contact _Relvel _result,
	bool contact _Relvel _visual, bool contact _State _result,
	bool contact _State _visual, bool contact _NTraction _result,
	bool contact _NTraction _visual, bool contact _FTraction _result,
	bool contact _FTraction _visual, bool default _step,
	int directExecution, String singleCoreExeFilePath,
	String singleCoreCalculationExeFile, String parallelCoreMPIPath,
	String parallelCoreMPIExeFile, String parallelCoreMPIOption,
	String parallelCoreFrontISTRExeFilePath, String parallelCoreAreaDivisionExeFile,
	String parallelCoreCalculationExeFile, bool bWriteGroup,
	bool bExportCntFile, bool bExportMshFile,
	//Eigen Analysis parameters
	String NumEigenValues, String Tolerance, String MaxIteration,
	//Frequency Response parameters
	int iMotionEquation, int iDynamicAnalysisType, String MinimumFreq,
	String MaximumFreq, String NumIncrement, String FreqObtainDisplacement,
	String StartTime, String EndTime, int iMassMatrix, int iDamping,
	String ParameterRm, String ParameterRk, String EigenvalueAnalysisLog,
	String StartMode, String EndMode, String OutputInterval,
	int iVisualizeType, String MonitoringNode, int iDisplacement,
	int iVelocity, int iAcceleration, int iComplexOutputType, 
	String strRestartOutputInterval, String strRestartOutputFilename,
	bool bEnableRestartSettings, int iStepInveralOutputResult,	
	int iStepInveralOutputVisual,	
},
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

File path

<!-- @since:5.1.0 -->
### 2. Cursor\[]

Step sequence

<!-- @since:5.1.0 -->
### 3. Int

Operation number

<!-- @since:5.1.0 -->
### 4. String

Job name

<!-- @since:5.1.0 -->
### 5. Int

Solver version

<!-- @since:5.1.0 -->
### 6. Int

Main iteration count

<!-- @since:5.1.0 -->
### 7. Int

Schwartz iteration count

<!-- @since:5.1.0 -->
### 8. Int

Number of Krylov vectors

<!-- @since:5.1.0 -->
### 9. Int

Number of colors used in coloring

<!-- @since:5.1.0 -->
### 10. Double

Convergence threshold

<!-- @since:5.1.0 -->
### 11. Double

Diagonal sigma value

<!-- @since:5.1.0 -->
### 12. Double

Sigma coefficient

<!-- @since:5.1.0 -->
### 13. Int

Number of thermal steps

<!-- @since:5.1.0 -->
### 14. Int

Initial step number

<!-- @since:5.1.0 -->
### 15. String

Result file name for thermal analysis

<!-- @since:5.1.0 -->
### 16. String

Step name

<!-- @since:5.1.0 -->
### 17. Bool

Enable Auto Increment setting

<!-- @since:5.1.0 -->
### 18. String

\[AutoIncrement] Name

<!-- @since:5.1.0 -->
### 19. Double

\[AutoIncrement] RS

<!-- @since:5.1.0 -->
### 20. Int

\[AutoIncrement] NS\_MAX

<!-- @since:5.1.0 -->
### 21. Int

\[AutoIncrement] NS\_SUM

<!-- @since:5.1.0 -->
### 22. Int

\[AutoIncrement] NS\_COUNT

<!-- @since:5.1.0 -->
### 23. Int

\[AutoIncrement] N\_S

<!-- @since:5.1.0 -->
### 24. Double

\[AutoIncrement] RL

<!-- @since:5.1.0 -->
### 25. Int

\[AutoIncrement] NL\_MAX

<!-- @since:5.1.0 -->
### 26. Int

\[AutoIncrement] NL\_SUM

<!-- @since:5.1.0 -->
### 27. Int

\[AutoIncrement] NL\_COUNT

<!-- @since:5.1.0 -->
### 28. Int

\[AutoIncrement] N\_L

<!-- @since:5.1.0 -->
### 29. Double

\[AutoIncrement] RC

<!-- @since:5.1.0 -->
### 30. Int

\[AutoIncrement] N\_C

<!-- @since:5.1.0 -->
### 31. Bool

Enable Time Points setting

<!-- @since:5.1.0 -->
### 32. String

\[TimePoints] Name

<!-- @since:5.1.0 -->
### 33. Bool

\[TimePoints] Is generate enabled

<!-- @since:5.1.0 -->
### 34. Int

\[TimePoints] Type

<!-- @since:5.1.0 -->
### 35. Double

\[TimePoints] Time

<!-- @since:5.1.0 -->
### 36. Double

\[TimePoints] End time

<!-- @since:5.1.0 -->
### 37. Double

\[TimePoints] Start time

<!-- @since:5.1.0 -->
### 38. Double

\[TimePoints] Interval

<!-- @since:5.1.0 -->
### 39. Double

Convergence criterion

<!-- @since:5.1.0 -->
### 40. Int

Number of substeps

<!-- @since:5.1.0 -->
### 41. Int

Maximum iterations

<!-- @since:5.1.0 -->
### 42. Double

Delta time

<!-- @since:5.1.0 -->
### 43. Double

End time

<!-- @since:5.1.0 -->
### 44. String

Output interval

<!-- @since:5.1.0 -->
### 45. String

Output file name

<!-- @since:5.1.0 -->
### 46. Int

Number of computation nodes

<!-- @since:5.1.0 -->
### 47. Int

Processors per node

<!-- @since:5.1.0 -->
### 48. Int

Refinement level

<!-- @since:5.1.0 -->
### 49. Int

Analysis type

<!-- @since:5.1.0 -->
### 50. Int

Step type

<!-- @since:5.1.0 -->
### 51. Int

Matrix solver method

<!-- @since:5.1.0 -->
### 52. Int

Preconditioner type

<!-- @since:5.1.0 -->
### 53. Int

Output iteration toggle

<!-- @since:5.1.0 -->
### 54. Int

Output elapsed time toggle

<!-- @since:5.1.0 -->
### 55. Int

Output model info to log file

<!-- @since:5.1.0 -->
### 56. Int

Visualize file type

<!-- @since:5.1.0 -->
### 57. Int

Parallel setting

<!-- @since:5.1.0 -->
### 58. Int

Algorithm type

<!-- @since:5.1.0 -->
### 59. Bool

Enable result data output

<!-- @since:5.1.0 -->
### 60. Bool

Enable visualize data output

<!-- @since:5.1.0 -->
### 61. Bool

Enable displacement result

<!-- @since:5.1.0 -->
### 62. Bool

Enable displacement visualization

<!-- @since:5.1.0 -->
### 63. Bool

Enable velocity result

<!-- @since:5.1.0 -->
### 64. Bool

Enable velocity visualization

<!-- @since:5.1.0 -->
### 65. Bool

Enable acceleration result

<!-- @since:5.1.0 -->
### 66. Bool

Enable acceleration visualization

<!-- @since:5.1.0 -->
### 67. Bool

Enable nodal strain result

<!-- @since:5.1.0 -->
### 68. Bool

Enable nodal strain visualization

<!-- @since:5.1.0 -->
### 69. Bool

Enable nodal stress result

<!-- @since:5.1.0 -->
### 70. Bool

Enable nodal stress visualization

<!-- @since:5.1.0 -->
### 71. Bool

Enable nodal Mises stress result

<!-- @since:5.1.0 -->
### 72. Bool

Enable nodal Mises stress visualization

<!-- @since:5.1.0 -->
### 73. Bool

Enable elemental strain result

<!-- @since:5.1.0 -->
### 74. Bool

Enable elemental stress result

<!-- @since:5.1.0 -->
### 75. Bool

Enable elemental Mises stress result

<!-- @since:5.1.0 -->
### 76. Bool

Enable strain result at integration points

<!-- @since:5.1.0 -->
### 77. Bool

Enable stress result at integration points

<!-- @since:5.1.0 -->
### 78. Bool

Enable reaction force result

<!-- @since:5.1.0 -->
### 79. Bool

Enable reaction force visualization

<!-- @since:5.1.0 -->
### 80. Bool

Enable contact normal force result

<!-- @since:5.1.0 -->
### 81. Bool

Enable contact normal force visualization

<!-- @since:5.1.0 -->
### 82. Bool

Enable contact friction result

<!-- @since:5.1.0 -->
### 83. Bool

Enable contact friction visualization

<!-- @since:5.1.0 -->
### 84. Bool

Enable contact relative velocity result

<!-- @since:5.1.0 -->
### 85. Bool

Enable contact relative velocity visualization

<!-- @since:5.1.0 -->
### 86. Bool

Enable contact state result

<!-- @since:5.1.0 -->
### 87. Bool

Enable contact state visualization

<!-- @since:5.1.0 -->
### 88. Bool

Enable contact normal traction result

<!-- @since:5.1.0 -->
### 89. Bool

Enable contact normal traction visualization

<!-- @since:5.1.0 -->
### 90. Bool

Enable contact friction traction result

<!-- @since:5.1.0 -->
### 91. Bool

Enable contact friction traction visualization

<!-- @since:5.1.0 -->
### 92. Bool

Default step setting

<!-- @since:5.1.0 -->
### 93. Int

Direct execution mode

<!-- @since:5.1.0 -->
### 94. String

Single-core executable file path

<!-- @since:5.1.0 -->
### 95. String

Single-core calculation executable file

<!-- @since:5.1.0 -->
### 96. String

MPI path for parallel execution

<!-- @since:5.1.0 -->
### 97. String

MPI executable file

<!-- @since:5.1.0 -->
### 98. String

MPI execution options

<!-- @since:5.1.0 -->
### 99. String

FrontISTR parallel executable path

<!-- @since:5.1.0 -->
### 100. String

Parallel area division executable file

<!-- @since:5.1.0 -->
### 101. String

Parallel calculation executable file

<!-- @since:5.1.0 -->
### 102. Bool

Enable writing group

<!-- @since:5.1.0 -->
### 103. Bool

Export CNT file

<!-- @since:5.1.0 -->
### 104. Bool

Export MSH file

<!-- @since:5.1.0 -->
### 105. String

Number of eigenvalues (Eigen Value Analysis)

<!-- @since:5.1.0 -->
### 106. String

Tolerance (Eigen Value Analysis)

<!-- @since:5.1.0 -->
### 107. String

Maximum iterations (Eigen Value Analysis)

<!-- @since:5.1.0 -->
### 108. Int

Motion equation type

<!-- @since:5.1.0 -->
### 109. Int

Dynamic Analysis type

<!-- @since:5.1.0 -->
### 110. String

Minimum frequency

<!-- @since:5.1.0 -->
### 111. String

Maximum frequency

<!-- @since:5.1.0 -->
### 112. String

Number of increments

<!-- @since:5.1.0 -->
### 113. String

Displacement Frequency Response

<!-- @since:5.1.0 -->
### 114. String

Start time for Frequency Response

<!-- @since:5.1.0 -->
### 115. String

End time for Frequency Response

<!-- @since:5.1.0 -->
### 116. Int

Mass matrix setting

<!-- @since:5.1.0 -->
### 117. Int

Damping setting

<!-- @since:5.1.0 -->
### 118. String

Parameter Rm

<!-- @since:5.1.0 -->
### 119. String

Parameter Rk

<!-- @since:5.1.0 -->
### 120. String

Eigen Value Analysis log path

<!-- @since:5.1.0 -->
### 121. String

Start mode

<!-- @since:5.1.0 -->
### 122. String

End mode

<!-- @since:5.1.0 -->
### 123. String

Frequency Response output interval

<!-- @since:5.1.0 -->
### 124. Int

Visualization type

<!-- @since:5.1.0 -->
### 125. String

Monitoring node name

<!-- @since:5.1.0 -->
### 126. Int

Displacement result toggle

<!-- @since:5.1.0 -->
### 127. Int

Velocity result toggle

<!-- @since:5.1.0 -->
### 128. Int

Acceleration result toggle

<!-- @since:5.1.0 -->
### 129. Int

Complex output type

<!-- @since:5.1.0 -->
### 130. String

Restart output interval

<!-- @since:5.1.0 -->
### 131. String

Restart output file name

<!-- @since:5.1.0 -->
### 132. Bool

Enable restart settings

<!-- @since:5.1.0 -->
### 133. Int

Step interval for result output

<!-- @since:5.1.0 -->
### 134. Int

Step interval for visualization output

## Return Code

- "1": The function can be executed
- "FAILED": The function cannot be executed

## Sample Code

```psj
JPT.Exec('FrontISTR _LinearStatic("D:/", [], "Job _1", 3, 20000, 2, 0, 0, 1e-06, 1, 0, 0, 0, "", "STEP0", 1, ["AP1", 0.25, 10, 50, 10, 1, 1.25, 1, 1, 1, 5, 0.25, 5], 1, ["TP1", 0, 1, 1, 0, 0, 0], 1e-05, 10, 0, 0, 0, "", "", 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, "", "", "", "", "", "", "", "", 0, 0, 1, "10", "1.0e-8", "60", 0, 0, "0", "1000", "10", "10", "0.0", "1.0", 0, 0, "0.0", "0.0", "0.log", "0", "1000", "10", 1, "1", 0, 0, 0, 0, "1", "test", 1, 1, 1)')
```
