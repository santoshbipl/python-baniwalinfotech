from django.middleware.common import CommonMiddleware
from django.http import HttpResponse

class GlobalMiddleware(CommonMiddleware):
    def process_response(self, request, response):
        # Example: Add a custom header
        #response['X-My-Custom-Header'] = 'Some Value'

        # Example: Modify response content (be cautious)
        #response.content = response.content.replace("work", "new_text") 

        return super().process_response(request, response)