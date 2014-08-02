import epo_ops

anonymous_client = epo_ops.Client()  # Instantiate a default client
response = anonymous_client.published_data(  # Retrieve bibliography data
  reference_type = 'publication',  # publication, application, priority
  input = epo_ops.models.Docdb('1000000', 'EP', 'A1'),  # original, docdb, epodoc
  endpoint = 'biblio',  # optional, defaults to biblio in case of published_data
  constituents = []  # optional, list of constituents
)

registered_client = epo_ops.RegisteredClient(key='abc', secret='xyz')
registered_client.access_token  # To see the current token
response = registered_client.published_data()