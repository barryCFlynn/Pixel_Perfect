from django.shortcuts import render


def handler404(request, exception):
    """
    Custom error handler for HTTP 404 - Page Not Found.

    This function renders a custom error page (errors/404.html) with a
    status code of 404 when a page is not found.

    Parameters:
    - request: The HTTP request object.
    - exception: The exception instance raised for the 404 error.

    Returns:
    - HttpResponse: Rendered HTTP response with the custom error page.
    """
    return render(request, "errors/404.html", status=404)
