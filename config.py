 #!/usr/bin/env python
 #conding:utf-8


settings= {
     "cookie_secret": "bZJc2sWbQLKos6GkHn/VB4oXwQt2S0R0kRvJ5/xJ89E=",
     "xsrf_cookies": True,
     "login_url": "/login"
}


# from urls import app 要在 settings 下边引用
from urls import app
port = 8080
app.listen(port)
