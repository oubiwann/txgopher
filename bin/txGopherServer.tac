#!/usr/bin/env python2.7
from twisted.application import service

from txgopher.scripts import services


application = service.Application("txGopher Server")
serviceMaker = services.GopherServiceMaker()
gopherService = serviceMaker.makeService(serviceMaker.options())
gopherService.setServiceParent(application)
