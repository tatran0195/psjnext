---
title: DElem
id: DElem
---

## Description

This is an instance of a DElem class, represents an Element inside Jupiter.

## Properties

| Attribute      | Description                                                                                                                                                           |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| typeID         | Type ID of the Element (ID = 11).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                |
| id             | External ID of the Element.<br />ID can be duplicated, but not recommended.<br />ID can be changed using the renumbering function.<br />The return value is ID (int). |
| type           | Type of the Element.<br />The return value is [`ElemType`](../../../psj-command/element-types).                                                                       |
| kind           | Kind of the Element.<br />The return value is [`ElemKind`](../../../psj-command/element-types).                                                                       |
| nodes          | The nodes belong to the Element.<br />The return value is a list of nodes.                                                                                            |
| color\* [^(1)] | Element color information.<br />This value can be adjusted.<br />The return value is a RGB color.                                                                     |

### Notice

[^(1)]: An asterisk symbol \* in attribute name means that attribute can be changed/assigned from the current to the new value.
