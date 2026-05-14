---
title: "Analysis.Ansys.Harmonic()"
description: "Export the Ansys Harmonic Structural solver file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Ansys > Harmonic"
---

## Description

Export the Ansys Harmonic Structural solver file.

## Syntax

```psj
Analysis.Ansys.Harmonic(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strJobName`

- The job name of Ansys analysis.

<!-- @since:5.0.1 @type:String @optional @default:"Job1" -->
### `strAnsysJobName`

- The name of Ansys NorHarmonic Structural analysis.

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
### `dAnsysAnalysisEndFreq`

- The end frequency number.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAnsysAnalysisStartFreq`

- The start frequency number.

<!-- @since:5.0.1 @type:HARMONIC @optional @default:HARMONIC -->
### `ansysAnalysisHarmonic`

- The Ansys Analysis - Hamonic Structural input parameter.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLoadCaseId`

- The load case identify number.

<!-- @since:5.0.1 @type:MODAL @optional @default:MODAL -->
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

```psj {3-4}
Geometry.Part.Cube()

Analysis.Ansys.Harmonic("Job1", ansysAnalysisHarmonic=HARMONIC(bHarmonicOutputDisplacements=True),
    iLoadCaseId=1, strFileName="C:/Job1.dat")
```
