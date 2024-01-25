import gspread
SHEET_TITLE = "Flight Deals"
class DataManager:
    def __init__(self):
        self.client = gspread.service_account(filename="credentials.json")
        
        self.wb_1 = self.client.open(SHEET_TITLE)
        self.worksheet = self.wb_1.get_worksheet(0)
        # self.worksheet.update('A11', [[1, 2], [3, 4]])
    
    def update(self,range, value):
        cell_list = self.worksheet.range(range)
        for cell in cell_list:
            cell.value = "Rahi"
        self.worksheet.update_cells(cell_list)
        