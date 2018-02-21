hellodcc
========

a project for cookiecutter


:License: BSD


Basic Commands
--------------

* To start the api server, use this command::

    $ sudo docker-compose -f local.yml up

and curl the url with command::

    $ curl -i  "http://127.0.0.1:8000/api/v1/echo?hello=www"


Running tests,first time run the test will take a while because this build the environment,and test script located at api/tests.py::

  $ sudo docker-compose -f local.yml run django python manage.py test api
