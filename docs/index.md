# UnionAI Serverless Docs!

## Account Creation

To get started with Union serverless:

- Create an account on [github.com](github.com)
- Go to the serverless tenant on your browser: [https://serverless-gcp.cloud-staging.union.ai](https://serverless-gcp.cloud-staging.union.ai)
- Click Sign in with GitHub, and you should be taken to the Union serverless console.
- Now you're ready to start using Union serverless!

## Installation

1. Create a virtual environment with Python’s `venv` or `conda`:

    1. For `venv`, run:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

    2. For `conda`, run:

    ```bash
    conda create -n dev python=3.11 -y
    conda activate dev
    ```

2. Install `unionai`

```bash
pip install unionai
```

To use all the features of UnionAI's Severless, please use `unionai` as the entrypoint:

```bash
unionai run --remote ...
```
