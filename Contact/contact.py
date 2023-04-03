contactList={1:{'name':'Mush','contact':'07111111'}}
def contact(order):
    if order.lower() =='add':
       name=input('enter the name of the person: ').capitalize()
       number=input('Enter the number:')
       for i in contactList:
        if contactList[i]['contact'] !=number:
            contactList[len(contactList)+1]={'name':name, 'number':number}
            return name , number , 'is added to the contact list', '\n', contactList
        else: 
            return name, number, 'is already in the contact list'
            
    elif order.lower() =='delete':
        number=input('Enter the number the number you want to delete:')
        for i in contactList:
            if contactList[i]['contact'] ==number:
                contactList.pop(i)
                return  number , 'is deleted from the contact list', '\n', contactList
            else: 
                return number, 'does not exist in the contact list'
       
    elif order.lower() =='search':
        number=input('Enter the number the number you want to search:')
        for i in contactList:
            if contactList[i]['contact'] ==number:
               
                return  contactList[i] , 'is the contact you searched from the contact list', '\n', contactList
            else: 
                return number, 'does not exist in the contact list'





        return 'search'
    elif order.lower() =='print':
        return 'print'
    



print(contact(input('do you want to: add, delete, search or print: ')))