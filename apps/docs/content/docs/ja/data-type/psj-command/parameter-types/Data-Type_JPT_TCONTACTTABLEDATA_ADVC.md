---
title: TCONTACTTABLEDATA_ADVC
id: TCONTACTTABLEDATA_ADVC
---

## Description

A data type uses to control parameters of ADVC Contact Table data.

## Attributes

### `strMaster`

- A _String_ specifying master group's name.
- This is a required input.

### `strSlave`

- A _String_ specifying slave group's name.
- This is a required input.

### `listFacesMaster`

- A _List of Cursor_ specifying master faces.
- This is a required input.

### `listFacesSlave`

- A _List of Cursor_ specifying slave faces.
- This is a required input.

### `iContactType`

- An _Integer_ specifying constraint type.
- The default value is 1.

### `stAdvcParam`

- A _DCAD_ADVCCONTACTPARAM_[./DCAD_ADVCCONTACTPARAM] specifying contact parameters

### `iColor`

- An _Integer_ specifying color of contact.
- The default value is 65280.
