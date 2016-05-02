from flask import Flask

# create our application :)
app = Flask(__name__)
#default configurations 
app.config.from_object('settings.development')
print("Debug before " + str(app.config['DEBUG']))
#overide default configurations at file specified by USERMGT_SETTINGS environment variable
app.config.from_envvar('USERMGT_SETTINGS', silent=True)
print("Debug after " + str(app.config['DEBUG']))

@app.route('/api/v1.0/usermgt/users',methods=['GET'])
def get_users():
	user_list = "operativos"
	return user_list

if __name__ == "__main__":
	app.run('0.0.0.0')
