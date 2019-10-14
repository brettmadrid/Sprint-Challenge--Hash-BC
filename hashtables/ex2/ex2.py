#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert tickets into hash table
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    # look for ticket with key = "NONE" which is the first ticket
    # store the value in current_ticket -> "PDX"
    current_ticket = hash_table_retrieve(hashtable, "NONE")

    while current_ticket is not "NONE": # to to the last ticket
        for i in range(len(route)): 
            route[i] = current_ticket # insert ticket into array

            # Now take the value of what was just stored and use it as a key
            # call retrieve again, passing this key in to get the next ticket in order
            current_ticket = hash_table_retrieve(hashtable, current_ticket)
            if current_ticket is "NONE": # if at last ticket
                route[i+1] = current_ticket # increment index and insert at end
                break

    return route
