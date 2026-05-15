---
title: "Connections.Contacts.MSCNastran.ContactGroupByMatrix()"
description: "create contacts of MSC Nastran Contact Group By Matrix"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > MSCNastran > ContactGroupByMatrix"
---

## Description

Create contacts of MSC Nastran Contact Group By Matrix

## Syntax

```psj
Connections.Contacts.MSCNastran.ContactGroupByMatrix(strName="", nastranContact=NASTRAN _CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### nastranContact

- Specify the contact.
- The default value is NASTRAN\_CONTACT().

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
- The default value is 65280.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.MSCNastran.ContactGroupByMatrix(strName="", nastranContact=NASTRAN _CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```
