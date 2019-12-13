from flask import jsonify

HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600'
}


class _HttpWrapper:
    def __init__(self, request):
        self.request = request

    def send_response(self, result):
        if self.request.method == 'OPTIONS':
            return ('', 204, HEADERS)
        return (jsonify(result[0]), result[1], HEADERS)


def gcf(func):
    def wrapper(*args):
        try:
            result = func(args[0])
        except Exception as error:
            return ({'error': str(error)}, 500, HEADERS)
        return _HttpWrapper(args[0]).send_response(result)

    return wrapper
