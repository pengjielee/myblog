Using systemctl to manage services

systemctl is the command line tool you can use to control and manage services in systemd.

### 1. Listing Service Units and Unit files

To list all the units that are loaded
systemctl list-units

To list only units of type service
systemctl list-units -t service

To list all installed unit files of type service
systemctl list-unit-files -t service

To lists all services that are enabled
systemctl list-unit-files --state enabled


the difference between list-units and list-unit-files is that
list-unit will only show units that are loaded while 
list-unit-files shows all unit files that are installed on the system.

### 2. Start and Stop service
systemctl start service_name.service
systemctl stop service_name.service

### 3. Restart and Reload services

The restart option will restart a service that is running. If the service is not running, it will be started.
systemctl restart service_name.service

If you want to restart the service only if its running then use the try-restart option.
systemctl try-restart service_name.service

The reload option will try to reload the service specific configuration of a unit if it is supported.
systemctl reload service_name.service

### 4. Enable and Disable services
systemctl enable service_name.service
systemctl disable service_name.service

### 5. Reload Unit Files

Whenever you make any changes to the unit files you need to let systemd know by executing daemon-reload which reloads all unit files
systemctl daemon-reload

### 6. Modifying system services

The unit files that come with installed packages are stored in /usr/lib/systemd/system/.
The unit files in this directory should not be modified directly as the changes will be lost when if you update the package. 
The recommended method is to first copy the unit file to /etc/systemd/system/ and make the changes in that location. 
The unit files in /etc/systemd/system/ takes precedence over unit files in /usr/lib/systemd/system/ so the original unit file will be overridden.
