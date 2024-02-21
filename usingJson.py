import json
data = '{"firstName": "deniz","lastName": "güngördü"}'
y = json.loads(data)
print(y["lastName"])


customer = {
          "firstName":"ırmak",
          "lastName":"güngördü"
         }
customerjson = json.dumps(customer)
print(customer)