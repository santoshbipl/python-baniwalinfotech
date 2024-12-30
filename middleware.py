# middleware.py

class AddProgrammingLanguageHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Add a custom header to identify the backend language
        response['X-Powered-By'] = 'Python/Django'
        return response
