## Odoo-Installation-with-Docker

### Steps
1. Clone: `git clone https://github.com/Arafath1019/Odoo-15-Development.git`
2. Run: `docker-compose up`
3. Browse: http://localhost:8069

### Steps for Generating a Odoo module using Scaffold
1. Navigate to Odoo source directory from terminal
2. Run this command: `./odoo-bin scaffold custom_addon_name custom_addon_path` <br />
For example: `./odoo-bin scaffold om_odoo_inheritance /home/dev/odoo/15.0/custom_addons`

### Run Odoo From Terminal
Run the command from terminal `python_path odoo_bin_path -c odoo_conf_path`