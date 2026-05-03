---
title: "Analysis.Ansys.Harmonic()"
description: "Export the Ansys Harmonic Structural solver file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > Ansys > Harmonic"
---

## Description

Export the Ansys Harmonic Structural solver file.

## Syntax

```psj
Analysis.Ansys.Harmonic(...)
```

## Inputs

### `strJobName` @type(String) @required

- The job name of Ansys analysis.

### `strAnsysJobName` @type(String) @default("Job1")

- The the name of Ansys NorHarmonic Structural analysis.

### `strAnsysJobdescription` @type(String) @default("")

- The description for new Ansys analysis.

### `bRunAPDL` @type(Boolean) @default(False)

- Enable/disalbe the option that running Ansys Parametric Design Language (APDL).

### `bWriteResultDB` @type(Boolean) @default(False)

- Enable/disalbe the option that write result database.

### `dAnsysAnalysisEndFreq` @type(Double) @default(DFLT\_DBL)

- The end frequency number.

### `dAnsysAnalysisStartFreq` @type(Double) @default(DFLT\_DBL)

- The start frequency number.

### `ansysAnalysisHarmonic` @type(HARMONIC) @default(HARMONIC)

- The Ansys Analysis - Hamonic Structural input parameter.

### `iLoadCaseId` @type(Integer) @default(0)

- The load case identify number.

### `ansysAnalysisModal` @type(MODAL) @default(MODAL)

- The Ansys Analysis - Modal Structural input parameter.

### `strAnsysVersion` @type(String) @default("")

- The Ansys Version information.

### `strCommandLineOption` @type(String) @default("")

- The Command Line Option information.

### `bOutputSOLVE` @type(Boolean) @default(False)

- Enable/disalbe SOLVE command write out.

### `crEdit` @type(Cursor) @default(None)

- The editing ansys job.

### `strFileName` @type(String) @default("")

- The exporting path for .dat file.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-4}
Geometry.Part.Cube()

Analysis.Ansys.Harmonic("Job1", ansysAnalysisHarmonic=HARMONIC(bHarmonicOutputDisplacements=True),
    iLoadCaseId=1, strFileName="C:/Job1.dat")
```
