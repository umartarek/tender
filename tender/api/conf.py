import frappe
from frappe import _
@frappe.whitelist(allow_guest=True)
def ping():
    return "hello world nas"



@frappe.whitelist(allow_guest=True)
def get_daily_work(filters=None):
    """
    Fetch data from the Daily Work DocType based on filters.
    :param filters: JSON string containing filter conditions (optional)
    :return: List of matching Daily Work records
    """
    try:
        filters = frappe.parse_json(filters) if filters else {}
        daily_work_data = frappe.get_all(
            "Daily Work", 
            filters=filters,
            fields=["name", "title", "status", "assigned_to", "date"]
        )
        return daily_work_data
    except Exception as e:
        frappe.log_error(message=frappe.get_traceback(), title="Error in get_daily_work")
        return {"error": _("An error occurred while fetching Daily Work data: {0}").format(e)}
