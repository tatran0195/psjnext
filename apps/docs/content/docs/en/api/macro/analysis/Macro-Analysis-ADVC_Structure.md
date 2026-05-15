---
title: "ADVC _Structure()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC job (Structure)

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
    LoadNodeData[] LoadData, int HeatConvection, bool bCreateProcessForBoltFixedLength, string Path, 
    int NumType, int UiWidth, int UiWidth, bool ExportGeometryID, bool SeparatePartInfoFile,
    string ADVCTemplateFilePath, bool OutputDefinition, int DetaFormatType,
    List ObjectiveFunction, List ConstraintFunction, List NonDesignableArea, List ShapeTopology, List OptimizationOutput)
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

Job type \[0: Structural]

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

Separated file type\[0:None; 1:By Model; 2:By Body; 3:By Selected Body, 4:Select LBCs]

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

<!-- @since:5.1.0 -->
### 31. Int

Heat convection  (not used for Structural), set 0.

<!-- @since:5.1.0 -->
### 32. Bool

Create process for bolt fixed lentgh flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 33. String

Exported adx file path

<!-- @since:5.1.0 -->
### 34. Int

Numric type.  \[0:Real; 1:Power, 2:Auto]

<!-- @since:5.1.0 -->
### 35. Int

UI Width

<!-- @since:5.1.0 -->
### 36. Int

UI Precision

<!-- @since:5.1.0 -->
### 37. Bool

Export geometry id flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 38. Bool

Separate part info file flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 39. String

ADVC Template file path

<!-- @since:5.1.0 -->
### 40. Bool

Output definition flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 41. Bool

Data format type. \[0:Single, 1:Double]

<!-- @since:5.1.0 -->
### 42. ObjectiveFunction

- A _Vector_ specifying Objective Function.
- Defined by _Optimization\_ObjectiveConstraint\_Parameter_. Members are as follows: <a id="Optimization-ObjectiveConstraint-Parameter" />

  ### ` enFunctionType`

  - An _Integer_ specifying the function type.
    <a id="Optimization-Function-Type" />

  <!-- <Link to="#Optimization-Function-Type">link</Link> -->

  | ID  | Function                             |  Description|
  | --- | ------------------------------------------------- | ----|
  | -1   | Unknown\_Function            |No selection |
  | 0   | Compliance\_Function                |Compliance Function|
  | 1   | Displacement\_Function                 |Displacement Function|
  | 2   | Eigen\_Frequency\_Function                 |Eigen Frequency Function|
  | 3   | Mass\_Function                 |Mass Function|
  | 4   | Maximum Displacement Function                 |Maximum Displacement Function|
  | 5   | Maximum\_Mises\_Stress\_Function                 |Maximum Mises Stress Function|
  | 6   | Maximum\_Principal\_Stress\_Function                 |Maximum Principal Stress Function|
  | 7   | Minimum\_Principal\_Stress\_Function                 |Minimum Principal Stress Function|
  | 8   | Surface\_Area\_Function | Surface Area Function|
  | 9   | Volume\_Function |Volume Function |
  | 10  | Optimization\_Frozen\_Node |Optimization Frozen Node  |
  | 11  | Optimization\_Frozen\_Element |Optimization\_Frozen Element |
  | 12  | Shape\_Optimization\_Fixed\_Node | Shape Optimization Fixed Node|
  | 13  | Shape\_Optimization | Shape Optimization |
  | 14  | Shape\_Optimization\_Contact\_pair |Shape Optimization Contact pair |
  | 15  | Shape\_Optimization\_Die\_Drawing | Shape Optimization Die Drawing |
  | 16  | Shape\_Optimization\_Interference\_Node |Shape Optimization Interference Node  |
  | 17  | Shape\_Optimization\_Thickness | Shape Optimization Thickness |
  | 18  | Topology\_Optimization | Topology Optimization|
  | 19  | Topology\_Optimization\_Die\_Drawing | Topology Optimization Die Drawing|
  | 20  | Optimization\_Function\_Type\_Count |Optimization Function Type Count|

  - This is a required input.

  ### ` strFunctionName`

  - A _String_ specifying the name of function.
  - This is a required input.

  ### `iDisplacementRelation`

  - A _Int_ specifying to set Displacement Relation or not.
  - The default value is -1.

  ### `strDegreeOfFreedomNum`

  - A _String_ specifying to set Degree Of Freedom Number.

  ### `dDisplacementCoefficient`

  - A _Double_ specifying to set Displacement Coefficient.

  ### `iConstraint`

  - A _Int_ specifying type of Constraint.
    - If _iConstraint=0_: Equality
    - If _iConstraint=1_: Inequality

  ### `dConstraintTol`

  - A _Double_ specifying Constraint Tolerance.

  ### `iTargetType`

  - An _Int_ specifying Target Type.
    - If _iTargetType=0_: Ratio
    - If _iTargetType=1_: Value

  ### `dRatioOrValue`

  - A _Double_ specifying Ratio or Value.

  ### `dCoefficient`

  - A _Double_ specifying to set Coefficient.

  ### `crNodeSet`

  - A _Cursor_ specifying Node Set.

  ### `crPropOrElemSet`

  - A _Cursor_ specifying Element Set.

  ### `crSurfaceSet`

  - A _Cursor_ specifying Surface Set.

  ### `iKSKernel`

  - A _Int_ specifying type of KS Kernel.
    - If _iKSKernel=0_: Exponential
    - If _iKSKernel=1_: Monomial

  ### `dRHO`

  - A _Double_ specifying RHO.

  ### `dExponent`

  - A _Double_ specifying Exponent.

  ### `iEigenNumber;`

  - An _Int_ specifying Eigen Number.

