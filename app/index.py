from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# JSON data with 100 students (Example)
students_data = [{"name":"ho8ePmxFs","marks":34},{"name":"UZfmiiFJ","marks":98},{"name":"iDM","marks":8},{"name":"tJXs","marks":33},{"name":"t5BhO","marks":99},{"name":"0Jkky1M","marks":53},{"name":"hQc63UWR8","marks":46},{"name":"Rgv6876piP","marks":70},{"name":"IJ","marks":7},{"name":"cFtAFg","marks":14},{"name":"3","marks":0},{"name":"l","marks":34},{"name":"na9r","marks":53},{"name":"G","marks":28},{"name":"5IQVXqZo","marks":38},{"name":"LJrpc","marks":14},{"name":"O928AJO7n","marks":83},{"name":"HsV1","marks":2},{"name":"b3w3gIzle","marks":86},{"name":"FSOla8","marks":24},{"name":"ChW","marks":33},{"name":"MGhTYYiSb","marks":2},{"name":"YaJceFvNfx","marks":97},{"name":"wBOX","marks":44},{"name":"Pdwz1","marks":20},{"name":"AvdGL","marks":24},{"name":"6AmvEwfK","marks":72},{"name":"YiFUiPKOcM","marks":6},{"name":"1vcbyn","marks":54},{"name":"iSAZliKHla","marks":1},{"name":"0XKLrzyuN","marks":84},{"name":"AXWXrJNQ4","marks":34},{"name":"g8Q","marks":67},{"name":"V","marks":33},{"name":"hfcL","marks":11},{"name":"90dGEn6l","marks":56},{"name":"Tna","marks":86},{"name":"idiP795bQ","marks":2},{"name":"6","marks":62},{"name":"Re","marks":47},{"name":"FhFbgYc","marks":74},{"name":"g4NYMG31","marks":60},{"name":"3PMeVCSoi","marks":74},{"name":"eo9lDbQN","marks":59},{"name":"5kJNg01wvL","marks":61},{"name":"B","marks":90},{"name":"DOYhW64","marks":4},{"name":"OGOo4FXj","marks":75},{"name":"rzutYo6VnM","marks":39},{"name":"RseuUP","marks":20},{"name":"Z","marks":22},{"name":"a0Qr","marks":16},{"name":"ZXzUR","marks":21},{"name":"TN","marks":28},{"name":"dl5","marks":94},{"name":"ULlOs9u","marks":94},{"name":"0Kxwv6","marks":81},{"name":"mBh1","marks":62},{"name":"GTz6","marks":77},{"name":"pyY","marks":57},{"name":"O","marks":43},{"name":"fR38puO","marks":72},{"name":"6jxsGjevJ","marks":29},{"name":"egBWDGXh","marks":35},{"name":"OvU0","marks":4},{"name":"645cUg","marks":65},{"name":"FBBjvbP","marks":65},{"name":"pqkEMXpF","marks":29},{"name":"cSMDB","marks":41},{"name":"u","marks":24},{"name":"TMzi","marks":76},{"name":"aJWmZE","marks":54},{"name":"qySZqHP0e","marks":68},{"name":"vByjQufe","marks":95},{"name":"DV","marks":10},{"name":"Ji6Uflo","marks":33},{"name":"o9s","marks":39},{"name":"JGNn","marks":33},{"name":"It","marks":66},{"name":"z9T1HLSwbI","marks":24},{"name":"w4","marks":1},{"name":"lG","marks":62},{"name":"oD","marks":4},{"name":"2Iiwo","marks":37},{"name":"Bg","marks":24},{"name":"YAIaNN","marks":54},{"name":"GRc0d","marks":93},{"name":"nAoQsMDj1","marks":66},{"name":"u556BFC","marks":93},{"name":"J","marks":1},{"name":"0Aybcrw","marks":11},{"name":"L","marks":18},{"name":"kpIs59MA","marks":51},{"name":"swlCJayF","marks":13},{"name":"HTNQ0bz","marks":11},{"name":"sva","marks":2},{"name":"uevGi","marks":2},{"name":"ONP","marks":85},{"name":"KBptT","marks":0},{"name":"Fw0jE","marks":1}]
@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    """
    Fetch marks of students by name.
    Example usage:
    - `/api?name=ho8ePmxFs` -> {"marks": [70]}
    - `/api?name=ho8ePmxFs&name=Zfmi` -> {"marks": [70, 55]}
    """
    if name:
        marks = [next((s["marks"] for s in students_data if s["name"] == n), None) for n in name]
        return {"marks": marks}
    return {"marks": []}
