# Title:   Connections.Connector()
# Desc:    Create connectors between nodes, edges, and faces according to specified connection types. User selects master/slave targets and the connectors will be created to connect nodes on master/slave targets with each other
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Connector
# ---
Geometry.Part.Cube()

created_contact = Connections.Connector(strName="Connector_1",   # [hl:start]
                                        iMethod=3, 
                                        crlElasticity=[Unknown(0, 
                                                               0, 
                                                               0, 
                                                               0,
                                                               0, 
                                                               0)], 
                                        crlDamp=[Unknown(0, 
                                                         0, 
                                                         0, 
                                                         0, 
                                                         0, 
                                                         0)], 
                                        crlMasterTargets=[Face(22)], 
                                        crlSlaveTargets=[Face(21)])  # [hl:end]

JPT.Debugger(created_contact)
