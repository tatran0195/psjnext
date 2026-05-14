---
title: "Analysis.Ansys.NormalModes()"
description: "Export the Ansys Normal Modes Structural solver file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Ansys > NormalModes"
---

## Description

Export the Ansys Normal Modes Structural solver file.

## Syntax

```psj
Analysis.Ansys.NormalModes(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strJobName`

- The job name of Ansys analysis.

<!-- @since:5.0.1 @type:String @optional @default:"Job1" -->
### `strAnsysJobName`

- The name of Ansys Normal Modes Structural analysis.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strAnsysJobdescription`

- The description for new Ansys analysis.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bRunAPDL`

- The enable/disalbe the option that running Ansys Parametric Design Language (APDL).

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bWriteResultDB`

- The enable/disalbe the option that write result database.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dEndFreq`

- The end frequency number.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dStartFreq`

- The start frequency number.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLoadCaseId`

- The load case identify number .

<!-- @since:5.0.1 @type:[MODAL]./../../data-type/psj-command/parameter-types/(MODAL) @optional @default:MODAL -->
### `ansysAnalysisModal`

- The Ansys Analysis - Modal Structural input parameter.

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

```psj {3}
Geometry.Part.Cube()

Analysis.Ansys.NormalModes("Job1", iLoadCaseId=1, strFileName="C:/Job1.dat")
```
