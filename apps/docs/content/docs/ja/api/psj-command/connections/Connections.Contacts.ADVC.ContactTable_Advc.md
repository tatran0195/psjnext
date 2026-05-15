---
title: "Connections.Contacts.ADVC.ContactTable _Advc()"
description: "Create contacts for ADVC solver by using table"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Connections > Contacts > ADVC > ContactTable"
macro _link: "[ContactTable _Advc](../../macro/connections/ContactTable _Advc)"
---

## Description

Create contacts for ADVC solver by using table.

## Syntax

```psj
Connections.Contacts.ADVC.ContactTable _Advc(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### taContactFound\_ADVC

- Specify ADVC contact sets.
- The default value is \[].

### `taContactDeleted _ADVC`

- A list of _Cursor_ of groups to delete ADVC contacts.
- The default value is \[].

## Return Code

- A _Boolean_ specifying Succeeded or Failed.
  - True: Succeeded.
  - False: Failed.

## Sample Code

```psj {18}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], 
                   strName="Cube _3", 
                   iPartColor=6417130)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube _4", 
                   iPartColor=6053060)

# Find Contact
contacts _found = Connections.Contacts.ADVC.FindContactPairs(crlParts=[Part(1, 2, 3, 4)])
for contact in contacts _found:
    contact.iContactType = 0 # General

# Create Contact
Connections.Contacts.ADVC.ContactTable _Advc(taContactFound _ADVC = contacts _found)
```
