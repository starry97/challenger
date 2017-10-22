import httplib, urllib, base64, json, boto3


def emotionAPI(url):
    body = "{ 'url': '%s' }" % url
    print(body)
    try:
        # API call to emotion API
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        parsed = json.loads(data)
        print(len(parsed))
        print(json.dumps(parsed, indent=4, sort_keys=True))
        conn.close()
        return response
    except Exception as e:
        print(e)


if __name__ == '__main__':
    headers = {
        # Request headers. subscription key below is for MS Azure.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '13ecc9b40ce34bc89d937d131391d44e',
    }

    params = urllib.urlencode({
    })

    client = boto3.client(
        's3',
        aws_access_key_id='AKIAJFOVQUF3EYLXWPHA',
        aws_secret_access_key='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'
    )

    resource = boto3.resource(
        's3',
        aws_access_key_id='AKIAJFOVQUF3EYLXWPHA',
        aws_secret_access_key='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'
    )

    response = client.list_buckets()

    buckets = [bucket['Name'] for bucket in response['Buckets']]

    print("Bucket List: %s" % buckets)

    bucket = resource.Bucket('dubhacks17')

    username = 'temp-user'

    for key in bucket.objects.filter(Prefix=username):
        print('https://s3-us-west-2.amazonaws.com/dubhacks17/' + key.key)

    response = emotionAPI('https://s3-us-west-2.amazonaws.com/dubhacks17/temp-user/bla.jpg')
