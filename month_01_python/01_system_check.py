import platform
import sys
import os

def run_sre_system_check() -> None:
    print("\n" + "=" * 45)
    print(" SRE CODESPACE ENVIRONMENT CHECK")
    print("=" * 45)

    # Python Runtime
    print(f" Python Version : {sys.version.split()[0]}")

    # OS $ Host Information
    print(f" Operating System: {platform.system()} ({platform.release()})")
    print(f" Architecture    : {platform.machine()}")

    # Environment Detection
    is_codespace = os.environ.get("CODESPACES") == "true"
    env_type = "GitHub Codespace (Cloud Container)" if is_codespace else "Local Machine"
    print(f" Environment     : {env_type}")

    print("=" * 45)
    print(" Status: Portable SRE Sandbox is Fullly Operational")
    print("=" * 45 + "\n")

if __name__ == "__main__":
    run_sre_system_check()