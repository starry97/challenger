import httplib, urllib, base64, json, boto3

ACCESS_KEY = 'AKIAJFOVQUF3EYLXWPHA'
SECRET_KEY = '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'
AZURE_KEY = '13ecc9b40ce34bc89d937d131391d44e'
S3_BUCKET_NAME = 'dubhacks17'


def emotion_api(url):
    """
    Calls emotion API once for the image located at the url passed in.
    :param url: the url for the image.
    :return: the response of the API call.
    """
    body = "{ 'url': '%s' }" % url
    print('starting API call now...')
    try:
        # API call to emotion API
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # JSON printing format
        parsed = json.loads(data)
        print('number of faces recognized in image: %d' % len(parsed))
        print(json.dumps(parsed, indent=4, sort_keys=True))

        conn.close()
        return data
    except Exception as e:
        print(e)


def compute_for_username(username):
    """
    Compute emotion scores for all the images in the folder for this user.
    :param username: the username for this user.
    :return a list of JSON responses for all the images in this user's folder.
    """
    bucket = resource.Bucket(S3_BUCKET_NAME)
    response = []
    for key in bucket.objects.filter(Prefix=username):
        url = 'https://s3-us-west-2.amazonaws.com/dubhacks17/' + key.key
        print(url)
        if url.endswith('/'):
            print('It is a folder, skipping it...')
        else:
            response.append(emotion_api(url))
    return response


if __name__ == '__main__':
    headers = {
        # Request headers. subscription key below is for MS Azure.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': AZURE_KEY,
    }

    params = urllib.urlencode({
    })

    client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )

    resource = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )

    print("Bucket List: %s" % [bucket['Name'] for bucket in client.list_buckets()['Buckets']])

    username = 'sunbw'

    result_list = compute_for_username(username)

    print(result_list)
