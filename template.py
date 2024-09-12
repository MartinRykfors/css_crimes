import random
from airium import Airium
import lib.cohost as cohost


def body(a):
    description = """Description"""
    cohost.with_description(a, content, description, "crime")
    a("")
    a("---")
    a("")
    a("A read more text")

def content(a):
    a('hello')


cohost.create_document(body, "post.html")
