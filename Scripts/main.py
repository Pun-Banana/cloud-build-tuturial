import functions_framework

@functions_framework.http
def process_data(request):
    """HTTP Cloud Function."""
    if request.method == 'GET':
        request_json = request.get_json(silent=True)
        
        if not request_json or 'business_unit' not in request_json or 'year' not in request_json:
            return 'Missing parameters: "business_unit" and "year" are required.', 400

        bu = request_json['business_unit']
        year = request_json['year']
        
        start_date = f"{year}-01-01"
        end_date = f"{year}-12-31"
        
        print(f"Starting job -> Business Unit: {bu} | Date Range: {start_date} to {end_date}")
        
        # TODO: Add your core processing logic here (e.g., BigQuery, pandas, etc.)
        
        return {
            "status": "success",
            "business_unit": bu,
            "year": year,
            "message": f"Successfully processed data from {start_date} to {end_date}"
        }, 200
    else:
        return {
            "status": "error",
            "message": "method not allow"
        }, 400