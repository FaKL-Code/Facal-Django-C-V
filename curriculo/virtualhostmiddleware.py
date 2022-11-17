virtual_hosts = {
    "www.facal.dev": "curriculo.urls",
}


class VirtualHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        request.urlconf = virtual_hosts.get(host)
        response = self.get_response(request)
        return response
