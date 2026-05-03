---
title: "Analysis.Ansys.HeadTransferSteady()"
description: "Export the Ansys Heat Transfer solver file"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Analysis > Ansys > HeadTransferSteady"
macro_link: "[CreateAnsysJob](../../macro/analysis/CreateAnsysJob)"
---

## Description

Export the Ansys Heat Transfer solver file

## Syntax

```psj
Analysis.Ansys.HeadTransferSteady(...)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `iJobdataAnatype` @type(Integer) @default(0)

- The job data analysis type.

### `iJobdataSoltype` @type(Integer) @default(0)

- The job data solution type.

### `strJobdataJobname` @type(String) @default("Job1")

- The job data job name.

### `strJobdataJobdescription` @type(String) @default("")

- The job data job description.

### `bBasicdataBoutputdisplacements` @type(Boolean) @default(False)

- The basic data output displacements.

### `bBasicdataBoutputreactionload` @type(Boolean) @default(False)

- The basic data output reaction oad.

### `bBasicdataBoutputstrain` @type(Boolean) @default(False)

- The basic data output strain.

### `bBasicdataBoutputstress` @type(Boolean) @default(False)

- The basic data output stress.

### `iBasicdataIanalysisopt` @type(Integer) @default(0)

- The basic data analysis option.

### `bBasicdataBcalPressEffects` @type(Boolean) @default(False)

- The basic data caculation press effects.

### `dBasicdataFunitem` @type(Double) @default(0.0)

- The basic data unit temperature.

### `dBasicdataFreftemp` @type(Double) @default(0.0)

- The basic data reference temperature.

### `dBasicdataFendloadtime` @type(Double) @default(0.0)

- The basic data end load time.

### `iBasicdataItimestep` @type(Integer) @default(0)

- The basic data time step.

### `iBasicdataIstepchosen` @type(Integer) @default(0)

- The basic data step chosen.

### `iBasicdataIsubstepnum` @type(Integer) @default(0)

- The basic data sub step number.

### `iBasicdataImaxsubstep` @type(Integer) @default(0)

- The basic data maximum sub step.

### `iBasicdataIminstepnum` @type(Integer) @default(0)

- The basic data minimum sub step.

### `dBasicdataFtimestepsize` @type(Double) @default(0.0)

- The basic data time step size.

### `dBasicdataFmintimestep` @type(Double) @default(0.0)

- The basic data minimum sub step.

### `dBasicdataFmaxtimestep` @type(Double) @default(0.0)

- The basic data maximum sub step.

### `iBasicdataIwritereslutfre` @type(Integer) @default(1)

- The basic data write result frequency.

### `iBasicdataIn` @type(Integer) @default(1)

- The basic data in.

### `bRunAPDL` @type(Boolean) @default(False)

- The run Ansys APDL.

### `bWriteResultDB` @type(Boolean) @default(False)

- The write result d .

### `dFEndFreq` @type(Double) @default(DFLT\_DBL)

- The end frequence.

### `dFStartFreq` @type(Double) @default(DFLT\_DBL)

- The start frequence.

### `iFulltransdataIsolutionoption` @type(Integer) @default(0)

- The full translation data solution option.

### `dFulltransdataFpropchange` @type(Double) @default(0.05)

- The full translation data property change.

### `iFulltransdataIpointnum` @type(Integer) @default(64)

- The full translation data point number.

### `dFulltransdataFmintemp` @type(Double) @default(0.0)

- The full translation data minimum temperature.

### `dFulltransdataFmaxtemp` @type(Double) @default(0.0)

- The full translation data maximum temperature.

### `iFulltransdataIequationsolv` @type(Integer) @default(0)

- The full translation data equation solve.

### `dFulltransdataFtollevel` @type(Double) @default(0.0)

- The full translation data tolerance level.

### `dFulltransdataFmultiplier` @type(Double) @default(0.0)

- The full translation data multiplier.

### `bFulltransdataBsignleprecision` @type(Boolean) @default(False)

- The full translation data single precision.

### `bFulltransdataBmemorysave` @type(Boolean) @default(False)

- The full translation data memory save.

### `dFulltransdataFtempdiff` @type(Double) @default(1.1)

- The full translation data temperature difference.

### `dHarmonicdataFstartfreq` @type(Double) @default(0.0)

- The harmonic data start frequence.

### `dHarmonicdataFendfreq` @type(Double) @default(1.0)

- The harmonic data end frequence.

### `iHarmonicdataNsubsteps` @type(Integer) @default(0)

- The harmonic data sub steps.

### `dHarmonicdataFalphad` @type(Double) @default(0.0)

- The harmonic data alpha.

### `dHarmonicdataFbetad` @type(Double) @default(0.0)

- The harmonic data beta.

### `dHarmonicdataFdmprat` @type(Double) @default(0.0)

- The harmonic data DMP ratio.

### `bHarmonicdataBoutputdisplacements` @type(Boolean) @default(False)

- The harmonic data output displacements.

### `bHarmonicdataBoutputstrain` @type(Boolean) @default(False)

- The harmonic data output strain.

### `bHarmonicdataBoutputstress` @type(Boolean) @default(False)

- The harmonic data output stress.

### `iLCId` @type(Integer) @default(0)

- The LC ID.

### `iModeShape` @type(Integer) @default(0)

- The mode shape.

### `iModaldataImodemethod` @type(Integer) @default(0)

- The modal data mode method.

### `iModaldataIextractnum` @type(Integer) @default(1)

- The modal data extract number.

### `bModaldataBexpandshape` @type(Boolean) @default(True)

- The modal data expand shape.

### `iModaldataIexpandnum` @type(Integer) @default(0)

- The modal data expand number.

### `bModaldataBuseapprox` @type(Boolean) @default(False)

- The modal data use approximately.

### `bModaldataBinclprsseff` @type(Boolean) @default(False)

- The modal data include prsseff.

### `bModaldataBmemorysave` @type(Boolean) @default(False)

- The modal data memory save.

### `bModaldataBrsvec` @type(Boolean) @default(False)

- The modal data resource vector.

### `bModaldataBoutputdisplacements` @type(Boolean) @default(False)

- The modal data output displacements.

### `bModaldataBoutputstrain` @type(Boolean) @default(False)

- The modal data output strain.

### `bModaldataBoutputstress` @type(Boolean) @default(False)

- The modal data output stress.

### `iReduceddataIprintnum` @type(Integer) @default(0)

- The reduceddata print number.

### `bSsdataBmemorysave` @type(Boolean) @default(False)

- The ssdata memory save.

### `bSsdataBoutputheatflux` @type(Boolean) @default(False)

- The ssdata output heat flux.

### `bSsdataBoutputtemperature` @type(Boolean) @default(False)

- The ssdata output temperature.

### `bSsdataBpivotscheck` @type(Boolean) @default(True)

- The ssdata pivots check.

### `bSsdataBsignleprecision` @type(Boolean) @default(False)

- The ssdata single precision.

### `dSsdataFmultiplier` @type(Double) @default(0.0)

- The ssdata multiplier.

### `dSsdataFtempdiff` @type(Double) @default(0.0)

- The ssdata temperature difference.

### `dSsdataFtollevel` @type(Double) @default(0.0)

- The ssdata tolerance level.

### `iSsdataIadaptivedes` @type(Integer) @default(0)

- The ssdata adaptive destination.

### `iSsdataIequationsolv` @type(Integer) @default(0)

- The ssdata equation solve.

### `iSsdataInpoption` @type(Integer) @default(0)

- The ssdata inpoption.

### `strAnsysVersion` @type(String) @default("")

- The ansys version.

### `strCommandLineOption` @type(String) @default("")

- The command line option.

### `bOutputSOLVE` @type(Boolean) @default(False)

- The output solve.

### `iSubspacedataIrigidmode` @type(Integer) @default(0)

- The subspace data rigid mode.

### `iSubspacedataIworksize` @type(Integer) @default(8)

- The subspace data work size.

### `iSubspacedataInpadnum` @type(Integer) @default(4)

- The subspace data inpad number.

### `iSubspacedataIblocknum` @type(Integer) @default(5)

- The subspace data block number.

### `iSubspacedataImaxiteratcnt` @type(Integer) @default(0)

- The subspace data maximum iterator number.

### `iSubspacedataIminnshift` @type(Integer) @default(0)

- The subspace data iminnshift.

### `iSubspacedataIseqcheck` @type(Integer) @default(0)

- The subspace data iseqcheck.

### `bTransientdataBtraneffect` @type(Boolean) @default(True)

- The transient data effection.

### `iTransientdataIloadingtype` @type(Integer) @default(0)

- The transient data loading type.

### `dTransientdataFmassmatrixmult` @type(Double) @default(0.0)

- The transient data mass matrix multiple.

### `dTransientdataFstiffmatrixmult` @type(Double) @default(0.0)

- The transient data stiff matrix multiple.

### `bTransientdataBmidstep` @type(Boolean) @default(False)

- The transient data midle step.

### `dTransientdataFtolerancebisection` @type(Double) @default(0.0)

- The transient data tolerance binary section.

### `dTransientdataFtolerancetimestep` @type(Double) @default(0.0)

- The transient data tolerance time step.

### `iTransientdataItimeinteralgor` @type(Integer) @default(0)

- The transient data time inter algorithm.

### `iTransientdataItimeinter` @type(Integer) @default(0)

- The transient data time inter.

### `dTransientdataFgamma` @type(Double) @default(0.005)

- The transient data gamma.

### `dTransientdataFalpha` @type(Double) @default(0.25250625)

- The transient data alpha.

### `dTransientdataFdelta` @type(Double) @default(0.505)

- The transient data delta.

### `dTransientdataFalphaf` @type(Double) @default(0.005)

- The transient data alpha f.

### `dTransientdataFalpham` @type(Double) @default(0.0)

- The transient data alpha m.

### `bTransientdataBoutputtemperature` @type(Boolean) @default(False)

- The transient data output temperature.

### `bTransientdataBoutputheatflux` @type(Boolean) @default(False)

- The transient data output heat flux.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.Ansys.HeatTransferSteady(strName="", iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None)
```
