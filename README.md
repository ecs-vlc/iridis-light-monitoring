# slurm-monitoring
Monitoring GPU, RAM and CPU usage for slurm partitions and users.

This is an app written in Python using flask. It gathers information using the standard slurm functions (squeue, scontrol etc.)
The implementation assumes some fixed parameters such as maximum resource available to reduce  the number of requests sent to the slurm server.

To use it go to http://degas.ecs.soton.ac.uk:7777/ with your VPN activated.

In the case that resources can be locked by a user and not actually being used, this can be monitored too. This is when a job requests resources from a node containing GPUs, but does not actually use them.

![alt text](https://github.com/ecs-vlc/iridis-light-monitoring/blob/main/media/front-end-example-0.png)
![alt text](https://github.com/ecs-vlc/iridis-light-monitoring/blob/main/media/front-end-example-1.png)

Things to do in the future:
  0. Add the new nodes and partitions a100.
  1. Create a dummy user to connect to iridis5.
  2. Talk to isolutions to setup a DNS address, sth like: iridis-light-monitoring.ecs.soton.ac.uk
  3. Add more stuff and improve the code.
  4. Improve the interface. For example on mobile, it looks a bit weird.


If the app does not work:
  1. ssh into degas@soton.ac.uk
  2. Inspect the output: `journalctl -u iridis-light-monitoring.service --no-pager`
  3. Make the code changes needed.
  4. Restart the service : `sudo systemctl restart iridis-light-monitoring.service`

