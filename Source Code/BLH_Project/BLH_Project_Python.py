from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Charles10'
app.config['MYSQL_DB'] = 'ProjectBLH'

mysql = MySQL(app)
# @app.route('/',methods=['GET','POST'])
# def hello():
#     return "Hello World!"
# ,methods=['GET','POST']
#inserting----------------------------
# @app.route('/')
# def hello():
# 	# if request.method =='POST'
# 	cur = mysql.connection.cursor()
# 	cur.execute("INSERT INTO `ProjectBLH`.`user_auth` (`user_id`, `username`, `password`, `access`) VALUES ('4', 'test4', 'test4', 'employee')")
# 	mysql.connection.commit()
# 	cur.close()
# 	return 'success'
#     # return render_template('Login_Page.html')
user_id = ''
template =''
full_name = ''
access = ''
department = ''
service_info = []
service_infoS = []
Frequest_id = []
Frequest_title = []
Frequest_category = []
Frequest_description = []
Frequest_time = []
Frequest_date = []
Frequest_level = []
column_count = ''
column_countS = ''
pyProcess = ''
fname = ''
mname = ''
lname = ''
AID =[]
count =''
Afullname = []
edit_department = ''
edit_id = ''
service_info_detail = []
detail_request_id = ''
detail_request_title = ''
detail_request_category = ''
detail_request_level = ''
detail_start_date = ''
detail_start_time = ''
detail_request_description = ''
detail_department_head_id = ''
detail_department_head_fname = ''
detail_maintenance_id = ''
detail_maintenance_fname = ''
detail_department = ''
assign_info = []
assign_personel_fullname = ''
count_repair = ''
count_request = ''
count_replace = ''
count_pending = ''
count_unassign = ''
count_inprogress = ''
count_closed = ''
SFrequest_id = []
SFrequest_title = []
SFrequest_category = []
commentcount = ''
SFrequest_description = []
SFrequest_time = []
SFrequest_date = []
SFrequest_level = []
selectedview = ''
selectedviewid = ''
selected = ''
commentDetail = []
commentreply = []
commentinfo = []
commentdesign = []
@app.route('/')
def index():

    return render_template('Login_Page.html')

def login_process(username,password):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT user_id FROM user_auth WHERE username = '{}' AND password = '{}'".format(username,password))
	if result == 1:
		user_id = cur.fetchone()
		return user_id[0]
	else:
		return 'Fail'


def retriev_user_info(user_id,user_info):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT first_name, middle_name, last_name, department,access FROM user_info WHERE user_id = '{}'".format(user_id))
	resultData = cur.fetchall()
	user_info.extend(resultData)

def retriev_maintenance_info(assign_info):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT user_id, first_name, middle_name, last_name FROM user_info WHERE department = 'Maintenance'")
	resultData = cur.fetchall()
	assign_info.extend(resultData)

def assign_maintenance_info(assign_personel_id, assign_maintenance):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT first_name, middle_name, last_name FROM user_info WHERE user_id = '{}'".format(assign_personel_id))
	resultData = cur.fetchall()
	assign_maintenance.extend(resultData)

def retriev_service_info(service_info,user_id):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT request_id, request_title,request_category,request_level, DATE_FORMAT(request_date_start, '%M %d %Y') as start_date, TIME_FORMAT(request_time_start, '%r') as start_time,request_description FROM service_request where (request_level = 'Pending' or  request_level = 'Inprogress' or request_level = 'Unassign') AND (department_head_id = '{}' OR maintenance_id = '{}') ORDER BY start_date DESC, start_time DESC".format(user_id,user_id))
	resultData = cur.fetchall()
	service_info.extend(resultData)

def retriev_service_info_admin(service_info):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT request_id, request_title,request_category,request_level, DATE_FORMAT(request_date_start, '%M %d %Y') as start_date, TIME_FORMAT(request_time_start, '%r') as start_time,request_description FROM service_request where (request_level = 'Pending' or request_level = 'Unassign' or  request_level = 'Inprogress') ORDER BY start_date DESC, start_time DESC")
	resultData = cur.fetchall()
	service_info.extend(resultData)

