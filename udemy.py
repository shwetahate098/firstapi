from flask import Flask, jsonify,request
import json
import requests
app = Flask(__name__)





# stores = [
#     {
#         "name": "My Store",
#         "items": [
#             {
#                 "name": "Chair",
#                 "price": 15.99
#             }
#         ]
#     },
#     {
#         "name": "My 2nd Store",
#         "items": [
#             {
#                 "name": "Chair",
#                 "price": 15.99
#             }
#         ]
#     }
# ]


# @app.get("/store")
# def get_stores():
#     return jsonify({"stores": stores})

# @app.post("/store")
# def create_store():
#     request_data = request.get_json()
#     new_store = {"name": request_data["name"], "items": []}
#     stores.append(new_store)
#     return new_store, 201

# @app.post("/store/<string:name>/item")
# def create_item(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store["name"] == name:
#             new_item = {"name": request_data["name"], "price": request_data["price"]}
#             store["items"].append(new_item)
#             return new_item
#     return {"message": "Store not found"}, 404

# @app.get("/store/<string:name>")
# def get_store(name):
#     for store in stores:
#         if store["name"] == name:
#             return store
#     return {"message": "Store not found"}, 404


# @app.get("/store/<string:name>/item")
# def get_item_in_store(name):
#     for store in stores:
#         if store["name"] == name:
#             return {"items": store["items"]}
#     return {"message": "Store not found"}, 404

#acc={
  #  "nameu": "ankita",
   # "address": "Mumbai",
   # "email": "ankita@gmail.com",
#}


# @app.get("/acc")
# def get_acc():
#     user_agent = request.headers.get('User-Agent')
#     return jsonify({"acc": acc, "user_agent": user_agent})
                                                                                  

@app.post("/acc")
def create_acc():
    user_agent = request.headers.get('User-Agent')
    request_data=request.get_json()
    
    response = requests.post("http://localhost:5001/bbc", json=request_data)
    # print(response.text)
    return "acc"
   # if "phone" in request_data and "price" in request_data:
        #acc["phone"] = request_data["phone"]
        #acc["price"] = request_data["price"]
        #return jsonify({"acc":acc, "user_agent": user_agent}), 201
    #else:
        #return jsonify({"error": "phone number is missing"})

    #if "price" in request_data:
       # acc["price"]=request_data["price"]

        #return jsonify({"acc":acc}), 201
   # else:
        #return jsonify({"error": "price number is missing"})





if __name__ == '__main__':
    app.run(debug=True)