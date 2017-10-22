import httplib, urllib, base64, json, boto3

headers = {
    # Request headers. subscription key below is for MS Azure.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '13ecc9b40ce34bc89d937d131391d44e',
}

params = urllib.urlencode({
})

# url is from AWS S3.
body = "{ 'url': 'https://s3-us-west-2.amazonaws.com/dubhacks17/5e19d9d9b51056b8180e34d04f94a74e_Top-Secrets-of-How-to-be-Happy-814-363-c.jpg' }"

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

objs = bucket.meta.client.list_objects(Bucket='dubhacks17')

for key in bucket.objects.all():
    print('https://s3-us-west-2.amazonaws.com/dubhacks17/' + key.key)

#
# try:
#     # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
#     #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
#     #   URL below with "westcentralus".
#     conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
#     conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
#     response = conn.getresponse()
#     data = response.read()
#     parsed = json.loads(data)
#     print(len(parsed))
#     print(json.dumps(parsed, indent=4, sort_keys=True))
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))
