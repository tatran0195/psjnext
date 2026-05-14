---
title: "Analysis.Ansys.Steady()"
description: "Export the Ansys Steady Static Heat Transfer solver file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Ansys > Steady"
---

## Description

Export the Ansys Steady Static Heat Transfer solver file

## Syntax

```psj
Analysis.Ansys.Steady(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The job name of Ansys analysis.

<!-- @since:5.0.1 @type:String @optional @default:"Job1" -->
### `strAnsysJobName`

- The name of Ansys Steady Static Heat Transfer analysis.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strJobName`

- The description for new Ansys analysis.

<!-- @since:5.0.1 @type:BASIC @optional @default:BASIC -->
### `ansysAnalysisBasic`

- The Ansys Analysis - Linear Static Structure input parameter.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bRunAPDL`

- The enable/disalbe the option that running Ansys Parametric Design Language (APDL).

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bWriteResultDB`

- The enable/disalbe the option that write result database.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLoadCaseId`

- The load case identify number .

<!-- @since:5.0.1 @type:STEADY _STATIC @optional @default:STEADY _STATIC -->
### `ansysAnalysisSteadyStatic`

- The Ansys Analysis - Steady Static Heat Transfer input parameter.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strAnsysVersion`

- The Ansys Version information.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strCommandLineOption`

- The Command Line Option information.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bOutputSOLVE`

- The enable/disalbe SOLVE command write out.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The editing ansys job.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFileName`

- The exporting path for .dat file.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-4}
Geometry.Part.Cube()

Analysis.Ansys.Steady("Job1", ansysAnalysisBasic=BASIC(dTimeStepSize=1.0, dMinTimeStep=1.0),
    iLoadCaseId=1, ansysAnalysisSteadyStatic=STEADY _STATIC(bSteadyStaticMemorySave=True), strFileName="D:/Job1.dat")
```
