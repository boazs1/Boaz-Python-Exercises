from zenpy import Zenpy
# Create a Zenpy instance
credentials = {
    'email' : 'boaz.s@pepperi.com',
    'password' : 'Bs123456!',
    'subdomain': 'pepperi'
}
zenpy_client = Zenpy(**credentials)

# Create a new ticket
#ticket = zenpy_client.tickets(id=ticket_id[98515])
Ticket = zenpy_client.tickets(id=98515)
zenpy_client.tickets.create(Ticket(subject="Important", description="Thing"))

# Perform a simple search
for Ticket in zenpy_client.search('PC LOAD LETTER', type='Ticket', assignee='facetoe'):
    # No need to mess around with ids, linked objects can be accessed directly.
    print(Ticket.requester.name)

    # All objects can be converted to a Python dict.
    print(Ticket.to_dict())

    # Or to JSON.
    print(Ticket.to_json())