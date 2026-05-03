---
title: "Report.List()"
description: "Export the selected results to a CSV file or a universal format"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Report > List"
macro_link: "[ResultOutputList](../../macro/report/ResultOutputList)"
---

## Description

Export the selected results to a CSV file or a universal format.

## Syntax

```psj
Report.List(...)
```

## Inputs

### `strPath` @type(String) @required

- The file path to be exported.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The selected parts to be exported data.

### `iResultType` @type(Integer) @default(0)

- The result type to be exported.
  - 0: Displacement
  - 1: Temperature
  - 2: Energy
  - 3: SPC Force
  - 4: MPC Force
  - 5: Stress
  - 6: Strain
  - 7: Other

### `iOutput` @type(Integer) @default(0)

- To output all selected subcases in one file or in separated files for each selected subcase.
  - 0: Single.
  - 1: Multiple.

### `iOutPutType` @type(Integer) @default(0)

- The format of the output file.
  - 0: CSV
  - 1: Unv

### `iResultPosition` @type(Integer) @default(0)

- The output position of the result.
  - 0: Node
  - 1: Element

### `bMidNode` @type(Boolean) @default(False)

- Whether to enable/disable middle node for the exported results.

### `listPostResultKey` @type(List\[POST\_RESULT\_KEY]) @default(POST\_RESULT\_KEY())

- The attributes of the selected result.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25-29}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
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
                iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
Post.EnableMiddleNodes()

# Make List report
reportList = Report.List(strPath="C:/temp/ReportList.csv", 
                        crlTargets=[Part(3)], 
                        iOutput=1, 
                        bMidNode=True, 
                        listPostResultKey=[[2, 1, 1, 0], [2, 1, 2, 0], [2, 1, 3, 0], [2, 1, 4, 0], [2, 1, 5, 0]])
JPT.Debugger(reportList)
```
