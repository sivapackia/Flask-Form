from flask import Flask,render_template,url_for,redirect,request,session,flash
App=Flask(__name__)
App.secret_key="R.Sivapackia"
bike=[
            {
            "image":"https://etimg.etb2bimg.com/photo/63534904.cms",
            "name":"Tvs Xl 100",
            "Millege":"40",
            "rate":"80000"
            },
    
            {
             "image":"https://i0.wp.com/gomechanic.in/blog/wp-content/uploads/2020/02/KTM-Duke-200-BS6.jpg?resize=1000%2C750&ssl=1",
            "name":"Tvs Jam",
            "rate":"50000",
            "Millege":"35"
            },
    
            {
             "image":"https://imgd.aeplcdn.com/272x153/n/cw/ec/145595/sportster-s-right-side-view.jpeg?isig=0&q=75",
             "name":"Tvs Heavy Duty",
             "rate":"75000",
            "Millege":"40"
            },
    
            {
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR-L-UH1AZA_q__rIbzgXHqqY2KhYCWYgYdg&usqp=CAU",
            "name":"Tvs Nest",
            "rate":"95000",
            "Millege":"50"
            },
    
            {
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs4LqZRd-lXTkfjmKdNxbOli7jPyJ4k97V6w&usqp=CAU",
             "name":"Tvs Start City",
             "rate":"85000",
            "Millege":"70"
            },
    
            {
            "image":"https://static.autox.com/uploads/bikes/2022/06/kawasaki-ninja-400.jpg",
            "name":"Tvs  Pept",
            "rate":"80000",
            "Millege":"45"
            }
        ]
@App.route("/Navbar")
def Navbar():
    return render_template("index.html")

@App.route("/",methods=["GET","POST"])
def Home():
    Email="kannan2001@gamil.com"
    Password="1234"
    if request.method == "POST":
        email=request.form.get("email")
        password=request.form.get("password")
        if email == Email and Password == password :
        #    flash("Login Success","Fully")
           session['Email']=Email
           return redirect(url_for("Bike"))
    return render_template("home.html")
    
@App.route("/login",methods=["GET","POST"])
def Login():
    if request.method == "POST":
        email=request.form.get("email")
        password=request.form.get("password")
    return render_template("login.html")

@App.route("/logout")
def Logout():
    session.pop('Email',None)
    return redirect(url_for("Home"))

@App.route("/bike")
def Bike():
    return render_template("bike.html",data=bike)

@App.route("/delete/<int:index>")
def Delete(index):
    bike.pop(int(index-1))
    return render_template("bike.html",data=bike)

@App.route("/edit/<int:index>",methods=["GET","POST"])
def Edit(index):
    if request.method == "POST":
        Millege=request.form.get("millege")
        amount=request.form.get("amount")
        bike_edit=bike[int(index-1)]
        bike_edit.update({"Millege":Millege})
        bike_edit.update({"rate":amount})
        return redirect(url_for("Bike"))
    bike_update=bike[int(index-1)]
    return render_template("edit.html",data=bike_update)
if __name__ == "__main__":
    App.run(debug=True)