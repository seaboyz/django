from django.shortcuts import render
from django.http import HttpResponse


def home(_request):
    return HttpResponse("""
        <h1>Blog Home Page<h1>
    """)


def about(_request):
    return HttpResponse("""
        <h1>About Page</h1>
    """)
