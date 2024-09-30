

@app.route('/<int:id>', methods=['GET'])
def search(id):
    if id < len(data1):
        temp = data1[id]
        flash('Successfully got the data!', 'success')  
        return render_template('search.html', temp=temp)
    else:
        return render_template('404.html')