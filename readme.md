# Fancontrol Control
A set of utilities and scripts that are useful to force fancontrol to work in
an intuitive way.

## Warning
As with any script that sets the speeds of the fans in your computer directly,
please read through the scripts and be wary to not fry everything!

## Features
- Regenerate /etc/fancontrol based on a template file at each boot.
- Restart the fancontrol daemon on wake.

### Regeneration
0. Generate a fancontrol file like you normally would with 
1. Install fancontrolcontrol.py to /opt/fancontrolcontrol
2. Copy the generated /etc/fancontrol to /opt/fancontrolcontrol with the name
   fancontrol.template
3. Install fancontrolcontrol.service to /lib/systemd/system
4. Reload your unit files with `#> systemctl daemon-reload`
5. Try out the service with `#> systemctl start fancontrolcontrol`
6. Inspect the generated file. If things look good, enable the service with
   `#> systemctl enable fancontrolcontrol`

### Restart on wake.
Copy lib/systemd/system-sleep/fancontrol_unsleeper to your
/lib/systemd/system-sleep directory to force fancontrol to restart every time
your computer wakes.

