import datetime
import random

def generate_dynamic_stats():
    # List of status messages that alternate randomly
    statuses = [
        "Network Status: Fully Operational 🟢",
        "System Check: 100% stable ⚡",
        "Active routing nodes: Online 🌐",
        "Database synchronization: Complete ✅"
    ]
    
    current_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    random_status = random.choice(statuses)
    
    stats_block = f"""
> **Last Automated Update:** `{current_time}`
> 
> `{random_status}`
> 
> *Looking for automated networking? Check out our featured bot link above!*
"""
    return stats_block

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- START_STATS -->"
    end_marker = "<!-- END_STATS -->"
    
    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        
        dynamic_content = generate_dynamic_stats()
        
        new_content = f"{before}{start_marker}{dynamic_content}{end_marker}{after}"
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README updated successfully.")
    else:
        print("Markers not found in README.md")

if __name__ == "__main__":
    update_readme()
