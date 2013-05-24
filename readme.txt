C:\Server\Apache2.2\conf\httpd.conf

LoadModule wsgi_module modules/mod_wsgi.so
WSGIScriptAlias / "C:\Server\Apache2.2\htdocs\weixin\weixin.wsgi"

#解析目录用的Apache配置文件部分 与 weixin.wsgi 配合使用