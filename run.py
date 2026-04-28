#!/usr/bin/env python3
import Code_Cyber
import sys

if __name__ == "__main__":
    try:
        Code_Cyber.main()
    except KeyboardInterrupt:
        Code_Cyber.stop_event.set()
        print(f"\n{Code_Cyber.RED}Turbo Engine Shutdown...{Code_Cyber.RESET}")
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        sys.exit(1)
