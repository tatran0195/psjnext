---
title: "Post.PartialContour()"
description: "Show contour only on the selected entities"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > PartialContour"
macro _link: "[DisplayPartialContour](../../macro/post/DisplayPartialContour)"
---

## Description

Show contour only on the selected entities.

## Syntax

```psj
Post.PartialContour(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The targets to be displayed with contour. The targets can be part, face, bar, node, element, or groups.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bUsePartColor`

- Whether to display part color on the unselected entities.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=4))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# Display contour only on Part(3)
Post.PartialContour(crlTargets=[Part(3)])
```
