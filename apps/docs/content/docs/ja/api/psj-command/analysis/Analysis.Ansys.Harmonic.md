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

<!-- @since:5.0.1 @required -->
### strJobName

- Specify the job name of Ansys analysis.

<!-- @since:5.0.1 @optional -->
### strAnsysJobName

- Specify the the name of Ansys NorHarmonic Structural analysis.
- The default value is "Job1".

<!-- @since:5.0.1 @optional -->
### strAnsysJobdescription

- Specify the description for new Ansys analysis.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### bRunAPDL

- Specify running Ansys Parametric Design Language (APDL).
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bWriteResultDB

- Specify write result database.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dAnsysAnalysisEndFreq

- Specify the end frequency number.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dAnsysAnalysisStartFreq

- Specify the start frequency number.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### ansysAnalysisHarmonic

- Specify the Ansys Analysis - Hamonic Structural input parameter.
- The default value is [HARMONIC](./../../data-type/psj-command/parameter-types/HARMONIC).

<!-- @since:5.0.1 @optional -->
### iLoadCaseId

- Specify the load case identify number.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ansysAnalysisModal

- Specify the Ansys Analysis - Modal Structural input parameter.
- The default value is [MODAL](./../../data-type/psj-command/parameter-types/MODAL).

<!-- @since:5.0.1 @optional -->
### strAnsysVersion

- Specify the Ansys Version information.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### strCommandLineOption

- Specify the Command Line Option information.
- The default value is "".

### `bOutputSOLVE`

- A _Boolean_ enable/disalbe SOLVE command write out.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the editing ansys job.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### strFileName

- Specify the exporting path for .dat file.
- The default value is "".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-4}
Geometry.Part.Cube()

Analysis.Ansys.Harmonic("Job1", ansysAnalysisHarmonic=HARMONIC(bHarmonicOutputDisplacements=True),
    iLoadCaseId=1, strFileName="C:/Job1.dat")
```
