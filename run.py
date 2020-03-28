from flaskblog import create_app

# If we want to use config class that we pass by default then we dont have to
# pass any config parameter to create_app() function but if want to use
# different config then we should pass it as a parameter to the create_app()
# function

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
