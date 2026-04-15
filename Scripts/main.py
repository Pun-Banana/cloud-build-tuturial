import functions_framework

@functions_framework.http
def message(request):
    path = request.path

    if path == '/message':
        return "Hello! This is message test version 3!\n\n", 200
    else:
        return f"Error: The path {path} is invalid.", 404