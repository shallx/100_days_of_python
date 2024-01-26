import gspread
SHEET_TITLE = "Flight Deals"
class DataManager:
    def __init__(self):
        self.client = gspread.service_account(filename="credentials.json")
        
        self.wb_1 = self.client.open(SHEET_TITLE)
        self.worksheet = self.wb_1.get_worksheet(0)
    
    def update(self,range, value):
        print(range)
        print(value)
        cell_list = self.worksheet.range(range)
        for i, val in enumerate(value):
            cell_list[i].value = val
        self.worksheet.update_cells(cell_list)
        
    def get_cities(self):
        self.records = self.worksheet.get_records()
        return self.records
        