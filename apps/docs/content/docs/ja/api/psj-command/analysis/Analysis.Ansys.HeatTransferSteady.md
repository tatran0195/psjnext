---
title: "Analysis.Ansys.HeadTransferSteady()"
description: "Export the Ansys Heat Transfer solver file"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Analysis > Ansys > HeadTransferSteady"
macro _link: "[CreateAnsysJob](../../macro/analysis/CreateAnsysJob)"
---

## Description

Export the Ansys Heat Transfer solver file

## Syntax

```psj
Analysis.Ansys.HeadTransferSteady(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strName

- Specify the name.

<!-- @since:5.1.0 @optional -->
### iJobdataAnatype

- Specify the job data analysis type.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iJobdataSoltype

- Specify the job data solution type.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strJobdataJobname

- Specify the job data job name.
- The default value is "Job1".

<!-- @since:5.1.0 @optional -->
### strJobdataJobdescription

- Specify the job data job description.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### bBasicdataBoutputdisplacements

- Specify the basic data output displacements.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bBasicdataBoutputreactionload

- Specify the basic data output reaction oad.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bBasicdataBoutputstrain

- Specify the basic data output strain.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bBasicdataBoutputstress

- Specify the basic data output stress.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### iBasicdataIanalysisopt

- Specify the basic data analysis option.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bBasicdataBcalPressEffects

- Specify the basic data caculation press effects.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### dBasicdataFunitem

- Specify the basic data unit temperature.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dBasicdataFreftemp

- Specify the basic data reference temperature.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dBasicdataFendloadtime

- Specify the basic data end load time.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iBasicdataItimestep

- Specify the basic data time step.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iBasicdataIstepchosen

- Specify the basic data step chosen.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iBasicdataIsubstepnum

- Specify the basic data sub step number.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iBasicdataImaxsubstep

- Specify the basic data maximum sub step.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iBasicdataIminstepnum

- Specify the basic data minimum sub step.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dBasicdataFtimestepsize

- Specify the basic data time step size.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dBasicdataFmintimestep

- Specify the basic data minimum sub step.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dBasicdataFmaxtimestep

- Specify the basic data maximum sub step.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iBasicdataIwritereslutfre

- Specify the basic data write result frequency.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iBasicdataIn

- Specify the basic data in.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bRunAPDL

- Specify the run Ansys APDL.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bWriteResultDB

- Specify the write result d .
- The default value is False.

<!-- @since:5.1.0 @optional -->
### dFEndFreq

- Specify the end frequence.
- The default value is DFLT\_DBL.

<!-- @since:5.1.0 @optional -->
### dFStartFreq

- Specify the start frequence.
- The default value is DFLT\_DBL.

<!-- @since:5.1.0 @optional -->
### iFulltransdataIsolutionoption

- Specify the full translation data solution option.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dFulltransdataFpropchange

- Specify the full translation data property change.
- The default value is 0.05.

<!-- @since:5.1.0 @optional -->
### iFulltransdataIpointnum

- Specify the full translation data point number.
- The default value is 64.

<!-- @since:5.1.0 @optional -->
### dFulltransdataFmintemp

- Specify the full translation data minimum temperature.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dFulltransdataFmaxtemp

- Specify the full translation data maximum temperature.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iFulltransdataIequationsolv

- Specify the full translation data equation solve.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dFulltransdataFtollevel

- Specify the full translation data tolerance level.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dFulltransdataFmultiplier

- Specify the full translation data multiplier.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### bFulltransdataBsignleprecision

- Specify the full translation data single precision.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bFulltransdataBmemorysave

- Specify the full translation data memory save.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### dFulltransdataFtempdiff

- Specify the full translation data temperature difference.
- The default value is 1.1.

<!-- @since:5.1.0 @optional -->
### dHarmonicdataFstartfreq

- Specify the harmonic data start frequence.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dHarmonicdataFendfreq

- Specify the harmonic data end frequence.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### iHarmonicdataNsubsteps

- Specify the harmonic data sub steps.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dHarmonicdataFalphad

- Specify the harmonic data alpha.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dHarmonicdataFbetad

- Specify the harmonic data beta.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dHarmonicdataFdmprat

- Specify the harmonic data DMP ratio.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### bHarmonicdataBoutputdisplacements

- Specify the harmonic data output displacements.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bHarmonicdataBoutputstrain

- Specify the harmonic data output strain.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bHarmonicdataBoutputstress

- Specify the harmonic data output stress.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### iLCId

- Specify the LC ID.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iModeShape

- Specify the mode shape.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iModaldataImodemethod

- Specify the modal data mode method.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iModaldataIextractnum

- Specify the modal data extract number.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bModaldataBexpandshape

- Specify the modal data expand shape.
- The default value is True.

<!-- @since:5.1.0 @optional -->
### iModaldataIexpandnum

- Specify the modal data expand number.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bModaldataBuseapprox

- Specify the modal data use approximately.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bModaldataBinclprsseff

- Specify the modal data include prsseff.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bModaldataBmemorysave

- Specify the modal data memory save.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bModaldataBrsvec

- Specify the modal data resource vector.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bModaldataBoutputdisplacements

- Specify the modal data output displacements.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bModaldataBoutputstrain

- Specify the modal data output strain.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bModaldataBoutputstress

- Specify the modal data output stress.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### iReduceddataIprintnum

- Specify the reduceddata print number.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bSsdataBmemorysave

- Specify the ssdata memory save.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bSsdataBoutputheatflux

- Specify the ssdata output heat flux.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bSsdataBoutputtemperature

- Specify the ssdata output temperature.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bSsdataBpivotscheck

- Specify the ssdata pivots check.
- The default value is True.

<!-- @since:5.1.0 @optional -->
### bSsdataBsignleprecision

- Specify the ssdata single precision.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### dSsdataFmultiplier

- Specify the ssdata multiplier.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dSsdataFtempdiff

- Specify the ssdata temperature difference.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dSsdataFtollevel

- Specify the ssdata tolerance level.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iSsdataIadaptivedes

- Specify the ssdata adaptive destination.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iSsdataIequationsolv

- Specify the ssdata equation solve.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iSsdataInpoption

- Specify the ssdata inpoption.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strAnsysVersion

- Specify the ansys version.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strCommandLineOption

- Specify the command line option.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### bOutputSOLVE

- Specify the output solve.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### iSubspacedataIrigidmode

- Specify the subspace data rigid mode.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iSubspacedataIworksize

- Specify the subspace data work size.
- The default value is 8.

<!-- @since:5.1.0 @optional -->
### iSubspacedataInpadnum

- Specify the subspace data inpad number.
- The default value is 4.

<!-- @since:5.1.0 @optional -->
### iSubspacedataIblocknum

- Specify the subspace data block number.
- The default value is 5.

<!-- @since:5.1.0 @optional -->
### iSubspacedataImaxiteratcnt

- Specify the subspace data maximum iterator number.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iSubspacedataIminnshift

- Specify the subspace data iminnshift.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iSubspacedataIseqcheck

- Specify the subspace data iseqcheck.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bTransientdataBtraneffect

- Specify the transient data effection.
- The default value is True.

<!-- @since:5.1.0 @optional -->
### iTransientdataIloadingtype

- Specify the transient data loading type.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dTransientdataFmassmatrixmult

- Specify the transient data mass matrix multiple.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dTransientdataFstiffmatrixmult

- Specify the transient data stiff matrix multiple.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### bTransientdataBmidstep

- Specify the transient data midle step.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### dTransientdataFtolerancebisection

- Specify the transient data tolerance binary section.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dTransientdataFtolerancetimestep

- Specify the transient data tolerance time step.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iTransientdataItimeinteralgor

- Specify the transient data time inter algorithm.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iTransientdataItimeinter

- Specify the transient data time inter.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dTransientdataFgamma

- Specify the transient data gamma.
- The default value is 0.005.

<!-- @since:5.1.0 @optional -->
### dTransientdataFalpha

- Specify the transient data alpha.
- The default value is 0.25250625.

<!-- @since:5.1.0 @optional -->
### dTransientdataFdelta

- Specify the transient data delta.
- The default value is 0.505.

<!-- @since:5.1.0 @optional -->
### dTransientdataFalphaf

- Specify the transient data alpha f.
- The default value is 0.005.

<!-- @since:5.1.0 @optional -->
### dTransientdataFalpham

- Specify the transient data alpha m.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### bTransientdataBoutputtemperature

- Specify the transient data output temperature.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bTransientdataBoutputheatflux

- Specify the transient data output heat flux.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.Ansys.HeatTransferSteady(strName="", iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT _DBL, dFStartFreq=DFLT _DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None)
```
