from j1 import J1Client

j1 = J1Client(
    environment='dev',
    account='j1dev',
    access_token='')

properties = {
    'myProperty': 'myValue',
    'tag.myTagProperty': 'value_will_be_a_tag'
}

entity = j1.entity.create(
   entity_key='my-unique-key',
   entity_type='my_type',
   entity_class='MyClass',
   properties=properties,
#    timestamp=int(time.time()) * 1000 # Optional, defaults to current datetime
)

print(entity['entity']['_id'])
id = entity['entity']['_id']
# print(id)

# j1.delete_entity(entity_id=id)

# print("WORKED?")