def retriev_service_infoS(service_infos,user_id,selected):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT request_id, request_title,request_category,request_level, DATE_FORMAT(request_date_start, '%M %d %Y') as start_date, TIME_FORMAT(request_time_start, '%r') as start_time,request_description FROM service_request where request_category = '{}' AND (request_level = 'Pending' or  request_level = 'Inprogress') AND (department_head_id = '{}' OR maintenance_id = '{}') ORDER BY start_date DESC, start_time DESC".format(selected, user_id,user_id))
	resultData = cur.fetchall()
	service_infoS.extend(resultData)

def retriev_service_info_adminS(service_infos,selected):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT request_id, request_title,request_category,request_level, DATE_FORMAT(request_date_start, '%M %d %Y') as start_date, TIME_FORMAT(request_time_start, '%r') as start_time,request_description FROM service_request where request_category = '{}' AND  (request_level = 'Pending' or request_level = 'Unassign' or  request_level = 'Inprogress') ORDER BY start_date DESC, start_time DESC".format(selected))
	resultData = cur.fetchall()
	service_infoS.extend(resultData)

def retriev_service_info_adminSearch(service_infos,selected):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT request_id, request_title,request_category,request_level, DATE_FORMAT(request_date_start, '%M %d %Y') as start_date, TIME_FORMAT(request_time_start, '%r') as start_time,request_description FROM service_request where id like '%{}%' OR request_id like '%{}%' OR department_head_id like '%{}%' OR maintenance_id like '%{}%' OR department_head_fname like '%{}%' OR maintenance_fname like '%{}%' OR request_title like '%{}%' OR request_category like '%{}%' OR request_description like '%{}%' OR request_time_start like '%{}%' OR request_date_start like '%{}%' OR request_level like '%{}%' OR department like '%{}%' OR request_time_end like '%{}%' OR request_date_end like '%{}%' OR close_name like '%{}%' OR close_id like '%{}%' AND (request_level = 'Pending' or request_level = 'Unassign' or  request_level = 'Inprogress')".format(selected,selected,selected,selected,selected,selected,selected,selected,selected,selected,selected,selected,selected,selected,selected,selected,selected))
	resultData = cur.fetchall()
	service_infoS.extend(resultData)

def retriev_service_info_adminSO(service_infos,selected):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT request_id, request_title,request_category,request_level, DATE_FORMAT(request_date_start, '%M %d %Y') as start_date, TIME_FORMAT(request_time_start, '%r') as start_time,request_description FROM service_request where request_level = '{}' ORDER BY start_date DESC, start_time DESC".format(selected))
	resultData = cur.fetchall()
	service_infoS.extend(resultData)

def retriev_service_info_comment(commentDetail,request_id_detail):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT user_id,service_replay, user_name, DATE_FORMAT(date, '%M %d %Y') as reply_date , TIME_FORMAT(time, '%r') as reply_time FROM ProjectBLH.service_request_convo where request_id = '{}'".format(request_id_detail))
	resultData = cur.fetchall()
	commentDetail.extend(resultData)


def retriev_service_count_admin():
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) as column_count FROM service_request where (request_level = 'Pending' or request_level = 'Unassign' or  request_level = 'Inprogress')")
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def retriev_service_count(user_id):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) as column_count FROM service_request where (request_level = 'Pending'  or  request_level = 'Inprogress') AND (department_head_id = '{}' OR maintenance_id = '{}')".format(user_id,user_id))
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def retriev_service_count_adminS(selected):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) as column_count FROM service_request where request_category = '{}' AND (request_level = 'Pending' or request_level = 'Unassign' or  request_level = 'Inprogress')".format(selected))
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def retriev_service_count_adminSO(selected):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) as column_count FROM service_request where request_level = '{}'".format(selected))
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def retriev_service_countS(user_id,selected):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) as column_count FROM service_request where request_category = '{}' AND (request_level = 'Pending' or  request_level = 'Inprogress') AND (department_head_id = '{}' OR maintenance_id = '{}')".format(selected,user_id,user_id))
	resultData = cur.fetchone()
	result = resultData[0]
	return result


def retriev_service_full_info(request_id_detail,service_info_detail):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT request_id, request_title,request_category,request_level,DATE_FORMAT(request_date_start, '%M %d %Y') as start_date, TIME_FORMAT(request_time_start, '%r') as start_time,request_description,department_head_id, department_head_fname, maintenance_id, maintenance_fname,department FROM service_request where request_id = '{}'".format(request_id_detail))
	resultData = cur.fetchall()
	service_info_detail.extend(resultData)


