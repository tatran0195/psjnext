---
title: DEdge
id: DEdge
---

## Description

This is an instance of a DEdge class, represents an Edge inside Jupiter.

## Properties

| Attribute      | Description                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| typeID         | Type ID of the Edge (ID = 5).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                 |
| id             | External ID of the Edge.<br />ID can be duplicated, but not recommended.<br />ID can be changed using the renumbering function.<br />The return value is ID (int). |
| nodes          | The nodes belong to the Edge.<br />The return value is a list of nodes.                                                                                            |
| color\* [^(1)] | Edge color information.<br />This value can be adjusted.<br />The return value is a RGB color.                                                                     |

### Notice

[^(1)]: An asterisk symbol \* in attribute name means that attribute can be changed/assigned from the current to the new value.
