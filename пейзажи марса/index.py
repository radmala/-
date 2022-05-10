from flask import Flask, url_for

app = Flask(__name__)


@app.route("/carousel")
def image_mars():
    return f"""
        <!doctype html>
        <html lang="ru">
          <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
             rel="stylesheet"
             integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
             crossorigin="anonymous">
             
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
                    integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
                    crossorigin="anonymous"></script>
                    
            <title>Привет, Марс!</title>
          </head>
          <body>
            <h1>Пейзажи Марса</h1>
            <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="{url_for('static', filename='img/mars1.jpg')}" class="d-block w-60" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="{url_for('static', filename='img/mars2.jpg')}" class="d-block w-60" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="{url_for('static', filename='img/mars3.jpg')}" class="d-block w-60" alt="...">
                </div>
              </div>
              <button class="carousel-control-prev btn-primary" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next btn-primary" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
            </div>
          </body>
        </html>
    """


if __name__ == "__main__":
    app.run()
