"""
# Access S3 Buckets On AWS

In this guide, we learn how to access data on AWS S3 Buckets from Union Serverless. As a
prerequisite, we assume that our AWS S3 bucket is accessible with API keys:
`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
"""


# %%
# ## Creating Secrets on Union Serverless
#
# First, we create secrets on Union by running the following command:
#
# ``` bash
# unionai create secret AWS_ACCESS_KEY_ID
# ```
#
# This will open a prompt where we paste in our AWS credentials:
#
# ```
# Enter secret value: 🗝️
# ```
#
# Repeat this process for all other AWS credentials, such as `AWS_SECRET_ACCESS_KEY`.

# %%
# ## Using Secret in a Flyte Task
#
# Next, we can use the secrets directly in a task! With [AWS CLI](https://aws.amazon.com/cli/),
# we create a small text file and move it to a AWS bucket
#
# ```bash
# aws s3 mb s3://test_bucket
# echo "Hello Union" > my_file.txt
# aws s3 cp my_file.txt s3://test_bucket/my_file.txt
# ```
# Next, we give a task access to our AWS secrets by supplying them through
# `secret_requests`. Within the task, secrets are available through
# `current_context().secrets`:
from flytekit import task, current_context, Secret, workflow


@task(
    secret_requests=[
        Secret(key="AWS_ACCESS_KEY_ID"),
        Secret(key="AWS_SECRET_ACCESS_KEY"),
    ],
)
def read_s3_data() -> str:
    import s3fs

    secrets = current_context().secrets

    s3 = s3fs.S3FileSystem(
        secret=secrets.get("AWS_SECRET_ACCESS_KEY"),
        key=secrets.get("AWS_ACCESS_KEY_ID"),
    )

    with s3.open("test_bucket/my_file.txt") as f:
        content = f.read().decode("utf-8")

    return content


@workflow
def main():
    read_s3_data()


# %%
# ## Conclusion
#
# You can easily access your AWS S3 buckets by running `union create secret` and configuring
# your tasks to access the secrets! If you want to run this example, download the file below
# and run:
#
# ```bash
# unionai run --remote aws-s3-access.py main
# ```
