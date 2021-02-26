import sanic
from sanic.exceptions import abort
from sanic import response
import os

app = sanic.app.Sanic('ControlMyPC')

# Homepage
@app.route('/')
async def func(request):
    return(await response.file('index.html'))

# Open Terminal
@app.route('/api/terminal', methods=['GET'])
async def func(request):
    os.system('cd ~ && gnome-terminal')
    abort(200)

# Open Files
@app.route('/api/files', methods=['GET'])
async def func(request):
    os.system('cd ~ && (nemo &)')
    abort(200)

# Open Browser
@app.route('/api/browser', methods=['GET'])
async def func(request):
    os.system('(firefox &)')
    abort(200)

# Open Browser with pptos.ga  WIP
@app.route('/api/browser', methods=['GET'])
async def func(request):
    os.system('(firefox --new-window https://www.pptos.ga/ &)')
    abort(200)    
    
app.run(host="0.0.0.0", port=5700, workers=2)
