from flask import Flask, render_template
from form import Data
import matplotlib.pyplot as plt
from plot import Plot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
@app.route("/",methods=['GET','POST'])
def root():
    form = Data()
    X = []
    Y = []
    x = [form.x1.data,form.x2.data,form.x3.data,form.x4.data,form.x5.data,form.x6.data,form.x7.data,form.x8.data,form.x9.data,form.x10.data]
    y = [form.y1.data,form.y2.data,form.y3.data,form.y4.data,form.y5.data,form.y6.data,form.y7.data,form.y8.data,form.y9.data,form.y10.data]
    for i in range(10):
        if(x[i]):
            X.append(x[i])
        if(y[i]):
            Y.append(y[i])
    if X and Y:
        Plot(X,Y,form.c.data)
    return render_template('index.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)
