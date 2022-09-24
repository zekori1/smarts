import requests


def _model_to_json(obj):
    """
    This method is used when describing request. It's possible to use json or Model transforming request object into json.
    Parameters
    ----------
    obj : json or Model
        Object that represents request data
    Returns
    -------
    out : json
        Json for request data
    """
    if hasattr(obj, 'json'):
        return obj.json()
    return obj


def request_to_json(obj):
    """
    This method is used when describing request. It's possible to use json or Model transforming request object into json.
    Parameters
    ----------
    obj : list(json) or list(Model) or json or Model
        Object that represents request data
    Returns
    -------
    out : list(json) or json
        List(json) for request data if obj list(json) or list(Model).
        Json for request data if obj is json or Model.
    """
    if isinstance(obj, list):
        return [_model_to_json(x) for x in obj]
    return _model_to_json(obj)


def response_to_json(response: requests.Response):
    """
    This method is used for logging requests.Response. It transforms the response object into json.
    Parameters
    ----------
    response : requests.Response
        Response object
    Returns
    -------
    out : json or None
        Json if response can be transformed to json.
        None if response cannot be transformed to json.
    """
    try:
        return response.json()
    except ValueError:
        return None


def request_to_curl(request, compressed=False):
    """
    Returns string with curl command by provided request object
    Parameters
    ----------
    compressed : bool
        If `True` then `--compressed` argument will be added to result
    """
    parts = [
        ('curl', None),
        ('-X', request.method),
    ]

    for k, v in sorted(request.headers.items()):
        parts += [('-H', '{0}: {1}'.format(k, v))]

    if request.body:
        # if body is bytes string, it should be decoded
        # if body is not decodable, first 1000 symbols should be used in curl
        if isinstance(request.body, bytes):
            try:
                parts += [('-d', request.body.decode())]
            except UnicodeDecodeError:
                parts += [('-d', str(request.body)[0:1000] + '...')]
        else:
            parts += [('-d', request.body)]

    if compressed:
        parts += [('--compressed', None)]

    parts += [(None, request.url)]

    flat_parts = []
    for k, v in parts:
        if k:
            flat_parts.append(k)
        if v:
            flat_parts.append("'{0}'".format(v))

    curl = ' '.join(flat_parts)
    print(curl)
    return curl