def retriev_edit_user_info(edit_id,edit_info):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT first_name, middle_name, last_name, department,access FROM user_info WHERE user_id = '{}'".format(edit_id))
	if result == 1:
		resultData = cur.fetchall()
		edit_info.extend(resultData)
	else:
		return 'Fail'


def retriev_request_count(request_category):
	cur = mysql.connection.cursor()
	cur.execute("SELECT count(*) FROM service_request WHERE request_category = '{}'".format(request_category))
	resultData = cur.fetchone()
	result = resultData[0]
	return result + 1


def user_add_info(request_user_id, fname, lname, mname, department,access):
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO `ProjectBLH`.`user_info` (`user_id`, `first_name`, `middle_name`, `last_name`, `department`, `access`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(request_user_id,fname,mname,lname,department,access))
	mysql.connection.commit()
	cur.close()
	return 'success'

def user_edit_info(edit_fname,edit_lname,edit_mname,edit_department,edit_access,edit_id):
	cur = mysql.connection.cursor()
	cur.execute("UPDATE `ProjectBLH`.`user_info` SET `first_name` = '{}', `middle_name` = '{}', `last_name` = '{}', `department` = '{}', `access` = '{}' WHERE (`user_id` = '{}')".format(edit_fname,edit_lname,edit_mname,edit_department,edit_access,edit_id))
	mysql.connection.commit()
	cur.close()
	return 'success'

def user_add_auth(request_user_id, username, password,access):
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO `ProjectBLH`.`user_auth` (`user_id`, `username`, `password`, `access`) VALUES ('{}', '{}', '{}', '{}')".format(request_user_id,username,password,access))
	mysql.connection.commit()
	cur.close()
	return 'success'

def assign_personel(assign_request_id,assign_personel_id,assign_personel_fullname):
	cur = mysql.connection.cursor()
	cur.execute("UPDATE `ProjectBLH`.`service_request` SET `request_level` = 'Inprogress', `maintenance_id` = '{}', `maintenance_fname` = '{}' WHERE `request_id` = '{}'".format(assign_personel_id,assign_personel_fullname,assign_request_id))
	mysql.connection.commit()
	cur.close()
	return 'success'

def clode_ticket(full_name,user_id,assign_request_id):
	cur = mysql.connection.cursor()
	cur.execute("UPDATE `ProjectBLH`.`service_request` SET `request_time_end` = CURTIME(), `request_date_end` = CURDATE(), `close_name` = '{}', `close_id` = '{}',`request_level` = 'Closed' WHERE `request_id` = '{}'".format(full_name,user_id,assign_request_id))
	mysql.connection.commit()
	cur.close()
	return 'success'


def pend_ticket(assign_request_id):
	cur = mysql.connection.cursor()
	cur.execute("UPDATE `ProjectBLH`.`service_request` SET `request_level` = 'Pending'WHERE `request_id` = '{}'".format(assign_request_id))
	mysql.connection.commit()
	cur.close()
	return 'success'

def user_edit_auth(edit_username,edit_password,edit_access,edit_id):
	cur = mysql.connection.cursor()
	cur.execute("UPDATE `ProjectBLH`.`user_auth` SET `username` = '{}', `password` = '{}', `access` = '{}' WHERE (`user_id` = '{}')".format(edit_username,edit_password,edit_access,edit_id))
	mysql.connection.commit()
	cur.close()
	return 'success'


def count_replace_process():
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) FROM ProjectBLH.service_request where request_level in (\'Pending\',\'Unassign\',\'Inprogress\') and request_category = \'Replace\'")
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def count_repair_process():
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) FROM ProjectBLH.service_request where request_level in (\'Pending\',\'Unassign\',\'Inprogress\')  and request_category = \'Repair\'")
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def count_request_process():
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) FROM ProjectBLH.service_request where request_level in (\'Pending\',\'Unassign\',\'Inprogress\')  and request_category = \'Request\'")
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def count_unassign_process():
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) FROM ProjectBLH.service_request where request_level = \'Unassign\'")
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def count_pending_process():
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) FROM ProjectBLH.service_request where request_level = \'Pending\'")
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def count_inprogress_process():
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) FROM ProjectBLH.service_request where request_level = \'Inprogress\'")
	resultData = cur.fetchone()
	result = resultData[0]
	return result

