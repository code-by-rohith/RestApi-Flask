from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

data1 = ['process', 'product', 'sales']

@app.route('/')
def main():
    data = ['process', 'product', 'sales']
    return render_template('index.html', data=data)

@app.route('/<int:id>', methods=['GET'])
def search(id):
    if id < len(data1):
        temp = data1[id]
        flash('Successfully got the data!', 'success')  
        return render_template('search.html', temp=temp)
    
    flash('Invalid ID. Please try again.', 'danger')  
    return redirect(url_for('main'))

@app.route('/search', methods=['GET'])
def search_by_query():
    query = request.args.get('query')
    if query is not None and query.isdigit():
        id = int(query)
        if id < len(data1):
            temp = data1[id]
            flash('Successfully got the data!', 'success') 
            return render_template('search.html', temp=temp)
    flash('Invalid ID. Please try again.', 'danger')  
    return redirect(url_for('main'))

@app.template_filter('op')
def upper(data):
    return data.upper()

@app.route('/loop')
def loop():
    loop = [i for i in range(100)]
    return render_template('loop.html', loop=loop)

if __name__ == '__main__':
    app.run(debug=True)
