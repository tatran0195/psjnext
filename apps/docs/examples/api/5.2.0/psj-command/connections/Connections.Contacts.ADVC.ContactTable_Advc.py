# Title:   Connections.Contacts.ADVC.ContactTable_Advc()
# Desc:    Create contacts for ADVC solver by using table
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.ADVC.ContactTable_Advc
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], 
                   strName="Cube_3", 
                   iPartColor=6417130)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube_4", 
                   iPartColor=6053060)

# Find Contact
contacts_found = Connections.Contacts.ADVC.FindContactPairs(crlParts=[Part(1, 2, 3, 4)])
for contact in contacts_found:
    contact.iContactType = 0 # General

# Create Contact
Connections.Contacts.ADVC.ContactTable_Advc(taContactFound_ADVC = contacts_found)  # [hl]
