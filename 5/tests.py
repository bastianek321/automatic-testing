import requests

# https://alexwohlbruck.github.io/cat-facts/
def create_request():
    return requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1')
    

def status_code_test():
    req = create_request()
    if(req.status_code >= 200 and req.status_code < 300 ):
        print('Status code test PASSED with code:', req.status_code)
        return req
    else:
        print('Status code test FAILED')
        return

def request_is_not_empty_test():
    req = status_code_test()
    if(req):
        if(req.json()):
            print('Content test PASSED, content:', req.json())
            return req
        else:
            print('Content test FAILED, response body is empty')
            return
    else:
        print('Content test FAILED, request is invalid')
        return

def field_test():
    req = request_is_not_empty_test()
    if(req):
        # prosimy o type=cat
        if(req.json()['type'] == 'cat'):
            print('Field test PASSED, expected: cat \n received:', req.json()['type'])
        else:
            print('Field test FAILED, received type other than cat')
    else:
        print('Field test FAILED, reponse body is empty')

def response_keys_test():
    req = request_is_not_empty_test()
    expected_keys = ['status', 'type', 'deleted', '_id', 'used', 'source', 'user', 'text', 'createdAt', 'updatedAt', '__v']
    keys = 0
    if(req):
        for key in req.json():
            if(key in expected_keys):
                keys+=1
        # zakladam, ze test jest nieudany jezeli chociaz polowa kluczy nie zgadza sie z kluczami, ktore maja przyjsc
        if(keys <= 6):
            print('Response keys test FAILED, keys received are not keys that were expected')
        else:
            print('Response keys test PASSED, number of keys that were expected out of all expected keys:', keys, '/', len(expected_keys))
    else:
        print('Reponse keys test FAILED, reponse body is empty')

response_keys_test()