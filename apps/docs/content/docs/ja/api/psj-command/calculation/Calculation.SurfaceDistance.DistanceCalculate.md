---
title: "Calculation.SurfaceDistance.DistanceCalculate()"
description: "Display the distance between parts as a contour"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > SurfaceDistance > DistanceCalculate"
macro _link: "[ACCombineSurfaceDistanceDistanceCalculatedAnimation](../../macro/calculation/SurfaceDistanceDistanceCalculate)"
---

## Description

Display the distance between parts as a contour.

## Syntax

```psj
Calculation.SurfaceDistance.DistanceCalculate(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strResultTitle

- Specify the name of the result to be created.
- The default value is 'Untitled'.

<!-- @since:5.1.0 @optional -->
### iCompareRegionType

- Specify the region type to make the comparison.
  - 0: by Parts
  - 1: by Groups
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dEdgeTolerance

- Specify the tolerance between edges.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iMeshOfTwoSurfaces

- Specify the position of mesh nodes.
  - 0: Same
  - 1: Different
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iAxisDirection

- Specify the axis direction.
  - 0: X
  - 1: Y
  - 2: Z
  - 3: Arbitrary direction
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dlDirection

- Specify the direction vector to be calculated.
- The default value is \[1.0,0.0,0.0].

<!-- @since:5.1.0 @optional -->
### crReferenceNode

- Specify the reference node.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crFirstTarget

- Specify the first target. The target can be Part or Group Element depend on the selection of _iCompareRegionType_.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crSecondTarget

- Specify the second target. The target can be Part or Group depend on the selection of _iCompareRegionType_.
- The default value is _None_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25-26}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Plot the displacement result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=1, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
Post.EnableMiddleNodes()

# Surface distance
Calculation.SurfaceDistance.DistanceCalculate(dEdgeTolerance=2.0, crReferenceNode=Node(124), crFirstTarget=Part(4), 
                                            crSecondTarget=Part(6))
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=1, 
                iAnalysisID=1, 
                iResultSet=1000, 
                strResultName="Untitled", 
                strResultCompName="SurfaceDistance", 
                iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
Post.EnableMiddleNodes()
```
