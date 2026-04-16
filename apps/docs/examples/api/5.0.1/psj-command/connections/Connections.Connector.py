# Title:   Connections.Connector()
# Desc:    Create connectors between nodes, edges, and faces according to specified connection types. User selects master/slave targets and the connectors will be created to connect nodes on master/slave targets with each other
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Connector
# ---
Geometry.Part.Cube()

created_contact = Connections.Connector(strName="Connector_1",   # [hl]
                                        iMethod=3,   # [hl]
                                        crlElasticity=[Unknown(0,   # [hl]
                                                               0,   # [hl]
                                                               0,   # [hl]
                                                               0,  # [hl]
                                                               0,   # [hl]
                                                               0)],   # [hl]
                                        crlDamp=[Unknown(0,   # [hl]
                                                         0,   # [hl]
                                                         0,   # [hl]
                                                         0,   # [hl]
                                                         0,   # [hl]
                                                         0)],   # [hl]
                                        crlMasterTargets=[Face(22)],   # [hl]
                                        crlSlaveTargets=[Face(21)])  # [hl]

JPT.Debugger(created_contact)
