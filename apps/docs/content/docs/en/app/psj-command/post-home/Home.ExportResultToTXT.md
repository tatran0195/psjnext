---
title: "Home.ExportResultToTXT()"
description: "Export the selected result file to text format (*.txt)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ExportResultToTXT"
macro_link: "[PostExportToTxt](../../macro/home/PostExportToTxt)"
---

## Description

Export the selected result file to text format (\*.txt).

## Syntax

```psj
Home.ExportResultToTXT(...)
```

## Inputs

### `strFileName` @type(String) @required

- The file path to be exported.

### `iSpliterType` @type(Integer) @default(0)

- The method to delimit output values.
  - 0: Space ( )
  - 1: Comma (,)
  - 2: Semicolon (;)

### `bAppend` @type(Boolean) @default(False)

- Whether to append the results to the specified file.

### `crlJobs` @type(List\[Cursor]) @default(\[])

- The post job.

### `ilAnalysisTypes` @type(List\[Integer]) @default(\[])

- The analysis type.

### `ilResultSets` @type(List\[Integer]) @default(\[])

- The result set.

### `ilTimeSteps` @type(List\[Integer]) @default(\[])

- The time step.

### `ilResultTypes` @type(List\[Integer]) @default(\[])

- The result type.

### `ilResultPos` @type(List\[Integer]) @default(\[])

- Result position.

### `strlResultNames` @type(List\[String]) @default(\[])

- The result name.

### `strlCompNames` @type(List\[String]) @default(\[])

- The component name.

### `strlNames` @type(List\[String]) @default(\[])

- The result name.

### `strlTypes` @type(List\[String]) @default(\[])

- The result type.

### `crlEdit` @type(List\[Cursor]) @default(\[])

- The edit target.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-18}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Export result to txt
exportFile = Home.ExportResultToTXT(strFileName="C:/temp/ExportTXT.txt", 
                                    iSpliterType=1, 
                                    crlJobs=[TSVPostJob(1, 1)], 
                                    ilAnalysisTypes=[1, 1], 
                                    ilResultSets=[1, 1], 
                                    ilTimeSteps=[1, 1], 
                                    ilResultTypes=[3, 4], 
                                    ilResultPos=[1, 1], 
                                    strlResultNames=["", ""], 
                                    strlCompNames=["", ""], 
                                    strlNames=["RX", "RY"], 
                                    strlTypes=["TYPE_VIRTUAL_RESULT_ITEM", "TYPE_VIRTUAL_RESULT_ITEM"], 
                                    crlEdit=[Unknown(0, 0)])
JPT.Debugger(exportFile )
```
