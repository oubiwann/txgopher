~~~~~~~~
txGopher
~~~~~~~~

An async (Twisted) implementation of gopher

Usage
=====

Running the Client
------------------

TBD

Running the Server
------------------

There are two ways to run the server. You can use the ``twistd`` plugin::

  $ sudo twistd -n gopher


Or you can do it the "old-fashioned" way, and use the ``.tac`` file::

  $ sudo twistd -ny ./bin/txGopherServer.tac

If you'd like to daemonize, simply leave off the ``-n``.

If you would like to run the gopher server on a non-privileged port and not run
as root, you can pass the port parameter::

  $ twistd -n gopher server --port 1070

Or::

  $ twistd -ny ./bin/txGopherServer.tac gopher server --port 1070
