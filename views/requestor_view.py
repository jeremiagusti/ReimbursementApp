from flask import render_template, request
from flask_classful import FlaskView, route
from libs.requestor_processor import RequestorProcessor

class RequestorView(FlaskView):
    """ Class that deals with views and other API endpoints for
    requestors"""
    def __init__(self):
        self.__TEMPLATE_DIR__ = "requestor"
        self.requestor_processor = RequestorProcessor()
        
    # Main page of the requestor
    @route("/")
    def index(self):
        return render_template(f"{self.__TEMPLATE_DIR__}/index.html")

    # Submit new reimbursement form
    @route("/new/", methods=["POST"])
    def submit_reimbursement(self):
        submitted_form = request.get_json()
        self.requestor_processor.submit_form(submitted_form)
        return "success", 200