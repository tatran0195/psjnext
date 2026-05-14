---
title: "Analysis.Ansys.LinearStatic()"
description: "Export the Ansys Linear Static Structural solver file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Ansys > LinearStatic"
---

## Description

Export the Ansys Linear Static Structural solver file.

## Syntax

```psj
Analysis.Ansys.LinearStatic(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strJobName`

- The job name of Ansys analysis.

<!-- @since:5.1.0 @type:Int @optional @default:0 -->
### `iVersion`

- The version of this command.

<!-- @since:5.0.1 @type:String @optional @default:"Job1" -->
### `strAnsysJobName`

- The name of Ansys Linear Static Structural analysis.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strAnsysJobDescription`

- The description for new Ansys analysis.

<!-- @since:5.0.1 @type:BASIC @optional @default:BASIC -->
### `ansysAnalysisBasic`

- The Ansys Analysis - Linear Static input parameter.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bRunAPDL`

- The enable/disalbe the option that running Ansys Parametric Design Language (APDL).

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bWriteResultDB`

- The enable/disalbe the option that write result database.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLoadCaseId`

- The load case identify number.

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

Analysis.Ansys.LinearStatic(strJobName="Job1", iVersion=1, strAnsysJobName="Job1", ansysAnalysisBasic=BASIC(dTimeStepSize=1.0, dMinTimeStep=1.0), iLoadCaseId=1, strFileName="C:/temp/Job1.dat")
```
