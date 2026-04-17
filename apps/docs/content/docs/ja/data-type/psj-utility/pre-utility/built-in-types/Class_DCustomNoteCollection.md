---
title: DCustomNoteCollection
id: DCustomNoteCollection
---

## Description

This is an instance of a CustomNoteCollection class, represents a custom note collections inside Jupiter.

## Properties

| Attribute | Description                                                                                                                                                                            |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| isValid   | For checking whether the indicated object is available or not. <br />The return value is bool.                                                                                         |
| typeID    | Type ID of the custom note collection(ID = 271).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                  |
| tableID   | Table ID of the custom note collection item (ID = 155). The return value is an [`Int notation of DTable Types`](../../../psj-utility/pre-utility/enumeration-types/dtable-types)(int). |
| id        | External ID of the custom note collection.<br />The return value is ID (int).                                                                                                          |
| name      | Name of the custom note collection.<br />The return value is a string.                                                                                                                 |
| notes     | The child custom notes under the custom note collection. The return value is [`CustomNoteVector`](./CustomNoteVector).                                                                 |
