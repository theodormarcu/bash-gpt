# BashGPT

BashGPT is a simple python script that helps you generate and understand terminal commands.

## How to run

1. Clone the repository
2. Install `python3` and `pip` using `brew install` or `apt-get install` or whatever
3. `pip install -r requirements.txt` (or use `pipenv install` / `virtualenv` if you know what that is)
4. Open a separate terminal window and run `python3 -m server`
5. Open another terminal window and run `python3 -m bashgpt --help`


## How to use

### To Explain a Command

`python3 -m bashgpt "brew install python3"`

### To Generate a Command

`python3 -m bashgpt --generate "Install python3 using brew"`


### Credits

Thanks @danielgross for the unofficial ChatGPT API (in server.py). Check out his repo [here](https://github.com/danielgross/whatsapp-gpt/blob/main/multichat.py);