def count_closed_process():
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT count(*) FROM ProjectBLH.service_request where request_level = \'Closed\'")
	resultData = cur.fetchone()
	result = resultData[0]
	return result


@app.route('/BLH_REQUEST_SERVICE_SYSTEM',methods=['GET','POST'])
def login():
	global template
	global user_id
	global full_name
	global department
	global service_info
	user_info = []
	global Frequest_id
	global Frequest_title
	global Frequest_category
	global Frequest_description
	global Frequest_time
	global Frequest_date
	global Frequest_level
	global column_count
	global pyProcess
	global access
	global count_repair
	global count_request
	global count_replace
	global count_pending
	global count_unassign
	global count_inprogress
	global count_closed

	retriev_user_info(user_id,user_info)
	for a in user_info:
		fname = a[0]
		mname = a[1]
		lname = a[2]
		department = a[3]
		access = a[4]
		full_name = (str(fname) + " " + str(mname) + " " +str(lname))
	if request.method =='POST':
		username = request.values.get('username')
		password = request.values.get('password')
		user_info = []
		login_result = login_process(username,password)
		department = ''
		access= ''

		if login_result != 'Fail':
			user_id = login_result
			retriev_user_info(user_id,user_info)
			for a in user_info:
				fname = a[0]
				mname = a[1]
				lname = a[2]
				department = a[3]
				access = a[4]
				full_name = (str(fname) + " " + str(mname) + " " +str(lname))

			if access == '1':
				retriev_service_info_admin(service_info)
				for a in service_info:
					Frequest_id.append(a[0])
					Frequest_title.append(a[1])
					Frequest_category.append(a[2])
					Frequest_description.append(a[6])
					Frequest_time.append(a[5])
					Frequest_date.append(a[4])
					Frequest_level.append(a[3])
				count_repair = count_repair_process()
				count_request = count_request_process()
				count_replace = count_replace_process()
				count_pending = count_pending_process()
				count_unassign =  count_unassign_process()
				count_inprogress = count_inprogress_process()
				count_closed = count_closed_process()
				column_count = retriev_service_count_admin()
				template = 'Home_Page_Access1.html'
			elif access == '2':
				retriev_service_info(service_info,user_id)
				for a in service_info:
					Frequest_id.append(a[0])
					Frequest_title.append(a[1])
					Frequest_category.append(a[2])
					Frequest_description.append(a[6])
					Frequest_time.append(a[5])
					Frequest_date.append(a[4])
					Frequest_level.append(a[3])
				column_count = len(service_info)
				template = 'Home_Page_Access2.html'
			else:
				retriev_service_info(service_info,user_id)
				for a in service_info:
					Frequest_id.append(a[0])
					Frequest_title.append(a[1])
					Frequest_category.append(a[2])
					Frequest_description.append(a[6])
					Frequest_time.append(a[5])
					Frequest_date.append(a[4])
					Frequest_level.append(a[3])
				column_count = len(service_info)
				print(column_count)
				template = 'Home_Page_Access3.html'
			pyProcess = 'login'
		else:
			template = 'Login_Page.html'
			pyProcess = 'fail_login'
	return render_template('{}'.format(template), full_name =full_name, department = department, user_id = user_id, pyProcess = pyProcess, column_count = column_count
		,Frequest_id=Frequest_id,Frequest_title=Frequest_title,Frequest_category=Frequest_category,Frequest_description=Frequest_description,Frequest_time=Frequest_time,
		Frequest_date=Frequest_date,Frequest_level=Frequest_level,count_repair = count_repair,count_request= count_request, count_replace = count_replace,count_pending=count_pending,
		count_unassign = count_unassign, count_inprogress = count_inprogress, count_closed = count_closed)


