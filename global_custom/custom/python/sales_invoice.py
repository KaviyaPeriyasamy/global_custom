from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
import frappe

def make_custom_fields(update=True):
    custom_fields = {
        "Sales Invoice": [
            {
                "fieldname": "si_itemwise_rate_details",
                "label": "Itemwise Rate Details",
                "fieldtype": "Table",
                "options": "Sales Invoice Itemwise Rate Details",
                "insert_after": "items",
                "read_only": 1,
                "depends_on": "eval: doc.docstatus == 0",
            }
        ]
    }
    create_custom_fields(
        custom_fields, ignore_validate=frappe.flags.in_patch, update=update
    )

@frappe.whitelist()
def fetch_rate_details(item_code):
    doc_count = 0
    rate_details = []
    po_details = frappe.get_all('Sales Invoice Item',['rate','parent'],{'item_code':item_code,'parenttype':'Sales Invoice'},order_by="modified")
    for row in po_details[::-1]:
        if frappe.db.get_value('Sales Invoice', row.parent,'docstatus') == 1:
            po_doc = frappe.get_doc('Sales Invoice', row.parent)
            rate_details.append(
                {
                'sales_invoice': row.parent,
                'date': po_doc.posting_date,
                'customer': po_doc.customer, 
                'rate': row.rate}
            )
            doc_count += 1
        if doc_count == 5:
            break
    return rate_details