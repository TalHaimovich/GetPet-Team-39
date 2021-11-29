from GetPet import create_app
#this is the operating for the website

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)