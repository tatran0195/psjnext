---
title: "AbaqusStaticStep()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create ABAQUS static step.

All the parameters except for the setting and process indications are the same among there settings.

## Syntax

```psj
AbaqusStaticStep(string m _strName, string m _strDescription,	int m _bAutomatic, int m _maxInc, double m _initSize, double m _minSize, double m _maxSize, 
int m _Method, int m _MatrixStorage, int m _SolutionTech, int m _AllowedIters, double m _AdjustFactor, int m _MaxContactIter,  int m _Type, double m _dampingfactor, 
int m _bUseAdaptive, double m _maxRationofStrainEnergy, int m _bNlgeom, double m _TimePeriod, int m _bIncldHeatEffect, int m _ConvertDscntIter, int m _Ramp, 
int m _ExtrapolateMethod, int m _bAcceptByMaxIters, int m _bLongTerm, int m _bPerturbation, int m _FullPlasticRegion.bchecked, string[] m _FullPlasticRegion, AbaOutputParam[] m _Output)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

name of Abaqus Static Step

<!-- @since:5.1.0 -->
### 2. String

description of Abaqus Static Step

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
### 8. Int

Equation Solver Method\[0:direct;1:iterative]

<!-- @since:5.1.0 -->
### 9. int

Matrix Storage\[0:use solver default;1:Unsymmetric;2:Symmetric]

<!-- @since:5.1.0 -->
### 10. Int

SolutionTech\[0:full new ton; 1:quasi-newton;2:contact iterations]

<!-- @since:5.1.0 -->
### 11. Int

Number of iterations allowed before the kernal matrix is reformed

<!-- @since:5.1.0 -->
### 12. Double

Adjust Factor

<!-- @since:5.1.0 -->
### 13. Int

Maximum of contact iterations

<!-- @since:5.1.0 -->
### 14. Int

Automatic static stablization\[0:none; 1:specify dissipated energy fraction; 2:specify damping factor;3:use daming factors from previous general step]

<!-- @since:5.1.0 -->
### 15. Double

Damping factor

<!-- @since:5.1.0 -->
### 16. Int

Use adaptive stablization with max.

<!-- @since:5.1.0 -->
### 17. Double

Max radio strain energy

<!-- @since:5.1.0 -->
### 18. Int

Nlgem\[0:off; 1:on]

<!-- @since:5.1.0 -->
### 19. Double

Time Period

<!-- @since:5.1.0 -->
### 20. Int

Include adiabatic heating effects\[0:off;1:on]

<!-- @since:5.1.0 -->
### 21. Int

Convert severe discontinuity iterations

<!-- @since:5.1.0 -->
### 22. Int

Ramp\[0:instantaneous; 1:ramp linearly over step]

<!-- @since:5.1.0 -->
### 23. Int

ExtrapolateMethod\[0:none; 1:linear; 2:parabolic]

<!-- @since:5.1.0 -->
### 24. Int

Accept solution after reaching maximum iterations\[0:off;1:on]

<!-- @since:5.1.0 -->
### 25. Int

Obtain long-term solution with time-domain material properties\[0:off;1:on]

<!-- @since:5.1.0 -->
### 26. Int

Perturbation\[0:no;1:yes]

<!-- @since:5.1.0 -->
### 27. Int

Full Plastic Region\[0:off;1:on]

<!-- @since:5.1.0 -->
### 28. String\[]

Indicate full plastic region.

<!-- @since:5.1.0 -->
### 29. AbaOutputParam\[]

output setting

<!-- @since:5.1.0 -->
### 30. Cursor

Indicate AbaqusStaticStep when edit it.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
JPT.Exec('AbaqusStaticStep("Step2", "", 1, 100, 1, 1e-05, 1, 0, 0, 0, 8, 1, 30, 0, 0.0002, 1, 0.05, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, [""], [], 0:0)')
```
