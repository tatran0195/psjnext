---
title: "AbaqusSteadyStateStep()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create ABAQUS steady state step.

All the parameters except for the setting and process indications are the same among there settings.

## Syntax

```psj
AbaqusSteadyStateStep(string m _strName, string m _strDesp, int m _bAutomatic, int m _maxInc, double m _initSize, double m _minSize, double m _maxSize, double  m _MaxAllowTChange, int m _EndStepT.bChecked,               std::vector<double> m _EndStepT.TList double m _MaxAllowEmissivityChange, int m _Method, int m _MatrixStorage, int m _SolutionTech,	int m _AllowedIters,	double m _AdjustFactor, int m _MaxContactIter,  
int m _bNlgeom, double m _TimePeriod, int m _ConvertDscntIter,	int m _Ramp,	int m _ExtrapolateMethod, AbaOutputParam[] m _Output)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

name of Abaqus Steady State Step

<!-- @since:5.1.0 -->
### 2. String

description of Abaqus Steady State Step

<!-- @since:5.1.0 -->
### 3. Int

Automatic\[0:fixed; 1:automatic;]

<!-- @since:5.1.0 -->
### 4. Int

maximum number of increments

<!-- @since:5.1.0 -->
### 5. Double

initial increment size

<!-- @since:5.1.0 -->
### 6. Double

min increment size

<!-- @since:5.1.0 -->
### 7. Double

max increment size

<!-- @since:5.1.0 -->
### 8. Double

max allow termperature change

<!-- @since:5.1.0 -->
### 9. Int

End Step Time\[0:off; 1:on]

<!-- @since:5.1.0 -->
### 10. std::vector\<Double>

End Step Time list

<!-- @since:5.1.0 -->
### 11. Double

Max allow emissivity change

<!-- @since:5.1.0 -->
### 12. Int

Equation Solver Method\[0:direct;1:iterative]

<!-- @since:5.1.0 -->
### 13. int

Matrix Storage\[0:use solver default;1:Unsymmetric;2:Symmetric]

<!-- @since:5.1.0 -->
### 14. Int

SolutionTech\[0:full new ton; 1:quasi-newton;2:contact iterations]

<!-- @since:5.1.0 -->
### 15. Int

Number of iterations allowed before the kernal matrix is reformed

<!-- @since:5.1.0 -->
### 16. Double

Adjust Factor

<!-- @since:5.1.0 -->
### 17. Int

Maximum of contact iterations

<!-- @since:5.1.0 -->
### 18. Int

Nlgem\[0:off; 1:on;]

<!-- @since:5.1.0 -->
### 19. Double

Time Period

<!-- @since:5.1.0 -->
### 20. Int

Convert severe discontinuity iterations

<!-- @since:5.1.0 -->
### 21. Int

Ramp\[0:instantaneous; 1:ramp linearly over step]

<!-- @since:5.1.0 -->
### 22. Int

ExtrapolateMethod\[0:none; 1:linear; 2:parabolic]

<!-- @since:5.1.0 -->
### 23. AbaOutputParam\[]

output setting

<!-- @since:5.1.0 -->
### 30. Cursor

Indicate AbaqusSteadyStateStep when edit it.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
JPT.Exec('AbaqusSteadyStateStep("Step1", "", 1, 100, 1, 1e-05, 1, 1.79769e+308, 0, [], 0.1, 0, 0, 0, 8, 1, 30, 0, 1, 0, 1, 0, [], 0:0)')
```
