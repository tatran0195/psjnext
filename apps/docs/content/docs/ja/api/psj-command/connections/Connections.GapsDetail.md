---
title: "Connections.GapsDetail()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > GapsDetail"
macro _link: "[ConnectGap](../../macro/connections/ConnectGap)"
---

## Description

Unknown Description

## Syntax

```psj
Connections.GapsDetail(crlMaster=[], crlSlave=[], iMethod=0, iOriMode=0, crCoord=None, strName="", dU0=DFLT _DBL, dF0=DFLT _DBL, dKa=DFLT _DBL, dKb=DFLT _DBL, dKt=DFLT _DBL, dMar=DFLT _DBL, dMu1=DFLT _DBL, dMu2=DFLT _DBL, dlOriVec=[], dTmax=DFLT _DBL, dTol=DFLT _DBL, dTrmin=DFLT _DBL, crEditCur=None)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlMaster

- Specify the master.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlave

- Specify the slave.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iOriMode

- Specify the ori mode.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### dU0

- Specify the u0.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dF0

- Specify the f0.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dKa

- Specify the ka.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dKb

- Specify the kb.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dKt

- Specify the kt.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMar

- Specify the mar.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMu1

- Specify the mu1.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMu2

- Specify the mu2.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dlOriVec

- Specify the ori vector.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dTmax

- Specify the tmax.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTrmin

- Specify the trmin.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crEditCur

- Specify the edit cur.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.GapsDetail(crlMaster=[], crlSlave=[], iMethod=0, iOriMode=0, crCoord=None, strName="", dU0=DFLT _DBL, dF0=DFLT _DBL, dKa=DFLT _DBL, dKb=DFLT _DBL, dKt=DFLT _DBL, dMar=DFLT _DBL, dMu1=DFLT _DBL, dMu2=DFLT _DBL, dlOriVec=[], dTmax=DFLT _DBL, dTol=DFLT _DBL, dTrmin=DFLT _DBL, crEditCur=None)
```
