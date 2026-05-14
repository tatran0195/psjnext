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

<!-- @since:5.1.0 @type:String @optional @default:'Untitled' -->
### `strResultTitle`

- The name of the result to be created.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iCompareRegionType`

- The region type to make the comparison.
  - 0: by Parts
  - 1: by Groups

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dEdgeTolerance`

- The tolerance between edges.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iMeshOfTwoSurfaces`

- The position of mesh nodes.
  - 0: Same
  - 1: Different

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iAxisDirection`

- The axis direction.
  - 0: X
  - 1: Y
  - 2: Z
  - 3: Arbitrary direction

<!-- @since:5.1.0 @type:List[Double] @optional @default:[1.0,0.0,0.0] -->
### `dlDirection`

- The direction vector to be calculated.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crReferenceNode`

- The reference node.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crFirstTarget`

- The first target. The target can be Part or Group Element depend on the selection of _iCompareRegionType_.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crSecondTarget`

- The second target. The target can be Part or Group depend on the selection of _iCompareRegionType_.

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
