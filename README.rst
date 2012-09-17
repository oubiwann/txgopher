~~~~~~~~
txgopher
~~~~~~~~

An async (Twisted) implementation of gopher

Usage
=====

Running the Client
------------------

TBD

Running the Server
------------------

There are two ways to run the server. You can use the "old-fashined" way, and
call the ``.tac`` file::

  $ sudo twistd -ny ./bin/txGopherServer.tac

Or you can use the ``twistd`` plugin::

  $ sudo twistd -n gopher
