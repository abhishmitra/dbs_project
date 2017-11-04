from flask import Flask, render_template, json, request, redirect,url_for
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'iwbiberm'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

SITE = "http://localhost:5000"

#AWS UI Links
AWS_UI_LINK = "https://s3-ap-south-1.amazonaws.com/onecall-ui-assets/Merged%20Site/"

@app.route("/")                                     #HOME PAGE
def main():
    return redirect(url_for('listings'))
    #return render_template('index.html')

@app.route("/post", methods = ['GET','POST'])                           
def postnow():
    if request.method == 'POST':
        print(request.form)
    return '''
    <!DOCTYPE html>
    <html>
    <head>
      <!-- Site made with Mobirise Website Builder v4.0.17, https://mobirise.com -->
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="generator" content="Mobirise v4.0.17, mobirise.com">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="shortcut icon" href="assets/images/logo21.png" type="image/x-icon">
      <meta name="description" content="Web Builder Description">
      <title>Post A New Job</title>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Rubik:300,300i,400,400i,500,500i,700,700i,900,900i">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/web/assets/mobirise-icons/mobirise-icons.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/tether/tether.min.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/bootstrap/css/bootstrap.min.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/dropdown/css/style.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/theme/css/style.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/mobirise/css/mbr-additional.css" type="text/css">



    </head>
    <body>
    <section class="menu cid-qqpBmXmdnM" once="menu" id="menu2-q" data-rv-view="1354">



        <nav class="navbar navbar-dropdown align-items-center navbar-fixed-top navbar-toggleable-sm">
            <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <div class="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </button>
            <div class="menu-logo">
                <div class="navbar-brand">

                    <span class="navbar-caption-wrap">
                        <a class="navbar-caption text-white display-4" href="https://mobirise.com">ONECALL JOBS</a>
                    </span>
                </div>
            </div>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true">
                    <li class="nav-item">
                        <a class="nav-link link text-white display-4" href="''' + SITE + '''/postnew">
                            Services
                        </a>
                    </li>
                </ul>

            </div>
        </nav>
    </section>

    <section class="engine"><a href="https://mobirise.co/c">free web maker</a></section><section class="mbr-section form1 cid-qqpJOIjXJF" id="form1-r" data-rv-view="1356">




        <div class="container">
            <div class="media-container-column title col-12 col-lg-8 offset-lg-2">
                <h2 class="mbr-section-title align-center pb-3 mbr-fonts-style display-2">Post A New Job</h2>
                <h3 class="mbr-section-subtitle align-center mbr-light pb-3 mbr-fonts-style display-5">Please fill up the data below</h3>
            </div>
        </div>
        <div class="container">
            <div class="media-container-column col-lg-8 offset-lg-2" data-form-type="formoid">
                    <div data-form-alert="" hidden="">
                        Thanks for filling out the form!
                    </div>

                    <form class="mbr-form" action="''' + SITE + '''/post" method="post" data-form-title="User Registration">
                        <div class="row row-sm-offset">
                            <div class="col-md-4 multi-horizontal" data-for="name">
                                <div class="form-group">
                                    <label class="form-control-label mbr-fonts-style display-7" for="name-form1-r"><b>Title</b></label>
                                    <input type="text" class="form-control" name="title" data-form-field="Name" required="" id="title" value= "">
                                </div>
                            </div>
                        </div>
                        <div class="row row-sm-offset">
                            <div class="col-md-4 multi-horizontal" data-for="name">
                                <div class="form-group">
                                    <label class="form-control-label mbr-fonts-style display-7" for="name-form1-r"><b>Description</b></label>
                                    <input type="text" class="form-control" name="desc" data-form-field="Name" required="" id="desc" value= "">
                                </div>
                            </div>
                        </div>
                        <div class="form-group" data-for="message">
                            <div class="row row-sm-offset">
                                <div class="col-md-4 multi-horizontal" data-for="name">
                                        <label class="form-control-label mbr-fonts-style display-7" for="name-form1-r"><b>Minimum</b></label>
                                        <input type="text" class="form-control" name="min" required="" id="min" value= "">
                                </div>

                            </div>

                        </div>
                        <div class="row row-sm-offset">
                            <div class="col-md-4 multi-horizontal" data-for="phone">
                                <div class="form-group">
                                        <label class="form-control-label mbr-fonts-style display-7" for="phone-form1-r"><b>Phone</b></label>
                                        <input type="tel" class="form-control" name="mobile" data-form-field="Phone" id="mobile">
                                </div>
                            </div>
                        </div>
                        

                        <span class="input-group-btn">
                            <button href="" type="submit" class="btn btn-primary btn-form display-4">DONE</button>
                        </span>
                    </form>
            </div>
            
        </div>
    </section>


      <script src="''' + AWS_UI_LINK + '''assets/web/assets/jquery/jquery.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/tether/tether.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/bootstrap/js/bootstrap.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/smooth-scroll/smooth-scroll.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/dropdown/js/script.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/touch-swipe/jquery.touch-swipe.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/theme/js/script.js"></script>

    </body>
    </html>
'''
@app.route("/apply", methods = ['GET','POST'])                           
def apply():
    try:
        if request.method == 'POST':
            ### Enter this as a listing in the database ###
            _name = request.form['name']
            _idvar = request.form['idvar']
            _bid = request.form['bid']
            
        if 'id' in request.args:
            idvar = request.args['id']
            return '''
    <!DOCTYPE html>
    <html>
    <head>
      <!-- Site made with Mobirise Website Builder v4.0.17, https://mobirise.com -->
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="generator" content="Mobirise v4.0.17, mobirise.com">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="shortcut icon" href="assets/images/logo21.png" type="image/x-icon">
      <meta name="description" content="Web Builder Description">
      <title>More User Details (Page 2)</title>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Rubik:300,300i,400,400i,500,500i,700,700i,900,900i">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/web/assets/mobirise-icons/mobirise-icons.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/tether/tether.min.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/bootstrap/css/bootstrap.min.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/dropdown/css/style.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/theme/css/style.css">
      <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/mobirise/css/mbr-additional.css" type="text/css">



    </head>
    <body>
    <section class="menu cid-qqpBmXmdnM" once="menu" id="menu2-q" data-rv-view="1354">



        <nav class="navbar navbar-dropdown align-items-center navbar-fixed-top navbar-toggleable-sm">
            <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <div class="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </button>
            <div class="menu-logo">
                <div class="navbar-brand">

                    <span class="navbar-caption-wrap">
                        <a class="navbar-caption text-white display-4" href="https://mobirise.com">ONECALL JOBS</a>
                    </span>
                </div>
            </div>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true">
                    <li class="nav-item">
                        <a class="nav-link link text-white display-4" href="''' + SITE + '''/postnew">
                            Services
                        </a>
                    </li>
                </ul>

            </div>
        </nav>
    </section>

    <section class="engine"><a href="https://mobirise.co/c">free web maker</a></section><section class="mbr-section form1 cid-qqpJOIjXJF" id="form1-r" data-rv-view="1356">




        <div class="container">
            <div class="media-container-column title col-12 col-lg-8 offset-lg-2">
                <h2 class="mbr-section-title align-center pb-3 mbr-fonts-style display-2">Your Bid Details</h2>
                <h3 class="mbr-section-subtitle align-center mbr-light pb-3 mbr-fonts-style display-5">Please fill up the data below</h3>
            </div>
        </div>

        <div class="container">
            <div class="media-container-column col-lg-8 offset-lg-2" data-form-type="formoid">
                    <div data-form-alert="" hidden="">
                        Thanks for filling out the form!
                    </div>

                    <form class="mbr-form" action="''' + SITE + '''/apply" method="post" data-form-title="User Registration">
                        <div class="row row-sm-offset">
                            <div class="col-md-4 multi-horizontal" data-for="name">
                                <div class="form-group">
                                    <label class="form-control-label mbr-fonts-style display-7" for="name-form1-r"><b>Name</b></label>
                                    <input type="text" class="form-control" name="name" data-form-field="Name" required="" id="name" value= "">
                                    <input type="hidden" class="form-control" name="idvar" data-form-field="idvar" required="" id="idvar" value= "''' + idvar + '''">
                                </div>
                            </div>

                        </div>
                        <div class="form-group" data-for="message">
                            <div class="row row-sm-offset">
                                <div class="col-md-4 multi-horizontal" data-for="name">
                                        <label class="form-control-label mbr-fonts-style display-7" for="name-form1-r"><b>Bid Amount</b></label>
                                        <input type="text" class="form-control" name="bid" required="" id="bid" value= "">
                                </div>

                            </div>

                        </div>
                        <div class="row row-sm-offset">
                            <div class="col-md-4 multi-horizontal" data-for="phone">
                                <div class="form-group">
                                        <label class="form-control-label mbr-fonts-style display-7" for="phone-form1-r"><b>Phone</b></label>

                                        <input type="hidden" value = "0" name = "validated" id = "validated" name = "validated">
                                        <input type="tel" class="form-control" name="mobile" data-form-field="Phone" id="mobile">
                                </div>
                            </div>
                        </div>
                        

                        <span class="input-group-btn">
                            <button href="" type="submit" class="btn btn-primary btn-form display-4">DONE</button>
                        </span>
                    </form>
            </div>
            
        </div>
    </section>


      <script src="''' + AWS_UI_LINK + '''assets/web/assets/jquery/jquery.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/tether/tether.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/bootstrap/js/bootstrap.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/smooth-scroll/smooth-scroll.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/dropdown/js/script.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/touch-swipe/jquery.touch-swipe.min.js"></script>
      <script src="''' + AWS_UI_LINK + '''assets/theme/js/script.js"></script>

    </body>
    </html>
    '''
    except Exception as ex:
        print(ex)
        traceback.print_exc()
        
