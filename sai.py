from flask import Flask,render_template ## we need to import Flask class from flask package render_template is used for template rendering

FAI=Flask(__name__)  ### FAI is Flask Application Instance & __name__ is default name of module ex: where i gave my file as sai.py is standard name is __name__


@FAI.route('/wish')  ## decarator  route is a routing method in flask like url mapping in django
def wish():  ## in flask request in not needed
    return 'Hai mr Sai Shankar Vemula'  

@FAI.route('/first')
def first():
    return render_template('first.html',name='sai shankar',age=24)


FAI.run(debug=True) ### in djano runserver is done by manage.py but here routing is like (urlmapping) and run is like (runserver) , here debug=True is manditory to give to run server


# FAI.run(debug=True)