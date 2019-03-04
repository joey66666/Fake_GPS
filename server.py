# -*- coding: utf-8 -*-
#! /usr/bin/env python
#
# @Author: z.Joey
# @Date: 2019-03-04 10:48:05
# @Last Modified by:   z.Joey
# @Last Modified time: 2019-03-04 10:48:05

import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print("from conn:", self.request)


s1 = socketserver.ThreadingTCPServer(("127.0.0.1", 9999), MyServer)
s1.serve_forever()
