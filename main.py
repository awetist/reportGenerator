from flask import *
import pandas as pd
import numpy as np


app = Flask(__name__)

@app.route("/show_tables",methods=['GET','POST'])
def show_tables():
    path="./uploads/"
    f=request.form['filename']
    filename=path+f;
    data = pd.read_excel(filename);
    data.drop(data.filter(regex="Unname"),axis=1, inplace=True)
    data = data.replace(np.nan, '', regex=True)    
    col = data.columns;
    data.index=data.index+1;

    #data.set_index('ID', inplace=True)
    return render_template('table.html', table=data.to_html(classes='student" id="table1" hidden="true'), title =f, colnames=col)

@app.route("/")
def upload_tables():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)