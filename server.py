from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')
def eight_by_eight(colmn = 8, row=8):           #This creates as many boxes as you enter
    return render_template('index.html', colmn = colmn, row = row) 

@app.route('/<int:colmn>/<int:row>')
def row_by_column(colmn, row):           #This creates as many boxes as you enter
    return render_template('index.html', colmn = colmn, row = row) 

@app.route('/<int:colmn>/<int:row>/<string:color1>/<string:color2>')
def row_by_column_with_color(colmn, row, color1, color2):           #This creates as many boxes as you enter
    return render_template('index.html', colmn = colmn, row = row, color1 = color1, color2 = color2) 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
