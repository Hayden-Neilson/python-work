# #def a function
# # create a while that goes through info and take out the key
# #You have been given a raw data dump that has an array of objects. The objects keys are companies, and the values are arrays of emails followed by a 3 digit department number. I need you to write a program that will go through the data, print the emails for each company and what department number that email belongs to.
# """

# data = [
# { "Google": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 123" ]},
# { "Yahoo": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 451" ]},
# { "IBM": ["test@test.com 888", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
# { "GREGS": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
# { "AUTO SHOP": ["test@test.com 888", "test@test.com 555", "test@test.com 555", "test@test.com 123" ]},
# { "PAWN SHOP": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
# { "Nike": ["test@test.com 123", "test@test.com 123", "test@test.com 555", "test@test.com 123" ]},
# { "Franks": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]},
# { "Tims": ["test@test.com 123", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
# { "Apple": ["test@test.com 123", "test@test.com 555", "test@test.com 123", "test@test.com 123" ]},
# { "Sony": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
# { "Disney": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
# { "Popies": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
# { "Sally": ["test@test.com 123", "test@test.com 555", "test@test.com 888", "test@test.com 123" ]},
# { "Henry": ["test@test.com 123", "test@test.com 555", "test@test.com 555", "test@test.com 555" ]},
# { "Dave's": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]}
# ]
# """


# mymap = [{ 
#     name: "Google", 
#     id: "test@test.com 123"
# }, {
#     { 
#     name: "Yahoo", 
#     id: "test@test.com 451"
# }, {
# { 
#     name: "IBM", 
#     id: "test@test.com 888"
# }, {

# { 
#     name: "GREGS", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "AUTO SHOP", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "PAWN SHOP", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "NIKE", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "FRANKS", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "TIMS", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "APPLE", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "SONY", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "DISNEY", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "POPIES", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "SALLY", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "HENRY", 
#     id: "test@test.com 123"
# }, {
# { 
#     name: "Daves", 
#     id: "test@test.com 123"
# }, {






# let mymap = new Map(); 

# unique = objects.filter(el => { 
#     const val = mymap.get(el.name); 
#     if(name) { 
#         if(el.id < name) { 
#             mymap.delete(el.name); 
#             mymap.set(el.name, el.id); 
#             return true; 
#         } else { 
#             return false; 
#         } 
#     } 
#     mymap.set(el.name, el.id); 
#     return true; 
# });

# print(unique)
  
 
 def funkyfunc (data)

   for dictionary in data
     company_name = list(dictionary.keys()[0])
     values = list(dictionary.values())[0]) 
     print(f'company: {'company_name'}
     for emails in values:
       print(emails =emails.split())
       print(f'email: {emails[0]}  department number: {email[1]}')
       print('')
    
    funkyfunc(data)