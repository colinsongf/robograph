import requests
from datamodel.base import node


class HttpClient(node.Node):

    DEFAULT_TIMEOUT_SECS = 3

    def __init__(self, name=None):
        node.Node.__init__(self, name=name)

    def input(self, request_params):
        self._url = request_params.get('url', None)
        self._headers = request_params.get('headers', dict())
        self._auth = request_params.get('auth', tuple())
        self._output_encoding = request_params.get('output_encoding', 'json')
        self._verify_ssl = request_params.get('verify_ssl', True)
        self._timeout_secs = request_params.get('timeout_secs',
                                                self.DEFAULT_TIMEOUT_SECS)

    def _encode_payload(self, response):
        if self._output_encoding == 'json':
            return response.json()
        if self._output_encoding == 'binary':
            return response.content
        return response.text

    def output(self):
        pass

    def reset(self):
        del self._url
        del self._headers
        del self._auth
        del self._output_encoding
        del self._verify_ssl
        del self._timeout_secs


# GET

class RawGet(HttpClient):

    def input(self, request_params):
        self._query = request_params.get('query', dict())
        HttpClient.input(self, request_params)

    def output(self):
        r = requests.get(self._url, auth=self._auth, params=self._query,
                         headers=self._headers, timeout=self._timeout_secs,
                         verify=self._verify_ssl)
        payload = self._encode_payload(r)
        return r.status_code, payload, r

    def reset(self):
        del self._query
        HttpClient.reset(self)


class Get(RawGet):

    def output(self):
        status_code, payload, raw_response = RawGet.output(self)
        if status_code != requests.codes.ok:
            return None
        return payload


# POST

class RawPost(HttpClient):

    def input(self, request_params):
        self._post_data = request_params.get('post_data', None)
        self._files= request_params.get('files', None)
        HttpClient.input(self, request_params)

    def output(self):
        r = requests.post(self._url, auth=self._auth, data=self._post_data,
                          files=self._files, headers=self._headers,
                          timeout=self._timeout_secs, verify=self._verify_ssl)
        payload = self._encode_payload(r)
        return r.status_code, payload, r

    def reset(self):
        del self._post_data
        del self._files
        HttpClient.reset(self)


class Post(RawPost):

    def output(self):
        status_code, payload, raw_response = RawPost.output(self)
        if status_code != requests.codes.ok:
            return None
        return payload


# PUT

class RawPut(HttpClient):

    def input(self, request_params):
        self._put_data = request_params.get('put_data', None)
        HttpClient.input(self, request_params)

    def output(self):
        r = requests.put(self._url, auth=self._auth, data=self._put_data,
                         headers=self._headers, timeout=self._timeout_secs,
                         verify=self._verify_ssl)
        payload = self._encode_payload(r)
        return r.status_code, payload, r

    def reset(self):
        del self._put_data
        HttpClient.reset(self)


class Put(RawPut):

    def output(self):
        status_code, payload, raw_response = RawPut.output(self)
        if status_code != requests.codes.ok:
            return None
        return payload


# DELETE

class RawDelete(HttpClient):

    def output(self):
        r = requests.delete(self._url, auth=self._auth,
                            headers=self._headers, timeout=self._timeout_secs,
                            verify=self._verify_ssl)
        payload = self._encode_payload(r)
        return r.status_code, payload, r


class Delete(RawDelete):

    def output(self):
        status_code, payload, raw_response = RawDelete.output(self)
        if status_code != requests.codes.ok:
            return None
        return payload