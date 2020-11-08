"""
This class contains multiple processors related to requestor role. 
This contains mostly business logic to process the data and insert it 
to the database 
"""
class RequestorProcessor():
    # New reimbursement form submission will be processed here
    def submit_form(self, reimbursement_form):
        # Parse data 
        # Do some validation 
        # Save to database
        print(f"Processing {reimbursement_form}")
        pass