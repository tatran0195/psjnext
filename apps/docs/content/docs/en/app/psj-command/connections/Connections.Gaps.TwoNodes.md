---
title: "Connections.Gaps.TwoNodes()"
description: "create gap connection"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Gaps > TwoNodes"
---

## Description

Create gap connection

## Syntax

```psj
Connections.Gaps.TwoNodes(crlMaster=[], crlSlave=[], iMethod=1, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None)
```

## Inputs

### `crlMaster` @type(List\[Cursor]) @default(\[])

- The master.

### `crlSlave` @type(List\[Cursor]) @default(\[])

- The slave.

### `iMethod` @type(Integer) @default(1)

- The method.

### `iOriMode` @type(Integer) @default(0)

- The ori mode.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `strName` @type(String) @default("")

- The name.

### `dU0` @type(Double) @default(DFLT\_DBL)

- The u0.

### `dF0` @type(Double) @default(DFLT\_DBL)

- The f0.

### `dKa` @type(Double) @default(DFLT\_DBL)

- The ka.

### `dKb` @type(Double) @default(DFLT\_DBL)

- The kb.

### `dKt` @type(Double) @default(DFLT\_DBL)

- The kt.

### `dMar` @type(Double) @default(DFLT\_DBL)

- The mar.

### `dMu1` @type(Double) @default(DFLT\_DBL)

- The mu1.

### `dMu2` @type(Double) @default(DFLT\_DBL)

- The mu2.

### `dlOriVec` @type(Double List) @default(\[])

- The ori vector.

### `dTmax` @type(Double) @default(DFLT\_DBL)

- The tmax.

### `dTol` @type(Double) @default(DFLT\_DBL)

- The tolerance.

### `dTrmin` @type(Double) @default(DFLT\_DBL)

- The trmin.

### `crEditCur` @type(Cursor) @default(None)

- The edit cur.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Gaps.TwoNodes(crlMaster=[], crlSlave=[], iMethod=1, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None)
```
