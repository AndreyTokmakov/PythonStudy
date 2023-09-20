from fastapi import FastAPI
import uvicorn

api_server = FastAPI()


@api_server.get("/")
def hello():
    return {"Hello": "World"}


@api_server.get("/greeting")
def greeting(name: str = "Jonh"):
    return {"message": f"Hello {name}"}


@api_server.post("/store_some_data")
def handle_post_request(key: str,
                        value: str):
    return {"key": key, "value": value}


if __name__ == '__main__':
    uvicorn.run(api_server, host="0.0.0.0", port=52525, log_level="debug")

# Открыть главную страничку (root)
#
#   http://localhost:52525/    -> будет вызван метод hello()
#
# Открыть страничку Swagger-a:
#
#   http://localhost:52525/docs
