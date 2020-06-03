from flask import Flask
from flask import render_template,request,redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')



@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


#this is for writing into a text file
# def write_to_file(data):
# 	with open('database.txt', mode = 'a') as database:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]	
# 		file = database.write(f'\n{email},{subject},{message}')



#this is used to convert it into the csv files
# def write_to_csv(data):
# 	with open('database.csv', mode = 'a',newline = '') as database2:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]	
# 		csv_writer = csv.writer(database2, delimiter = ',' , quotechar = ' ' , quoting=csv.QUOTE_MINIMAL)
# 		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
	        data = request.form.to_dict()
	        write_to_csv(data)
	        return redirect('/thankyou.html')
	except:
	    	return "did not save to the database"
    else:
    	return "something went wrong"




# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/<username>')
# def about(username = None):
#     return render_template('about1.html',name = username)


# @app.route('/<username>/<int:post_id>')
# def show_post(username = None, post_id = None):
#     # show the post with the given id, the id is an integer
#     # return 'Post %d' % post_id
#     return render_template('about1.html',name = username, post_id = post_id )

# @app.route('/girl')
# def blog():
#     return 'This is a Woman\'s World'


# @app.route('/blog/2020/dogs')
# def dogs():
#     return 'I LOVE DOGGIES'




# @app.route('/index.html')
# def homepage():
#     return render_template('index.html')



# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')

