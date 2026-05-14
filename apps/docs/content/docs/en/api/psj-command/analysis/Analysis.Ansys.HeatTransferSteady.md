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

<!-- @since:5.1.0 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iJobdataAnatype`

- The job data analysis type.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iJobdataSoltype`

- The job data solution type.

<!-- @since:5.1.0 @type:String @optional @default:"Job1" -->
### `strJobdataJobname`

- The job data job name.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strJobdataJobdescription`

- The job data job description.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBasicdataBoutputdisplacements`

- The basic data output displacements.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBasicdataBoutputreactionload`

- The basic data output reaction oad.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBasicdataBoutputstrain`

- The basic data output strain.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBasicdataBoutputstress`

- The basic data output stress.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBasicdataIanalysisopt`

- The basic data analysis option.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBasicdataBcalPressEffects`

- The basic data caculation press effects.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dBasicdataFunitem`

- The basic data unit temperature.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dBasicdataFreftemp`

- The basic data reference temperature.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dBasicdataFendloadtime`

- The basic data end load time.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBasicdataItimestep`

- The basic data time step.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBasicdataIstepchosen`

- The basic data step chosen.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBasicdataIsubstepnum`

- The basic data sub step number.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBasicdataImaxsubstep`

- The basic data maximum sub step.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBasicdataIminstepnum`

- The basic data minimum sub step.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dBasicdataFtimestepsize`

- The basic data time step size.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dBasicdataFmintimestep`

- The basic data minimum sub step.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dBasicdataFmaxtimestep`

- The basic data maximum sub step.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iBasicdataIwritereslutfre`

- The basic data write result frequency.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iBasicdataIn`

- The basic data in.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bRunAPDL`

- The run Ansys APDL.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bWriteResultDB`

- The write result d .

<!-- @since:5.1.0 @type:Double @optional @default:DFLT _DBL -->
### `dFEndFreq`

- The end frequence.

<!-- @since:5.1.0 @type:Double @optional @default:DFLT _DBL -->
### `dFStartFreq`

- The start frequence.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iFulltransdataIsolutionoption`

- The full translation data solution option.

<!-- @since:5.1.0 @type:Double @optional @default:0.05 -->
### `dFulltransdataFpropchange`

- The full translation data property change.

<!-- @since:5.1.0 @type:Integer @optional @default:64 -->
### `iFulltransdataIpointnum`

- The full translation data point number.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dFulltransdataFmintemp`

- The full translation data minimum temperature.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dFulltransdataFmaxtemp`

- The full translation data maximum temperature.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iFulltransdataIequationsolv`

- The full translation data equation solve.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dFulltransdataFtollevel`

- The full translation data tolerance level.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dFulltransdataFmultiplier`

- The full translation data multiplier.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFulltransdataBsignleprecision`

- The full translation data single precision.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFulltransdataBmemorysave`

- The full translation data memory save.

<!-- @since:5.1.0 @type:Double @optional @default:1.1 -->
### `dFulltransdataFtempdiff`

- The full translation data temperature difference.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dHarmonicdataFstartfreq`

- The harmonic data start frequence.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dHarmonicdataFendfreq`

- The harmonic data end frequence.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iHarmonicdataNsubsteps`

- The harmonic data sub steps.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dHarmonicdataFalphad`

- The harmonic data alpha.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dHarmonicdataFbetad`

- The harmonic data beta.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dHarmonicdataFdmprat`

- The harmonic data DMP ratio.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bHarmonicdataBoutputdisplacements`

- The harmonic data output displacements.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bHarmonicdataBoutputstrain`

- The harmonic data output strain.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bHarmonicdataBoutputstress`

- The harmonic data output stress.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLCId`

- The LC ID.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iModeShape`

- The mode shape.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iModaldataImodemethod`

- The modal data mode method.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iModaldataIextractnum`

- The modal data extract number.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bModaldataBexpandshape`

- The modal data expand shape.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iModaldataIexpandnum`

- The modal data expand number.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bModaldataBuseapprox`

- The modal data use approximately.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bModaldataBinclprsseff`

- The modal data include prsseff.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bModaldataBmemorysave`

- The modal data memory save.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bModaldataBrsvec`

- The modal data resource vector.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bModaldataBoutputdisplacements`

- The modal data output displacements.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bModaldataBoutputstrain`

- The modal data output strain.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bModaldataBoutputstress`

- The modal data output stress.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iReduceddataIprintnum`

- The reduceddata print number.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSsdataBmemorysave`

- The ssdata memory save.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSsdataBoutputheatflux`

- The ssdata output heat flux.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSsdataBoutputtemperature`

- The ssdata output temperature.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bSsdataBpivotscheck`

- The ssdata pivots check.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSsdataBsignleprecision`

- The ssdata single precision.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dSsdataFmultiplier`

- The ssdata multiplier.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dSsdataFtempdiff`

- The ssdata temperature difference.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dSsdataFtollevel`

- The ssdata tolerance level.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSsdataIadaptivedes`

- The ssdata adaptive destination.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSsdataIequationsolv`

- The ssdata equation solve.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSsdataInpoption`

- The ssdata inpoption.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strAnsysVersion`

- The ansys version.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strCommandLineOption`

- The command line option.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bOutputSOLVE`

- The output solve.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSubspacedataIrigidmode`

- The subspace data rigid mode.

<!-- @since:5.1.0 @type:Integer @optional @default:8 -->
### `iSubspacedataIworksize`

- The subspace data work size.

<!-- @since:5.1.0 @type:Integer @optional @default:4 -->
### `iSubspacedataInpadnum`

- The subspace data inpad number.

<!-- @since:5.1.0 @type:Integer @optional @default:5 -->
### `iSubspacedataIblocknum`

- The subspace data block number.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSubspacedataImaxiteratcnt`

- The subspace data maximum iterator number.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSubspacedataIminnshift`

- The subspace data iminnshift.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSubspacedataIseqcheck`

- The subspace data iseqcheck.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bTransientdataBtraneffect`

- The transient data effection.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTransientdataIloadingtype`

- The transient data loading type.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dTransientdataFmassmatrixmult`

- The transient data mass matrix multiple.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dTransientdataFstiffmatrixmult`

- The transient data stiff matrix multiple.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bTransientdataBmidstep`

- The transient data midle step.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dTransientdataFtolerancebisection`

- The transient data tolerance binary section.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dTransientdataFtolerancetimestep`

- The transient data tolerance time step.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTransientdataItimeinteralgor`

- The transient data time inter algorithm.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTransientdataItimeinter`

- The transient data time inter.

<!-- @since:5.1.0 @type:Double @optional @default:0.005 -->
### `dTransientdataFgamma`

- The transient data gamma.

<!-- @since:5.1.0 @type:Double @optional @default:0.25250625 -->
### `dTransientdataFalpha`

- The transient data alpha.

<!-- @since:5.1.0 @type:Double @optional @default:0.505 -->
### `dTransientdataFdelta`

- The transient data delta.

<!-- @since:5.1.0 @type:Double @optional @default:0.005 -->
### `dTransientdataFalphaf`

- The transient data alpha f.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dTransientdataFalpham`

- The transient data alpha m.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bTransientdataBoutputtemperature`

- The transient data output temperature.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bTransientdataBoutputheatflux`

- The transient data output heat flux.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.Ansys.HeatTransferSteady(strName="", iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT _DBL, dFStartFreq=DFLT _DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None)
```
