from django.http import HttpRequest

class JwtCheckingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        # Define the list of URLs to exclude from JWT checking
        excluded_urls = ['/authapp/userlogin', '/authapp/usersignup','/authapp/api/token']
        if request.method == "POST" and request.path in excluded_urls:
            response = self.get_response(request)
            print("Skipping JWT check for", request.path)
            return response
        # other requests that does need the jwt access token
        else:
            response = self.get_response(request)
            auth_header = request.headers.get('Authorization')
            bearer_token = auth_header.split()
            if not auth_header or len(bearer_token)!= 2 or bearer_token[0].lower() != 'bearer':
                    request.custom_message = "Invalid Authorization header format."
                    return self.get_response(request)
            if auth_header:
                 return response
            



        

