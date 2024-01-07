# Generating Clickstream events data using Python
This project generates clickstream data and saves it to an AWS S3 bucket.

To run the Python script, you will need the following prerequisites:

* An EC2 instance running a Windows or Linux machine.
* An IAM role that has permissions to write data to the S3 bucket.
* An IAM policy that grants write access to the S3 bucket.

### Installation
To install the required packages, run:

```
pip install -r requirements.txt
```

### Usage
To generate clickstream data and save it to an S3 bucket, run:

```
python generate_clickstream_data.py <RECORDS> <MAX_SECONDS_BETWEEN_EVENTS>
```
where `<RECORDS>` is the number of records to generate and `<MAX_SECONDS_BETWEEN_EVENTS>` is the maximum number of seconds between events.

### S3 Bucket
The generated clickstream data is saved to an S3 bucket named `my-clickstream-bucket`.

### License
This project is licensed under the MIT License.
