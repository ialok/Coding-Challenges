
Usage:
  Daemon: python MonitorService.py  >/dev/null 2>&1 < /dev/null &
  Foreground: python MonitorService.py

1. Logs in the localdirectory as 'monitor.log'
2. Does not handle HUP/TERM etc. Uknown behavior on interrupts
3. Log lines shows the status only and not error message
