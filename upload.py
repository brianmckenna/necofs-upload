import boto
import boto.s3
from boto.s3.bucket import Bucket
from boto.s3.key import Key
import sys

BUCKET_NAME = 'necofs'

# Instantiate a new client for Amazon Simple Storage Service (S3). With no
# parameters or configuration, the AWS SDK for Python (Boto) will look for
# access keys in these environment variables:
#
#    AWS_ACCESS_KEY_ID='...'
#    AWS_SECRET_ACCESS_KEY='...'
# 

connection = boto.connect_s3()
bucket = Bucket(connection, BUCKET_NAME)

def upload(filename):
    print 'uploading %s to Amazon S3 bucket %s' % (filename, BUCKET_NAME)
    def percent_callback(complete, total):
        sys.stdout.write('.')
        sys.stdout.flush()
    k = Key(bucket)
    k.key = 'input/%s' % filename
    k.set_contents_from_filename(filename, cb=percent_callback, num_cb=10)
 
for filename in sys.argv[1:]:
    upload(filename)
