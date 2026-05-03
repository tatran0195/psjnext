---
title: "Tools.ResultToLoad()"
description: "Export the selected result name to solver information (as solver keyword card) for the selected entities. Depending on selection of convert load type, the analysis result will be exported to solver card information respectively."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > ResultToLoad"
macro_link: "[CmdExportLoad](../../macro/tools/CmdExportLoad)"
---

## Description

Export the selected result name to solver information (as solver keyword card) for the selected entities. Depending on selection of convert load type, the analysis result will be exported to solver card information respectively.

## Syntax

```psj
Tools.ResultToLoad(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The selected entities. The entities can be Part, Face, Node, Element or Group.

### `listPostStepItem` @type(List\[POST\_STEP\_ITEM]) @default(POST\_STEP\_ITEM())

- The attributes of each Post Step Item.

### `vecResultLoad` @type(Vector of RESULT\_LOAD) @default(RESULT\_LOAD())

- The components of the selected result.

### `strExportPath` @type(String) @required

- The path of file to be exported.

### `iSolverType` @type(Integer) @default(2 (Nastran))

- The solver type.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25-34}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=1, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# Result to load
sampleFile = Tools.ResultToLoad(crlTargets=[Face(10)], 
                                postStepItem=POST_STEP_ITEM(
                                    iAnalysisType=1, 
                                    iResultSet=1, 
                                    iTimeStep=1), 
                                vecResultLoad=[RESULT_LOAD(
                                    iVrType=6, 
                                    strResultName="Displacement", 
                                    strLoadName="Enforced Displacement")], 
                                strExportPath="C:/temp/ResultToLoadFile")
JPT.Debugger(sampleFile)
```
