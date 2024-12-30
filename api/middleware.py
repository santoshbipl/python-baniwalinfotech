# your_project/middleware.py

class AddCustomHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # This is the next middleware or view handler

    def __call__(self, request):
        response = self.get_response(request)  # Get the response from the next middleware/view
        response['X-Powered-By'] = 'Django version 4.2 Python version 3.13'  # Add your custom header here
        return response
