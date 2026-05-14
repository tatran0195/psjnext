---
title: "Home.ExportResultToTXT()"
description: "Export the selected result file to text format (*.txt)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ExportResultToTXT"
macro _link: "[PostExportToTxt](../../macro/home/PostExportToTxt)"
---

## Description

Export the selected result file to text format (\*.txt).

## Syntax

```psj
Home.ExportResultToTXT(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strFileName`

- The file path to be exported.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSpliterType`

- The method to delimit output values.
  - 0: Space ( )
  - 1: Comma (,)
  - 2: Semicolon (;)

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bAppend`

- Whether to append the results to the specified file.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlJobs`

- The post job.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilAnalysisTypes`

- The analysis type.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilResultSets`

- The result set.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilTimeSteps`

- The time step.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilResultTypes`

- The result type.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilResultPos`

- The result position.

<!-- @since:5.1.0 @type:List[String] @optional @default:[] -->
### `strlResultNames`

- The result name.

<!-- @since:5.1.0 @type:List[String] @optional @default:[] -->
### `strlCompNames`

- The component name.

<!-- @since:5.1.0 @type:List[String] @optional @default:[] -->
### `strlNames`

- The result name.

<!-- @since:5.1.0 @type:List[String] @optional @default:[] -->
### `strlTypes`

- The result type.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlEdit`

- The edit target.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-18}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
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
                                    strlTypes=["TYPE _VIRTUAL _RESULT _ITEM", "TYPE _VIRTUAL _RESULT _ITEM"], 
                                    crlEdit=[Unknown(0, 0)])
JPT.Debugger(exportFile )
```
