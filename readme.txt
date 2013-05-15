C:\Server\Apache2.2\conf\httpd.conf

LoadModule wsgi_module modules/mod_wsgi.so
WSGIScriptAlias / "C:\Server\Apache2.2\htdocs\weixin\weixin.wsgi"

<Directory "C:\Server\Apache2.2\htdocs\weixin">
    Order Deny,Allow
    Allow from all
</Directory>

Alias /admin_media "C:\Server\Django-1.0.4\django\contrib\admin\media"
<Directory "C:\Server\Django-1.0.4\django\contrib\admin\media">
    AllowOverride None
    Options None
    Order allow,deny
    Allow from all
</Directory>

<Location "/media/">
    SetHandler None
</Location>

<LocationMatch "\.(jpg|gif|png|txt|ico|pdf|css|jpeg)$">
    SetHandler None
</LocationMatch>