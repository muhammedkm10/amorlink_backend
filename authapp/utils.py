import json,base64

def convertjwt(token):
    token_without_bearer = token.split(" ")[1]
    header_payload_signature = token_without_bearer.split(".")
    encoded_payload = header_payload_signature[1]
    decoded_payload = base64.urlsafe_b64decode(encoded_payload + "==").decode('utf-8')
    payload_dict = json.loads(decoded_payload)
    user_id = payload_dict.get('user_id') 
    email = payload_dict.get('email') 
    return user_id,email