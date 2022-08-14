import cv2
import numpy
from skimage import io
from flask import Flask, request, Response
import requests
from colorthief import ColorThief

app = Flask(__name__)


def get_color_thief_image(url):
    r = requests.get(url, allow_redirects=True)
    open('image.jpg', 'wb').write(r.content)
    return ColorThief('image.jpg')


@app.route("/", methods=['GET'])
def get_avg_color():
    img = cv2.cvtColor(io.imread(request.args['img']), cv2.COLOR_BGR2RGB)
    avg_color_per_row = numpy.average(img, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    resp = Response(response=f"{{\"r\": {avg_color[2]:.2f}, \"g\": {avg_color[1]:.2f}, \"b\": {avg_color[0]:.2f}}}",
                    status=200,
                    mimetype="application/json")
    return resp


@app.route("/dominant", methods=['GET'])
def get_dominant_color():
    dominant_color = get_color_thief_image(request.args['img']).get_color(quality=10)
    return Response(response=f'{{"r": {dominant_color[0]}, "g": {dominant_color[1]}, "b": {dominant_color[2]}}}',
                    status=200,
                    mimetype="application/json")


@app.route("/palette", methods=['GET'])
def get_dominant_color_palette():
    color_palette = get_color_thief_image(request.args['img']).get_palette(quality=10, color_count=2)
    json = f'[{{"r": {color_palette[0][0]}, "g": {color_palette[0][1]}, "b": {color_palette[0][2]}}},' \
           f' {{"r": {color_palette[1][0]}, "g": {color_palette[1][1]}, "b": {color_palette[1][2]}}}]'
    return Response(response=json,
                    status=200,
                    mimetype="application/json")


if __name__ == '__main__':
    app.run(host="localhost", port=8097)