@app.route('/signUp',methods=['POST'])              #SIGNUP METHOD
def signUp():

    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        json.dumps({'html':'<span>All fields good !!</span>'})
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser',(_name,_email,_password))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'message':'User created successfully !'})
        else:
            return json.dumps({'error':str(data[0])})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/listings',methods = ['POST','GET'])
def listings():

    titles = ['Hyundai for sale','Bike for Sale','Samsung Mobile for sale']
    cost = ['200000','30000','4000']
    id_of_item = ['1','2','3','4']
    desc = ["asdaasdasdasdsdf asd fasdf asdf asd fasd fads f","asdaasdasdasdsdf asd fasdf asdf asd fasd fads f","asdaasdasdasdsdf asd fasdf asdf asd fasd fads f"]
    LIST = ""
    for i in range(0,len(titles)):
        LIST += """
<div class="row timeline-element reverse separline">
     <div class="timeline-date-panel col-xs-12 col-md-6  align-left">
        <div class="time-line-date-content">

        </div>
    </div>
<span class="iconBackground"></span>
<div class="col-xs-12 col-md-6 align-right">
    <div class="timeline-text-content">
        <h3>""" + titles[i] + """</h3><br>        
        <h4></h4>
        <h5>₹""" + str(cost[i]) + """ per month</h5><br>
        <h4>Description</h4>
        <h4>""" + desc[i] + """</h4>
        <form method = "POST" action='""" + SITE + """/apply?id=""" + id_of_item[i] + """'>
                

                <center><button type="submit" class="btn btn-primary display-4">ONE CLICK APPLY</button></center>
        </form>
     </div>
</div>
</div>
"""

           
    return '''
<!DOCTYPE html>
<html>
<head>
  <!-- Site made with Mobirise Website Builder v4.0.17, https://mobirise.com -->
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v4.0.17, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" href="assets/images/logo21.png" type="image/x-icon">
  <meta name="description" content="Website Builder Description">
  <title>Jobslist</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Rubik:300,300i,400,400i,500,500i,700,700i,900,900i">
  <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/web/assets/mobirise-icons/mobirise-icons.css">
  <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/tether/tether.min.css">
  <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/dropdown/css/style.css">
  <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/theme/css/style.css">
  <link rel="stylesheet" href="''' + AWS_UI_LINK + '''assets/mobirise/css/mbr-additional.css" type="text/css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
 <!-- SELECTIZE BEGINS -->

  <link rel="stylesheet" href="https://s3.ap-south-1.amazonaws.com/onecall-ui-assets/Selectize/normalize.css">
  <link rel="stylesheet" href="https://s3.ap-south-1.amazonaws.com/onecall-ui-assets/Selectize/selectize.css">
  <!--[if IE 8]><script src="js/es5.js"></script><![endif]-->
  <script src="https://s3.ap-south-1.amazonaws.com/onecall-ui-assets/Selectize/selectize.min.js"></script>
  <script src="https://s3.ap-south-1.amazonaws.com/onecall-ui-assets/Selectize/index.js"></script>

  <!-- SELECTIZE ENDS -->

  <script src="https://apis.google.com/js/client.js"></script>




</head>
<body>

<section class="engine"><a href="https://mobirise.co/j">how to design a website for free</a></section><section class="mbr-section form3 cid-qqpC9TCU8J" id="form3-1" data-rv-view="1395">





    <div class="container">
        <div class="media-container-column title col-12 col-lg-8 offset-lg-2">
            <h2 class="align-center pb-2 mbr-fonts-style display-2">Find your listings now!</h2>
            <h3 class="mbr-section-subtitle align-center pb-5 mbr-light mbr-fonts-style display-5">Find over 10,000 listings on our website. Find jobs, properties on rent, cars and more!
            </h3>
        </div>

        
    </div>
</section>
</div>

<section class="menu cid-qqpBmXmdnM" once="menu" id="menu2-0" data-rv-view="1393">



    <nav class="navbar navbar-dropdown align-items-center navbar-fixed-top navbar-toggleable-sm">
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </button>
        <div class="menu-logo">
            <div class="navbar-brand">

                <span class="navbar-caption-wrap">
                    <a class="navbar-caption text-white display-4" href="https://mobirise.com">ONECALL JOBS</a>
                </span>
            </div>
        </div>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true">
                <li class="nav-item">
                    <a class="nav-link link text-white display-4" href="''' + SITE + '''/post">
                        Post For Free
                    </a>
                </li>
                
            </ul>

        </div>
    </nav>
</section>


<section class="timeline1 cid-qqpDdMihQ2" id="timeline1-3" data-rv-view="1398" style = "background-color:#e2e2e2;">





    <div class="container align-center">
        <h2 class="mbr-section-title pb-3 mbr-fonts-style display-2">
            Apply to any job you want</h2>


        <div class="container timelines-container" mbri-timelines="">

''' + LIST + '''

        </div>
    </div>
</section>


  <script src="''' + AWS_UI_LINK + '''assets/web/assets/jquery/jquery.min.js"></script>
  <script src="''' + AWS_UI_LINK + '''assets/tether/tether.min.js"></script>
  <script src="''' + AWS_UI_LINK + '''assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="''' + AWS_UI_LINK + '''assets/smooth-scroll/smooth-scroll.js"></script>
  <script src="''' + AWS_UI_LINK + '''assets/dropdown/js/script.min.js"></script>
  <script src="''' + AWS_UI_LINK + '''assets/touch-swipe/jquery.touch-swipe.min.js"></script>
  <script src="''' + AWS_UI_LINK + '''assets/theme/js/script.js"></script>
  <script src="''' + AWS_UI_LINK + '''assets/formoid/formoid.min.js"></script>


</body>
</html>
'''
        


if __name__ == "__main__":
    app.run()
