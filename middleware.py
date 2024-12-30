# myapp/middleware.py

class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request (optional)
        
        # Get the response
        response = self.get_response(request)
        
        # Add a custom header to the response
        response['X-Custom-Header'] = 'Powered by Django'
        
        return response
