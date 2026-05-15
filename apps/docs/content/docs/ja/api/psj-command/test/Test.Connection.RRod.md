---
title: "Test.Connection.RRod()"
description: "create RRod"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Test > Connection > RRod"
---

## Description

Create RRod

## Syntax

```psj
Test.Connection.RRod(rbarConnection=RBAR _CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTargets=[], crlSlaveTargets=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### rbarConnection

- Specify the connection.
- The default value is RBAR\_CONNECTION().

<!-- @since:5.0.1 @optional -->
### iUlDOFs

- Specify the ul d o fs.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.Connection.RRod(rbarConnection=RBAR _CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTargets=[], crlSlaveTargets=[])
```
