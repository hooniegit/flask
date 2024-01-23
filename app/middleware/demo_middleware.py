
class DemoMiddleware:
    def __init__(self, app):
        self.app = app
        
    def __call__(self, environ, start_response):
        print("There must be some logics in here..")
        # return self.app(environ, start_response)
        return self.internal_error(environ=environ, start_response=start_response)
    
    def internal_error(self, environ, start_response):
        try:
            response = self.app(environ, start_response)
            return response
        except Exception as E:
            print(f"Oops.. Here is some errors, {E}")
