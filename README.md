requestdriver
=============

[![Build Status](https://travis-ci.org/Shapeways/requestdriver.svg?branch=master)](https://travis-ci.org/Shapeways/requestdriver)

Python requests wrapper for making session-based requests and some extra sprinkling of love.

Instantiating a new RequestDriver will store a session on the instance and use that session to make all requests, the
advantage being that cookies will persist across requests without having to pass them into each request.

For instance, you can make a login request:
> rd = requestdriver.RequestDriver()
> rd.request('http://mysite.com/login', method=rd.POST, data={'username': 'smitty', 'password': 'werbenjagermanjensen'})

And all subsequent requests will be made as that logged-in user (assuming your site uses cookies-based authentication)
> rd.request('http://mysite.com/new-post, method=rd.POST, data={'body': 'He was number 1'})

Since requestdriver will save all responses, so you can do things like:

> rd.save_last_response_to_file('/temp/response.html')
