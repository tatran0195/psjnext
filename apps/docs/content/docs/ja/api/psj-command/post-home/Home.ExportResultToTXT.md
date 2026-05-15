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

<!-- @since:5.1.0 @required -->
### strFileName

- Specify the file path to be exported.

<!-- @since:5.1.0 @optional -->
### iSpliterType

- Specify the method to delimit output values.
  - 0: Space ( )
  - 1: Comma (,)
  - 2: Semicolon (;)
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bAppend

- Specify whether to append the results to the specified file.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### crlJobs

- Specify the post job.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### ilAnalysisTypes

- Specify the analysis type.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### ilResultSets

- Specify the result set.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### ilTimeSteps

- Specify the time step.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### ilResultTypes

- Specify the result type.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### ilResultPos

- Specify result position.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### strlResultNames

- Specify the result name.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### strlCompNames

- Specify the component name.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### strlNames

- Specify the result name.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### strlTypes

- Specify the result type.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crlEdit

- Specify the edit target.
- The default value is \[].

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
