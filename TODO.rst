Spec Implementation / Bug Fixes
-------------------------------

 * add support for error pages and parsing them effectively

 * add more tests in test_protocol


Featues
-------

 * Write a getPage utility.

 * Write a gopher spider... or tunneler... or burrower.

 * Full text search on a gopher server with Solr?

 * MongoDB and full text search in a gopher server?

 * Serving JSON... the overhead on the gopher server is so low, it'd be ideal...

 * Read remote gopher files... get a file handle, read data, etc.

 * Create the server

   - add support for serving a static directory

   - add mimetypes <-> gopher type id support

   - support gophermap files and .cache files

   - add an "About this gopher server" menu item to every top-level page

     . include the list of supported mimetypes

     . include the list of supported gopher types
