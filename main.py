from flask import Flask, render_template, request, url_for
from flask_sock import Sock
import winkeys
from os import system

""" Use Task manager run start.vbs script"""

app = Flask(__name__)
sock = Sock(app)
#app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))
def shutdown():
    print('run')
def fullscreen():
    winkeys.altpress('enter')

commands = {
    'power': shutdown,
    'mute': 'volume_mute',
    'up': 'up_arrow',
    'vup': 'volume_up',
    'left': 'left_arrow',
    'pause': 'spacebar',
    'right': 'right_arrow',
    'fullscreen': fullscreen,
    'down': 'down_arrow',
    'vdown':'volume_down',
    'f': 'f',
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        if request.form.get('volume') == 'VOL+':
            winkeys.press('volume_up')

        elif request.form.get('volume') == 'VOL-':
            winkeys.press('volume_down')

        elif request.form.get('volume') == 'MUTE':
            winkeys.press('volume_mute')

        elif request.form.get('control') == 'SPACE':
            winkeys.press('spacebar')

        elif request.form.get('control') == 'PLAY/PAUSE':
            winkeys.press('play/pause_media')

        elif request.form.get('control') == 'F':
            winkeys.press('f')

        elif request.form.get('control') == 'ALT+ENTER':
            winkeys.altpress('enter')

        elif request.form.get('control') == '←':
            winkeys.press('left_arrow')

        elif request.form.get('control') == '→':
            winkeys.press('right_arrow')

        elif request.form.get('control') == '↑':
            winkeys.press('up_arrow')

        elif request.form.get('control') == '↓':
            winkeys.press('down_arrow')

        elif request.form.get('control') == 'OFF':
            pass
            print("shutdown")
            system("shutdown /s")
            # winkeys.press('right_arrow')

        else:
            pass
    elif request.method == 'GET':
        return render_template("remote.html")
    return ('', 204)
    # return render_template("index.html")


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        print(type(data), data)
        sock.send(data)


@sock.route('/command')
def command(sock):
    while True:
        data = sock.receive()
        cmd = commands[data]
        #print(data)
        if callable(cmd):
            cmd()
        else:
            winkeys.press(cmd)





if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)