---
title: "Connections.Contacts.Ansys.ContactTable()"
description: "create contact ansys Contact Table"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Ansys > ContactTable"
---

## Description

Create contact ansys Contact Table

## Syntax

```psj
Connections.Contacts.Ansys.ContactTable(strName="ContactAnsys _1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS _CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "ContactAnsys\_1".

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactAlgorithm

- Specify the contact algorithm.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ansysContact

- Specify the contact.
- The default value is ANSYS\_CONTACT().

<!-- @since:5.0.1 @optional -->
### crplTarget

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the color.
- The default value is 16711680.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.Ansys.ContactTable(strName="ContactAnsys _1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS _CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)
```
