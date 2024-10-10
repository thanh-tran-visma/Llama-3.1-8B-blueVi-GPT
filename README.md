# Llama-3.1-8B-blueVi

## Overview

This project involves training or fine-tuning the **Llama-3.1-8B** model.

## Hugging Face Model

- **Base Model**: [Llama3.1-8B-blueVi-GPT-base](https://huggingface.co/ThanhTranVisma/Llama3.1-8B-blueVi-GPT-base)
- **LORA**: [Llama3.1-8B-blueVi-GPT-lora](https://huggingface.co/ThanhTranVisma/Llama3.1-8B-blueVi-GPT-lora)

## Hugging Face Access Token Required

You will need a Hugging Face access token to run this project. You can get your token at [Hugging Face Tokens](https://huggingface.co/settings/tokens).

### How to Setup Locally

1. **Clone the Repository**: Clone the repository and navigate to the project folder.
2. **Create Python env, activate env and install requirements**
    ```bash
    make venv
    source env/bin/activate
    make install
    ```
3. **Copy Environment Variables**: Copy the environment variables example file and adjust the Hugging Face token with your own.
    ```bash
    cp .env.example .env
    vim .env
    ```
4. **Add the**
    ```
    127.0.0.1 gpt.dotweb.test
    to your /etc/hosts file (Linux/MAC) or C:\Windows\System32\drivers\etc\hosts (Windows)
   ```
4. **Run the server**
    ```bash
    make dev
    ```
5. **Run the tests**
    ```bash
    make tests
    ```

### Playground

By default, the playground can be accessed via: 
 - https://gpt.dotweb.test (docker)
 - http://0.0.0.0:8000/ (local)