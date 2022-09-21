import j1

j1_client = j1.J1Client(
        account='j1dev',
        access_token='123token'
        )

entity = j1_client.entity()
new_entity = entity.create(entity_key='123',
                           entity_type='example_entity',
                           entity_class='example_class')

