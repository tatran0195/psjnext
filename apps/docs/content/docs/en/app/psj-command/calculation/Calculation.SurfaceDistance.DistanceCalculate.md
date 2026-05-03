---
title: "Calculation.SurfaceDistance.DistanceCalculate()"
description: "Display the distance between parts as a contour"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > SurfaceDistance > DistanceCalculate"
macro_link: "[ACCombineSurfaceDistanceDistanceCalculatedAnimation](../../macro/calculation/SurfaceDistanceDistanceCalculate)"
---

## Description

Display the distance between parts as a contour.

## Syntax

```psj
Calculation.SurfaceDistance.DistanceCalculate(...)
```

## Inputs

### `strResultTitle` @type(String) @default('Untitled')

- The name of the result to be created.

### `iCompareRegionType` @type(Integer) @default(0)

- The region type to make the comparison.
  - 0: by Parts
  - 1: by Groups

### `dEdgeTolerance` @type(Double) @default(0.0)

- The tolerance between edges.

### `iMeshOfTwoSurfaces` @type(Integer) @default(0)

- The position of mesh nodes.
  - 0: Same
  - 1: Different

### `iAxisDirection` @type(Integer) @default(0)

- The axis direction.
  - 0: X
  - 1: Y
  - 2: Z
  - 3: Arbitrary direction

### `dlDirection` @type(List\[Double]) @default(\[1.0,0.0,0.0])

- The direction vector to be calculated.

### `crReferenceNode` @type(Cursor) @default(None)

- The reference node.

### `crFirstTarget` @type(Cursor) @default(None)

- The first target. The target can be Part or Group Element depend on the selection o&#x66;_&#x69;CompareRegionType_.

### `crSecondTarget` @type(Cursor) @default(None)

- The second target. The target can be Part or Group depend on the selection o&#x66;_&#x69;CompareRegionType_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25-26}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
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
