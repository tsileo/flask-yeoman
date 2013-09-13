==============
 Flask-Yeoman
==============

A `Flask <http://flask.pocoo.org/>`_ blueprint to make create web application using `Yeoman <http://yeoman.io/>`_ and Flask an easy task.


Features
--------

* Automatically inject Flask config in index.html
* Support for development and production mode


Installation
------------

.. code-block:: console

    $ pip install flask-yeoman


Getting Started
---------------

Create a server.py file in at the root of your yeoman app:

.. code-block:: python

    from flask import Flask, jsonify
    from flask_yeoman import flask_yeoman

    app = Flask(__name__)
    app.register_blueprint(flask_yeoman)

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)

You can start working on your app as usual, and since it automatically injects Flask ``config``` allowing you to easily share configuration between Flask and your Backbone app (using the ``tojson`` jinja helper):

.. code-block:: html

    <script>
    window.myapp.config = {myvar: {{ config.MYVAR|tojson }},
                           myvar2: {{ config.MYVAR2|tojson }}};
    </script>

Grunt configuration
~~~~~~~~~~~~~~~~~~~

In order to use your own server with Yeoman, you must create a new task in your Gruntfile.js file:

.. code-block:: javascript

    // New task for flask server
    grunt.registerTask('flask', 'Run flask server.', function() {
       var spawn = require('child_process').spawn;
       grunt.log.writeln('Starting Flask development server.');
       // stdio: 'inherit' let us see flask output in grunt
       process.env.FLASK_YEOMAN_DEBUG = 1;
       var PIPE = {stdio: 'inherit'};
       spawn('python', ['server.py'], PIPE);
    });

And replace the ``connect:reload`` task by ``flask`` in the server task:

.. code-block:: javascript

    grunt.registerTask('server', function (target) {
        if (target === 'dist') {
            return grunt.task.run(['build', 'open', 'connect:dist:keepalive']);
        } else if (target === 'test') {
            return grunt.task.run([
                'clean:server',
                'coffee',
                'createDefaultTemplate',
                'jst',
                'compass:server',
                'connect:test:keepalive'
            ]);
        }

        grunt.task.run([
            'clean:server',
            'coffee:dist',
            'createDefaultTemplate',
            'jst',
            'compass:server',
            'flask',
            'open',
            'watch'
        ]);
    });


Livereload support
~~~~~~~~~~~~~~~~~~

And for the livereload support, add this snippet before the closing body in your index.html file:

.. code-block:: html

    {% if config.FLASK_YEOMAN_DEBUG %}
    <!-- livereload script -->
    <script>document.write('<script src="http://'
    + (location.host || 'localhost').split(':')[0]
    + ':35729/livereload.js?snipver=1" type="text/javascript"><\/script>')
    </script>
    {% endif %}


License (MIT)
-------------

Copyright (c) 2013 Thomas Sileo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
