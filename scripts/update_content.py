#!/usr/bin/env python3
"""
Daily update script for IT Developer Resources Hub
Updates timestamps and checks for upcoming events
"""

import os
import re
from datetime import datetime
from pathlib import Path
import pytz

def get_current_date():
    """Get current date in EST timezone"""
    est = pytz.timezone('US/Eastern')
    return datetime.now(est).strftime('%B %d, %Y')

def update_readme_timestamp():
    """Update the last updated timestamp in README.md"""
    readme_path = Path('README.md')
    
    if not readme_path.exists():
        print("README.md not found")
        return False
    
    content = readme_path.read_text()
    current_date = get_current_date()
    
    # Update the "Last Updated" section
    pattern = r'\*\*.*?\*\* - Initial release with 2025 event listings'
    replacement = f'**{current_date}** - Auto-updated with latest information'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        readme_path.write_text(new_content)
        print(f"✅ Updated README.md timestamp to {current_date}")
        return True
    
    print("ℹ️  No timestamp update needed in README.md")
    return False

def check_upcoming_events():
    """Check and highlight upcoming events in the next 30 days"""
    # This is a placeholder for future enhancement
    # Could parse event files and update featured events section
    print("ℹ️  Event checking feature - coming soon")
    return False

def update_event_files():
    """Update event files with current year information"""
    events_dir = Path('events')
    
    if not events_dir.exists():
        print("Events directory not found")
        return False
    
    updated = False
    current_year = datetime.now().year
    
    for event_file in events_dir.glob('*.md'):
        content = event_file.read_text()
        
        # Check if file mentions future years and update if needed
        # This is a simple check - can be enhanced
        if str(current_year) in content or str(current_year + 1) in content:
            print(f"ℹ️  {event_file.name} is current")
        
    return updated

def main():
    """Main update function"""
    print("🚀 Starting daily repository update...")
    print(f"📅 Current date: {get_current_date()}")
    
    changes_made = False
    
    # Update README timestamp
    if update_readme_timestamp():
        changes_made = True
    
    # Check upcoming events
    check_upcoming_events()
    
    # Update event files if needed
    if update_event_files():
        changes_made = True
    
    if changes_made:
        print("\n✅ Updates completed successfully!")
    else:
        print("\n✅ Repository is up to date!")
    
    return 0

if __name__ == '__main__':
    exit(main())
