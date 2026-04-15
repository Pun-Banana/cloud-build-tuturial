import functions_framework

@functions_framework.http
def message(request):
    return "Hello! This is message test version 3!\n\n"