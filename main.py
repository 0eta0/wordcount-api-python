# -*- coding:utf-8 *-
import falcon
import json
from mainfunc import MainFunc

class CORSMiddleware:
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')

class Root(object):
    def on_get(self, req, resp):
        resp.body = "Hello!"
        resp.status = falcon.HTTP_200

class WordCount(object):
    def on_post(self, req, resp):
        reqBody = respBody = ""
        try:
            reqBody = json.loads(req.stream.read().decode('utf-8'))
            langResult = MainFunc.DetectFunc(reqBody["words"])
            respBody = {"status":"success","lang":langResult,"length":MainFunc.WordCounter(langResult,reqBody["words"])}
        except:
            respBody = {"status":"failure"}

        resp.body = json.dumps(respBody, indent=2)
        resp.status = falcon.HTTP_200

class LangDetect(object):
    def on_post(self, req, resp):
        reqBody = respBody = ""
        try:
            reqBody = json.loads(req.stream.read().decode('utf-8'))
            langResult = MainFunc.DetectFunc(reqBody["words"])
            respBody = {"status":"success","lang":langResult}
        except:
            respBody = {"status":"failure"}

        resp.body = json.dumps(respBody, indent=2)
        resp.status = falcon.HTTP_200

api = falcon.API(middleware=[CORSMiddleware()])
api.add_route("/", Root())
api.add_route("/api/langdetect", LangDetect())
api.add_route("/api/wordcount", WordCount())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("0.0.0.0", 8080, api)
    httpd.serve_forever()
