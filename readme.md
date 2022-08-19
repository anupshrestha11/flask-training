## Halo Automation
### BDD tests for Halo Device APIs
Framework Used: Behave


Steps to run the tests:
1. Pull the latest Master branch
2. Run the command `pipenv install` to create an environment and  install dependencies
3. Run the command `pipenv shell` to activate the environment
4. Use the command ```behave ./e2e/api/features -D halo_ip=<ip> -D halo_user_password=<pswd>```

Required arguments:
1. Halo IP Address <br>
   ```-D halo_ip=<ip>```
2. Halo User Password <br>
   ```-D halo_user_password=<pswd>```

Optional Arguments:
1. ```-no-firmware-update``` <br>
   To skip firmware upgrade tests [ Use this if you have Halo connected via cellular ]
2. ```-D skip_recording_backup_reboot_scenario``` <br>
   To skip rf recording backup on reboot scenario
3. ```-D skip_long_recording_backup_scenario```<br>
   To skip 30 minutes long rf recording backup scenario

#### Requisites that might fail the tests if not fulfilled
1. Use `eth0` for the connection as `eth1` is used during the tests. <br>
   `eth0` requires following static settings: <br>
   ```
   gateway: 0.0.0.0,
   ip: 20.0.0.2,
   subnet: 255.255.255.0,
   used_for_data: false,
   dns: '' 
   ```

2. Never use `eth0` for any kind of test throughout the scenarios.

3. Have `eth1` connected with a DHCP server <br>
   Effect: `eth1` doesn't get IP assigned and the test fails. <br>
   Failing Scenario: `root user updates ethernet settings as dhcp client`

4. Have a modem that supports the tech limitations \[2G, 3G, LTE] on ttyACM0 to test tech_limitations \[Cellular] <br>
   Failing Scenario: `admin user is able to update the cellular nic technology`
