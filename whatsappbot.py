from twilio.rest import Client 
 
account_sid = '#########################' #REDACTED FOR SECURITY
auth_token = '######################'  #REDACTED FOR SECURITY
client = Client(account_sid, auth_token) 

def checkup_patient():
    message = client.messages.create( 
                                from_='whatsapp:+##########',  #REDACTED FOR SECURITY
                                body='How are you feeling now?',      
                                to='whatsapp:+##########' #REDACTED FOR SECURITY
                            ) 
    
    print(message.sid)