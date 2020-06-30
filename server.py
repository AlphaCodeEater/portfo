from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

print(__name__)


@app.route('/')
def first_page():
    return render_template('index.html')




@app.route('/<string:page_named>')
def html_form(page_named):
    return render_template(page_named)

def write_to_csv(data):
	with open('database.csv', mode= 'a',newline='') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']

		csv_writer = csv.writer(database2,delimiter =',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
		
		
		csv_writer.writerow([email,subject,message])
def write_to_file(data):
	with open('database.txt', mode= 'a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong'
	 	
    
    














# @app.route('/about.html')
# def about_me():
#     return render_template('about.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
















# # @app.route('/about.html')
# # def my_future():
	
	
# # 	return render_template('about.html')



# @app.route('/blog')
# def blogger():
#     return 'I have the very best blogs on my site'


# @app.route('/blog/2020/dogs')
# def blogger23():
#     return 'I love the loyalty of dogs'