<!-- @since:5.1.0 -->
### 43 ConstraintFunction

- A _Vector_ specifying Constraint Function.
- Defined by _Optimization\_ObjectiveConstraint\_Parameter_.

<!-- @since:5.1.0 -->
### 44 NonDesignableArea

- A _Vector_ specifying Non-Designable Area.
- Defined by _Optimization\_NonDesignableArea\_Parameter_. Members are as follows:
  ### `enFunctionType`
  - An _Integer_ specifying the [function type](./ADVC _Structure#Optimization-Function-Type).
  - This is a required input.
  ### `strFunctionName`
  - A _String_ specifying the name of function.
  - This is a required input.
  ### `iOptimization = -1`
  - An _Int_ specifying type of Optimization.
  - If _iOptimization=0_: Shape
  - If _iOptimization=1_: Topology
  ### `strDegreeOfFreedomNum`
  - A _String_ specifying Degree of Freedom Number.
  ### `crNodeSet`
  - A _Cursor_ specifying Node Set.
    ### `crPropOrElemSet`
  - A _Cursor_ specifying Element Set.
  ### `vecShapeTopology`
  - A _Vector_ specifying Shape/Topology.
  - Defined by _Optimization\_ShapeTopology\_Parameter_. Members are as follows:
    ### `enFunctionType = Unknown _Function;`
    - An _Integer_ specifying the [function type](./ADVC _Structure#Optimization-Function-Type).
    - This is a required input.
      ### `strFunctionName`
    - A _String_ specifying the name of function.
    - This is a required input.
      ### `dInitialDensity`
    - A _Double_ specifying Initial Density.
      ### `dDensityRandom`
    - A _Double_ specifying Density Random.
      ### `dAlpha`
    - A _Double_ specifying Alpha.
      ### `dDraftAngle`
    - A _Double_ specifying Draft Angle.
      ### `dGap`
    - A _Double_ specifying Gap.
      ### `dDepth`
    - A _Double_ specifying Depth.
      ### `dAngle`
    - A _Double_ specifying Angle.
      ### `dClearance`
    - A _Double_ specifying Clearance.
      ### `dThicknessDepth`
    - A _Double_ specifying Thickness Depth.
      ### `dMaxThickness`
    - A _Double_ specifying Max Thickness.
      ### `dMinThickness`
    - A _Double_ specifying Min Thickness.
      ### `iMaxIteration`
    - An _Int_ specifying Max Iteration.
      ### `dMaxStrain`
    - A _Double_ specifying Max Strain.
      ### `dMaxTheta`
    - A _Double_ specifying Max Theta.
      ### `dH1Tolerance`
    - A _Double_ specifying H1 Tolerance.
      ### `iOutputLast`
    - An _Int_ specifying selection of Output Last.
    - If _iOutputLast=0_: No
    - If _iOutputLast=1_: Yes
      ### `iOutputInterval`
    - An _Int_ specifying Output Interval.
      ### `iResoutLast`
    - An _Int_ specifying selection of Resout Last.
    - If _iResoutLast=0_: No
    - If _iResoutLast=1_: Yes
      ### `iResoutInterval`
    - An _Int_ specifying Resout Interval.
      ### `iArmijoCheck`
    - An _Int_ specifying selection of Armijo Check.
    - If _iArmijoCheck=0_: No
    - If _iArmijoCheck=1_: Yes
      ### `dArmijoParam`
    - A _Double_ specifying Armijo Param.
      ### `strDirection`
    - A _String_ specifying Direction.
      ### `iPunchingOneSide`
    - An _Int_ specifying selection of Punching|Outside.
    - If _iPunchingOneSide=0_: Punching
    - If _iPunchingOneSide=1_: Oneside
      ### `iAutoIncrement`
    - An _Int_ specifying selection of Auto Increment.
    - If _iAutoIncrement=0_: No
    - If _iAutoIncrement=1_: Yes
      ### `dStabilizationFactor`
    - A _Double_ specifying Stabilization Factor.
      ### `dPoissonRatio`
    - A _Double_ specifying Poisson Ratio.
      ### `iAutoFrozen`
    - An _Int_ specifying selection of Auto Frozen.
    - If _iAutoFrozen=0_: No
    - If _iAutoFrozen=1_: Yes
      ### `iKeyCoordinate`
    - An _Int_ specifying selection of Coodinate.
      ### `crNodeSet`
    - A _Cursor_ to specifying Node Set.
      ### `crPropOrElemSet`
    - A _Cursor_ to specifying Element Set.
      ### `crSurfaceSetNonInterferingArea`
    - A _Cursor_ to specifying Non-Interfering Area.
      ### `crSurfaceSetOptimizedArea`
    - A _Cursor_ to specifying Optimized Area.
      ### `iWolfeCheck`
    - An _Int_ specifying selection of Wolfe Check.
    - If _iWolfeCheck=0_: No
    - If _iWolfeCheck=1_: Yes
      ### `dWolfeParam`
    - A _Double_ specifying Wolfe Param.
      ### `iMatrix`
    - An _Int_ specifying selection of Matrix.
    - If _iMatrix=0_: StiffnessLinear
    - If _iMatrix=1_: Stiffness
      ### `iElementDStiffness`
    - An _Int_ specifying selection of Element D.Stiffness.
    - If _iElementDStiffness=0_: No
    - If _iElementDStiffness=1_: Yes
      ### `iConstraintMethod`
    - An _Int_ specifying selection of Constraint Method.
    - If _iConstraintMethod=0_: No
    - If _iConstraintMethod=1_: Yes
    ### `dGrayScaleRatio`
    - A _Double_ specifying gray scale ratio.
    ### `iOutputGrayScaleRatio`
    - An _Int_ Specifing whether or not output gray scale ratio.

<!-- @since:5.1.0 -->
### 45. OptimizationOutput

- A list of _Boolean_ specifying the optimization output paramters. Output if it set 1. From left to right,
- NodalShapeVariation
- ShapeVariation
- NodalDensityRation
- DensityRation
- Sensitivity
- Sensitivity\_Of\_Objective
- Sensitivity\_Of\_Constraint
- Sensitivities

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 31. HeatConvection

Heat convection  (not used for Structural), set 0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 32. bool

Create process for bolt fixed lentgh flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 34. int

Numric type.  \[0:Real; 1:Power, 2:Auto]

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 35. int

UI Width

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 36. int

UI Precision

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 37. bool

Export geometry id flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 38. bool

Separate part info file flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 39. string

ADVC Template file path

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 40. bool

Output definition flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 41. bool

Data format type. \[0:Single, 1:Double]

## Return Code

- "1": The function can be executed
- "FAILED": The function cannot be executed

## Sample Code

```psj
ADVC _Structure("Job _1", "", 0, [119:1], [], [], 0, 0:0, 0, 0, 0, 0, 0, 0, 0, [3:2], 1, 1, 1, 1, 0, 1, 22:1, 0, "", 2147483647, 2147483647, 0, 1, [], 0, 0, "C:/Temp/Export.adx", 0, 10, 6, 0, 0, "", 1, 0, [(0, "Compliance _1", 0, "", 1.79769e+308, [119:1], -1, 1.79769e+308, -1, 1.79769e+308, 1, 0:0, 0:0, 0:0, -1, 1.79769e+308, 1.79769e+308, 2147483647)], [(9, "Volume _1", 0, "", 1.79769e+308, [], 0, 1.79769e+308, -1, 0.4, 1, 0:0, 0:0, 0:0, -1, 1.79769e+308, 1.79769e+308, 2147483647)], [], [(13, "ShapeOptimization _1", 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 100, 0.1, 1.79769e+308, 0.01, 1, 1, -1, 2147483647, -1, 1.79769e+308, "", -1, -1, 1.79769e+308, 1.79769e+308, 1, -1, 0:0, 0:0, 0:0, 0:0, [], -1, 1.79769e+308, -1, -1, -1, 1, 1)], (0, 1, 0, 0, 1, 1, 1, 1))
```
