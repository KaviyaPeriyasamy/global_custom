## Global Custom

Custom application

Enable Allow on submit for against_sales_invoice in delivery note item

Sales Invoice Dashboard Py File
``` 
'internal_links': {
			'Sales Order': ['items', 'sales_order'],
			'Delivery Note': ['items', 'delivery_note']
		},
```
Supplier Custom script
```
 let state=false;
frappe.ui.form.on('Supplier', {
	before_save:function(frm){
        if (frm.is_new()){
            state = true;
        }
	},
    after_save:function(frm){
	        if (state){
    	    frappe.db.insert({
        	 "doctype" :"Address",
        	 "address_title":frm.doc.supplier_name,
        	 "address_type":frm.doc.address_type,
        	 "address_line1":frm.doc.address_line_1,
        	 "address_line2":frm.doc.address_line_2,
        	 "city":frm.doc.city,
        	 "pincode":frm.doc.postal_code,
        	 "emirate":frm.doc.emitates,
        	 "country":frm.doc.country,
        	 'links':[{
            "link_doctype":'Supplier',
        	 "link_name":frm.doc.supplier_name
        	      	 }]
        	        
        	    }).then(vlt => {
        	        frappe.model.set_value(frm.doctype, frm.doc.name, 'Address', vlt);
        	        frappe.show_alert({
        	            message:__('Address {0} Created', [vlt.name]),
        	            indicator:'green'
        	        });
    	    });   
    	    }
	}
});

```
```
**Note

Dynalite
Add below line to setters in delivery_note_btn:  - Sales Invoice
posting_date: undefined
```
#### License

MIT
