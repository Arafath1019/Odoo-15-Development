## Odoo-Installation-with-Docker

### Steps
1. Clone: `git clone https://github.com/Arafath1019/Odoo-15-Development.git`
2. Run: `docker-compose up`
3. Browse: http://localhost:8069

### Demo Data 
1. Master Password: admin1234
2. Database Name: odoo15
3. Email: odoo15@gmail.com 
4. Password: odoo15
5. Country: Bangladesh
6. Demo Data: Click Checkbox
7. Create Database and login

### Steps for Generating a Odoo module using Scaffold
1. Navigate to Odoo source directory from terminal
2. Run this command: `./odoo-bin scaffold custom_addon_name custom_addon_path` <br />
For example: `./odoo-bin scaffold om_odoo_inheritance /home/dev/odoo/15.0/custom_addons`

### Run Odoo From Terminal
Run the command from terminal `python_path odoo_bin_path -c odoo_conf_path`
<br />
OR <br />
`python_path odoo_bin_path --addons=all_addons_path -r odoo -w odoo --db_host=localhost --db_port=5432 -p 8069`

### Generate Odoo configuration file from terminal
Run the command from terminal `python_path odoo_bin_path --addons=all_addons_path -r odoo -w odoo --db_host=localhost --db_port=5432 -p 8069 --stop-after-init -s -c odoo_conf_new_path`

### Install Module From Terminal
Run the command from terminal `python_path odoo_bin_path -c odoo_conf_path -d db_name -i module_name`

### Error no 98 Address Already use Issue
1. List of all running processes `ps aux||grep odoo`<br />
2. Kill a process `sudo kill -9 process_id`

### Update a module from odoo cli
Run the command from CLI `python_path odoo_bin_path -c odoo_conf_path -d db_name -u module_name`

### Create database from terminal
Run the command from cli `python_path odoo_bin_path -c odoo_conf_path -d db_name`