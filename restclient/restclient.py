import inspect
import uuid
import requests
import structlog
from restclient import transform


class RestClient:

    def __init__(self, host: str, headers: dict = None, proxies: dict = None):
        """
        Create RestClient instance
        Parameters
        ----------
        host : str
            part of url
            url = host + path
        headers: dict or None
            save default headers for all requests. If None than {'Content-Type': 'application/json'}
        proxies: dict or None
            save default proxies for all requests
        Returns
        -------
        out : RestClient
            rest client instance
        Raises
        ------
        AttributeError
            when `host` is empty
        Examples
        --------
        api = RestClient('http://httpbin.org')
        """
        if not host:
            raise AttributeError('Attribute host should not be empty.')
        self.host = host
        self.headers = headers
        self.proxies = proxies
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='api')
        self.session = requests.session()

    def bind_key_value_to_log(self, key: str, value):
        """
        Bind to logs some key and value
        Parameters
        ----------
        key: str
            key for logs
        value:
            value for logs
        Returns
        -------
        out : RestClient
            rest client instance with bound key value
        """
        self.log = self.log.bind(**{key: value})
        return self

    def get(self, path: str, params=None, **kwargs):
        """
        Send GET request
        Parameters
        ----------
        path : str
            part of url
            url = host + path
        params : object or None
            request parameters
        headers: dict or None
             key-value headers that will be added to request. Default {'Content-Type': 'application/json'}
        Returns
        -------
        out : requests.Response
            response object
        Examples
        --------
        response = httpbin.get('get')
        """
        return self._send_request(
            'GET', path,
            params=transform.request_to_json(params),
            **kwargs
        )

    def post(self, path: str, json=None, **kwargs):
        """
        Send POST request
        Parameters
        ----------
        path : str
            part of url
            url = host + path
        json : object or None
            request parameters as json object
        data : object or None
            request data
        files : object or None
            some files
        headers: dict or None
             key-value headers that will be added to request. Default {'Content-Type': 'application/json'}
        Returns
        -------
        out : requests.Response
            response object
        Examples
        --------
        response = httpbin.post('post', {'key': 'value'})
        """
        return self._send_request(
            'POST', path,
            json=transform.request_to_json(json),
            **kwargs
        )

    def put(self, path: str, json=None, **kwargs):
        """
        Send PUT request
        Parameters
        ----------
        path : str
            part of url
            url = host + path
        json : object or None
            request parameters as json object
        data : object or None
            request data
        files : object or None
            some files
        headers: dict or None
             key-value headers that will be added to request. Default {'Content-Type': 'application/json'}
        Returns
        -------
        out : requests.Response
            response object
        Examples
        --------
        response = httpbin.put('put', {'key': 'value'})
        """
        return self._send_request(
            'PUT', path,
            json=transform.request_to_json(json),
            **kwargs
        )

    def patch(self, path: str, json=None, **kwargs):
        """
        Send PATCH request
        Parameters
        ----------
        path : str
            part of url
            url = host + path
        json : object or None
            request parameters as json object
        data : object or None
            request data
        files : object or None
            some files
        headers: dict or None
             key-value headers that will be added to request. Default {'Content-Type': 'application/json'}
        Returns
        -------
        out : requests.Response
            response object
        Examples
        --------
        response = httpbin.put('put', {'key': 'value'})
        """
        return self._send_request(
            'PATCH', path,
            json=transform.request_to_json(json),
            **kwargs
        )

    def delete(self, path: str, params=None, **kwargs):
        """
        Send DELETE request
        Parameters
        ----------
        path : str
            part of url
            url = host + path
        params : object or None
            request parameters
        headers: dict or None
             key-value headers that will be added to request. Default {'Content-Type': 'application/json'}
        Returns
        -------
        out : requests.Response
            response object
        Examples
        --------
        response = httpbin.delete('delete')
        """
        return self._send_request(
            'DELETE', path,
            params=transform.request_to_json(params),
            **kwargs
        )

    def options(self, path: str, **kwargs):
        """
        Send OPTIONS request
        Parameters
        ----------
        path : str
            part of url
            url = host + path
        headers: dict or None
             key-value headers that will be added to request. Default {'Content-Type': 'application/json'}
        Returns
        -------
        out : requests.Response
            response object
        Examples
        --------
        response = httpbin.options('get')
        """
        return self._send_request(
            'OPTIONS', path,
            **kwargs
        )

    def _send_request(self, method: str, path: str, **kwargs):
        url = f'{self.host}{path}'
        log = self.log.bind(request_id=str(uuid.uuid4()))
        log.msg(
            'request',
            caller=inspect.stack()[2][3],
            method=method,
            url=url,
            json=kwargs.get('json', None),
            params=kwargs.get('params', None),
            data=kwargs.get('data', None),
            headers=kwargs.get('headers', self.headers),
            proxies=kwargs.pop('proxies', self.proxies),
        )
        response = self.session.request(
            method=method,
            url=url,
            headers=kwargs.pop('headers', self.headers),
            proxies=kwargs.pop('proxies', self.proxies),
            **kwargs
        )
        log.msg(
            'response',
            status_code=response.status_code,
            json=transform.response_to_json(response),
            text=response.text,
            headers=response.headers,
            elapsed=(response.elapsed.microseconds / 1000),
            curl=transform.request_to_curl(response.request),
        )
        return response