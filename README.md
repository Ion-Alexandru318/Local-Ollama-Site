# Local AI Chat Site

This is a simple Python program that uses the [Ollama API](https://github.com/ollama/ollama-python) and [Flask](https://flask.palletsprojects.com/en/stable/) to create a simple local website that allows the user and AI model to chat.


## Requirements
* [Ollama](https://ollama.com)
* AI model (for example [Llama3](https://ollama.com/library/llama3))

## Dependecies
All required packages are listed in ["requirement.txt"](/blob/main/requirements.txt) file.

Would also heavily recommend using [venv](https://docs.python.org/3/library/venv.html) before installing and setting it up.

Run this command in terminal for installing:

```sh
pip install -r requirement.txt
```

## Accessing site
When Flask code is running, your terminal will output at the start showing you exactly which addresses the website is available on.

If something is wrong and doesn't output could also access by:
* On the same machine:
Open your browser and write down: `https://127.0.0.1:9901`

* From other devices on the same network:
Use the IP address from the machine running Flask, and with the port (E.g `https://192.168.1.50:9901`).