@app.route('/BLH_REQUEST_SERVICE_SYSTEM/Home',methods=['GET','POST'])
def home():

	global user_id
	global template
	global full_name
	global department
	global service_info
	global service_infoS
	global pyProcess
	global Frequest_id
	global Frequest_title
	global Frequest_category
	global Frequest_description
	global Frequest_time
	global Frequest_date
	global Frequest_level
	global SFrequest_id
	global SFrequest_title
	global SFrequest_category
	global SFrequest_description
	global SFrequest_time
	global SFrequest_date
	global SFrequest_level
	global column_count
	global column_countS
	global commentreply
	global commentinfo
	global commentdesign
	department_head_id = user_id
	department_head_fname = full_name
	if (request.values.get('title1') != '') or (request.values.get('title1' is not None)):
		request_title = request.values.get('title1')
	else:
		request_title = request.values.get('title2')
	if (request.values.get('category2') != '') or (request.values.get('category2' is not None)):
		request_category = request.values.get('category2')
	else:
		request_category = request.values.get('category1')
		print ('2')
	if (request.values.get('description1') != '') or (request.values.get('description1' is not None)):
		request_description = request.values.get('description1')
	else:
		request_description = request.values.get('description2')
	request_id_counter = format(retriev_request_count(request_category),"07")
	global fname
	global mname
	global lname
	global AID
	global count
	global Afullname
	global edit_department
	global edit_id
	global service_info_detail
	global detail_request_id
	global detail_request_title
	global detail_request_category
	global detail_request_level
	global detail_start_date
	global detail_start_time
	global detail_request_description
	global detail_department_head_id
	global detail_department_head_fname
	global detail_maintenance_id
	global detail_maintenance_fname
	global detail_department
	global assign_info
	global assign_personel_fullname
	global access
	global count_repair
	global count_request
	global count_replace
	global count_pending
	global count_unassign
	global count_inprogress
	global count_closed
	global selectedview
	global selectedviewid
	global selected
	global commentDetail
	global commentcount
	service_info = []
	service_infoS = []
	Frequest_id[:] = []
	Frequest_title[:] = []
	Frequest_category[:] = []
	Frequest_description[:] = []
	Frequest_time[:] = []
	Frequest_date[:] = []
	Frequest_level[:] = []
	SFrequest_id[:] = []
	SFrequest_title[:] = []
	SFrequest_category[:] = []
	SFrequest_description[:] = []
	SFrequest_time[:] = []
	SFrequest_date[:] = []
	SFrequest_level[:] = []
	service_info.clear()
	service_infoS.clear()
	column_count = ''
	column_countS = ''
	fname = ''
	mname = ''
	lname = ''
	AID[:] = []
	count =''
	Afullname[:] = []
	edit_department = ''
	edit_id = ''
	service_info_detail[:] = []
	detail_request_id = ''
	detail_request_title = ''
	detail_request_category = ''
	detail_request_level = ''
	detail_start_date = ''
	detail_start_time = ''
	detail_request_description = ''
	detail_department_head_id = ''
	detail_department_head_fname = ''
	detail_maintenance_id = ''
	detail_maintenance_fname = ''
	detail_department = ''
	assign_info[:] = []
	assign_personel_fullname = ''
	pyProcess = ''
	selectedview = ''
	selectedviewid = ''
	selected = ''
	commentDetail[:] = []
	commentreply[:] = []
	commentinfo[:] = []
	commentdesign[:] = []
	commentcount=''
	count_repair = count_repair_process()
	count_request = count_request_process()
	count_replace = count_replace_process()
	count_pending = count_pending_process()
	count_unassign =  count_unassign_process()
	count_inprogress = count_inprogress_process()
	count_closed = count_closed_process()
	if access == '2' or access == '3':
		retriev_service_info(service_info,user_id)
		for a in service_info:
			Frequest_id.append(a[0])
			Frequest_title.append(a[1])
			Frequest_category.append(a[2])
			Frequest_description.append(a[6])
			Frequest_time.append(a[5])
			Frequest_date.append(a[4])
			Frequest_level.append(a[3])
		column_count = len(service_info)
		print('3')
	if request.method =='POST':
		service_info = []
		service_info.clear()
		process = request.values.get('process')
		if request_category == 'Repair':
			front_id = 'R1-'
		elif request_category == 'Replace':
			front_id = 'R2-'
		else:
			front_id = 'R3-'
		request_id = front_id + request_id_counter
		if process == 'Allview':
			retriev_service_info_admin(service_info)
			for a in service_info:
				Frequest_id.append(a[0])
				Frequest_title.append(a[1])
				Frequest_category.append(a[2])
				Frequest_description.append(a[6])
				Frequest_time.append(a[5])
				Frequest_date.append(a[4])
				Frequest_level.append(a[3])
			column_count = retriev_service_count_admin()
			print(column_count)
			print(service_info)
			count_repair = count_repair_process()
			count_request = count_request_process()
			count_replace = count_replace_process()
			count_pending = count_pending_process()
			count_unassign =  count_unassign_process()
			count_inprogress = count_inprogress_process()
			count_closed = count_closed_process()
			pyProcess = 'AllviewDone'
		elif process == 'add_ticket':
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO `ProjectBLH`.`service_request`  (`request_id`, `department_head_id`, `department_head_fname`, `request_title`, `request_category`,  `request_description`,`request_time_start`,`request_date_start`, `request_level`,`department`) VALUES ('{}', '{}', '{}', '{}', '{}','{}', CURTIME(),CURDATE(),'Unassign','{}')".format(request_id,department_head_id,department_head_fname,request_title,request_category,request_description,department))
			mysql.connection.commit()
			cur.close()
			pyProcess = 'addTicket'
		elif process == 'add_user':
			request_user_id = request.values.get('idnumber')
			fname = request.values.get('fname')
			lname = request.values.get('lname')
			mname = request.values.get('mname')
			department = request.values.get('department')
			username = request.values.get('username')
			password = request.values.get('password')
			if department == 'Admin':
				access = '1'
			elif department == 'Maintenance':
				access = '3'
			else:
				access = '2'
			user_info = user_add_info(request_user_id, fname, lname, mname, department,access)
			user_auth = user_add_auth(request_user_id, username, password,access)
			pyProcess = 'addUser'

		elif process == 'search_user':
			edit_id = request.values.get('edit_id')
			edit_info = []
			result = retriev_edit_user_info(edit_id,edit_info)
			if result == 'Fail':
				pyProcess = 'search_fail'
			else:
				for a in edit_info:
					fname = a[0]
					mname = a[1]
					lname = a[2]
					edit_department = a[3]
				pyProcess = 'search_success'
		elif process == 'edit_user':
			edit_id = request.values.get('edit_id')
			edit_fname = request.values.get('edit_fname')
			edit_lname = request.values.get('edit_lname')
			edit_mname = request.values.get('edit_mname')
			edit_department = request.values.get('edit_department')
			edit_username = request.values.get('edit_username')
			edit_password = request.values.get('edit_password')
			if edit_department == 'Admin':
				edit_access = '1'
			elif edit_department == 'Maintenance':
				edit_access = '3'
			else:
				edit_access = '2'
			user_edit_info(edit_fname,edit_lname,edit_mname,edit_department,edit_access,edit_id)
			user_edit_auth(edit_username,edit_password,edit_access,edit_id)
			pyProcess = 'edit_success'
		elif process == 'detail_open':
			request_id_detail = request.values.get('selected_open')
			retriev_service_full_info(request_id_detail,service_info_detail)
			for a in service_info_detail:
				detail_request_id = a[0]
				detail_request_title = a[1]
				detail_request_category = a[2]
				detail_request_level = a[3]
				detail_start_date = a[4]
				detail_start_time = a[5]
				detail_request_description = a[6]
				detail_department_head_id = a[7]
				detail_department_head_fname = a[8]
				detail_maintenance_id = a[9]
				detail_maintenance_fname = a[10]
				detail_department = a[11]
			retriev_maintenance_info(assign_info)
			count = len(assign_info)
			for a in assign_info:
				AID.append(a[0])
				Afullname.append(a[1]+" "+a[2]+" "+a[3])
			retriev_service_info_comment(commentDetail,request_id_detail)
			for x in commentDetail:
				commentreply.append(x[1])
				commentinfo.append(str(x[2]) + " (" + str(x[3]) + "," + str(x[4]) + ")")
				if x[0] == user_id:
					commentdesign.append('1')
				else:
					commentdesign.append('2')
			commentcount = len(commentDetail)
			pyProcess = 'selected_open'
		elif process == 'assign_personel':
			assign_maintenance = []
			assign_request_id = request.values.get('detail_id')
			assign_personel_id = request.values.get('assign_personel')
			assign_maintenance_info(assign_personel_id, assign_maintenance)
			for a in assign_maintenance:
				assign_personel_fullname = (a[0]+" "+a[1]+" "+a[2])

			assign_personel(assign_request_id,assign_personel_id,assign_personel_fullname)
			pyProcess = 'assign_complete'
			count_repair = count_repair_process()
			count_request = count_request_process()
			count_replace = count_replace_process()
			count_pending = count_pending_process()
			count_unassign =  count_unassign_process()
			count_inprogress = count_inprogress_process()
			count_closed = count_closed_process()
		elif process == 'close_ticket':
			assign_request_id = request.values.get('detail_id')
			clode_ticket(full_name,user_id,assign_request_id)
			pyProcess == 'close_ticket'
			count_repair = count_repair_process()
			count_request = count_request_process()
			count_replace = count_replace_process()
			count_pending = count_pending_process()
			count_unassign =  count_unassign_process()
			count_inprogress = count_inprogress_process()
			count_closed = count_closed_process()
		elif process == 'selectedtype':
			selected = request.values.get('selected')
			retriev_service_info_adminS(service_infoS,selected)
			for a in service_infoS:
				SFrequest_id.append(a[0])
				SFrequest_title.append(a[1])
				SFrequest_category.append(a[2])
				SFrequest_description.append(a[6])
				SFrequest_time.append(a[5])
				SFrequest_date.append(a[4])
				SFrequest_level.append(a[3])
			column_countS = retriev_service_count_adminS(selected)
			count_repair = count_repair_process()
			count_request = count_request_process()
			count_replace = count_replace_process()
			count_pending = count_pending_process()
			count_unassign =  count_unassign_process()
			count_inprogress = count_inprogress_process()
			count_closed = count_closed_process()
			pyProcess = 'selectedDone'
			selectedview = request.values.get('selected_td')
			selectedviewid = request.values.get('selected_tdid')
		elif process == 'selectedtypeS':
			selected = request.values.get('selected')
			retriev_service_info_adminSO(service_infoS,selected)
			for a in service_infoS:
				SFrequest_id.append(a[0])
				SFrequest_title.append(a[1])
				SFrequest_category.append(a[2])
				SFrequest_description.append(a[6])
				SFrequest_time.append(a[5])
				SFrequest_date.append(a[4])
				SFrequest_level.append(a[3])
			column_countS = retriev_service_count_adminSO(selected)
			count_repair = count_repair_process()
			count_request = count_request_process()
			count_replace = count_replace_process()
			count_pending = count_pending_process()
			count_unassign =  count_unassign_process()
			count_inprogress = count_inprogress_process()
			count_closed = count_closed_process()
			pyProcess = 'selectedDone'
			selectedview = request.values.get('selected_td')
			selectedviewid = request.values.get('selected_tdid')
		elif process == 'search':
			i = 1
			if (request.values.get('searchitem1') != '') or (request.values.get('searchitem1' is not None)):
				selected = request.values.get('searchitem1')
			else:
				selected = request.values.get('searchitem2')
			retriev_service_info_adminSearch(service_infoS,selected)
			for a in service_infoS:
				SFrequest_id.append(a[0])
				SFrequest_title.append(a[1])
				SFrequest_category.append(a[2])
				SFrequest_description.append(a[6])
				SFrequest_time.append(a[5])
				SFrequest_date.append(a[4])
				SFrequest_level.append(a[3])
			column_countS =len(service_infoS)
			print(service_infoS)
			count_repair = count_repair_process()
			count_request = count_request_process()
			count_replace = count_replace_process()
			count_pending = count_pending_process()
			count_unassign =  count_unassign_process()
			count_inprogress = count_inprogress_process()
			count_closed = count_closed_process()
			pyProcess = 'searchDone'
			selectedview = request.values.get('selected_td')
			selectedviewid = request.values.get('selected_tdid')
		elif process == 'pend_ticket':
			assign_request_id = request.values.get('detail_id')
			pend_ticket(assign_request_id)
			pyProcess == 'pend_ticket'
			count_repair = count_repair_process()
			count_request = count_request_process()
			count_replace = count_replace_process()
			count_pending = count_pending_process()
			count_unassign =  count_unassign_process()
			count_inprogress = count_inprogress_process()
			count_closed = count_closed_process()
		elif process == 'comment':
			assign_request_id = request.values.get('detail_id')
			replytext = request.values.get('replytext')
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO `ProjectBLH`.`service_request_convo` (`user_id`, `request_id`, `service_replay`, `date`, `time`, `user_name`) VALUES ('{}', '{}', '{}', CURDATE(), CURTIME(), '{}')".format(user_id,assign_request_id,replytext,full_name))
			mysql.connection.commit()
			cur.close()
			pyProcess = 'commentDone'
			count_repair = count_repair_process()
			count_request = count_request_process()
			count_replace = count_replace_process()
			count_pending = count_pending_process()
			count_unassign =  count_unassign_process()
			count_inprogress = count_inprogress_process()
			count_closed = count_closed_process()
		elif process == 'logout':
			user_id = ''
			template ='Login_Page.html'
			full_name = ''
			department = ''
			service_info = []
			service_infoS = []
			Frequest_id[:] = []
			Frequest_title[:] = []
			Frequest_category[:] = []
			Frequest_description[:] = []
			Frequest_time[:] = []
			Frequest_date[:] = []
			Frequest_level[:] = []
			SFrequest_id[:] = []
			SFrequest_title[:] = []
			commentDetail[:] = []
			SFrequest_category[:] = []
			SFrequest_description[:] = []
			SFrequest_time[:] = []
			commentreply[:] = []
			commentinfo[:] = []
			commentdesign[:] = []
			SFrequest_date[:] = []
			SFrequest_level[:] = []
			commentcount = ''
			service_info.clear()
			service_infoS.clear()
			column_count = ''
			column_countS = ''
			fname = ''
			mname = ''
			lname = ''
			AID[:] = []
			count =''
			Afullname[:] = []
			edit_department = ''
			edit_id = ''
			service_info_detail[:] = []
			detail_request_id = ''
			detail_request_title = ''
			detail_request_category = ''
			detail_request_level = ''
			detail_start_date = ''
			detail_start_time = ''
			detail_request_description = ''
			detail_department_head_id = ''
			detail_department_head_fname = ''
			detail_maintenance_id = ''
			detail_maintenance_fname = ''
			detail_department = ''
			assign_info[:] = []
			assign_personel_fullname = ''
			pyProcess = ''
			selectedview = ''
			selectedviewid = ''
			selected = ''
	return render_template(template,full_name= full_name, user_id=user_id, department = department,pyProcess =pyProcess, fname = fname, mname = mname,
		lname = lname, edit_department = edit_department, edit_id = edit_id, detail_request_id= detail_request_id,detail_request_title=detail_request_title
		,detail_request_category=detail_request_category,detail_request_level=detail_request_level,detail_start_date=detail_start_date,detail_start_time=detail_start_time
		,detail_request_description=detail_request_description,detail_department_head_id=detail_department_head_id,detail_department_head_fname=detail_department_head_fname,
		detail_maintenance_id=detail_maintenance_id,detail_maintenance_fname=detail_maintenance_fname,detail_department=detail_department,column_count = column_count
		,Frequest_id=Frequest_id,Frequest_title=Frequest_title,Frequest_category=Frequest_category,Frequest_description=Frequest_description,Frequest_time=Frequest_time,
		Frequest_date=Frequest_date,Frequest_level=Frequest_level,AID=AID,Afullname=Afullname,count=count,count_repair = count_repair,count_request= count_request, count_replace = count_replace,count_pending=count_pending,
		count_unassign = count_unassign, count_inprogress = count_inprogress, count_closed = count_closed,column_countS = column_countS,SFrequest_id=SFrequest_id,SFrequest_title=SFrequest_title,SFrequest_category=SFrequest_category,SFrequest_description=SFrequest_description,SFrequest_time=SFrequest_time,
		SFrequest_date=SFrequest_date,SFrequest_level=SFrequest_level,selectedview=selectedview,commentreply =commentreply ,commentcount= commentcount, commentdesign=commentdesign,commentinfo = commentinfo,selectedviewid = selectedviewid, selected = selected)
