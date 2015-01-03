from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Folks!"

@app.route("/colour/<rgb>")
def change_colour(rgb, ip):
    pins = [17, 18, 22]
    rgb_list = hex_to_rgb(rgb)
    i = 0
    cmdstr = ''
    while i < len(pins):
        colour = round((rgb_list[i]/255.0), 2)
        cmdstr = '%i=%f\n' % (pins[i], colour)
        pbfile = open('/dev/pi-blaster', 'w')
        pbfile.write(cmdstr)
        pbfile.close()
        i = i + 1
    return "changed: %s" % rgb

# Hex to RGB
def hex_to_rgb(hexcolor):
    lv = len(hexcolor)
    return tuple(int(hexcolor[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
